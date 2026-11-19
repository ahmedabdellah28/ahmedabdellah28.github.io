import os
import sys
import json
import shutil
import hashlib
from datetime import datetime, timezone
from pathlib import Path

from graphify.detect import detect
from graphify.extract import collect_files, extract
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from graphify.export import to_json

WORKSPACE = Path.cwd()
PORTFOLIO_ROOT = WORKSPACE / "portfolio"
INTEL_DIR = PORTFOLIO_ROOT / ".portfolio-intelligence"

PROJECTS = [
    {
        "slug": "image-to-animate",
        "name_hint": "Image-to-Animate / EffectCraft Studio Engine",
        "path": r"E:\image_to_animate",
        "archive_source": None,
    },
    {
        "slug": "school-timetable",
        "name_hint": "AI School Timetable & Constraint Solver (جدول مدرسة)",
        "path": r"E:\جدول_مدرسة",
        "archive_source": None,
    },
    {
        "slug": "enaya-ai-workspace",
        "name_hint": "Enaya AI Ecosystem, Audit & FigCraft Workspace",
        "path": r"D:\enaya_ai_audit_workspace",
        "archive_source": None,
    },
    {
        "slug": "gmail-options-suite",
        "name_hint": "Gmail Options & Multi-Profile Browser Automation System",
        "path": r"D:\gmail-options-main\gmail-options-main",
        "archive_source": None,
    },
    {
        "slug": "phone-commander",
        "name_hint": "Phone Commander — Cross-Platform ADB & Vision Automation Hub",
        "path": r"D:\app_access\phone_commander",
        "archive_source": r"D:\app_access",
    },
    {
        "slug": "rok-vision-controller",
        "name_hint": "RoK Universal Computer-Vision & ADB Controller",
        "path": r"D:\rok",
        "archive_source": None,
    },
    {
        "slug": "remix-sole-marketplace",
        "name_hint": "SOLE — Footwear E-Commerce Marketplace & Full-Stack Catalog",
        "path": str(INTEL_DIR / "staging" / "remix-sole"),
        "archive_source": r"C:\Users\loper\Downloads\remix-sole-—-footwear-marketplace (8).zip",
    },
]

SKIP_DIRS = {
    "node_modules", ".git", "dist", "build", "vendor", ".next",
    "__pycache__", ".pytest_cache", ".dart_tool", ".cache", "cache",
    ".artifacts_cache", "installer_output", "backup_gui_baseline",
    ".hypothesis", ".neural_db", ".neural_memory", "graphify-out",
    "scratch_cells", "scratch_crops", "scratch_inspect", "step_inspection_images",
    "audio_chunks", "output_animations", "exports", "browsers", "output"
}

SENSITIVE_NAMES = {".env", "license.key", "phone_commander.db", "school_scheduler.db"}
SENSITIVE_EXTS = {".db", ".sqlite", ".sqlite3", ".pem", ".key", ".p12", ".pfx"}


def is_sensitive(filename: str) -> bool:
    low = filename.lower()
    if low in SENSITIVE_NAMES or low.startswith(".env"):
        return True
    if any(low.endswith(ext) for ext in SENSITIVE_EXTS):
        return True
    if "2fa" in low or "secret" in low or "credential" in low or "token" in low:
        return True
    return False


def scan_inventory(proj: dict) -> dict:
    p = Path(proj["path"])
    slug = proj["slug"]
    if not p.exists():
        return {"slug": slug, "path": proj["path"], "exists": False}

    ext_counts = {}
    total_files = 0
    total_bytes = 0
    subprojects = []
    sensitive_skipped = []
    top_level_entries = []

    for item in sorted(p.iterdir(), key=lambda x: x.name.lower()):
        if item.name in SKIP_DIRS or is_sensitive(item.name):
            if is_sensitive(item.name):
                sensitive_skipped.append(item.name)
            continue
        top_level_entries.append({
            "name": item.name,
            "type": "dir" if item.is_dir() else "file",
        })

    hasher = hashlib.sha256()
    for root, dirs, files in os.walk(p):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".git")]
        rel_root = os.path.relpath(root, p)
        for marker in ["package.json", "pyproject.toml", "pubspec.yaml", "requirements.txt", "Dockerfile", "installer.iss", "vercel.json"]:
            if marker in files:
                subprojects.append({"dir": rel_root, "marker": marker})
        for f in sorted(files):
            rel_path = os.path.join(rel_root, f) if rel_root != "." else f
            if is_sensitive(f):
                if rel_path not in sensitive_skipped:
                    sensitive_skipped.append(rel_path)
                continue
            fp = os.path.join(root, f)
            try:
                st = os.stat(fp)
                sz = st.st_size
                mtime = int(st.st_mtime)
            except OSError:
                sz = 0
                mtime = 0
            total_files += 1
            total_bytes += sz
            ext = Path(f).suffix.lower() or "(no_ext)"
            ext_counts[ext] = ext_counts.get(ext, 0) + 1
            hasher.update(f"{rel_path}:{sz}:{mtime}\n".encode("utf-8", errors="replace"))

    top_exts = sorted(ext_counts.items(), key=lambda x: x[1], reverse=True)[:12]
    existing_graph = p / "graphify-out" / "graph.json"

    return {
        "slug": slug,
        "name_hint": proj["name_hint"],
        "path": proj["path"],
        "archive_source": proj["archive_source"],
        "exists": True,
        "fingerprint": hasher.hexdigest()[:16],
        "total_files": total_files,
        "total_mb": round(total_bytes / (1024 * 1024), 2),
        "top_extensions": dict(top_exts),
        "subprojects": subprojects[:25],
        "top_level_entries": top_level_entries[:40],
        "sensitive_excluded_count": len(sensitive_skipped),
        "sensitive_excluded_samples": sensitive_skipped[:15],
        "has_existing_graphify": existing_graph.exists(),
    }


