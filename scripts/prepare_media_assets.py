import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

WORKSPACE = Path.cwd()
PORTFOLIO_ROOT = WORKSPACE / "portfolio"
MEDIA_ROOT = PORTFOLIO_ROOT / "public" / "media" / "projects"
MEDIA_ROOT.mkdir(parents=True, exist_ok=True)


def save_sanitized_image(src_path: Path, dest_dir: Path, name: str, crop_box=None, redact_boxes=None, max_width=1400):
    dest_dir.mkdir(parents=True, exist_ok=True)
    with Image.open(src_path) as im:
        img = im.convert("RGB")
        w, h = img.size

        if redact_boxes:
            draw = ImageDraw.Draw(img)
            for (x1_r, y1_r, x2_r, y2_r, fill_hex) in redact_boxes:
                box = (int(x1_r * w), int(y1_r * h), int(x2_r * w), int(y2_r * h))
                draw.rectangle(box, fill=fill_hex)

        if crop_box:
            cbox = (int(crop_box[0] * w), int(crop_box[1] * h), int(crop_box[2] * w), int(crop_box[3] * h))
            img = img.crop(cbox)

        if img.width > max_width:
            ratio = max_width / float(img.width)
            img = img.resize((max_width, int(img.height * ratio)), Image.Resampling.LANCZOS)

        webp_path = dest_dir / f"{name}.webp"
        img.save(webp_path, "WEBP", quality=86, method=6)
        return webp_path, img.size


def write_svg_diagram(dest_dir: Path, name: str, badge_text: str, title_ar: str, title_en: str, stages: list, metrics: list, accent="#2663EB", secondary="#18B8A7"):
    dest_dir.mkdir(parents=True, exist_ok=True)
    svg_path = dest_dir / f"{name}.svg"

    stage_boxes = []
    n = len(stages)
    box_w = int((1080 - (n - 1) * 18) / n)
    for i, (st_title, st_sub, st_code) in enumerate(stages):
        x = 60 + i * (box_w + 18)
        y = 195
        stage_boxes.append(f"""
        <g transform="translate({x}, {y})">
          <rect width="{box_w}" height="175" rx="12" fill="#182438" stroke="{accent if i % 2 == 0 else secondary}" stroke-width="1.5"/>
          <rect x="14" y="14" width="32" height="22" rx="6" fill="{accent if i % 2 == 0 else secondary}" fill-opacity="0.18"/>
          <text x="30" y="29" fill="#F5F7FA" font-family="JetBrains Mono, monospace" font-size="11" font-weight="700" text-anchor="middle">0{i+1}</text>
          <text x="16" y="62" fill="#F5F7FA" font-family="Manrope, IBM Plex Sans Arabic, sans-serif" font-size="14" font-weight="700">{st_title}</text>
          <text x="16" y="88" fill="#94A3B8" font-family="Manrope, IBM Plex Sans Arabic, sans-serif" font-size="11.5">{st_sub}</text>
          <rect x="12" y="128" width="{box_w - 24}" height="32" rx="6" fill="#0B1220" stroke="#334155" stroke-width="1"/>
          <text x="20" y="148" fill="{secondary}" font-family="JetBrains Mono, monospace" font-size="10.5">{st_code}</text>
        </g>
        """)

    metric_pills = []
    mw = int((1080 - (len(metrics) - 1) * 20) / len(metrics))
    for j, (m_val, m_label) in enumerate(metrics):
        mx = 60 + j * (mw + 20)
        my = 415
        metric_pills.append(f"""
        <g transform="translate({mx}, {my})">
          <rect width="{mw}" height="82" rx="10" fill="#111C2D" stroke="#1E293B" stroke-width="1.5"/>
          <text x="20" y="34" fill="{secondary if j % 2 == 1 else '#60A5FA'}" font-family="JetBrains Mono, monospace" font-size="18" font-weight="700">{m_val}</text>
          <text x="20" y="58" fill="#CBD5E1" font-family="Manrope, IBM Plex Sans Arabic, sans-serif" font-size="12">{m_label}</text>
        </g>
        """)

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 540" width="1200" height="540" role="img" aria-label="{title_en}">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0B1220"/>
      <stop offset="100%" stop-color="#131E31"/>
    </linearGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="#1E293B" stroke-width="0.7"/>
    </pattern>
  </defs>
  <rect width="1200" height="540" fill="url(#bgGrad)"/>
  <rect width="1200" height="540" fill="url(#grid)" opacity="0.55"/>
  <rect x="24" y="24" width="1152" height="492" rx="18" fill="none" stroke="#1E293B" stroke-width="1.5"/>

  <!-- Top Badge -->
  <rect x="60" y="48" width="270" height="28" rx="14" fill="{accent}" fill-opacity="0.16" stroke="{accent}" stroke-width="1"/>
  <text x="195" y="66" fill="#93C5FD" font-family="JetBrains Mono, monospace" font-size="11" font-weight="600" text-anchor="middle">{badge_text}</text>

  <!-- Titles -->
  <text x="60" y="114" fill="#F8FAFC" font-family="Manrope, IBM Plex Sans Arabic, sans-serif" font-size="24" font-weight="800">{title_en}</text>
  <text x="60" y="148" fill="#94A3B8" font-family="IBM Plex Sans Arabic, Manrope, sans-serif" font-size="16" font-weight="500">{title_ar}</text>

  <!-- Pipeline Stages -->
  {''.join(stage_boxes)}

  <!-- Verified Metrics Footer -->
  {''.join(metric_pills)}
