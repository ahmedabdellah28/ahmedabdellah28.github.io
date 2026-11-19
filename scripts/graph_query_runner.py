import json
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path.cwd()
PORTFOLIO_ROOT = WORKSPACE / "portfolio"
INTEL_DIR = PORTFOLIO_ROOT / ".portfolio-intelligence"

PROJECT_QUERIES = {
    "image-to-animate": [
        "What are the main user-facing workflows, CLI entry points, and studio UI components?",
        "How does the animation rendering pipeline and EffectCraft project (.ecproj) generation work?",
        "Where are retries, timeouts, idempotency, checkpoints, or error recovery implemented?",
        "How are audio timing, TTS synchronization, and asset sheet extraction handled?",
        "What validation, contracts, or automated tests verify rendering and motion templates?",
        "How are Arabic text shaping or RTL subtitles handled in video rendering?"
    ],
    "school-timetable": [
        "What are the main entry points, GUI/web interfaces, and timetable solving workflows?",
        "How does the constraint solver engine handle hard and soft school scheduling constraints?",
        "Where are database persistence, input validation, and duplicate/missing class checks implemented?",
        "How does the PDF export and Arabic RTL printable timetable generation work?",
        "What automated tests, property-based tests, or verification suites exist?"
    ],
    "enaya-ai-workspace": [
        "What are the core systems in enaya_monorepo and figcraft and how do they interact?",
        "What are the main mobile/web application features, Supabase integrations, and state management?",
        "Where are lifecycle resilience, offline recovery, retries, or security/RLS policies implemented?",
        "How does FigCraft automate Figma/UI design-to-code or audit workflows?",
        "What tests, architectural governance, and audit verification mechanisms exist?"
    ],
    "gmail-options-suite": [
        "What are the main entry points, admin panel, and multi-profile browser automation workflows?",
        "How are browser slots, Camoufox/Playwright sessions, and profile isolation managed?",
        "Where are retries, timeouts, crash recovery, watch diagnostics, and concurrency controls implemented?",
        "How does the licensing, Supabase backend, and user system packaging work?",
        "What tests or diagnostic verification scripts exist?"
    ],
    "phone-commander": [
        "What is the architecture of the Flutter app, ADB controller, and device automation engine?",
        "How do computer vision ROI zones, template matching, and screen capture recovery work?",
        "Where are license management, Supabase auth, and device task queues/retries implemented?",
        "How does the automation loop recover from frozen screens, disconnects, or unexpected dialogs?",
        "What tests or diagnostic tools are included?"
    ],
    "rok-vision-controller": [
        "What are the core classes and entry points in rok_controller and rok_universal_controller?",
        "How does the computer vision template matching, OCR, and coordinate calibration work?",
        "Where are retries, state detection, error recovery, and safety timeouts implemented?",
        "How does the universal controller abstract resolution differences or ADB command execution?"
    ],
    "remix-sole-marketplace": [
        "What are the main frontend components, server endpoints, and e-commerce catalog workflows?",
        "How does catalog data loading, fallback resilience (catalog-fallback.json), and filtering work?",
        "Where are image optimization (OptimizedImage), error handling, and input validation implemented?",
        "What unit tests exist in catalog.test.ts and security.test.ts and what edge cases do they verify?"
    ],
}

STOPWORDS = {
    "what", "where", "which", "how", "does", "are", "the", "and", "with",
    "from", "that", "this", "work", "main", "exist", "handled", "implemented",
    "core", "into", "their", "they"
}


def load_combined_graph(slug: str) -> tuple[list, list]:
    graph_dir = INTEL_DIR / "graphs" / slug
    graph_path = graph_dir / "graph.json"
    nodes = []
    edges = []
    seen_ids = set()

    if graph_path.exists():
        gdata = json.loads(graph_path.read_text(encoding="utf-8"))
        for n in gdata.get("nodes", []):
            nid = n.get("id")
            if nid not in seen_ids:
                seen_ids.add(nid)
                nodes.append(n)
        edges.extend(gdata.get("links", gdata.get("edges", [])))

    ast_path = graph_dir / ".graphify_ast.json"
    if ast_path.exists():
        adata = json.loads(ast_path.read_text(encoding="utf-8"))
        for n in adata.get("nodes", []):
            nid = n.get("id")
            if nid not in seen_ids:
                seen_ids.add(nid)
                nodes.append(n)
        edges.extend(adata.get("edges", []))

    return nodes, edges