def build_or_reuse_graph(proj: dict, inv: dict) -> dict:
    slug = proj["slug"]
    p = Path(proj["path"])
    graph_dir = INTEL_DIR / "graphs" / slug
    graph_dir.mkdir(parents=True, exist_ok=True)
    target_graph_json = graph_dir / "graph.json"
    target_report_md = graph_dir / "GRAPH_REPORT.md"

    existing_graph_dir = p / "graphify-out"
    reused_existing = False

    if (existing_graph_dir / "graph.json").exists():
        shutil.copy2(existing_graph_dir / "graph.json", target_graph_json)
        if (existing_graph_dir / "GRAPH_REPORT.md").exists():
            shutil.copy2(existing_graph_dir / "GRAPH_REPORT.md", target_report_md)
        reused_existing = True

    # For enaya-ai-workspace, check if enaya_monorepo & figcraft code files are in the graph;
    # or build an additional code-focused AST index if existing graph was only docs, or build fresh for projects without existing graph.
    if not reused_existing or slug == "enaya-ai-workspace":
        det = detect(p, extra_excludes=list(SKIP_DIRS))
        (graph_dir / ".graphify_detect.json").write_text(
            json.dumps(det, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        code_files = []
        for f in det.get("files", {}).get("code", []):
            fp = Path(f)
            if any(part in SKIP_DIRS for part in fp.parts):
                continue
            if is_sensitive(fp.name):
                continue
            code_files.extend(collect_files(fp) if fp.is_dir() else [fp])

        if code_files:
            ast_res = extract(code_files, cache_root=graph_dir, root=p)
        else:
            ast_res = {"nodes": [], "edges": [], "input_tokens": 0, "output_tokens": 0}

        (graph_dir / ".graphify_ast.json").write_text(
            json.dumps(ast_res, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        # If we reused an existing rich graph (like image-to-animate or enaya-ai-workspace), keep it if it already has nodes,
        # and also save the AST graph if enaya's existing graph lacked AST nodes.
        if not reused_existing and ast_res["nodes"]:
            G = build_from_json(ast_res, root=str(p), directed=False)
            if G.number_of_nodes() > 0:
                communities = cluster(G)
                cohesion = score_all(G, communities)
                tokens = {"input": 0, "output": 0}
                gods = god_nodes(G)
                surprises = surprising_connections(G, communities)
                labels = {cid: f"Community {cid}" for cid in communities}
                questions = suggest_questions(G, communities, labels)
                to_json(G, communities, str(target_graph_json), force=True)
                report = generate(
                    G, communities, cohesion, labels, gods, surprises,
                    det, tokens, str(p), suggested_questions=questions
                )
                target_report_md.write_text(report, encoding="utf-8")

    # Read summary statistics from target_graph_json without dumping full graph
    stats = {"nodes": 0, "edges": 0, "communities": 0, "top_nodes_by_degree": []}
    if target_graph_json.exists():
        gdata = json.loads(target_graph_json.read_text(encoding="utf-8"))
        nodes = gdata.get("nodes", [])
        edges = gdata.get("links", gdata.get("edges", []))
        stats["nodes"] = len(nodes)
        stats["edges"] = len(edges)
        comms = {n.get("community") for n in nodes if n.get("community") is not None}
        stats["communities"] = len(comms)
        deg = {}
        for e in edges:
            s = e.get("source")
            t = e.get("target")
            deg[s] = deg.get(s, 0) + 1
            deg[t] = deg.get(t, 0) + 1
        id_to_node = {n.get("id"): n for n in nodes}
        top_ids = sorted(deg.items(), key=lambda x: x[1], reverse=True)[:15]
        for nid, d in top_ids:
            nobj = id_to_node.get(nid, {})
            stats["top_nodes_by_degree"].append({
                "id": nid,
                "label": nobj.get("label", nid),
                "file": nobj.get("source_file", ""),
                "location": nobj.get("source_location", ""),
                "degree": d,
            })

    index_record = {
        "slug": slug,
        "source_path": proj["path"],
        "fingerprint": inv["fingerprint"],
        "indexed_at": datetime.now(timezone.utc).isoformat(),
        "reused_existing_graphify": reused_existing,
        "graph_json_path": str(target_graph_json.relative_to(PORTFOLIO_ROOT)),
        "graph_report_path": str(target_report_md.relative_to(PORTFOLIO_ROOT)) if target_report_md.exists() else None,
        "stats": stats,
    }
    (INTEL_DIR / "project-index" / f"{slug}.json").write_text(
        json.dumps(index_record, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return index_record


def main():
    inventories = []
    indices = []
    for proj in PROJECTS:
        print(f"[1/2] Inventorying {proj['slug']}...")
        inv = scan_inventory(proj)
        inventories.append(inv)
        if inv.get("exists"):
            print(f"[2/2] Indexing {proj['slug']} with Graphify AST...")
            idx = build_or_reuse_graph(proj, inv)
            indices.append(idx)
            print(f"      -> {idx['stats']['nodes']} nodes, {idx['stats']['edges']} edges, {idx['stats']['communities']} communities (reused={idx['reused_existing_graphify']})")

    (INTEL_DIR / "inventory.json").write_text(
        json.dumps(inventories, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("Completed inventory and graphify indexing for all 7 projects.")


if __name__ == "__main__":
    main()