</svg>"""
    svg_path.write_text(svg_content, encoding="utf-8")
    return svg_path


def main():
    report = []

    # 1. image-to-animate
    ita_dir = MEDIA_ROOT / "image-to-animate"
    p1 = Path(r"E:\image_to_animate\projects\mehmed_the_conqueror_ar\exports\runs\mehmed_v2_pro\sections\section_01\qa\creative_contact_sheet.png")
    if p1.exists():
        wp, sz = save_sanitized_image(p1, ita_dir, "qa-contact-sheet")
        report.append(("image-to-animate", str(wp.relative_to(PORTFOLIO_ROOT)), "Real Rendered Output (QA 6-Frame Contact Sheet)", f"{sz[0]}x{sz[1]}", "Zero sensitive data"))
    p2 = Path(r"E:\image_to_animate\asset_sheet_extractor_v2_output\preview_diagnostics.png")
    if p2.exists():
        wp, sz = save_sanitized_image(p2, ita_dir, "storyboard-extractor-diagnostics")
        report.append(("image-to-animate", str(wp.relative_to(PORTFOLIO_ROOT)), "Real CV Bounding-Box Diagnostics (55 Entities)", f"{sz[0]}x{sz[1]}", "Zero sensitive data"))
    svg_ita = write_svg_diagram(
        ita_dir, "architecture-pipeline", "VERIFIED ARCHITECTURE · AION V6",
        "معمارية خط الإنتاج الآلي من 13 مرحلة والمترجم الرسومي ECGC (10 مراحل)",
        "AION Studio V6 — 13-Stage Contract Pipeline & 10-Stage ECGC GPU Compiler",
        [
            ("Voice & Whisper", "48kHz -15 LUFS + Word Sync", "Faster-Whisper + TTS"),
            ("PhotoCraft 3x HD", "Alpha Cutout & De-Sliver", "extract_stage.py"),
            ("Scene Graph V2", "Narrative & Luma Contrast", "audit_scene_graph()"),
            ("ECGC 10-Stage", ".ecproj + RMS Audio Ducking", "ecgc_compiler.py"),
            ("Automated QA Gate", "10-Frame Sheet & Drift <0.35s", "creative_quality_report")
        ],
        [
            ("13 Stages", "Contract-Gated Pipeline (PIPELINE_CONTRACTS.md)"),
            ("10 Compilers", "Modular ECGC Scene Graph V2 -> GPU Render"),
            ("< 0.35s", "Max A/V Drift Threshold + RMS Voice Ducking"),
            ("16:9 & 9:16", "Dual Documentary Master & Viral Shorts Engine")
        ]
    )
    report.append(("image-to-animate", str(svg_ita.relative_to(PORTFOLIO_ROOT)), "Illustrative Architecture Diagram", "1200x540", "Derived from PIPELINE_CONTRACTS.md"))

    # 2. school-timetable
    sch_dir = MEDIA_ROOT / "school-timetable"
    p_sch = Path(r"E:\جدول_مدرسة\ai_studio_app\.aistudio\artifacts\brain\9087a3c3-13b7-48ce-a56e-a09387b9787f\.tempmediaStorage\r4-master-table-rendered.png")
    if p_sch.exists():
        # Redact the license key pill at top-left (x: 0.01..0.22, y: 0.07..0.125)
        wp, sz = save_sanitized_image(
            p_sch, sch_dir, "master-schedule-ui",
            redact_boxes=[(0.015, 0.075, 0.22, 0.122, "#0F172A")]
        )
        report.append(("school-timetable", str(wp.relative_to(PORTFOLIO_ROOT)), "Real Application UI Screenshot (Sanitized License Header)", f"{sz[0]}x{sz[1]}", "Redacted top-left license key box"))
    svg_sch = write_svg_diagram(
        sch_dir, "architecture-cpsat", "VERIFIED ARCHITECTURE · OR-TOOLS CP-SAT",
        "محرك الاستمثال الرياضي الصارم وفحص الجدوى المسبق والإصلاح الذكي بأقل إزاحة",
        "School Timetable Engine — Pre-Solve Feasibility, CP-SAT Solver & Minimal-Perturbation Repair",
        [
            ("Feasibility Engine", "Pigeonhole & Quota Check", "feasibility.py"),
            ("OR-Tools CP-SAT", "Linear Gap Zero-Conflict", "scheduler.py (<0.1s)"),
            ("Zero-Trust Validator", "Independent 0-100 Score", "schedule_validator.py"),
            ("Smart Local Repair", "Causal Displacement Chain", "MoveLessonCommand"),
            ("RTL PDF & Excel", "Arabic Reshaper + Bidi A4", "pdf_exporter.py")
        ],
        [
            ("0% Conflicts", "Deterministic Hard-Constraint Satisfaction"),
            ("< 0.1s - 3s", "Solve Time (Small Schools to 600-Period Stress Test)"),
            ("36 Pytest", "Automated Unit, Integration & Stress Test Suite"),
            ("100% Offline", "PyQt6 Desktop + Protected FastAPI SaaS Edition")
        ]
    )
    report.append(("school-timetable", str(svg_sch.relative_to(PORTFOLIO_ROOT)), "Illustrative Architecture Diagram", "1200x540", "Derived from README.md & CHANGE_IMPACT_BEFORE_AFTER.md"))

    # 3. enaya-ai-workspace
    ena_dir = MEDIA_ROOT / "enaya-ai-workspace"
    svg_ena = write_svg_diagram(
        ena_dir, "enaya-ecosystem-architecture", "ILLUSTRATIVE ARCHITECTURE · ENAYA MONOREPO",
        "معمارية منظومة عناية الطبية (5 تطبيقات Flutter) ومزامنة الطوابير غير المتصلة وحوكمة التدقيق",
        "Enaya Healthcare Monorepo — 5-App Ecosystem, Offline Outbox Sync & 12-Role Audit Governance",
        [
            ("12-Role Audit Gate", "Observed Fact vs ADR", "00_governance..06_decisions"),
            ("5 Flutter Apps", "Patient/Doctor/Lab/Pharm/Admin", "enaya_monorepo/apps/*"),
            ("OfflineSyncManager", "Connectivity Stream & Requeue", "offline_sync_manager.dart"),
            ("ErrorRecoveryService", "Exponential Backoff + Jitter", "error_recovery_service.dart"),
            ("Supabase RLS & Events", "Atomic Pricing & Outbox", "Central Event Gateway")
        ],
        [
            ("5 Apps", "Patient, Doctor, Laboratory, Pharmacy & System Admin"),
            ("90+ Docs", "Evidence-Backed Architecture & RLS Governance Manifest"),
            ("0.8x–1.2x", "Jittered Exponential Backoff for Transient 503/504 Faults"),
            ("DEC-01..12", "Enforced Owner Policies & Atomic Booking Remediations")
        ]
    )
    report.append(("enaya-ai-workspace", str(svg_ena.relative_to(PORTFOLIO_ROOT)), "Illustrative Architecture Diagram (Multi-App Monorepo)", "1200x540", "No patient/clinic data exposed"))

    # 4. gmail-options-suite
    gml_dir = MEDIA_ROOT / "gmail-options-suite"
    svg_gml = write_svg_diagram(
        gml_dir, "slot-isolation-architecture", "ILLUSTRATIVE ARCHITECTURE · MULTI-SLOT ENGINE",
        "عزل جلسات المتصفح المتوازية وقفل البروكسيات والتصنيف الذري للأخطاء والتدقيق الجنائي",
        "Multi-Slot Browser Engine — Context Teardown Isolation, Proxy Locking & Forensic Stealth Audit",
        [
            ("Proxy Lock Pool", "Per-Slot Exclusive IP Bind", "lock_proxy / unlock_proxy"),
            ("Isolated Context", "Fresh BrowserContext + Fingerprint", "BrowserFactory"),
            ("Bezier Humanizer", "Cubic Bezier & Typing Physics", "humanization/mouse.py"),
            ("Atomic FailureHandler", "threading.Lock Real-Time IO", "failure_handler.py"),
            ("Full Context Destroy", "page.close + context.close", "Zero Cookie/Storage Leak")
        ],
        [
            ("100% Isolated", "Full BrowserContext Destruction Between Accounts"),
            ("83/83 Files", "Zero-Dependency-Leak Standalone Compilation Audit"),
            ("threading.Lock", "Crash-Safe Real-Time Input File Pruning & Routing"),
            ("10 Findings", "1,276-Line Forensic Camoufox/Playwright Detection Audit")
        ]
    )
    report.append(("gmail-options-suite", str(svg_gml.relative_to(PORTFOLIO_ROOT)), "Illustrative Architecture Diagram (CLI/Automation)", "1200x540", "Zero credentials or license keys exposed"))

    # 5. phone-commander
    phc_dir = MEDIA_ROOT / "phone-commander"
    p_phc = Path(r"D:\app_access\phone_commander\roi_visual_zones_new.png")
    if p_phc.exists():
        # Redact top-left player stats/coords (0.0..0.35, 0.0..0.15) and bottom-left chat box (0.10..0.46, 0.88..1.0)
        wp, sz = save_sanitized_image(
            p_phc, phc_dir, "cv-safe-roi-zones",
            redact_boxes=[
                (0.0, 0.0, 0.35, 0.15, "#1E293B"),
                (0.10, 0.88, 0.48, 1.0, "#1E293B")
            ]
        )
        report.append(("phone-commander", str(wp.relative_to(PORTFOLIO_ROOT)), "Real Computer-Vision Safe ROI Zone Diagnostic (Privacy-Redacted)", f"{sz[0]}x{sz[1]}", "Redacted top-left coordinates & bottom-left chat overlay"))
    svg_phc = write_svg_diagram(
        phc_dir, "zncc-vision-architecture", "VERIFIED ARCHITECTURE · ZERO-GC ZNCC VISION",
        "محرك الرؤية الحاسوبية ZNCC بدون استنزاف الذاكرة وآلة الحالة الذاتية مع بث اللوجز لـ Flutter",
        "Phone Commander — ThreadLocal Zero-GC ZNCC Matcher, Priority State Machine & Flutter Telemetry",
        [
            ("ReusableScaleBuffer", "ThreadLocal Bitmap Reuse", "Zero 8MB/Frame GC Churn"),
            ("Parallel ZNCC Matcher", "Precalculated Stride Offsets", "TemplateMatcher.kt (88-92%)"),
            ("ML Kit OCR & Back", "Zero Hardcoded Blind Taps", "GLOBAL_ACTION_BACK"),
            ("SQLite Queue Sync", "Deduplicated Session State", "Commit d5dc166 & 50927ed"),
            ("Flutter Live Console", "Real-Time MethodChannel", "AutomationLogPayload")
        ],
        [
            ("0 MB/Frame", "Eliminated Per-Frame Bitmap Heap Allocations via ThreadLocal"),
            ("86% – 92%", "Calibrated ZNCC Confidence Gates Across HUD Elements"),
            ("5,264 Lines", "Autonomous Kotlin State-Machine & Recovery Loop"),
            ("> 15 Min", "Battery-Saving Auto-Minimize During Long Idle Waits")
        ]
    )
    report.append(("phone-commander", str(svg_phc.relative_to(PORTFOLIO_ROOT)), "Illustrative Architecture Diagram", "1200x540", "Derived from TemplateMatcher.kt & AUTOMATION_UPGRADE_PLAN.md"))

    # 6. rok-vision-controller
    rok_dir = MEDIA_ROOT / "rok-vision-controller"
    svg_rok = write_svg_diagram(
        rok_dir, "anchor-screen-scaler", "ILLUSTRATIVE TECHNICAL DIAGRAM · SCREENSCALER",
        "خوارزمية التحويل الهندسي المرتكزة على نقاط الإرساء الخمس لمعالجة اختلاف أبعاد الشاشات",
        "RoK Universal Controller — Height-Locked Anchor Coordinate Transformation Across Aspect Ratios",
        [
            ("ADB uiautomator2", "Enforce Landscape w > h", "max(raw_w,h) x min(raw_w,h)"),
            ("Height-Locked Scale", "scale = current_h / 1080.0", "2400x1080 Reference Base"),
            ("5 Viewport Anchors", "center / corners / bottom", "ScreenScaler.get_coords()"),
            ("Multi-Character Grid", "Dynamic 2-Col Scroll Matrix", "CHAR_GRID_CONFIG"),
            ("Humanized Cycle", "Randomized 5s–10s Jitter", "Auto-Reload & Gather Loop")
        ],
        [
            ("5 Anchors", "center, bottom_left, top_left, bottom_center, top_right"),
            ("16:9 to 20:9", "Zero Coordinate Drift Across Phones, Foldables & Tablets"),
            ("2400x1080", "Normalized Reference Space with Height-Proportional Scaling"),
            ("5.0s – 10.0s", "Randomized Post-Click Humanization Timing Envelope")
        ]
    )
    report.append(("rok-vision-controller", str(svg_rok.relative_to(PORTFOLIO_ROOT)), "Illustrative Technical Diagram (CLI/ADB Controller)", "1200x540", "Avoids publishing raw player profile screenshots"))

    # 7. remix-sole-marketplace
    sol_dir = MEDIA_ROOT / "remix-sole-marketplace"
    p_sol1 = WORKSPACE / "portfolio" / ".portfolio-intelligence" / "staging" / "remix-sole" / ".aistudio" / "artifacts" / "brain" / "7aa75a93-fdb9-4dd7-b104-b5732a1d34e6" / ".tempmediaStorage" / "media_1793358406131_a8bb0909.png"
    if p_sol1.exists():
        wp, sz = save_sanitized_image(p_sol1, sol_dir, "storefront-catalog")
        report.append(("remix-sole-marketplace", str(wp.relative_to(PORTFOLIO_ROOT)), "Real Storefront UI Screenshot (506 Products / 15 Collections)", f"{sz[0]}x{sz[1]}", "Zero sensitive data"))
    svg_sol = write_svg_diagram(
        sol_dir, "security-architecture", "VERIFIED ARCHITECTURE · FULL-STACK & SECURITY",
        "معمارية متجر سول: تطبيع أسماء صور الاستوديو، فصل زيارات المتجر عن Cloudinary، وفحص Magic Bytes",
        "SOLE Marketplace — Bilingual Catalog Normalizer, Supabase/Fallback Isolation & Magic-Byte Security",
        [
            ("Magic-Byte Filter", "Rejects Spoofed SVG/HTML/EXE", "validateImageUploadBuffer"),
            ("PostgREST & Path Guard", "Blocks Injection & '../'", "src/server/security.ts"),
            ("Bilingual Normalizer", "WA0019 -> Y3 فاشون · موديل", "src/utils/catalog.ts"),
            ("Public Traffic Shield", "Supabase RLS + Static JSON", "Zero Live Cloudinary Scan"),
            ("Responsive CDN srcset", "f_auto,q_auto 400w..1200w", "OptimizedImage.tsx")
        ],
        [
            ("506 Products", "Normalized from 15 Studio Archive Collections"),
            ("0 Live Scans", "Public Visitors Served via Supabase + catalog-fallback.json"),
            ("100% Blocked", "Spoofed SVG/HTML/EXE Uploads & PostgREST Filter Injection"),
            ("React 19 + TS", "Full-Stack Express + Vite 8 + Vercel Edge/Serverless Ready")
        ]
    )
    report.append(("remix-sole-marketplace", str(svg_sol.relative_to(PORTFOLIO_ROOT)), "Illustrative Architecture Diagram", "1200x540", "Derived from security.ts & catalogService.ts"))

    print(f"Prepared {len(report)} visual proof assets across all 7 projects.")
    for r in report:
        print(" ", r)


if __name__ == "__main__":
    main()