def query_in_memory(nodes: list, edges: list, adj: dict, question: str) -> dict:
    keywords = [
        w.lower().strip("?,.()/'\"")
        for w in question.split()
        if len(w.strip("?,.()/'\"")) > 2 and w.lower().strip("?,.()/'\"") not in STOPWORDS
    ]

    scored = []
    for n in nodes:
        label = str(n.get("label", "")).lower()
        sfile = str(n.get("source_file", "")).lower()
        nid = str(n.get("id", "")).lower()
        cname = str(n.get("community_name", "")).lower()
        hay = f"{nid} {label} {sfile} {cname}"
        score = 0
        for kw in keywords:
            if kw in label:
                score += 4
            elif kw in sfile:
                score += 3
            elif kw in hay:
                score += 1
        if score > 0:
            degree_bonus = min(len(adj.get(n.get("id"), [])), 20) * 0.1
            scored.append((score + degree_bonus, n))

    scored.sort(key=lambda x: x[0], reverse=True)
    top_hits = [
        {
            "id": n.get("id"),
            "label": n.get("label"),
            "source_file": n.get("source_file"),
            "source_location": n.get("source_location"),
            "type": n.get("type", n.get("_origin", "ast")),
            "score": round(sc, 2),
        }
        for sc, n in scored[:15]
    ]

    top_ids = {h["id"] for h in top_hits}
    related_edges = []
    for tid in list(top_ids)[:10]:
        for e in adj.get(tid, [])[:4]:
            related_edges.append({
                "source": e.get("source"),
                "target": e.get("target"),
                "relation": e.get("relation", e.get("label", "")),
                "confidence": e.get("confidence", "EXTRACTED"),
            })
            if len(related_edges) >= 20:
                break
        if len(related_edges) >= 20:
            break

    return {
        "question": question,
        "keywords": keywords,
        "top_nodes": top_hits,
        "sample_edges": related_edges,
    }


def main():
    usage_log = {
        "policy": {
            "CONTEXT_MODE": "graph_first",
            "SOURCE_READ_POLICY": "targeted_only",
            "REINDEX_POLICY": "changed_files_only",
            "SEMANTIC_MEDIA_PASS": "disabled_by_default",
        },
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_queries_executed": 0,
        "projects": {},
    }

    for slug, questions in PROJECT_QUERIES.items():
        nodes, edges = load_combined_graph(slug)
        if not nodes:
            print(f"SKIP {slug}: no nodes")
            continue

        adj = {}
        for e in edges:
            s = e.get("source")
            t = e.get("target")
            adj.setdefault(s, []).append(e)
            adj.setdefault(t, []).append(e)

        print(f"Querying {slug} ({len(nodes)} nodes, {len(edges)} edges, {len(questions)} queries)...")
        q_results = []
        candidate_files = set()
        for q in questions:
            res = query_in_memory(nodes, edges, adj, q)
            q_results.append(res)
            usage_log["total_queries_executed"] += 1
            for h in res["top_nodes"]:
                if h.get("source_file"):
                    candidate_files.add(h["source_file"])

        (INTEL_DIR / "graphs" / slug / "query_results.json").write_text(
            json.dumps(q_results, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        usage_log["projects"][slug] = {
            "total_graph_nodes": len(nodes),
            "total_graph_edges": len(edges),
            "queries_count": len(questions),
            "candidate_evidence_files_identified": sorted(list(candidate_files))[:35],
            "targeted_slices_verified": 0,
        }
        print(f"  -> {slug}: {len(candidate_files)} candidate evidence files identified.")
        for c in sorted(list(candidate_files))[:12]:
            print(f"     * {c}")

    (INTEL_DIR / "analysis-usage.json").write_text(
        json.dumps(usage_log, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("All graph queries completed and logged.")


if __name__ == "__main__":
    main()
