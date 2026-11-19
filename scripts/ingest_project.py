"""
Phase H — Repeatable Graph-First Project Ingestion & Update Engine
Pipeline: discover -> audit -> evidence extraction -> content draft (visibility='review') -> owner review -> media verification -> publish
"""
import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from graphify.detect import detect
from graphify.extract import collect_files, extract
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.export import to_json

from graph_first_indexer import SKIP_DIRS, is_sensitive, scan_inventory
from prepare_media_assets import write_svg_diagram

WORKSPACE = Path.cwd()
PORTFOLIO_ROOT = WORKSPACE if (WORKSPACE / "astro.config.mjs").exists() else WORKSPACE / "portfolio"
INTEL_DIR = PORTFOLIO_ROOT / ".portfolio-intelligence"
CONTENT_DIR = PORTFOLIO_ROOT / "src" / "content" / "projects"
MEDIA_ROOT = PORTFOLIO_ROOT / "public" / "media" / "projects"


def ingest_new_project(project_path: str, slug: str, title_ar: str, title_en: str, force: bool = False):
    src = Path(project_path).resolve()
    if not src.exists():
        raise FileNotFoundError(f"Project path not found: {src}")

    for sub in ["project-index", "project-memory", "evidence", "graphs", "audits"]:
        (INTEL_DIR / sub).mkdir(parents=True, exist_ok=True)

    proj_descriptor = {
        "slug": slug,
        "name_hint": title_en,
        "path": str(src),
        "archive_source": None,
    }

    # 1. DISCOVER & INVENTORY
    print(f"[1/5] Discover & Inventory: {src}")
    inv = scan_inventory(proj_descriptor)

    # Check if fingerprint unchanged (REINDEX_POLICY = changed_files_only)
    idx_file = INTEL_DIR / "project-index" / f"{slug}.json"
    if idx_file.exists() and not force:
        old_idx = json.loads(idx_file.read_text(encoding="utf-8"))
        if old_idx.get("fingerprint") == inv.get("fingerprint"):
            print(f"      -> Fingerprint unchanged ({inv['fingerprint']}). Skipping AST re-indexing (REINDEX_POLICY=changed_files_only).")
            return old_idx

    # 2. GRAPHIFY AST INDEX
    print(f"[2/5] Graphify AST Indexing: {slug}")
    graph_dir = INTEL_DIR / "graphs" / slug
    graph_dir.mkdir(parents=True, exist_ok=True)
    det = detect(src, extra_excludes=list(SKIP_DIRS))
    code_files = []
    for f in det.get("files", {}).get("code", []):
        fp = Path(f)
        if any(part in SKIP_DIRS for part in fp.parts) or is_sensitive(fp.name):
            continue
        code_files.extend(collect_files(fp) if fp.is_dir() else [fp])

    if code_files:
        ast_res = extract(code_files, cache_root=graph_dir, root=src)
    else:
        ast_res = {"nodes": [], "edges": [], "input_tokens": 0, "output_tokens": 0}

    target_graph_json = graph_dir / "graph.json"
    nodes_count = len(ast_res.get("nodes", []))
    edges_count = len(ast_res.get("edges", []))
    if nodes_count > 0:
        G = build_from_json(ast_res, root=str(src), directed=False)
        communities = cluster(G)
        to_json(G, communities, str(target_graph_json), force=True)

    # 3. EVIDENCE EXTRACTION & AUDIT RECORD
    print(f"[3/5] Extracting initial evidence manifest & project audit...")
    top_exts = list(inv.get("top_extensions", {}).keys())[:6]
    detected_tech = [ext.lstrip(".").upper() for ext in top_exts if ext != "(no_ext)"] or ["Software System"]

    evidence_claims = [
        {
            "claimId": f"{slug[:3].upper()}-01",
            "claimAr": f"هيكل برمجي يضم {inv['total_files']} ملفًا و{nodes_count} عقدة AST مفهرسة",
            "claimEn": f"Codebase structure containing {inv['total_files']} files and {nodes_count} indexed AST nodes",
            "relationType": "EXTRACTED",
            "evidencePath": str(src.name),
            "lineOrSymbol": "Repository Root Inventory & AST Index",
            "confidence": "HIGH",
            "visibility": "public",
            "verificationStatus": "verified",
        }
    ]

    (INTEL_DIR / "evidence" / f"{slug}.json").write_text(
        json.dumps({"slug": slug, "generatedAt": datetime.now(timezone.utc).isoformat(), "claims": evidence_claims}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    index_record = {
        "slug": slug,
        "source_path": str(src),
        "fingerprint": inv["fingerprint"],
        "indexed_at": datetime.now(timezone.utc).isoformat(),
        "stats": {"nodes": nodes_count, "edges": edges_count},
    }
    idx_file.write_text(json.dumps(index_record, ensure_ascii=False, indent=2), encoding="utf-8")

    # 4. MEDIA PLACEHOLDER DIAGRAM
    print(f"[4/5] Generating illustrative architecture SVG diagram...")
    svg_path = write_svg_diagram(
        MEDIA_ROOT / slug,
        "architecture-overview",
        f"DRAFT INGESTION · {slug.upper()}",
        title_ar,
        title_en,
        [
            ("Inputs", "Source Intake", "Stage 01"),
            ("Core Processing", "AST Indexed Modules", f"{nodes_count} Nodes"),
            ("Verification", "Pending Owner Review", "visibility: review"),
        ],
        [
            (f"{inv['total_files']} Files", "Inventoried Source Files"),
            (f"{nodes_count} Nodes", "Graphify AST Symbols"),
        ],
    )

    # 5. CONTENT DRAFT (visibility = 'review' — NEVER auto-published!)
    print(f"[5/5] Writing content draft with visibility='review' (requires owner review before publish)...")
    draft_entry = {
        "slug": slug,
        "titleAr": title_ar,
        "titleEn": title_en,
        "summaryAr": f"مسودة مشروع مستوردة آليًا عبر محرك Graph-First ({inv['total_files']} ملفًا، {nodes_count} عقدة برمجية) — بانتظار مراجعة المالك.",
        "summaryEn": f"Auto-ingested Graph-First project draft ({inv['total_files']} files, {nodes_count} AST nodes) — awaiting owner review before publishing.",
        "valuePropositionAr": "مسودة مشروع جاهزة للمراجعة والتخصيص.",
        "valuePropositionEn": "Project draft ready for owner review and enrichment.",
        "category": ["other"],
        "status": "in_progress",
        "visibility": "review",
        "featured": False,
        "featuredOrder": 90,
        "role": {"ar": "يحتاج تأكيد المالك (needs_owner_confirmation)", "en": "Needs owner confirmation"},
        "audience": {"ar": "يحدد بعد مراجعة المالك", "en": "To be confirmed by owner"},
        "problem": {"ar": "مسودة مستخرجة آليًا تحتاج مراجعة المالك.", "en": "Auto-extracted draft requiring owner review."},
        "solution": {"ar": "مسودة مستخرجة آليًا تحتاج مراجعة المالك.", "en": "Auto-extracted draft requiring owner review."},
        "manualVsAutomated": {"ar": "مسودة مستخرجة آليًا.", "en": "Auto-extracted draft."},
        "capabilities": [{"ar": "فهرسة AST آلية عبر Graphify", "en": "Automated Graphify AST indexing"}],
        "architecture": {
            "overviewAr": "بانتظار مراجعة المالك.",
            "overviewEn": "Pending owner review.",
            "pipelineSteps": [
                {"step": "01", "titleAr": "استيراد آلي", "titleEn": "Automated Ingestion", "detailAr": "فحص أولي", "detailEn": "Initial scan"}
            ],
            "systemBoundariesAr": "محلي",
            "systemBoundariesEn": "Local",
        },
        "technologies": detected_tech,
        "challenges": [
            {
                "id": f"{slug[:3].upper()}-CH-1",
                "type": "unverified_story",
                "titleAr": "بانتظار مراجعة المالك",
                "titleEn": "Pending Owner Review",
                "problemAr": "مسودة",
                "problemEn": "Draft",
                "whyImportantAr": "مسودة",
                "whyImportantEn": "Draft",
                "solutionAr": "مسودة",
                "solutionEn": "Draft",
                "proofRef": "Repository Root",
                "impactAr": "مسودة",
                "impactEn": "Draft",
                "lessonAr": "مسودة",
                "lessonEn": "Draft",
            }
        ],
        "evidence": evidence_claims,
        "screenshots": [
            {
                "src": f"/media/projects/{slug}/architecture-overview.svg",
                "altAr": title_ar,
                "altEn": title_en,
                "captionAr": "مخطط أولي مولد آليًا أثناء الاستيراد",
                "captionEn": "Auto-generated architecture diagram created during ingestion",
                "kind": "architecture_diagram",
                "width": 1200,
                "height": 540,
            }
        ],
        "results": [
            {"metric": f"{nodes_count} Nodes", "labelAr": "عقدة برمجية مفهرسة", "labelEn": "Indexed AST nodes", "sourceRef": f".portfolio-intelligence/project-index/{slug}.json"}
        ],
        "skillsProven": ["Software Engineering"],
        "reviewFlags": ["Auto-generated draft (visibility='review') — review claims and set visibility='published' to publish"],
        "graphStats": {
            "totalFiles": inv["total_files"],
            "totalMb": inv["total_mb"],
            "nodes": nodes_count,
            "edges": edges_count,
        },
        "updatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }

    out_content = CONTENT_DIR / f"{slug}.json"
    if not out_content.exists() or force:
        out_content.write_text(json.dumps(draft_entry, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Created review draft: {out_content} (visibility='review')")
    return index_record


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest or refresh a project into the portfolio as a review draft.")
    parser.add_argument("--path", required=True, help="Path to the project directory")
    parser.add_argument("--slug", required=True, help="Unique project slug")
    parser.add_argument("--title-ar", default="مشروع جديد (مسودة للمراجعة)", help="Arabic title")
    parser.add_argument("--title-en", default="New Project (Review Draft)", help="English title")
    parser.add_argument("--force", action="store_true", help="Force re-index and overwrite draft")
    args = parser.parse_args()
    ingest_new_project(args.path, args.slug, args.title_ar, args.title_en, args.force)
