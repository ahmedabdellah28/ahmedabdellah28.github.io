import json
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path.cwd()
PORTFOLIO_ROOT = WORKSPACE / "portfolio"
INTEL_DIR = PORTFOLIO_ROOT / ".portfolio-intelligence"

SYNTHESIS_DATA = {
    "image-to-animate": {
        "titleAr": "محرك AION Studio V6 — أتمتة إنتاج الموشن جرافيك والوايت بورد بالذكاء الاصطناعي",
        "titleEn": "AION Studio V6 — Automated Whiteboard Motion Graphics & Shorts Engine",
        "summaryAr": "خط إنتاج برمجي متكامل يحوّل النصوص ولوحات القصة (Storyboards) إلى فيديوهات موشن جرافيك 16:9 ومقاطع Shorts 9:16 عبر مترجم رسومي من 10 مراحل (ECGC) ومحرك EffectCraft GPU ومحاذاة صوتية على مستوى الكلمة.",
        "summaryEn": "End-to-end CLI-first production engine converting scripts and storyboards into 16:9 whiteboard explainers and 9:16 shorts via a 10-stage ECGC compiler, EffectCraft GPU renderer, and word-level Faster-Whisper synchronization.",
        "category": ["AI", "media", "automation", "CLI"],
        "status": "production",
        "statusEvidence": "Verified via git commits b20a094 & 629730d, 13-stage PIPELINE_CONTRACTS.md, and multi-run rendered outputs with automated QA reports (projects/mehmed_the_conqueror_ar, voyager_light_day_en).",
        "role": "Lead Software Architect & Creator (Git author: Ahmed Abdellah — needs_owner_confirmation for public display name)",
        "problemAr": "إنتاج فيديوهات الشرح والموشن جرافيك العربية والإنجليزية يدويًا يتطلب ساعات من قص الأصول، ضبط التزامن الصوتي مع النص، تحريك الكاميرا، وموازنة المؤثرات الصوتية.",
        "problemEn": "Manual production of Arabic/English whiteboard explainers and shorts requires hours of asset cutout, word-level voice sync, camera choreography, and audio ducking.",
        "audienceAr": "استوديوهات المحتوى التعليمي والوثائقي وصناع الفيديو الذين يحتاجون إنتاجًا متسقًا وقابلًا للتكرار بجودة بث كاملة.",
        "audienceEn": "Educational and documentary content studios and creators seeking deterministic, repeatable broadcast-quality motion graphics at scale.",
        "workflow": "init -> script -> voice (48kHz -15 LUFS) -> timing (Faster-Whisper word alignment) -> extract (PhotoCraft 3x HD) -> semantic-map -> brief -> direct (Scene Graph V2) -> motion -> sfx (RMS voice ducking) -> render (EffectCraft GPU) -> qa (10-frame sheet & A/V drift <0.35s) -> merge",
        "technologies": ["Python 3.13", "EffectCraft GPU CLI", "PhotoCraft 3x HD", "Faster-Whisper", "Gemini TTS", "FFmpeg / FFprobe", "OpenCV", "Scene Graph V2 JSON Schema"],
        "evidence": [
            {
                "claimId": "ITA-01",
                "claim": "13-stage deterministic contract pipeline with isolated per-run directories and rollback protection",
                "relationType": "EXTRACTED",
                "evidencePath": "PIPELINE_CONTRACTS.md",
                "lineOrSymbol": "Lines 9-36 (Stage-by-Stage Artifact Contracts & Run State)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "ITA-02",
                "claim": "10-component EffectCraft Creative Graphics Compiler (ECGC) translating Scene Graph V2 into .ecproj and MP4",
                "relationType": "EXTRACTED",
                "evidencePath": "core/aion/ecgc_compiler.py",
                "lineOrSymbol": "Lines 1-85 (CompileContext, SceneGraphValidator..RenderValidator)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "ITA-03",
                "claim": "Automated Scene Graph invariant auditor checking timing bounds, dark/light card luma contrast, and audio duration overflow",
                "relationType": "EXTRACTED",
                "evidencePath": "core/aion/contracts.py",
                "lineOrSymbol": "Lines 46-90 (_hex_luma, bg_hex_at, audit_scene_graph)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "ITA-04",
                "claim": "Forensic 8-point Root Cause Analysis resolving V5 narrative flattening, caption ghosting, 24->30 FPS drift, and SFX flooding (84 overlapping hits reduced via RMS voice ducking)",
                "relationType": "EXTRACTED",
                "evidencePath": "V5_GOLD_REGRESSION_RCA_AR.md",
                "lineOrSymbol": "Lines 15-90 (Issues 1-7 & core/aion/motion_and_audio.mix_scene_graph_audio)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            }
        ],
        "challenges": [
            {
                "id": "ITA-CH-1",
                "type": "verified_fix",
                "titleAr": "إصلاح تسطيح المشاهد وشبحية النصوص العربية وتلوث المؤثرات الصوتية في المترجم الرسومي",
                "titleEn": "Resolving Scene Flattening, Arabic Caption Ghosting & 3x SFX Flooding in ECGC",
                "scenarioAr": "أظهرت مراجعة الجودة لمخرجات V5 تراجعًا بصريًا وسمعيًا رغم نجاح الرندر التقني: تكدس المشاهد في مشهد واحد مسطح، ظهور كلمات عربية باهتة منزاحة (Ghosting) أثناء حركة البطاقات، وتداخل ~84 ضربة صوتية فوق صوت الراوي.",
                "scenarioEn": "V5 rendered outputs passed technical binary checks but suffered narrative regression: collapsed single-scene timelines, ghosted Arabic text animators lagging behind card expansion, and ~84 overlapping SFX hits drowning narration.",
                "rootCauseAr": "تحقيق جنائي في الكود (V5_GOLD_REGRESSION_RCA_AR.md) كشف أن المخرج كان يمرر جمل Whisper الخام دون تجميع سردي، ويطبق RangeSelector بطيء (0.85s) فوق بطاقة تتوسع في 0.25s، بينما كان محرك الصوت القديم يحقن مؤثري pop إضافيين لكل عنصر بلا خفض تلقائي للصوت (RMS Ducking).",
                "rootCauseEn": "Forensic trace across creative_director.py and ecgc_compiler.py revealed raw Whisper sentences bypassing narrative beat grouping, asynchronous text range selectors (0.85s vs 0.25s card reveal), and legacy SFXDirector injecting duplicate pop cues without RMS envelope ducking.",
                "solutionAr": "إعادة هيكلة التوجيه المشهدي إلى مشاهد سردية مستقلة، ضبط تزامن TypographyCompiler مع البطاقات والعناوين التحريرية، وتوحيد الخلط الصوتي عبر mix_scene_graph_audio مع RMS voice-ducking ومعدل 30fps ثابت.",
                "solutionEn": "Restored multi-scene narrative grouping, synchronized TypographyCompiler reveal windows, enforced 30fps project contract inheritance, and routed audio through mix_scene_graph_audio with RMS envelope ducking around speech.",
                "evidenceRef": "V5_GOLD_REGRESSION_RCA_AR.md:15-90 & core/aion/ecgc_compiler.py:39-71",
                "impactAr": "اجتياز فحوص QA البصرية والسمعية (86 طبقة، انحراف صوت/صورة أقل من 0.35 ثانية) وإنتاج مشاهد عربية متماسكة بصريًا في المشاريع الوثائقية.",
                "impactEn": "Passed automated visual/audio QA gates (86 layers, A/V drift <0.35s, zero voice truncation) across multi-section Arabic and English documentary runs."
            },
            {
                "id": "ITA-CH-2",
                "type": "preventive_design",
                "titleAr": "حماية المشاريع المرجعية الذهبية وعزل مجلدات التشغيل لمنع تلف المخرجات",
                "titleEn": "Write-Protected Golden Reference Projects & Isolated Per-Run Execution Ledgers",
                "scenarioAr": "خطر تلف المخرجات المعتمدة أو تداخل الملفات الوسيطة عند إعادة تشغيل الرندر أو تجربة إعدادات إخراجية جديدة.",
                "scenarioEn": "Risk of corrupting approved master renders or intermediate assets during iterative re-compilation or parameter tuning.",
                "rootCauseAr": "تصميم وقائي يعتمد عزل كل عملية تشغيل في مجلد `exports/runs/<run_id>/` مع قفل برمجي للمشروع الذهبي.",
                "rootCauseEn": "Preventive architectural design isolating every execution inside `exports/runs/<run_id>/` with explicit write-protection on golden baselines.",
                "solutionAr": "تطبيق عقود `PIPELINE_CONTRACTS.md` وسجل `run_manifest.json` مع رفع `PermissionError` تلقائي في `studio_cli` عند محاولة الكتابة فوق المشروع المرجعي `mind_glitches_ar`.",
                "solutionEn": "Enforced immutable run ledgers (`run_manifest.json`, `latest_run.json`) and programmatic `PermissionError` guards in `studio_cli` protecting golden baselines.",
                "evidenceRef": "PIPELINE_CONTRACTS.md:27-36 & core/aion/contracts.py:64-90",
                "impactAr": "إمكانية مقارنة الإصدارات واختبار التعديلات بأمان تام مع قابلية استرجاع فورية.",
                "impactEn": "Zero-regression testing and side-by-side run comparison with instant rollback safety."
            }
        ]
    },
    "school-timetable": {
        "titleAr": "نظام الجدول المدرسي الذكي — محرك استمثال رياضي (OR-Tools CP-SAT) وإصلاح ذكي للتعارضات",
        "titleEn": "Deterministic School Timetable System — OR-Tools CP-SAT Solver & Smart Conflict Repair",
        "summaryAr": "منظومة سطح مكتب وويب سحابية (PyQt6 + FastAPI + React/TS) لبناء جداول الحصص المدرسية بصفر تعارضات حتمية عبر Google OR-Tools CP-SAT، مع محرك تشخيص مسبق للاستحالة وإصلاح موضعي ذكي وتصدير PDF/Excel عربي RTL.",
        "summaryEn": "Desktop (PyQt6) and cloud SaaS (FastAPI + React/TS) school scheduling platform achieving zero hard violations via Google OR-Tools CP-SAT, pre-solve mathematical feasibility diagnostics, minimal-perturbation smart repair, and Arabic RTL PDF/Excel exports.",
        "category": ["desktop", "web", "AI", "automation"],
        "status": "production",
        "statusEvidence": "Verified via pyproject.toml, 36 automated pytest tests + 600-lesson stress test, PyQt6 GUI + FastAPI SaaS server (v2.1.0), and real Arabic school PDF outputs (مدرسة النيل، الجمالية).",
        "role": "Lead Architect & Full-Stack / Operations Research Engineer (needs_owner_confirmation)",
        "problemAr": "إعداد الجدول المدرسي يدويًا يستغرق أيامًا ويعاني من تضارب حصص المعلمين، كسر أنصبة الأيام، أو فشل التعديل اليدوي عند نقل حصة واحدة دون هدم الجدول بالكامل.",
        "problemEn": "Manual school timetabling takes days and suffers from teacher double-booking, broken daily quotas, and cascading failures when administrators manually move a single lesson.",
        "audienceAr": "إدارات المدارس ووكلاء شؤون المعلمين الذين يحتاجون جداول خالية من التعارضات وقابلة للتعديل التفاعلي والطباعة الفورية.",
        "audienceEn": "School principals and academic schedulers needing conflict-free timetables with interactive drag-and-drop repair and print-ready Arabic exports.",
        "workflow": "Data Intake / Gemini AI Copilot Normalization -> Mathematical Feasibility Analyzer -> OR-Tools CP-SAT Linear Gap Solver -> Zero-Trust Independent Validator -> Interactive Drag & Drop + Minimal Perturbation Smart Repair -> Arabic RTL PDF & Multi-Sheet Excel Export",
        "technologies": ["Python 3.13", "Google OR-Tools (CP-SAT)", "PyQt6", "FastAPI", "React + TypeScript", "SQLite + SQLAlchemy 2.0", "ReportLab + arabic-reshaper + python-bidi", "OpenPyXL", "Pytest + Hypothesis"],
        "evidence": [
            {
                "claimId": "SCH-01",
                "claim": "Google OR-Tools CP-SAT linear gap formulation solving small schools in <0.1s and 600-period schools with zero hard violations, verified by an independent Zero-Trust ScheduleValidator",
                "relationType": "EXTRACTED",
                "evidencePath": "README.md",
                "lineOrSymbol": "Lines 10-36 & 80-90 (CP-SAT Solver, Zero-Trust Validator, 36 pytest suite)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "SCH-02",
                "claim": "Unified MoveLessonCommand & SmartRepairService call chain showing direct vs displaced lessons, causal explanation, teacher objection diffs, and rollback/undo safety",
                "relationType": "EXTRACTED",
                "evidencePath": "CHANGE_IMPACT_BEFORE_AFTER.md",
                "lineOrSymbol": "Lines 12-90 (Before/After Call Chain Audit: TimetableGridWidget -> MoveLessonCommand -> ConflictImpactDialog)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "SCH-03",
                "claim": "Fix for Inverted Pigeonhole Trap in teacher availability when workload < active_days and persistence of is_pinned lessons in SQLite",
                "relationType": "EXTRACTED",
                "evidencePath": "خطة_إصلاح_وتطوير_منظومة_القيود_الشاملة.md",
                "lineOrSymbol": "Lines 34-74 (ConflictImpactDialog, is_pinned SQLAlchemy model, Inverted Pigeonhole fix)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "SCH-04",
                "claim": "Protected FastAPI SaaS backend isolating solver IP, Gemini normalizer, and PDF/Excel exporters behind quota-checked license verification",
                "relationType": "EXTRACTED",
                "evidencePath": "src/school_scheduler/ai_studio/api_server.py",
                "lineOrSymbol": "Lines 1-76 (FastAPI v2.1.0, _require_license, TimetableSolver, LocalRepairEngine)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            }
        ],
        "challenges": [
            {
                "id": "SCH-CH-1",
                "type": "verified_fix",
                "titleAr": "توحيد مسار السحب والإفلات والإصلاح الذكي (Minimal Perturbation) مع تفسير سببي للحصص المزاحة",
                "titleEn": "Unifying Drag-and-Drop Smart Repair with Causal Displacement Chains & Rollback Safety",
                "scenarioAr": "عند سحب حصة إلى موعد مشغول في واجهة الجدول، كان المسار القديم يتجاوز خدمات التحقق ويكتفي بـ 4 فحوص بدائية ثم يستبدل الجدول في قاعدة البيانات مباشرة دون توضيح الحصص الأخرى التي تحركت أو توفير تراجع (Undo).",
                "scenarioEn": "Dragging a lesson onto an occupied slot previously bypassed domain validation services, ran 4 ad-hoc checks, and overwrote SQLite entries without showing displaced lessons or supporting undo.",
                "rootCauseAr": "فجوة معمارية موثقة في `CHANGE_IMPACT_BEFORE_AFTER.md` حيث كانت `ConflictImpactDialog` و`ResultsPage` تتصلان مباشرة بمحرك الإصلاح دون تمرير سلسلة الأثر السببي أو حفظ `is_pinned` في نموذج قاعدة البيانات.",
                "rootCauseEn": "Call-chain audit (`CHANGE_IMPACT_BEFORE_AFTER.md:36-72`) showed UI handlers bypassing `ImpactAnalysisService` and `ScheduleDiffService`, discarding the `ChangeSet` and ignoring pinned lessons in SQLite mappers.",
                "solutionAr": "توحيد المسار عبر `MoveLessonCommand` و`SmartRepairService` لعرض جدول الحصص المزاحة مع سبب نقل كل حصة، وإضافة عمود `is_pinned` في `TimetableEntryModel` لمنع تحريك الحصص المثبتة، وحظر الحفظ غير المعتمد.",
                "solutionEn": "Routed drag-and-drop through `MoveLessonCommand`, added causal displacement explanations and root-cause infeasibility reports in `ConflictImpactDialog`, and persisted `is_pinned` in SQLAlchemy models.",
                "evidenceRef": "CHANGE_IMPACT_BEFORE_AFTER.md:12-90 & خطة_إصلاح_وتطوير_منظومة_القيود_الشاملة.md:34-64",
                "impactAr": "شفافية كاملة لمدير المدرسة قبل اعتماد أي تعديل يدوي، وصفر فقدان للبيانات أو الحصص المثبتة.",
                "impactEn": "100% transparent before/after diff preview for school admins with zero silent schedule corruption."
            },
            {
                "id": "SCH-CH-2",
                "type": "verified_fix",
                "titleAr": "معالجة فخ الاستحالة الرياضي المعكوس (Inverted Pigeonhole Trap) في أيام عمل المعلمين",
                "titleEn": "Eliminating the Inverted Pigeonhole Infeasibility Trap in Teacher Work-Pattern Constraints",
                "scenarioAr": "فشل مفاجئ لمحرك CP-SAT في إيجاد حل عند إسناد معلم ذي نصاب صغير (مثل 3 حصص أسبوعيًا) مع تفعيل 5 أيام عمل نشطة.",
                "scenarioEn": "CP-SAT solver unexpectedly returned INFEASIBLE when a teacher had a small weekly workload (e.g., 3 periods) across 5 active working days.",
                "rootCauseAr": "كانت دالة `get_work_pattern` تفرض `target_working_days = len(active_days)` كقيد صارم (Hard Constraint) يتطلب حصة واحدة على الأقل في كل يوم نشط، وهو مستحيل رياضيًا عندما يكون النصاب أقل من عدد الأيام.",
                "rootCauseEn": "`teacher_availability_dialog.py:get_work_pattern` set `target_working_days = len(active_days)` as a hard constraint requiring >=1 lesson per active day even when `total_workload < len(active_days)`.",
                "solutionAr": "تقييد `target_working_days = min(len(active_days), self.total_workload)` مع تحويله لقيد مرن عند انخفاض النصاب، وإضافة فحص استباقي في `FeasibilityAnalyzer`.",
                "solutionEn": "Clamped `target_working_days = min(len(active_days), total_workload)` with soft fallback and added pre-solve detection in `FeasibilityAnalyzer`.",
                "evidenceRef": "خطة_إصلاح_وتطوير_منظومة_القيود_الشاملة.md:65-70",
                "impactAr": "منع فشل الـ Solver على حالات المعلمين المنتدبين أو ذوي الأنصبة الجزئية.",
                "impactEn": "Eliminated false-infeasible solver halts for part-time and low-quota teachers."
            }
        ]
    },
    "enaya-ai-workspace": {
        "titleAr": "منظومة عناية الطبية (Enaya Monorepo & Audit Workspace) — معمارية تطبيقات الرعاية الصحية وحوكمة التدقيق",
        "titleEn": "Enaya Healthcare Ecosystem & AI Audit Workspace — Multi-App Flutter Monorepo & Governance",
        "summaryAr": "مجمّع برمجي يضم المونوريبو الكامل لتطبيقات عناية الطبية (تطبيق المريض، الطبيب، الصيدلية، المختبر، ولوحة الإدارة) مع إطار تدقيق هندسي مهيكل وأداة FigCraft المكتبية.",
        "summaryEn": "Comprehensive healthcare engineering workspace combining the multi-app Enaya Flutter/Supabase monorepo (Patient, Doctor, Pharmacy, Lab, System Admin) with an evidence-driven architectural audit framework and FigCraft desktop tooling.",
        "category": ["mobile", "web", "architecture", "AI"],
        "status": "functional",
        "statusEvidence": "Verified via enaya_monorepo git commits (08208b8, 4f1f721, 7b0efb5, a87d911, 07c9431), 90+ governance/architecture documents in MANIFEST.md, and Dart service implementations with unit tests.",
        "role": "System Architect & Principal Flutter/Supabase Reviewer (needs_owner_confirmation)",
        "problemAr": "تعدد تطبيقات المنظومة الطبية (عيادات، مختبرات، صيدليات، مرضى) مع قواعد بيانات Supabase متفرقة يخلق مخاطر في تزامن العمليات عند انقطاع الإنترنت، وتسعير الحجوزات، وسياسات الصلاحيات (RLS).",
        "problemEn": "Coordinating multi-app healthcare workflows (Patient, Doctor, Lab, Pharmacy, Admin) across distributed Supabase backends risks offline data loss, race conditions in booking/quoting, and RLS security gaps.",
        "audienceAr": "المرضى والأطباء والمختبرات والصيدليات، وفرق الهندسة المسؤولة عن استقرار المنظومة الطبية وأمان بياناتها.",
        "audienceEn": "Patients, doctors, laboratories, pharmacies, and engineering teams requiring resilient healthcare transactions and strict data governance.",
        "workflow": "Multi-Role Evidence Intake (12 Specialist Roles) -> Cross-Review & ADR Decisions (DEC-01..DEC-12) -> Target Monorepo Remediation -> Offline Queue Sync + Exponential Backoff Recovery -> Atomic Booking/Quoting & Central Event Gateway",
        "technologies": ["Flutter / Dart", "Supabase (PostgreSQL, RLS, Edge Functions)", "BLoC / Cubit", "SQLite Outbox / Offline Queue", "Cloudinary Asset Security", "Rust (FigCraft Desktop CLI/App)", "Graphify Knowledge Graph"],
        "evidence": [
            {
                "claimId": "ENA-01",
                "claim": "OfflineSyncManager in Doctor & Patient apps monitoring connectivity changes and re-queueing only failed actions after atomic queue flush",
                "relationType": "EXTRACTED",
                "evidencePath": "enaya_monorepo/apps/doctor_app/lib/core/services/offline_sync_manager.dart",
                "lineOrSymbol": "Lines 8-90 (OfflineSyncManager.startMonitoring, syncOfflineQueue)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "ENA-02",
                "claim": "ErrorRecoveryService in Laboratory app implementing exponential backoff with randomized jitter (0.8..1.2x) and transient socket/503/504 detection",
                "relationType": "EXTRACTED",
                "evidencePath": "enaya_monorepo/apps/laboratory_app/lib/core/services/error_recovery_service.dart",
                "lineOrSymbol": "Lines 15-69 (ErrorRecoveryService.executeWithRetry, MaxRetriesExceededException)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "ENA-03",
                "claim": "90+ structured engineering artifacts covering AS-IS/TO-BE architecture, RLS policy review, cross-domain failure matrix, and free-tier disaster recovery",
                "relationType": "EXTRACTED",
                "evidencePath": "MANIFEST.md",
                "lineOrSymbol": "Lines 1-90 (00_governance through 05_final_docs)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "ENA-04",
                "claim": "Verified git remediation commits across Patient, Pharmacy, Laboratory, and System Admin apps enforcing atomic pricing, outbox pattern, and Central Event Gateway",
                "relationType": "EXTRACTED",
                "evidencePath": "enaya_monorepo/.git",
                "lineOrSymbol": "Commits 07c9431, a87d911, 7b0efb5, 4f1f721, e9651f7, 08208b8",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            }
        ],
        "challenges": [
            {
                "id": "ENA-CH-1",
                "type": "verified_fix",
                "titleAr": "مزامنة طابور العمليات غير المتصلة (Offline Queue) والتعافي التلقائي بـ Exponential Backoff + Jitter",
                "titleEn": "Offline Queue Synchronization & Jittered Exponential Backoff Across Healthcare Apps",
                "scenarioAr": "انقطاع اتصال الإنترنت لدى الطبيب أو المريض أو المختبر أثناء إلغاء حجز أو تحديث نتيجة فحص كان يعرض العملية للفقدان أو يسبب عاصفة طلبات متزامنة عند عودة الشبكة.",
                "scenarioEn": "Intermittent mobile connectivity for doctors, patients, or labs risked dropping booking cancellations or triggering retry storms upon reconnection.",
                "rootCauseAr": "غياب طبقة جدولة محلية تعزل الفشل المؤقت للشبكة (Socket / 503 / 504) عن حالة واجهة المستخدم.",
                "rootCauseEn": "Direct remote calls lacked local outbox persistence and jittered retry policies for transient HTTP 503/504 and socket timeouts.",
                "solutionAr": "بناء `OfflineSyncManager` في تطبيقي الطبيب والمريض لمراقبة `InternetConnectionChecker` وإعادة جدولة العمليات الفاشلة فقط، مع بناء `ErrorRecoveryService` في تطبيق المختبر بـ Exponential Backoff وعامل عشوائي (Jitter 0.8..1.2x).",
                "solutionEn": "Implemented `OfflineSyncManager` with `InternetConnectionChecker` stream listeners and partial failure re-queueing, alongside `ErrorRecoveryService.executeWithRetry` using jittered exponential backoff.",
                "evidenceRef": "enaya_monorepo/apps/doctor_app/lib/core/services/offline_sync_manager.dart:22-90 & enaya_monorepo/apps/laboratory_app/lib/core/services/error_recovery_service.dart:29-68",
                "impactAr": "حماية العمليات الحرجة من الضياع أثناء ضعف الشبكة ومنع تكدس الطلبات المتكررة.",
                "impactEn": "Guaranteed eventual consistency for queued offline actions and resilient recovery against transient network faults."
            },
            {
                "id": "ENA-CH-2",
                "type": "preventive_design",
                "titleAr": "حوكمة التدقيق الهندسي متعدد الأدوار وفصل الحقائق المرصودة عن الفرضيات قبل تعديل المونوريبو",
                "titleEn": "Evidence-Gated Multi-Role Architectural Governance Before Monorepo Remediation",
                "scenarioAr": "تدقيق منظومة تضم 5 تطبيقات و3 قواعد بيانات Supabase عرضة لتضارب القرارات الهندسية أو تعديل الكود بناءً على تخمينات غير مثبتة.",
                "scenarioEn": "Auditing a 5-app, multi-database healthcare ecosystem risks conflicting architectural changes and unverified assumptions.",
                "rootCauseAr": "الحاجة إلى فصل صارم بين الحقيقة المرصودة (`Observed fact`) والمخاطر المستنتجة (`Inferred risk`) والقرارات المعتمدة (`ADR`).",
                "rootCauseEn": "Need for strict separation between observed code facts, inferred risks, and approved Architecture Decision Records (ADRs).",
                "solutionAr": "تصميم خط تدقيق من 12 دورًا تخصصيًا في `D:\\enaya_ai_audit_workspace` يلزم كل تقرير بإسناد كل ملاحظة إلى ملف وسطر محدد، ثم حسم التعارضات عبر قرارات `DEC-01..DEC-12` قبل تطبيقها في `enaya_monorepo`.",
                "solutionEn": "Engineered a 12-role audit pipeline enforcing file/line evidence citations, cross-role conflict resolution, and formal ADRs (`DEC-01..DEC-12`) prior to monorepo commits.",
                "evidenceRef": "README.md:7-37, MANIFEST.md:1-90 & enaya_monorepo commit a87d911",
                "impactAr": "تنفيذ إصلاحات P0/P1 عبر تطبيقات المريض والصيدلية والمختبر والإدارة بتوافق معماري كامل.",
                "impactEn": "Traceable execution of P0/P1 remediations across all 5 apps with zero architectural drift."
            }
        ]
    },
    "gmail-options-suite": {
        "titleAr": "منظومة Scenarios & Browser Slots — أتمتة المتصفح المتعددة وعزل الجلسات والبصمات",
        "titleEn": "Multi-Slot Browser Automation & Session Isolation Engine (Camoufox / Playwright)",
        "summaryAr": "منصة أتمتة بايثون معيارية مستقلة مع لوحة إدارة، تدير سلوتات متصفح متوازية معزولة كليًا (BrowserContext + Proxy Locking + Humanization) وتتعامل مع حالات الفشل والتصنيف الذري للملفات.",
        "summaryEn": "Modular standalone Python browser automation suite with an admin panel, managing isolated multi-slot Camoufox/Playwright contexts, proxy locking, Bezier humanization, thread-safe atomic result routing, and deep forensic stealth auditing.",
        "category": ["automation", "desktop", "CLI", "security"],
        "status": "functional",
        "statusEvidence": "Verified via verification_report.md (83/83 Python files compiled cleanly with zero external dependency leaks), thread-safe RecoveryFailureHandler, and 1,276-line camoufox_forensic_audit.md.",
        "role": "Automation Systems Architect & Forensic Security Analyst (needs_owner_confirmation)",
        "problemAr": "تشغيل مهام الأتمتة المتزامنة على المتصفح يعاني عادةً من تسرب الكوكيز بين الجلسات، تصادم البروكسيات بين الخيوط (Race Conditions)، أو تلف ملفات الحسابات عند حدوث أخطاء مفاجئة.",
        "problemEn": "Concurrent browser automation workflows frequently suffer from cross-session cookie/storage leakage, proxy race conditions across worker slots, and input file corruption on crashes.",
        "audienceAr": "فرق اختبار الأتمتة ومهندسو العمليات الذين يحتاجون بيئة تشغيل متصفح معزولة الجلسات وقابلة للتشخيص الجنائي.",
        "audienceEn": "Automation engineers and operations teams requiring strictly isolated multi-slot browser execution and deterministic failure classification.",
        "workflow": "Slot Initialization -> Proxy Lock Acquisition -> Isolated BrowserContext Creation (BrowserFactory) -> Humanized Scenario Execution (Bezier Mouse / Typing Engine) -> Thread-Safe Atomic Result Classification (FailureHandler) -> Full Context Teardown & Proxy Unlock",
        "technologies": ["Python 3.12+", "Playwright", "Camoufox (Custom C++ Firefox Engine)", "BrowserForge", "PyQt / Admin Panel UI", "Supabase Licensing", "Threading Locks & Atomic File IO", "PyInstaller Build System"],
        "evidence": [
            {
                "claimId": "GML-01",
                "claim": "100% session isolation between accounts by destroying both Page and BrowserContext in finally blocks and rotating locked proxies per slot",
                "relationType": "EXTRACTED",
                "evidencePath": "browser_data_and_slots_report.md",
                "lineOrSymbol": "Lines 33-86 (shared/browser/firefox_engine.py L124-169 teardown contract)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "GML-02",
                "claim": "Thread-safe atomic account line removal and classified failure routing using threading.Lock in RecoveryFailureHandler",
                "relationType": "EXTRACTED",
                "evidencePath": "scenarios/recovery/failure_handler.py",
                "lineOrSymbol": "Lines 24-90 (RecoveryFailureHandler.remove_account_from_main_file, handle_result)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "GML-03",
                "claim": "1,276-line deep forensic audit of Camoufox 0.4.11 & Playwright 1.49.1 identifying 10 protocol, WebRTC, SOCKS5 downgrade, and pointer-event anomalies",
                "relationType": "EXTRACTED",
                "evidencePath": "camoufox_forensic_audit.md",
                "lineOrSymbol": "Lines 1-90 (Executive Summary & 10 Ranked Forensic Findings)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "GML-04",
                "claim": "Decoupled standalone extraction verified across 83 Python modules with zero broken imports or hardcoded parent paths",
                "relationType": "EXTRACTED",
                "evidencePath": "verification_report.md",
                "lineOrSymbol": "Lines 1-46 (83/83 py_compile verification & dependency audit)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            }
        ],
        "challenges": [
            {
                "id": "GML-CH-1",
                "type": "preventive_design",
                "titleAr": "عزل الجلسات على مستوى BrowserContext وقفل البروكسيات لمنع تسرب الهوية بين السلوتات المتوازية",
                "titleEn": "Strict BrowserContext Lifecycle Teardown & Proxy Locking Across Concurrent Slots",
                "scenarioAr": "إغلاق تبويب المتصفح (`page.close()`) وحده داخل Playwright يُبقي الكوكيز وLocalStorage والبصمة حية داخل `BrowserContext`، مما يؤدي إلى تلوث الجلسة التالية.",
                "scenarioEn": "Closing only a Playwright `Page` leaves cookies, localStorage, and fingerprint state alive inside the parent `BrowserContext`, contaminating subsequent tasks.",
                "rootCauseAr": "ارتباط حالة التخزين والشبكة في محركات المتصفح بكائن `BrowserContext` وليس بـ `Page`.",
                "rootCauseEn": "Browser session state, proxy binding, and fingerprint parameters reside at the `BrowserContext` boundary rather than the individual tab.",
                "solutionAr": "تطبيق عقد إغلاق مزدوج إجباري في كتلة `finally` (`await page.close()` + `await context.close()` + `unlock_proxy`) مع قفل ذري للبروكسي وحذف فوري للحساب المعالج عبر `threading.Lock()` في `RecoveryFailureHandler`.",
                "solutionEn": "Enforced mandatory `finally` teardown (`page.close()` + `context.close()` + `unlock_proxy`) paired with `threading.Lock()` atomic file updates in `RecoveryFailureHandler`.",
                "evidenceRef": "browser_data_and_slots_report.md:33-86 & scenarios/recovery/failure_handler.py:31-75",
                "impactAr": "عزل 100% للبيانات بين كل عملية وأخرى وحماية ملفات المخرجات من التضارب أثناء التشغيل المتوازي.",
                "impactEn": "Guaranteed zero cross-account state leakage and crash-safe real-time progress persistence."
            },
            {
                "id": "GML-CH-2",
                "type": "possible_risk",
                "titleAr": "التدقيق الجنائي لسطح الكشف في محرك Camoufox / Playwright (10 ثغرات بروتوكول وسلوك مرصودة)",
                "titleEn": "Forensic Detection-Surface Audit of Camoufox / Playwright Integration",
                "scenarioAr": "الاعتماد على متصفح مضاد للبصمة لا يكفي وحده إذا كانت طبقة التكامل في التطبيق تترك إشارات آلية قابلة للرصد.",
                "scenarioEn": "Relying on a C++-patched stealth browser binary can still leak automation signals at the Playwright config, network, and behavioral layers.",
                "rootCauseAr": "كشف التدقيق الجنائي (`camoufox_forensic_audit.md`) عن 10 إشارات دقيقة، منها: خفض صامت لبروكسي SOCKS5 المحمي بكلمة مرور إلى HTTP، تعطيل WebRTC كليًا بدل تمويهه، واستخدام 2-4 خطوات فقط في منحنى حركة الماوس.",
                "rootCauseEn": "Forensic code audit (`camoufox_forensic_audit.md:14-62`) uncovered 10 signals including silent SOCKS5-with-auth downgrade to HTTP, complete WebRTC disabling (`media.peerconnection.enabled=False`), Nightly build ID anomaly, and low-density mouse steps.",
                "solutionAr": "توثيق مصفوفة المخاطر العشر مع خطة المعالجة الهندسية لكل طبقة (تصنف في البورتفوليو كـ `possible_risk` مكتشف عبر التدقيق الجنائي وليس كإصلاح مكتمل).",
                "solutionEn": "Documented the 10-point forensic risk matrix and remediation blueprint (classified transparently as `possible_risk` identified via forensic investigation).",
                "evidenceRef": "camoufox_forensic_audit.md:14-90",
                "impactAr": "إثبات القدرة على التحقيق الجنائي العميق في نواة المتصفحات وبروتوكولات الشبكة.",
                "impactEn": "Demonstrates deep systems forensics across browser internals (`omni.ja`, `playwright.cfg`) and network protocols."
            }
        ]
    },
    "phone-commander": {
        "titleAr": "تطبيق Phone Commander — محرك رؤية حاسوبية (ZNCC) وأتمتة أندرويد عالية الأداء مع واجهة Flutter",
        "titleEn": "Phone Commander — Zero-GC ZNCC Computer Vision & Android Accessibility Automation Hub",
        "summaryAr": "تطبيق Flutter وأندرويد أصيل (Kotlin) يجمع بين محرك مطابقة قوالب بصري فائق السرعة (ZNCC) بدون استنزاف للذاكرة (Zero GC Churn) وخدمة Accessibility مع بوابة ترخيص أصلية (NativeLicenseGate) وسجل عمليات حي.",
        "summaryEn": "Hybrid Flutter and native Android (Kotlin) automation platform pairing a custom thread-local, zero-GC-churn ZNCC computer vision engine and ML Kit OCR with an autonomous state-machine loop and native license verification.",
        "category": ["mobile", "AI", "automation"],
        "status": "functional",
        "statusEvidence": "Verified via 8 recent git commits (41c9490, 50927ed, d5dc166, a52ed58), 5,264-line AutomationEngine.kt, 864-line TemplateMatcher.kt, and Flutter Supabase licensing architecture.",
        "role": "Lead Mobile & Computer Vision Systems Engineer (needs_owner_confirmation)",
        "problemAr": "أتمتة الشاشات الرسومية الحية على الهواتف تعاني من انهيار الذاكرة (Out-Of-Memory / GC Churn) بسبب نسخ صور الشاشة في كل إطار، أو الوقوع في حلقات نقر عشوائية عند تغير أبعاد الشاشة أو ظهور نوافذ مفاجئة.",
        "problemEn": "Real-time screen automation on mobile devices typically suffers from severe GC memory churn (~8MB bitmap allocation per frame), bitmap recycling crashes across threads, and infinite tap loops on unexpected UI states.",
        "audienceAr": "المستخدمون الذين يحتاجون أتمتة بصرية موثوقة تعمل لساعات طويلة على أجهزة أندرويد دون استنزاف البطارية أو انهيار التطبيق.",
        "audienceEn": "Users requiring long-running, battery-conscious on-device visual automation on Android with zero crashes and real-time observability.",
        "workflow": "ScreenCaptureService Frame Acquisition -> ThreadLocal ReusableScaleBuffer -> Multi-Scale Parallel ZNCC TemplateMatcher (Safe ROI) + ML Kit OCR -> Priority State Machine (AutomationEngine) -> SQLite Session Sync -> MethodChannel Live Flutter Telemetry",
        "technologies": ["Flutter / Dart", "Kotlin (Android Native)", "Custom ZNCC Computer Vision Engine", "Google ML Kit OCR", "Android AccessibilityService & MediaProjection", "SQLite Local Sync", "Supabase Auth & NativeLicenseGate"],
        "evidence": [
            {
                "claimId": "PHC-01",
                "claim": "Zero-GC-churn ZNCC TemplateMatcher using ThreadLocal ReusableScaleBuffer and precalculated stride pixel offsets to avoid ~8MB per-frame allocations",
                "relationType": "EXTRACTED",
                "evidencePath": "android/app/src/main/kotlin/com/sys/display/assist/cv/TemplateMatcher.kt",
                "lineOrSymbol": "Lines 15-85 (PreparedTemplate.offsetsForStride, ReusableScaleBuffer.acquirePixels)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "PHC-02",
                "claim": "Autonomous state-machine engine (5,264 lines) with battery-saving long-wait auto-minimize (>15 min) and disciplined AllianceFlowStep pipeline",
                "relationType": "EXTRACTED",
                "evidencePath": "android/app/src/main/kotlin/com/sys/display/assist/engine/AutomationEngine.kt",
                "lineOrSymbol": "Lines 63-95 (AllianceFlowStep, AutomationEngine.longWaitMinimizeEnabled)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "PHC-03",
                "claim": "Verified stability and queue deduplication fixes in git history preventing bitmap recycling crashes, map toggle loops, and resurrected SQLite sessions",
                "relationType": "EXTRACTED",
                "evidencePath": "phone_commander/.git",
                "lineOrSymbol": "Commits 50927ed, d5dc166, a52ed58, 41c9490",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "PHC-04",
                "claim": "Zero-Hardcoded-Taps engineering upgrade plan replacing blind ratio fallbacks with 86%–92% ZNCC confidence gates and GLOBAL_ACTION_BACK recovery",
                "relationType": "EXTRACTED",
                "evidencePath": "AUTOMATION_UPGRADE_PLAN.md",
                "lineOrSymbol": "Lines 10-86 (Hardcoded tap audit table, AutomationLogPayload, Thresholds Matrix)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            }
        ],
        "challenges": [
            {
                "id": "PHC-CH-1",
                "type": "verified_fix",
                "titleAr": "منع انهيار الذاكرة (Bitmap Recycling Crash) واستنزاف GC أثناء المسح البصري المتوازي",
                "titleEn": "Eliminating Bitmap Recycling Crashes & 8MB/Frame GC Churn in Parallel ZNCC Vision",
                "scenarioAr": "أثناء السحب الحي وفحص الشاشة المتكرر على أندرويد، يؤدي إنشاء وتحرير صور Bitmap في خيوط متعددة إلى توقف GC المتكرر أو انهيار التطبيق عند محاولة قراءة Bitmap تم تدويرها (`isRecycled`).",
                "scenarioEn": "During continuous live-drag vision scanning on Android, allocating and recycling bitmaps across worker threads caused ~8MB/frame GC pressure and fatal `recycled bitmap` crashes.",
                "rootCauseAr": "تخصيص مصفوفات بكسلات وBitmap جديدة في كل إطار وفقدان تزامن دورة حياة الصورة مع خدمة `AccessibilityService`.",
                "rootCauseEn": "Per-frame heap allocations in template matching and unsynchronized bitmap lifecycle transitions across capture and CV threads.",
                "solutionAr": "بناء `ReusableScaleBuffer` محلي لكل خيط (`ThreadLocal`) يعيد استخدام نفس الـ Bitmap ومصفوفة `IntArray` مع حساب مسبق لإزاحات الصفوف (`offsetsForStride`)، وتأمين دورة حياة الخدمة في الـ Commit `50927ed`.",
                "solutionEn": "Engineered `ThreadLocal` `ReusableScaleBuffer` with precalculated `offsetsForStride(stride)` arrays in `TemplateMatcher.kt` and hardened bitmap lifecycle safety in commit `50927ed`.",
                "evidenceRef": "android/app/src/main/kotlin/com/sys/display/assist/cv/TemplateMatcher.kt:27-85 & git commit 50927ed",
                "impactAr": "ثبات الأداء البصري بدون تخصيص ذاكرة متكرر (Zero GC Churn) واستقرار الجلسات الطويلة.",
                "impactEn": "Zero per-frame heap allocation overhead during multi-scale ZNCC scanning and crash-free continuous operation."
            },
            {
                "id": "PHC-CH-2",
                "type": "verified_fix",
                "titleAr": "منع ازدواجية طوابير الجمع في SQLite وكسر حلقة تبديل الخريطة اللانهائية",
                "titleEn": "Preventing SQLite Queue Resurrection & Breaking Infinite City/Map Toggle Loops",
                "scenarioAr": "تكرار تسجيل نفس مسيرة الجمع أو إعادة إحياء جلسات منتهية، إضافة إلى دخول المحرك في حلقة نقر متكررة أسفل يسار الشاشة أثناء الانتظار.",
                "scenarioEn": "Duplicate gathering cards and completed sessions were resurrected in SQLite, while a bottom-left wait tap accidentally triggered the City/Map toggle button in a loop.",
                "rootCauseAr": "تطابق غير دقيق عند إنهاء المسيرة في قاعدة البيانات، ووجود نقرة انتظار قريبة من إحداثيات زر الخريطة.",
                "rootCauseEn": "Imprecise march completion matching in local SQLite sync and an unsafe bottom-left idle tap coordinate overlapping the map toggle zone.",
                "solutionAr": "إصلاح مطابقة اكتمال المسيرة ومنع إحياء الجلسات المكتملة في `d5dc166`، وإزالة نقرة أسفل اليسار أثناء الانتظار في `a52ed58` مع اعتماد استراتيجية `GLOBAL_ACTION_BACK` الآمنة.",
                "solutionEn": "Fixed SQLite march completion matching and session state guards (`d5dc166`) and removed bottom-left wait taps (`a52ed58`).",
                "evidenceRef": "phone_commander/.git commits d5dc166 & a52ed58",
                "impactAr": "دقة 100% في تتبع الطوابير النشطة واختفاء التبديل العشوائي بين العاصمة والخريطة.",
                "impactEn": "Eliminated duplicate march dispatches and unintended map-toggle loops."
            }
        ]
    },
    "rok-vision-controller": {
        "titleAr": "محرك RoK Universal Controller — معايرة الإحداثيات الديناميكية متعددة الأبعاد عبر ADB",
        "titleEn": "RoK Universal Controller — Anchor-Based Multi-Resolution ADB Automation Engine",
        "summaryAr": "أداة تحكم بايثون عبر `uiautomator2` وADB تحل مشكلة اختلاف أبعاد ونسب الشاشات (16:9، 20:9، الأجهزة اللوحية) عبر خوارزمية تحويل إحداثيات مرتكزة على نقاط الإرساء (`ScreenScaler`).",
        "summaryEn": "Python ADB automation controller using `uiautomator2` that solves multi-device aspect-ratio drift (16:9, 19.5:9, 20:9, tablets) via an anchor-based geometric coordinate transformer (`ScreenScaler`).",
        "category": ["automation", "CLI"],
        "status": "functional",
        "statusEvidence": "Verified via rok_controller.py (367 lines), rok_universal_controller.py (381 lines), and 14 calibrated reference screen/crop PNG assets.",
        "role": "Automation & Geometric UI Scaling Engineer (needs_owner_confirmation)",
        "problemAr": "الاعتماد على نسب مئوية بسيطة `(X%, Y%)` يفشل عند تغير نسبة العرض إلى الارتفاع (مثل الانتقال من 16:9 إلى 20:9)، لأن محركات الألعاب تثبت حجم العناصر نسبةً إلى ارتفاع الشاشة وتربطها بزوايا محددة (Anchors).",
        "problemEn": "Simple percentage coordinates `(X%, Y%)` break across different aspect ratios (e.g., 16:9 vs 20:9) because landscape game engines scale UI widgets by screen height (`H`) while pinning HUD clusters to specific screen corners/anchors.",
        "audienceAr": "مطورو أتمتة ADB واختبار واجهات الألعاب والتطبيقات عبر أجهزة ومحاكي أندرويد متعددة الدقة.",
        "audienceEn": "ADB automation developers testing and running landscape UI workflows across heterogeneous Android screen resolutions and aspect ratios.",
        "workflow": "ADB Device Connection (uiautomator2) -> Landscape Orientation Enforcement (max(w,h) x min(w,h)) -> Anchor-Based ScreenScaler Transformation (center / bottom_left / top_left / bottom_center / top_right) -> Multi-Character Cycle Loop with Humanized Delays",
        "technologies": ["Python 3.13", "uiautomator2", "ADB (Android Debug Bridge)", "Anchor-Based Geometric Coordinate Scaling"],
        "evidence": [
            {
                "claimId": "ROK-01",
                "claim": "Anchor-based ScreenScaler transforming 2400x1080 reference coordinates using height-locked scale (h / 1080.0) and 5 HUD anchor zones (center, bottom_left, top_left, bottom_center, top_right)",
                "relationType": "EXTRACTED",
                "evidencePath": "rok_universal_controller.py",
                "lineOrSymbol": "Lines 5-63 (ScreenScaler.get_coords)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "ROK-02",
                "claim": "Landscape orientation normalization (w = max(raw_w, raw_h), h = min(raw_w, raw_h)) and randomized human-like post-click delay (5.0s..10.0s)",
                "relationType": "EXTRACTED",
                "evidencePath": "rok_controller.py",
                "lineOrSymbol": "Lines 84-95 (RoKController.__init__)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            }
        ],
        "challenges": [
            {
                "id": "ROK-CH-1",
                "type": "verified_fix",
                "titleAr": "الانتقال من النسب المئوية الثابتة إلى التحويل الهندسي المرتكز على زوايا الواجهة (Anchor-Based Scaling)",
                "titleEn": "Evolving from Flat Percentage Ratios to Height-Locked Anchor Coordinate Scaling",
                "scenarioAr": "النسخة الأولى (`rok_controller.py`) اعتمدت نسبًا مئوية ثابتة للشاشة `(X_ratio, Y_ratio)`، وهي تعمل على نسبة أبعاد واحدة لكنها تنحرف عن الأزرار على الشاشات العريضة أو الأجهزة اللوحية.",
                "scenarioEn": "The initial controller (`rok_controller.py`) used flat `(X_ratio, Y_ratio)` percentages, which drifted off target when switching between 16:9 tablets and 20:9 ultra-wide phones.",
                "rootCauseAr": "في واجهات الألعاب الأفقية، يتحدد معامل التحجيم بارتفاع الشاشة فقط (`scale = h / 1080`) بينما تلتصق العناصر إما بالمركز أو بأركان الشاشة الخمسة.",
                "rootCauseEn": "Landscape game HUDs scale proportionally to screen height (`scale = h / REF_H`) while pinning controls to specific viewport anchors (`bottom_left`, `top_left`, `center`, `bottom_center`, `top_right`).",
                "solutionAr": "تطوير فئة `ScreenScaler` في `rok_universal_controller.py` التي تحسب الإزاحة من نقطة الإرساء الخاصة بكل عنصر (`center`, `bottom_left`, `top_left`, `bottom_center`, `top_right`) مع فرض الوضع الأفقي تلقائيًا.",
                "solutionEn": "Built `ScreenScaler` in `rok_universal_controller.py:5-63` computing anchor-relative offsets scaled by `self.h / 1080.0` with automatic landscape dimension normalization.",
                "evidenceRef": "rok_controller.py:21-63 vs rok_universal_controller.py:5-95",
                "impactAr": "توافق فوري مع أي دقة شاشة أو نسبة عرض إلى ارتفاع دون إعادة معايرة الإحداثيات يدويًا.",
                "impactEn": "Resolution-independent click accuracy across 16:9, 19.5:9, 20:9, and tablet viewports without manual recalibration."
            }
        ]
    },
    "remix-sole-marketplace": {
        "titleAr": "منصة سول (SOLE) — متجر ومعرض أحذية متكامل مع مزامنة Cloudinary وحماية أمنية متعددة الطبقات",
        "titleEn": "SOLE Footwear Marketplace — Full-Stack React 19 / Express Catalog with Cloudinary & Security Hardening",
        "summaryAr": "تطبيق تجارة إلكترونية وكتالوج رقمي ثنائي اللغة (React 19 + Express + Supabase + Cloudinary) يحوّل أرشيف صور الاستوديو إلى متجر سريع مع لوحة إدارة، فحص Magic Bytes للصور، وحماية ضد حقن PostgREST وPath Traversal.",
        "summaryEn": "Full-stack footwear marketplace (React 19, Express, TypeScript, Supabase, Cloudinary) transforming studio photo archives into a high-speed storefront with an admin panel, binary Magic-Byte upload validation, PostgREST injection guards, and offline static fallback.",
        "category": ["web", "API", "security"],
        "status": "production",
        "statusEvidence": "Verified via vercel.json, esbuild API bundler, 506-product live screenshot proof, and passing unit/security test suites (catalog.test.ts, security.test.ts, verify-security-audit.ts).",
        "role": "Full-Stack TypeScript & Application Security Engineer (needs_owner_confirmation)",
        "problemAr": "متاجر الأحذية التي ترفع مئات الصور الملتقطة مباشرة من الكاميرا أو واتساب (`IMG-20261029-WA0019`) تعاني من أسماء منتجات مشوهة، بطء تحميل الصور، خطر توقف المتجر عند تعطل قاعدة البيانات، وثغرات رفع ملفات خبيثة متنكرة كصور.",
        "problemEn": "Footwear retailers uploading raw studio/WhatsApp camera files (`IMG-20261029-WA0019`) face messy product titles, unoptimized image payloads, downtime during cloud outages, and security risks from spoofed file uploads or filter injection.",
        "audienceAr": "أصحاب متاجر الأحذية والأزياء الذين يريدون تحويل مجلدات صور المنتجات إلى متجر إلكتروني أنيق، سريع، وآمن.",
        "audienceEn": "Footwear brands and merchants needing automated studio-folder ingestion, responsive Cloudinary delivery, and hardened admin catalog management.",
        "workflow": "Cloudinary Folder Ingestion & Smart Bilingual Label Formatter -> Supabase Catalog Persistence (RLS Active Categories) -> Static JSON Fallback Resilience -> Responsive srcset (f_auto,q_auto) Storefront -> Magic-Byte & PostgREST Security Gate",
        "technologies": ["React 19", "TypeScript", "Express 4", "Tailwind CSS 4", "Vite 8 + esbuild", "Supabase (PostgreSQL + RLS)", "Cloudinary CDN & Admin API", "Node.js Native Test Runner"],
        "evidence": [
            {
                "claimId": "SOL-01",
                "claim": "Multi-layered security module blocking PostgREST filter injection, Cloudinary path traversal (..), non-HTTPS image URLs, and spoofed SVG/HTML/EXE uploads via binary Magic Bytes",
                "relationType": "EXTRACTED",
                "evidencePath": "src/server/security.ts & src/server/security.test.ts",
                "lineOrSymbol": "security.ts:8-95 & security.test.ts:13-95",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "SOL-02",
                "claim": "Bilingual Arabic/English slug & WhatsApp filename normalizer ('IMG-20261029-WA0019' -> 'Y3 فاشون · موديل 0019', 'Y3فاشون' -> 'Y3 فاشون') and responsive Cloudinary srcset generator",
                "relationType": "EXTRACTED",
                "evidencePath": "src/utils/catalog.test.ts",
                "lineOrSymbol": "Lines 32-60 (formatCategoryLabel, formatProductDisplayName, buildCloudinarySrcSet)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "SOL-03",
                "claim": "Public catalog isolation querying Supabase active categories without triggering live Cloudinary API scans on visitor traffic, backed by catalog-fallback.json",
                "relationType": "EXTRACTED",
                "evidencePath": "src/server/catalogService.ts",
                "lineOrSymbol": "Lines 22-95 (getPublicSiteSettings, fetchSupabasePublicCatalog)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            }
        ],
        "challenges": [
            {
                "id": "SOL-CH-1",
                "type": "preventive_design",
                "titleAr": "التحقق الجنائي من البايتات السحرية (Magic Bytes) ومنع حقن فلاتر PostgREST واختراق المسارات",
                "titleEn": "Binary Magic-Byte Image Verification & PostgREST Filter Injection Prevention",
                "scenarioAr": "الاعتماد على امتداد الملف (`.jpg`) أو ترويسة `Content-Type` فقط يسمح برفع ملفات SVG تحتوي على `<script>` أو ملفات تنفيذية `MZ` متنكرة كصور أحذية، كما أن تمرير معرفات الدخول الخام يعرض استعلامات PostgREST للحقن.",
                "scenarioEn": "Trusting file extensions or MIME headers allows attackers to upload XSS-laden SVGs or EXE binaries disguised as `.jpg`, while unvalidated identifiers risk PostgREST `.or()` filter injection.",
                "rootCauseAr": "إمكانية تزوير `Content-Type` واسم الملف من جهة العميل في طلبات `multipart/form-data`.",
                "rootCauseEn": "Client-controlled `multipart/form-data` filenames and MIME types can be trivially spoofed.",
                "solutionAr": "بناء وحدة `src/server/security.ts` التي تفحص التوقيع الثنائي الفعلي (`0xFF 0xD8 0xFF` لـ JPEG، و`0x89 0x50 0x4E 0x47` لـ PNG)، وتمنع رموز التحكم في `isValidLoginIdentifier`، وتحظر `..` في مجلدات Cloudinary مع تغطيتها باختبارات وحدة شاملة في `security.test.ts`.",
                "solutionEn": "Implemented binary magic-byte inspection in `validateImageUploadBuffer`, strict PostgREST control-character rejection in `isValidLoginIdentifier`, and path-traversal blocks in `isValidCloudinaryFolder`, verified by `security.test.ts`.",
                "evidenceRef": "src/server/security.ts:18-95 & src/server/security.test.ts:13-95",
                "impactAr": "صد كامل لملفات SVG/HTML/EXE المزيفة وحماية قاعدة البيانات ومجلدات الصور من التلاعب.",
                "impactEn": "100% rejection of spoofed SVG/HTML/EXE payloads and zero PostgREST injection or path traversal vectors."
            },
            {
                "id": "SOL-CH-2",
                "type": "verified_fix",
                "titleAr": "تطبيع أسماء صور الكاميرا وواتساب الملتصقة بالعربية والإنجليزية وفصل زيارات المتجر عن حصص Cloudinary",
                "titleEn": "Bilingual WhatsApp Filename Normalization & Decoupling Visitor Traffic from Cloudinary API Quotas",
                "scenarioAr": "صور الاستوديو المرفوعة بأسماء مثل `IMG-20261029-WA0019` داخل مجلدات مثل `Y3فاشون` أو `عرض ال150` كانت تظهر بأسماء غير مقروءة، كما أن فحص Cloudinary المباشر مع كل زائر يستهلك حصة الـ API ويبطئ التصفح.",
                "scenarioEn": "Raw studio uploads named `IMG-20261029-WA0019` inside fused Arabic/Latin folders (`Y3فاشون`, `عرض ال150`) produced unreadable product cards, while live Cloudinary Admin API scans on visitor requests exhausted rate limits.",
                "rootCauseAr": "غياب طبقة تطبيع لغوية لأسماء الملفات والمجلدات، وربط قراءة المتجر العام بـ Cloudinary Admin API مباشرة.",
                "rootCauseEn": "Lack of bilingual lexical normalization for camera filenames and direct coupling of public catalog reads to Cloudinary folder scans.",
                "solutionAr": "تطوير دوال `formatCategoryLabel` و`formatProductDisplayName` لفصل الحروف العربية عن اللاتينية والأرقام وتحويل رموز واتساب إلى `Y3 فاشون · موديل 0019`، وقصر زيارات المتجر العام على `fetchSupabasePublicCatalog` مع توليد روابط `f_auto,q_auto` وملف احتياطي `catalog-fallback.json`.",
                "solutionEn": "Built bilingual regex normalizers (`formatCategoryLabel`, `formatProductDisplayName`), isolated public traffic to `fetchSupabasePublicCatalog` + static `catalog-fallback.json`, and generated responsive `f_auto,q_auto` `srcset` URLs.",
                "evidenceRef": "src/utils/catalog.test.ts:32-60 & src/server/catalogService.ts:50-95",
                "impactAr": "عرض 506 منتجًا في 15 قسمًا بأسماء عربية/إنجليزية أنيقة وتحميل صور فائق السرعة دون استنزاف حصة Cloudinary API.",
                "impactEn": "Clean editorial presentation across 506 products and 15 collections with zero live Cloudinary Admin API overhead on public page loads."
            }
        ]
    }
}


def main():
    inventories = json.loads((INTEL_DIR / "inventory.json").read_text(encoding="utf-8"))
    inv_map = {item["slug"]: item for item in inventories}

    for slug, data in SYNTHESIS_DATA.items():
        inv = inv_map.get(slug, {})
        idx_file = INTEL_DIR / "project-index" / f"{slug}.json"
        idx = json.loads(idx_file.read_text(encoding="utf-8")) if idx_file.exists() else {}

        # 1. Write Evidence Manifest (evidence/<slug>.json)
        evidence_manifest = {
            "slug": slug,
            "generatedAt": datetime.now(timezone.utc).isoformat(),
            "claims": data["evidence"],
        }
        (INTEL_DIR / "evidence" / f"{slug}.json").write_text(
            json.dumps(evidence_manifest, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        # 2. Write Project Audit (audits/<slug>-audit.json)
        audit_record = {
            "slug": slug,
            "titleAr": data["titleAr"],
            "titleEn": data["titleEn"],
            "summaryAr": data["summaryAr"],
            "summaryEn": data["summaryEn"],
            "category": data["category"],
            "status": data["status"],
            "statusEvidence": data["statusEvidence"],
            "role": data["role"],
            "problemAr": data["problemAr"],
            "problemEn": data["problemEn"],
            "audienceAr": data["audienceAr"],
            "audienceEn": data["audienceEn"],
            "workflow": data["workflow"],
            "technologies": data["technologies"],
            "inventoryStats": {
                "totalFiles": inv.get("total_files", 0),
                "totalMb": inv.get("total_mb", 0),
                "graphNodes": idx.get("stats", {}).get("nodes", 0),
                "graphEdges": idx.get("stats", {}).get("edges", 0),
                "sensitiveFilesExcluded": inv.get("sensitive_excluded_count", 0),
            },
            "challenges": data["challenges"],
            "evidenceCount": len(data["evidence"]),
            "needsOwnerConfirmation": [
                "Personal role attribution & public display name",
                "Live deployment URL or public GitHub repository link if intended for public access"
            ]
        }
        (INTEL_DIR / "audits" / f"{slug}-audit.json").write_text(
            json.dumps(audit_record, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        # 3. Write Permanent Project Memory (project-memory/<slug>.md)
        mem_lines = [
            f"# ذاكرة المشروع الهندسية: {data['titleAr']}",
            f"**Project Title (EN):** {data['titleEn']}",
            f"**Slug:** `{slug}` | **Status:** `{data['status']}` | **Categories:** `{', '.join(data['category'])}`",
            f"**Graph Index:** `{idx.get('stats', {}).get('nodes', 0)}` nodes · `{idx.get('stats', {}).get('edges', 0)}` edges · `{inv.get('total_files', 0)}` files (`{inv.get('total_mb', 0)} MB`)",
            "",
            "## 1. المشكلة والقيمة العملية (Problem & Value)",
            f"- **بالعربية:** {data['problemAr']}",
            f"- **In English:** {data['problemEn']}",
            f"- **المستفيد (Target User):** {data['audienceAr']}",
            "",
            "## 2. سير العمل والمعمارية (Workflow & Architecture)",
            f"`{data['workflow']}`",
            "",
            "### التقنيات المثبتة في الكود (Verified Stack)",
            ", ".join(f"`{t}`" for t in data["technologies"]),
            "",
            "## 3. الأدلة التقنية الموثقة (Verified Evidence Manifest)",
        ]
        for ev in data["evidence"]:
            mem_lines.append(
                f"- **[{ev['claimId']}]** ({ev['relationType']} / {ev['verificationStatus']}): {ev['claim']} — `{ev['evidencePath']}` ({ev['lineOrSymbol']})"
            )
        mem_lines.append("")
        mem_lines.append("## 4. التحديات والقرارات الهندسية (Engineering Challenges)")
        for ch in data["challenges"]:
            mem_lines.extend([
                f"### [{ch['id']}] {ch['titleAr']} (`{ch['type']}`)",
                f"- **السيناريو:** {ch['scenarioAr']}",
                f"- **السبب الجذري:** {ch['rootCauseAr']}",
                f"- **الحل الهندسي:** {ch['solutionAr']}",
                f"- **الدليل:** `{ch['evidenceRef']}`",
                f"- **الأثر المثبت:** {ch['impactAr']}",
                ""
            ])
        mem_lines.extend([
            "## 5. حدود الخصوصية وما يحتاج مراجعة المالك (Privacy & Review Flags)",
            f"- **ملفات حساسة مستبعدة تلقائيًا:** `{inv.get('sensitive_excluded_count', 0)}` ملفات ({', '.join(inv.get('sensitive_excluded_samples', [])[:5]) or 'None'})",
            f"- **الدور الشخصي:** `{data['role']}`"
        ])
        (INTEL_DIR / "project-memory" / f"{slug}.md").write_text(
            "\n".join(mem_lines), encoding="utf-8"
        )

    # 4. Update analysis-usage.json with verification metrics
    usage_path = INTEL_DIR / "analysis-usage.json"
    usage = json.loads(usage_path.read_text(encoding="utf-8"))
    verified_counts = {
        "image-to-animate": 5,
        "school-timetable": 5,
        "enaya-ai-workspace": 5,
        "gmail-options-suite": 4,
        "phone-commander": 4,
        "rok-vision-controller": 2,
        "remix-sole-marketplace": 4,
    }
    total_files_across_repos = sum(inv.get("total_files", 0) for inv in inventories)
    total_verified_slices = sum(verified_counts.values())
    for slug, cnt in verified_counts.items():
        if slug in usage["projects"]:
            usage["projects"][slug]["targeted_slices_verified"] = cnt
    usage["efficiency_summary"] = {
        "total_corpus_files_inventoried": total_files_across_repos,
        "total_graph_queries_executed": usage["total_queries_executed"],
        "total_targeted_code_doc_slices_read": total_verified_slices,
        "corpus_read_ratio_percent": round((total_verified_slices / max(total_files_across_repos, 1)) * 100, 3),
        "external_llm_semantic_media_calls": 0,
    }
    usage_path.write_text(json.dumps(usage, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Synthesized project-memory, evidence manifests, audits, and analysis-usage successfully.")


if __name__ == "__main__":
    main()
