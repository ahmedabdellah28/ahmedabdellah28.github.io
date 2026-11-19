import json
from pathlib import Path

WORKSPACE = Path.cwd()
PORTFOLIO_ROOT = WORKSPACE / "portfolio"
CONTENT_DIR = PORTFOLIO_ROOT / "src" / "content" / "projects"
CONTENT_DIR.mkdir(parents=True, exist_ok=True)

PROJECTS_CONTENT = [
    {
        "slug": "image-to-animate",
        "titleAr": "AION Studio — إنتاج الموشن جرافيك آليًا",
        "titleEn": "AION Studio — Automated Motion Graphics Engine",
        "summaryAr": "خط إنتاج برمجي متكامل يحوّل النصوص ولوحات القصة (Storyboards) إلى فيديوهات موشن جرافيك 16:9 ومقاطع Shorts 9:16 عبر مترجم رسومي من 10 مراحل (ECGC) ومحرك EffectCraft GPU ومحاذاة صوتية على مستوى الكلمة.",
        "summaryEn": "End-to-end CLI-first production engine converting scripts and storyboards into 16:9 whiteboard explainers and 9:16 shorts via a 10-stage ECGC compiler, EffectCraft GPU renderer, and word-level Faster-Whisper synchronization.",
        "valuePropositionAr": "تحويل النص الخام ولوحة القصة إلى فيديو موشن جرافيك كامل (1080p/720p) متزامن صوتيًا وبصريًا عبر 13 مرحلة محكومة بعقود برمجية دون مونتاج يدوي.",
        "valuePropositionEn": "Transforms raw scripts and storyboards into broadcast-ready 16:9 explainers and 9:16 shorts through a 13-stage contract-gated GPU pipeline without manual timeline editing.",
        "category": ["AI", "media", "automation", "CLI"],
        "status": "production",
        "visibility": "published",
        "featured": True,
        "featuredOrder": 1,
        "role": {
            "ar": "تصميم المعمارية وتطوير خط الإنتاج والمترجم الرسومي",
            "en": "System Architecture, Pipeline & Graphics Compiler Engineering"
        },
        "audience": {
            "ar": "استوديوهات المحتوى التعليمي والوثائقي وصناع الفيديو الذين يحتاجون إنتاجًا متسقًا وقابلًا للتكرار.",
            "en": "Educational and documentary studios and content creators needing deterministic, repeatable video production."
        },
        "problem": {
            "ar": "إنتاج فيديو شرح موشن جرافيك واحد يتطلب عادةً قص عشرات العناصر يدويًا، ضبط توقيت ظهور كل رسمة مع الكلمة المنطوقة بالثانية، تحريك الكاميرا، وخفض المؤثرات الصوتية تحت صوت الراوي — وهي عملية تستغرق أيامًا وعرضة للأخطاء عند أي تعديل في النص.",
            "en": "Producing a single whiteboard motion-graphics explainer manually requires cutting dozens of assets, keyframing every illustration to exact spoken words, choreographing camera moves, and ducking SFX under narration — taking days and breaking whenever the script changes."
        },
        "solution": {
            "ar": "بناء محرك AION Studio V6 المدار عبر CLI من 13 مرحلة: يولد التعليق الصوتي بمعيار -15 LUFS، ويستخرج توقيت كل كلمة عبر Faster-Whisper، ويقص عناصر اللوحة بدقة 3x HD عبر PhotoCraft، ثم يبني مخطط المشهد (Scene Graph V2) ويترجمه عبر مترجم ECGC ذي الـ 10 مراحل إلى مشروع EffectCraft قابل للتعديل وفيديو MP4 مفحوص آليًا.",
            "en": "Engineered AION Studio V6, a 13-stage contract-driven pipeline: generates -15 LUFS voiceovers, extracts word-level timestamps via Faster-Whisper, isolates storyboard entities at 3x HD via PhotoCraft, synthesizes a Scene Graph V2, and compiles it via the 10-stage ECGC compiler into editable .ecproj files and QA-verified MP4 masters."
        },
        "manualVsAutomated": {
            "ar": "بدلًا من القص اليدوي والمزامنة السمعية إطارًا بإطار في برامج المونتاج، يربط المحرك آليًا 100% من الأصول المستخرجة بفترات الكلمات، ويفحص تباين البطاقات (Luma Contrast)، ويخلط الصوت مع خفض المؤثرات (RMS Ducking) ويتحقق من أن انحراف الصوت/الصورة أقل من 0.35 ثانية.",
            "en": "Replaces manual asset cutout and frame-by-frame timeline syncing with automated 100% asset-to-word semantic binding, programmatic card luma contrast validation, RMS envelope voice ducking, and automated 10-frame QA verification (<0.35s A/V drift)."
        },
        "capabilities": [
            {
                "ar": "مترجم رسومي من 10 مراحل (ECGC) يحوّل مخطط المشهد `aion.scene_graph.v2` إلى مشاريع EffectCraft GPU وفيديوهات 16:9 و9:16.",
                "en": "10-stage EffectCraft Creative Graphics Compiler (ECGC) translating `aion.scene_graph.v2` into GPU-rendered 16:9 masters and 9:16 viral shorts."
            },
            {
                "ar": "محاذاة صوتية دقيقة على مستوى الكلمة والجملة عبر Faster-Whisper مع حماية ضد بتر نهاية الصوت أو التكرار.",
                "en": "Word-level audio timing alignment via Faster-Whisper with duplicate/truncation guards and -15 LUFS normalization."
            },
            {
                "ar": "استخراج ذكي لعناصر لوحة القصة بدقة 3x HD مع إزالة الخلفية وبقايا الحواف المتجاورة الأقل من 60 بكسل.",
                "en": "Automated storyboard entity extraction at 3x HD with transparent background isolation and <60px neighbor-sliver cleanup."
            },
            {
                "ar": "بوابة فحص جودة آلية (QA Gate) تفحص الإطارات السوداء، وتباين الألوان، وانحراف الصوت، وتولّد لوحة معاينة من 10 إطارات.",
                "en": "Automated QA Gate checking black frames, luma contrast, audio clipping, A/V drift (<0.35s), and generating contact sheets."
            }
        ],
        "architecture": {
            "overviewAr": "تعتمد المعمارية على عقود مراحل صارمة (`PIPELINE_CONTRACTS.md`) حيث يعمل كل تشغيل داخل مجلد معزول `exports/runs/<run_id>/` مع سجل حالة مستقل وحماية ضد الكتابة فوق المشاريع الذهبية.",
            "overviewEn": "Built on strict stage contracts (`PIPELINE_CONTRACTS.md`) where every run executes inside an isolated `exports/runs/<run_id>/` directory with immutable manifests and write-protected golden baselines.",
            "pipelineSteps": [
                {
                    "step": "01–03",
                    "titleAr": "النص، الصوت، والتوقيت (Script -> Voice -> Timing)",
                    "titleEn": "Script, Voice (-15 LUFS) & Faster-Whisper Timing",
                    "detailAr": "تقسيم السكربت وتوليد صوت 48kHz PCM مع استخراج `timing_master.json` وملفات SRT كلمة بكلمة.",
                    "detailEn": "Validates section scripts, synthesizes 48kHz mono PCM voiceovers, and generates word-by-word timing masters."
                },
                {
                    "step": "04–07",
                    "titleAr": "استخراج الأصول والإخراج المشهدي (Extract -> Direct)",
                    "titleEn": "3x HD Asset Extraction & Scene Graph V2 Direction",
                    "detailAr": "فصل عناصر اللوحة بـ PhotoCraft، وبناء الخريطة الدلالية ومخطط المشهد `aion.scene_graph.v2` المفحوص بـ `audit_scene_graph`.",
                    "detailEn": "Extracts transparent entities, maps 100% of assets to timing windows, and validates `scene_graph.v2.json`."
                },
                {
                    "step": "08–11",
                    "titleAr": "المترجم الرسومي ECGC والخلط الصوتي والرندر",
                    "titleEn": "10-Stage ECGC Compilation, RMS Audio Mix & GPU Render",
                    "detailAr": "توليد المشتقات البصرية، وخلط المؤثرات مع خفض الصوت حول الكلام، وتوليد `.ecproj` وملف MP4 النهائي.",
                    "detailEn": "Compiles vector geometry, kinetic typography, camera paths, and RMS-ducked stereo mix into `.ecproj` and MP4."
                },
                {
                    "step": "12–13",
                    "titleAr": "فحص الجودة والدمج النهائي (QA & Documentary Merge)",
                    "titleEn": "Automated QA Contact Sheet & Master Documentary Merge",
                    "detailAr": "التحقق من سلامة الفيديو وإنتاج `qa_contact_sheet.png` قبل دمج الفصول في الفيديو الوثائقي الكامل.",
                    "detailEn": "Verifies A/V drift and layer integrity before concatenating all section masters into the final documentary."
                }
            ],
            "systemBoundariesAr": "يعمل المحرك محليًا عبر بايثون وFFmpeg ومحركات EffectCraft/PhotoCraft الثنائية، مع استخدام اختياري لـ Gemini API في توليد الصوت.",
            "systemBoundariesEn": "Executes locally on Windows via Python 3.13, FFmpeg/FFprobe, and native EffectCraft/PhotoCraft binaries, with optional Gemini API key rotation for TTS."
        },
        "technologies": [
            "Python 3.13",
            "EffectCraft GPU CLI",
            "PhotoCraft 3x HD",
            "Faster-Whisper",
            "Gemini TTS",
            "FFmpeg / FFprobe",
            "OpenCV",
            "JSON Schema Contracts"
        ],
        "challenges": [
            {
                "id": "ITA-CH-1",
                "type": "verified_fix",
                "titleAr": "معالجة تسطيح المشاهد وشبحية النصوص العربية وتداخل المؤثرات الصوتية في V5",
                "titleEn": "Fixing Narrative Scene Flattening, Arabic Text Ghosting & 3x SFX Flooding",
                "problemAr": "أظهرت مراجعة الجودة لمخرجات V5 تراجعًا إخراجيًا: تكدس القسم في مشهد واحد مسطح، وظهور كلمات عربية باهتة منزاحة (Ghosting) أثناء توسع البطاقات، وتداخل ~84 ضربة صوتية فوق صوت الراوي.",
                "problemEn": "V5 renders passed binary execution checks but exhibited narrative flattening into single scenes, ghosted Arabic text animators lagging behind card expansion, and ~84 overlapping SFX hits drowning the narrator.",
                "whyImportantAr": "في المحتوى التعليمي والوثائقي، أي تشوه في قراءة النص العربي أو ضجيج يغطي على صوت المعلق يفقد الفيديو قيمته حتى لو كان الرندر سريعًا.",
                "whyImportantEn": "In educational explainers, broken Arabic caption legibility or un-ducked SFX collisions destroy viewer comprehension regardless of rendering speed.",
                "solutionAr": "إجراء تحقيق جنائي موثق لـ 8 أعطال جذرية (`V5_GOLD_REGRESSION_RCA_AR.md`): استعادة تجميع المشاهد السردية، ومزامنة `TypographyCompiler` مع زمن فتح البطاقات، وتثبيت 30fps من عقد المشروع، وتوجيه الصوت عبر `mix_scene_graph_audio` مع خفض تلقائي للمؤثرات (RMS Ducking).",
                "solutionEn": "Conducted an 8-point forensic RCA (`V5_GOLD_REGRESSION_RCA_AR.md`): restored narrative scene grouping, synchronized `TypographyCompiler` reveal windows, enforced 30fps contract inheritance, and routed audio through `mix_scene_graph_audio` with RMS envelope voice ducking.",
                "proofRef": "V5_GOLD_REGRESSION_RCA_AR.md:15-90 & core/aion/ecgc_compiler.py:39-71",
                "impactAr": "اجتياز بوابات الفحص الآلي (86 طبقة، انحراف صوت/صورة أقل من 0.35 ثانية) واستعادة جودة الإخراج المرجعي الذهبي.",
                "impactEn": "Passed automated QA gates (86 layers, A/V drift <0.35s, zero voice truncation) and restored golden-reference visual choreography.",
                "lessonAr": "فحوص النجاح الثنائية (Pass/Fail) لا تكفي في الأنظمة الإبداعية؛ يجب تضمين ثوابت الإخراج (تباين اللوما، كثافة المؤثرات، وتزامن النصوص) داخل عقود المترجم نفسه.",
                "lessonEn": "Binary render checks are insufficient for creative engines; editorial invariants (luma contrast, SFX density, and text-card reveal sync) must be enforced inside compiler contracts."
            },
            {
                "id": "ITA-CH-2",
                "type": "preventive_design",
                "titleAr": "حماية المشاريع المرجعية الذهبية وعزل مجلدات التشغيل (Per-Run Isolation)",
                "titleEn": "Write-Protected Golden Reference Baselines & Isolated Per-Run Ledgers",
                "problemAr": "تعديل خوارزميات التحريك أو الإضاءة قد يؤدي عن طريق الخطأ إلى الكتابة فوق المخرجات المرجعية المعتمدة أو خلط الملفات الوسيطة بين تشغيلين.",
                "problemEn": "Iterative tuning of motion or lighting compilers risks overwriting approved baseline renders or contaminating intermediate files across runs.",
                "whyImportantAr": "منع فقدان النسخ المعتمدة وضمان إمكانية المقارنة الدقيقة (A/B) بين أي إصدارين للمحرك.",
                "whyImportantEn": "Prevents irreversible loss of golden baselines and enables deterministic A/B regression testing across compiler versions.",
                "solutionAr": "عزل كل تشغيل في `exports/runs/<run_id>/` مع سجل `run_manifest.json`، وفرض حماية برمجية في `studio_cli` ترفع `PermissionError` عند محاولة الكتابة على المشروع الذهبي `mind_glitches_ar`.",
                "solutionEn": "Isolated all outputs under `exports/runs/<run_id>/` tracked by `run_manifest.json` and enforced a programmatic `PermissionError` guard on `projects/mind_glitches_ar`.",
                "proofRef": "PIPELINE_CONTRACTS.md:27-36 & core/aion/contracts.py:64-90",
                "impactAr": "صفر تلف في المشاريع المرجعية وإمكانية التراجع الفوري (Rollback) عند فشل أي مرحلة.",
                "impactEn": "Zero baseline corruption and instant rollback safety across multi-run documentary productions.",
                "lessonAr": "حماية البيانات المرجعية في الكود (`PermissionError`) أقوى وأضمن من الاعتماد على الحذر البشري أثناء التجارب.",
                "lessonEn": "Enforcing baseline immutability in code (`PermissionError`) is far safer than relying on operator caution during rapid experimentation."
            }
        ],
        "evidence": [
            {
                "claimId": "ITA-01",
                "claimAr": "خط إنتاج تعاقدي من 13 مرحلة مع عزل مجلدات التشغيل وسجلات حالة قابلة للاسترجاع",
                "claimEn": "13-stage deterministic contract pipeline with isolated per-run directories and rollback protection",
                "relationType": "EXTRACTED",
                "evidencePath": "PIPELINE_CONTRACTS.md",
                "lineOrSymbol": "Lines 9-36 (Stage-by-Stage Artifact Contracts & Run State)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "ITA-02",
                "claimAr": "مترجم EffectCraft الرسومي (ECGC) المكون من 10 وحدات لترجمة Scene Graph V2 إلى .ecproj وMP4",
                "claimEn": "10-component EffectCraft Creative Graphics Compiler (ECGC) translating Scene Graph V2 into .ecproj and MP4",
                "relationType": "EXTRACTED",
                "evidencePath": "core/aion/ecgc_compiler.py",
                "lineOrSymbol": "Lines 1-85 (CompileContext, SceneGraphValidator..RenderValidator)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "ITA-03",
                "claimAr": "مدقق تلقائي لثوابت مخطط المشهد يفحص حدود التوقيت وتباين إضاءة البطاقات (_hex_luma)",
                "claimEn": "Automated Scene Graph invariant auditor checking timing bounds, dark/light card luma contrast, and audio duration overflow",
                "relationType": "EXTRACTED",
                "evidencePath": "core/aion/contracts.py",
                "lineOrSymbol": "Lines 46-90 (_hex_luma, bg_hex_at, audit_scene_graph)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "ITA-04",
                "claimAr": "تحقيق جنائي للسبب الجذري (RCA) يعالج 8 ثغرات في تجميع المشاهد وشبحية النصوص وخلط الصوت",
                "claimEn": "Forensic 8-point Root Cause Analysis resolving V5 narrative flattening, caption ghosting, 24->30 FPS drift, and SFX flooding",
                "relationType": "EXTRACTED",
                "evidencePath": "V5_GOLD_REGRESSION_RCA_AR.md",
                "lineOrSymbol": "Lines 15-90 (Issues 1-7 & mix_scene_graph_audio)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            }
        ],
        "screenshots": [
            {
                "src": "/media/projects/image-to-animate/qa-contact-sheet.webp",
                "altAr": "لوحة فحص الجودة الآلية (6 إطارات مرندرة) من مشروع محمد الفاتح بالعربية تظهر تباين البطاقات والأسهم",
                "altEn": "Automated 6-frame QA contact sheet from Arabic historical explainer showing rendered cards, arrows, and pass metrics",
                "captionAr": "مخرج فحص الجودة الفعلي (`creative_contact_sheet.png`) بعد الرندر عبر ECGC — 86 طبقة رسومية مع اجتياز فحص الحركة والتباين.",
                "captionEn": "Real ECGC rendered QA contact sheet (`creative_contact_sheet.png`) verifying 86 layers, Arabic typography framing, and motion metrics.",
                "kind": "real_screenshot",
                "width": 1400,
                "height": 618
            },
            {
                "src": "/media/projects/image-to-animate/storyboard-extractor-diagnostics.webp",
                "altAr": "تشخيص استخراج 55 عنصرًا مستقلاً من لوحة القصة عبر الرؤية الحاسوبية",
                "altEn": "Computer-vision bounding-box diagnostics isolating 55 distinct storyboard entities",
                "captionAr": "تشخيص مرحلة الاستخراج الآلي (`preview_diagnostics.png`): فصل 55 عنصرًا وشخصية وأيقونة من لوحة القصة بدقة 3x HD.",
                "captionEn": "Automated storyboard extractor diagnostics (`preview_diagnostics.png`) isolating 55 discrete visual entities for scene-graph binding.",
                "kind": "diagnostic_output",
                "width": 1400,
                "height": 933
            },
            {
                "src": "/media/projects/image-to-animate/architecture-pipeline.svg",
                "altAr": "مخطط معمارية خط إنتاج AION Studio V6 من 13 مرحلة والمترجم الرسومي ECGC",
                "altEn": "AION Studio V6 13-stage pipeline and 10-stage ECGC architecture diagram",
                "captionAr": "مخطط معماري يوضح تسلسل المراحل الـ 13 من النص والصوت حتى الرندر وفحص الجودة الآلي.",
                "captionEn": "Architectural diagram of the 13-stage contract pipeline and 10-stage ECGC compilation flow.",
                "kind": "architecture_diagram",
                "width": 1200,
                "height": 540
            }
        ],
        "results": [
            {
                "metric": "13 Stages",
                "labelAr": "مراحل إنتاج محكومة بعقود JSON صارمة وعزل كامل لكل تشغيل",
                "labelEn": "Contract-gated pipeline stages with isolated per-run directories",
                "sourceRef": "PIPELINE_CONTRACTS.md:9-24"
            },
            {
                "metric": "10 Compilers",
                "labelAr": "وحدات ترجمة داخل ECGC لتحويل مخطط المشهد إلى مشروع GPU وفيديو",
                "labelEn": "Modular compiler stages inside ECGC (core/aion/ecgc_compiler.py)",
                "sourceRef": "core/aion/ecgc_compiler.py:1-15"
            },
            {
                "metric": "< 0.35s",
                "labelAr": "الحد الأقصى المسموح لانحراف الصوت عن الصورة في بوابة الفحص الآلي",
                "labelEn": "Maximum A/V drift threshold enforced by automated QA gate",
                "sourceRef": "PIPELINE_CONTRACTS.md:22"
            },
            {
                "metric": "16:9 & 9:16",
                "labelAr": "دعم مزدوج لإنتاج الفيديوهات الوثائقية الطويلة ومقاطع Shorts العمودية",
                "labelEn": "Dual rendering modes for 16:9 explainers and 9:16 vertical shorts",
                "sourceRef": "README.md:65-75 (Studio Compile & Shorts Pipeline)"
            }
        ],
        "skillsProven": [
            "AI Pipeline & Compiler Architecture",
            "Contract-Driven Systems & Schema Validation",
            "Computer Vision & Media Processing",
            "Arabic RTL Typography & Bidi Rendering",
            "Root-Cause Forensics & Automated QA Gates"
        ],
        "reviewFlags": [
            "Confirm public attribution of git author name (Ahmed Abdellah)",
            "Confirm whether sample MP4 video clips should be hosted publicly alongside contact sheets"
        ],
        "graphStats": {
            "totalFiles": 18242,
            "totalMb": 6693.15,
            "nodes": 3233,
            "edges": 8111
        },
        "updatedAt": "2026-11-19"
    },
    {
        "slug": "school-timetable",
        "titleAr": "نظام الجدول المدرسي الذكي",
        "titleEn": "Smart School Timetable System",
        "summaryAr": "منظومة سطح مكتب وويب سحابية (PyQt6 + FastAPI + React/TS) لبناء جداول الحصص المدرسية بصفر تعارضات حتمية عبر Google OR-Tools CP-SAT، مع محرك تشخيص مسبق للاستحالة وإصلاح موضعي ذكي وتصدير PDF/Excel عربي RTL.",
        "summaryEn": "Desktop (PyQt6) and cloud SaaS (FastAPI + React/TS) school scheduling platform achieving zero hard violations via Google OR-Tools CP-SAT, pre-solve mathematical feasibility diagnostics, minimal-perturbation smart repair, and Arabic RTL PDF/Excel exports.",
        "valuePropositionAr": "حل جداول المدارس المعقدة (حتى 600 حصة) في ثوانٍ بصفر تضارب، مع إتاحة التعديل اليدوي بالسحب والإفلات وإصلاح التعارضات تلقائيًا بأقل تغيير ممكن في الجدول.",
        "valuePropositionEn": "Solves complex school timetables (up to 600 weekly periods) in seconds with 0% hard conflicts, featuring interactive drag-and-drop rescheduling with causal minimal-perturbation repair.",
        "category": ["desktop", "web", "AI", "automation"],
        "status": "production",
        "visibility": "published",
        "featured": True,
        "featuredOrder": 2,
        "role": {
            "ar": "تصميم المعمارية ونمذجة القيود الرياضية وتطوير الواجهات",
            "en": "System Architecture, Constraint Modeling (CP-SAT) & Full-Stack Development"
        },
        "audience": {
            "ar": "إدارات المدارس ووكلاء شؤون المعلمين الذين يحتاجون جداول عادلة خالية من التضارب وجاهزة للطباعة بالعربية.",
            "en": "School administrators and academic principals requiring conflict-free, balanced schedules and print-ready Arabic PDFs."
        },
        "problem": {
            "ar": "بناء جدول حصص لمدرسة تضم عشرات المعلمين والفصول مع قيود التفرغ والأنصبة اليومية والانتدابات يستغرق أيامًا يدويًا، وعند غياب معلم أو الرغبة في تحريك حصة واحدة ينهار الجدول بسلسلة تعارضات يصعب تتبعها.",
            "en": "Constructing a school timetable across dozens of teachers, sections, availability windows, and daily quotas takes days manually — and moving a single lesson triggers cascading teacher collisions."
        },
        "solution": {
            "ar": "تصميم نظام مزدوج (تطبيق سطح مكتب PyQt6 يعمل 100% بدون إنترنت + نسخة SaaS محمية بـ FastAPI وReact) يعتمد صياغة رياضية خطية عبر Google OR-Tools CP-SAT، مسبوقة بمحرك تشخيص رياضي للاستحالة (`FeasibilityAnalyzer`)، ومتبوعة بمحرك تحقق مستقل (`Zero-Trust Validator`) ومحرك إصلاح ذكي (`Minimal Perturbation Repair`).",
            "en": "Engineered a dual-mode system (100% offline PyQt6 desktop app + license-protected FastAPI/React SaaS) powered by Google OR-Tools CP-SAT linear gap formulations, a pre-solve mathematical feasibility analyzer, an independent zero-trust validator, and a minimal-perturbation local repair engine."
        },
        "manualVsAutomated": {
            "ar": "بدلًا من المحاولة والخطأ اليدوي أو قبول جداول بها تضارب، يكتشف النظام أي استحالة في البيانات قبل تشغيل الـ Solver ويشرح سببها بالعربية، وعند سحب أي حصة يعرض جدول الحصص المزاحة وسبب نقل كل حصة مع خيار التراجع الفوري.",
            "en": "Instead of manual trial-and-error, the system mathematically detects infeasible input quotas pre-solve with Arabic explanations, and during drag-and-drop edits displays the exact causal chain of displaced lessons before committing to SQLite."
        },
        "capabilities": [
            {
                "ar": "محرك استمثال Google OR-Tools CP-SAT يحقق زمن حل أقل من 0.1 ثانية للمدارس الصغيرة وثوانٍ معدودة للمدارس الكبرى (600 حصة) بصفر تعارض.",
                "en": "Google OR-Tools CP-SAT solver achieving <0.1s solve times for small schools and seconds for 600-period schools with zero hard violations."
            },
            {
                "ar": "فاحص مستقل بدون ثقة مسبقة (Zero-Trust Independent Validator) يقيّم الجدول من 0 إلى 100 بمعزل عن الـ Solver.",
                "en": "Zero-Trust Independent Validator auditing every solver output against domain rules and computing a 0–100 quality score."
            },
            {
                "ar": "إصلاح ذكي تفاعلي (`ConflictImpactDialog` + `SmartRepairService`) يوضح الحصة الأساسية والحصص المزاحة والأطراف المتأثرة قبل الاعتماد.",
                "en": "Interactive Smart Repair dialog displaying direct vs. displaced lessons, affected teachers/sections, and root-cause infeasibility explanations."
            },
            {
                "ar": "تصدير فوري لملفات Excel متعددة الأوراق وملفات PDF للطباعة (A4/A3) بمعالجة كاملة للخط العربي ثنائي الاتجاه.",
                "en": "Instant multi-sheet RTL Excel (.xlsx) and print-ready A4/A3 Arabic PDF generation using ReportLab, arabic-reshaper, and python-bidi."
            }
        ],
        "architecture": {
            "overviewAr": "تفصل المعمارية بشكل صارم بين نطاق البيانات (`domain`)، محرك التشخيص (`validation/feasibility.py`)، محرك الحل والإصلاح (`solver/`)، المدقق المستقل (`verification/`)، وطبقة التخزين (`SQLAlchemy 2.0 + SQLite`)، مع واجهتي PyQt6 وFastAPI SaaS.",
            "overviewEn": "Clean domain architecture separating `domain` models, `validation/feasibility.py`, `solver/` (CP-SAT & LocalRepairEngine), `verification/` (Zero-Trust Validator), and SQLAlchemy 2.0 repositories across PyQt6 and FastAPI SaaS interfaces.",
            "pipelineSteps": [
                {
                    "step": "01",
                    "titleAr": "إدخال وتطبيع بيانات المدرسة (Intake & AI Copilot Normalizer)",
                    "titleEn": "School Data Intake & Smart Normalizer",
                    "detailAr": "استيراد بيانات المعلمين والفصول والأنصبة من الواجهة أو ملفات الوصف النصية عبر `SmartSchoolNormalizer`.",
                    "detailEn": "Ingests teachers, sections, subjects, and constraints via structured UI or `SmartSchoolNormalizer`."
                },
                {
                    "step": "02",
                    "titleAr": "التشخيص الرياضي المسبق (Pre-Solve Feasibility Engine)",
                    "titleEn": "Pre-Solve Mathematical Feasibility Diagnostics",
                    "detailAr": "فحص الطاقة الاستيعابية وأيام العمل لاكتشاف أي استحالة رياضية وتقديم حلول مقترحة قبل استدعاء CP-SAT.",
                    "detailEn": "Detects capacity bottlenecks and pigeonhole traps prior to solver invocation, returning actionable Arabic diagnostics."
                },
                {
                    "step": "03",
                    "titleAr": "محرك الاستمثال والتحقق المستقل (CP-SAT + Zero-Trust Validator)",
                    "titleEn": "CP-SAT Optimization & Independent Zero-Trust Validation",
                    "detailAr": "حل القيود الصارمة والمرنة ثم تمرير الجدول على `ScheduleValidator` المستقل لحساب مؤشر الجودة (0–100).",
                    "detailEn": "Solves hard and soft constraints via CP-SAT, then verifies the output independently via `ScheduleValidator`."
                },
                {
                    "step": "04",
                    "titleAr": "الإصلاح الموضعي الذكي والتصدير (Minimal Perturbation & RTL Export)",
                    "titleEn": "Minimal-Perturbation Smart Repair & RTL PDF/Excel Export",
                    "detailAr": "معالجة السحب والإفلات عبر `MoveLessonCommand` مع احترام الحصص المثبتة `is_pinned` وتصدير الجداول للطباعة.",
                    "detailEn": "Handles manual drag-and-drop via `MoveLessonCommand` respecting `is_pinned` locks and exports print-ready PDFs."
                }
            ],
            "systemBoundariesAr": "تعمل نسخة سطح المكتب محليًا بالكامل (100% Offline)، بينما تعزل نسخة SaaS (`api_server.py`) الخوارزميات ومفاتيح الذكاء الاصطناعي خلف بوابة تراخيص (`LicenseManager`).",
            "systemBoundariesEn": "Desktop edition operates 100% offline with local SQLite; SaaS edition (`api_server.py`) isolates solver IP and exporters behind `LicenseManager` quota validation."
        },
        "technologies": [
            "Python 3.13",
            "Google OR-Tools (CP-SAT)",
            "PyQt6",
            "FastAPI",
            "React + TypeScript",
            "SQLite + SQLAlchemy 2.0",
            "ReportLab + arabic-reshaper + python-bidi",
            "OpenPyXL",
            "Pytest + Hypothesis"
        ],
        "challenges": [
            {
                "id": "SCH-CH-1",
                "type": "verified_fix",
                "titleAr": "توحيد مسار السحب والإفلات والإصلاح الذكي مع شرح سببي لسلسلة الحصص المزاحة",
                "titleEn": "Unifying Drag-and-Drop Smart Repair with Causal Displacement Chains & Rollback",
                "problemAr": "عندما يسحب المستخدم حصة إلى موعد مشغول، كان المسار القديم يتجاوز خدمات التحقق ويكتفي بـ 4 فحوص بسيطة ثم يكتب الجدول الجديد في قاعدة البيانات مباشرة دون توضيح الحصص الأخرى التي تحركت أو احترام الحصص المثبتة.",
                "problemEn": "Dragging a lesson to an occupied slot previously bypassed domain validation services, ran 4 basic checks, and overwrote SQLite without showing displaced lessons or respecting pinned entries.",
                "whyImportantAr": "مدير المدرسة لا يقبل تعديلًا يغير مواعيد 3 معلمين آخرين في الخفاء دون أن يعرف من تأثر ولماذا.",
                "whyImportantEn": "School principals cannot trust an automated repair that silently shifts other teachers' lessons without transparency or undo capability.",
                "solutionAr": "إعادة هندسة مسار الاستدعاء عبر `MoveLessonCommand` و`SmartRepairService` لعرض جدول تفصيلي في `ConflictImpactDialog` بالحصة الأساسية والحصص المزاحة وسبب نقل كل منها، مع حفظ عمود `is_pinned` في `TimetableEntryModel` وإتاحة التراجع الكامل.",
                "solutionEn": "Refactored the call chain through `MoveLessonCommand` and `ConflictImpactDialog` to surface direct vs. displaced lessons with causal explanations, persisted `is_pinned` in SQLAlchemy models, and added rollback protection.",
                "proofRef": "CHANGE_IMPACT_BEFORE_AFTER.md:12-90 & خطة_إصلاح_وتطوير_منظومة_القيود_الشاملة.md:34-64",
                "impactAr": "شفافية كاملة قبل اعتماد أي تعديل يدوي، وحفظ دائم للحصص المثبتة في قاعدة البيانات.",
                "impactEn": "Full pre-commit visibility into ripple effects and persistent protection for pinned lessons.",
                "lessonAr": "محرك الاستمثال القوي يحتاج واجهة تفسيرية (Explainable Optimization) تحوّل القرارات الرياضية إلى أسباب مفهومة للمستخدم.",
                "lessonEn": "Mathematical optimization in user-facing tools requires explainable diffs that translate solver perturbations into human-readable reasons."
            },
            {
                "id": "SCH-CH-2",
                "type": "verified_fix",
                "titleAr": "حل فخ الاستحالة الرياضي المعكوس (Inverted Pigeonhole Trap) في أنصبة المعلمين الجزئية",
                "titleEn": "Eliminating the Inverted Pigeonhole Infeasibility Trap in Low-Workload Teachers",
                "problemAr": "توقف الـ Solver بإعلان استحالة الحل (INFEASIBLE) عند وجود معلم منتدب أو ذي نصاب قليل (مثل 3 حصص أسبوعيًا) مع تفعيل 5 أيام عمل في ملفه.",
                "problemEn": "The CP-SAT solver returned INFEASIBLE whenever a teacher with a small weekly quota (e.g., 3 periods) had 5 active working days selected.",
                "whyImportantAr": "المدارس الحقيقية تضم معلمين بأنصبة صغيرة أو مواد نشاط، وفشل الجدول بالكامل بسببهم يعطل النظام في الاستخدام الواقعي.",
                "whyImportantEn": "Real schools routinely have part-time or low-period teachers; halting the entire schedule over a rigid day-count constraint breaks real-world usability.",
                "solutionAr": "تعديل `get_work_pattern` في `teacher_availability_dialog.py` لربط سقف أيام العمل بـ `min(len(active_days), total_workload)` وتحويله لقيد مرن عند انخفاض النصاب، مع إضافة فحص استباقي في `FeasibilityAnalyzer`.",
                "solutionEn": "Updated `teacher_availability_dialog.py:get_work_pattern` to clamp `target_working_days = min(len(active_days), total_workload)` as a soft constraint when workload is low, backed by pre-solve checks in `FeasibilityAnalyzer`.",
                "proofRef": "خطة_إصلاح_وتطوير_منظومة_القيود_الشاملة.md:65-70",
                "impactAr": "نجاح توليد الجداول لبيانات المدارس الحقيقية المختبرة (مدرسة النيل، الجمالية، عرب مطير، الصداقة) دون توقف.",
                "impactEn": "Seamless solving across real multi-grade school datasets with mixed full-time and low-quota teachers.",
                "lessonAr": "القيود الافتراضية في الواجهة يجب أن تتحقق رياضيًا من توافقها مع حجم المدخلات قبل إرسالها لمحرك CP-SAT.",
                "lessonEn": "UI defaults that generate solver constraints must validate mathematical bounds against input cardinality before reaching CP-SAT."
            }
        ],
        "evidence": [
            {
                "claimId": "SCH-01",
                "claimAr": "محرك Google OR-Tools CP-SAT بصياغة خطية يحل جداول 600 حصة بصفر تعارض حتمي مع 36 اختبار Pytest",
                "claimEn": "Google OR-Tools CP-SAT linear gap formulation solving up to 600-period schools with zero hard violations and 36 pytest tests",
                "relationType": "EXTRACTED",
                "evidencePath": "README.md",
                "lineOrSymbol": "Lines 10-36 & 80-90 (CP-SAT Solver, Zero-Trust Validator, Pytest Suite)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "SCH-02",
                "claimAr": "مسار موحد للسحب والإفلات والإصلاح الذكي يعرض الحصص المزاحة وسلسلة الأثر السببي",
                "claimEn": "Unified MoveLessonCommand & SmartRepairService call chain surfacing displaced lessons and causal impact chains",
                "relationType": "EXTRACTED",
                "evidencePath": "CHANGE_IMPACT_BEFORE_AFTER.md",
                "lineOrSymbol": "Lines 12-90 (Before/After Call Chain Audit)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "SCH-03",
                "claimAr": "إصلاح فخ الاستحالة المعكوس لأيام عمل المعلم وحفظ الحصص المثبتة is_pinned في SQLite",
                "claimEn": "Inverted Pigeonhole availability fix and persistent is_pinned SQLAlchemy column",
                "relationType": "EXTRACTED",
                "evidencePath": "خطة_إصلاح_وتطوير_منظومة_القيود_الشاملة.md",
                "lineOrSymbol": "Lines 34-74 (ConflictImpactDialog, TimetableEntryModel.is_pinned)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "SCH-04",
                "claimAr": "خادم FastAPI SaaS محمي يعزل خوارزميات الحل والتصدير خلف بوابة تحقق من التراخيص والحصص",
                "claimEn": "Protected FastAPI SaaS backend isolating solver IP and exporters behind quota-checked license verification",
                "relationType": "EXTRACTED",
                "evidencePath": "src/school_scheduler/ai_studio/api_server.py",
                "lineOrSymbol": "Lines 1-76 (FastAPI v2.1.0, _require_license, TimetableSolver)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            }
        ],
        "screenshots": [
            {
                "src": "/media/projects/school-timetable/master-schedule-ui.webp",
                "altAr": "واجهة نظام الجدول المدرسي الذكي تعرض الجدول العام الشامل (252 حصة مجدولة بصفر تعارضات) مع وكيل الذكاء الاصطناعي",
                "altEn": "AI Studio School Timetable UI displaying a 252-period master schedule with 0% conflicts and AI Copilot sidebar",
                "captionAr": "لقطة شاشة فعلية لواجهة النظام السحابية (بعد إخفاء رمز الترخيص): جدولة 252 حصة لـ 7 فصول بنسبة تعارض 0% مع خيارات تصدير PDF A4/A3 وExcel.",
                "captionEn": "Real UI screenshot (with license key header sanitized): 252 scheduled lessons across 7 sections at 0% conflict rate with A4/A3 PDF and Excel exports.",
                "kind": "real_screenshot",
                "width": 1400,
                "height": 875
            },
            {
                "src": "/media/projects/school-timetable/architecture-cpsat.svg",
                "altAr": "مخطط معمارية محرك الجدول المدرسي OR-Tools CP-SAT والفاحص المستقل والإصلاح الذكي",
                "altEn": "School Timetable CP-SAT solver, Zero-Trust Validator, and Smart Repair architecture diagram",
                "captionAr": "مخطط تدفق البيانات من فحص الجدوى الرياضي المسبق حتى الحل بـ CP-SAT والتدقيق المستقل والإصلاح الموضعي.",
                "captionEn": "System flow from pre-solve feasibility diagnostics through CP-SAT optimization, zero-trust validation, and minimal-perturbation repair.",
                "kind": "architecture_diagram",
                "width": 1200,
                "height": 540
            }
        ],
        "results": [
            {
                "metric": "0% Conflicts",
                "labelAr": "تصفير تام للتعارضات الحتمية مفحوص بمحرك تحقق مستقل (Zero-Trust)",
                "labelEn": "Zero hard constraint violations verified by an independent Zero-Trust validator",
                "sourceRef": "README.md:17-22"
            },
            {
                "metric": "< 0.1s – 3s",
                "labelAr": "زمن الحل الرياضي من المدارس الصغيرة حتى اختبار الضغط (600 حصة)",
                "labelEn": "CP-SAT solve time ranging from <0.1s (small) to seconds (600-period stress test)",
                "sourceRef": "README.md:16 & 87-90"
            },
            {
                "metric": "36 Pytest",
                "labelAr": "اختبارًا آليًا يغطي النطاق، الجدوى، المحرك، التصدير، وقاعدة البيانات",
                "labelEn": "Automated pytest suite covering domain, feasibility, solver, export, and persistence",
                "sourceRef": "README.md:82-85"
            },
            {
                "metric": "A4/A3 & XLSX",
                "labelAr": "تصدير فوري لجداول PDF عربية ثنائية الاتجاه وملفات Excel متعددة الأوراق",
                "labelEn": "Print-ready Arabic RTL PDFs (A4/A3) and multi-sheet Excel exports",
                "sourceRef": "README.md:30-33 (Export Services)"
            }
        ],
        "skillsProven": [
            "Mathematical Optimization & Constraint Programming (CP-SAT)",
            "Explainable UX for Complex Algorithms (Causal Diffs)",
            "Cross-Platform Desktop & SaaS Architecture (PyQt6 + FastAPI + React)",
            "Arabic RTL Document Generation (ReportLab Bidi PDF & Excel)",
            "Zero-Trust Verification & Automated Stress Testing"
        ],
        "reviewFlags": [
            "Confirm personal role attribution",
            "Confirm whether sample school names in test markdown files should remain anonymized in future demos"
        ],
        "graphStats": {
            "totalFiles": 798,
            "totalMb": 22.97,
            "nodes": 5563,
            "edges": 16500
        },
        "updatedAt": "2026-11-19"
    },
    {
        "slug": "enaya-ai-workspace",
        "titleAr": "منظومة عناية الطبية وحوكمة التدقيق",
        "titleEn": "Enaya Healthcare Platform & Audit",
        "summaryAr": "مجمّع برمجي يضم المونوريبو الكامل لتطبيقات عناية الطبية (تطبيق المريض، الطبيب، الصيدلية، المختبر، ولوحة الإدارة) مع إطار تدقيق هندسي مهيكل من 12 دورًا وأداة FigCraft المكتبية.",
        "summaryEn": "Comprehensive healthcare engineering workspace combining the multi-app Enaya Flutter/Supabase monorepo (Patient, Doctor, Pharmacy, Lab, System Admin) with a 12-role evidence-gated architectural audit framework and FigCraft desktop tooling.",
        "valuePropositionAr": "توحيد وإصلاح منظومة رعاية صحية متعددة التطبيقات عبر حوكمة تدقيق صارمة، ومزامنة طوابير العمليات غير المتصلة بالإنترنت (Offline Queue)، وتسعير حجوزات ذري آمن.",
        "valuePropositionEn": "Unifies and hardens a 5-app healthcare ecosystem through evidence-gated architectural governance, offline outbox synchronization, jittered exponential backoff, and atomic booking/quoting workflows.",
        "category": ["mobile", "web", "architecture", "AI"],
        "status": "functional",
        "visibility": "published",
        "featured": False,
        "featuredOrder": 4,
        "role": {
            "ar": "معمارية الأنظمة ومراجعة وتطوير تطبيقات Flutter/Supabase",
            "en": "Systems Architecture & Flutter/Supabase Remediation Engineering"
        },
        "audience": {
            "ar": "منصات الرعاية الصحية الرقمية التي تربط المرضى والأطباء والمختبرات والصيدليات في بيئة عالية الاعتمادية.",
            "en": "Digital healthcare platforms connecting patients, doctors, laboratories, and pharmacies under strict reliability and privacy controls."
        },
        "problem": {
            "ar": "توزيع رحلة المريض عبر 5 تطبيقات و3 قواعد بيانات Supabase يخلق ثغرات حرجة عند انقطاع شبكة الهاتف، أو تعارض تسعير الحجوزات والبدائل الدوائية، أو تعديل الكود دون مرجعية معمارية موحدة.",
            "en": "Spanning patient journeys across 5 applications and multiple Supabase instances creates high risk of dropped offline actions, booking/quoting race conditions, and inconsistent RLS security policies."
        },
        "solution": {
            "ar": "تأسيس إطار تدقيق هندسي من 12 دورًا تخصصيًا يفصل الحقيقة المرصودة عن الفرضيات ويصدر قرارات معمارية ملزمة (`DEC-01..DEC-12`)، ثم تنفيذ الإصلاحات في `enaya_monorepo` متضمنةً `OfflineSyncManager` و`ErrorRecoveryService` وبوابة الأحداث المركزية (`Central Event Gateway`).",
            "en": "Established a 12-role evidence-gated audit framework producing binding ADRs (`DEC-01..DEC-12`), then executed end-to-end monorepo remediations across all 5 Flutter apps including `OfflineSyncManager`, jittered `ErrorRecoveryService`, atomic pricing, and a Central Event Gateway."
        },
        "manualVsAutomated": {
            "ar": "بدلًا من المراجعات العشوائية أو فقدان طلبات المريض والطبيب عند ضعف الشبكة، يُلزم النظام كل تقرير تدقيق بمرجع السطر والملف، ويعيد جدولة العمليات الفاشلة تلقائيًا في الخلفية فور عودة الاتصال.",
            "en": "Replaces ad-hoc code reviews and fragile network calls with file/line-mandated audit governance, automatic offline queue flushing on reconnect, and jittered exponential backoff for transient 503/504 errors."
        },
        "capabilities": [
            {
                "ar": "مزامنة طابور العمليات غير المتصلة (`OfflineSyncManager`) في تطبيقي الطبيب والمريض مع إعادة جدولة العمليات الفاشلة فقط.",
                "en": "`OfflineSyncManager` in Doctor and Patient apps listening to connectivity streams and re-queueing only failed actions."
            },
            {
                "ar": "محرك تعافٍ من الأخطاء (`ErrorRecoveryService`) في تطبيق المختبر يطبق Exponential Backoff مع Jitter عشوائي (0.8x–1.2x).",
                "en": "`ErrorRecoveryService` in Laboratory app executing transient network/503/504 retries with jittered exponential backoff."
            },
            {
                "ar": "حوكمة معمارية شاملة (أكثر من 90 وثيقة في `MANIFEST.md`) تغطي مراجعة سياسات RLS، مصفوفة الفشل العابرة للنطاقات، وخطة التعافي من الكوارث.",
                "en": "90+ structured engineering documents in `MANIFEST.md` covering RLS policy audits, cross-domain failure matrices, and disaster recovery."
            },
            {
                "ar": "تطبيقات متكاملة للصيدلية والمختبر والإدارة تشمل التسعير المخصص، التحقق من التوفر الفعلي، مراجعة إيصالات الدفع، وإدارة النزاعات.",
                "en": "End-to-end Pharmacy, Lab, and System Admin workflows including physical availability checks, custom quoting, receipt review, and dispute handling."
            }
        ],
        "architecture": {
            "overviewAr": "تجمع المساحة بين طبقة الحوكمة والتدقيق (`00_governance` إلى `08_lifecycle_resilience_audit`)، والمونوريبو التنفيذي (`enaya_monorepo/apps/*`)، وأداة سطح المكتب `figcraft`.",
            "overviewEn": "Integrates the architectural governance workspace (`00_governance`..`08_lifecycle_resilience_audit`), the executable 5-app Flutter monorepo (`enaya_monorepo`), and the Rust-based `figcraft` desktop controller.",
            "pipelineSteps": [
                {
                    "step": "01",
                    "titleAr": "الجرد والتدقيق المتخصص (12-Role Evidence Intake)",
                    "titleEn": "Read-Only Intake & 12-Role Specialist Audit",
                    "detailAr": "فحص المستودعات عبر 12 زاوية هندسية (الأمان، الهوية SSO، قواعد البيانات، Flutter، الاعتمادية، وتجربة المستخدم).",
                    "detailEn": "Audits source snapshots across 12 specialist roles (Security, SSO, Supabase Clinic/Lab/Pharmacy, Flutter, QA, UI/UX)."
                },
                {
                    "step": "02",
                    "titleAr": "المراجعة المتقاطعة وسجلات القرارات (Cross-Review & ADRs)",
                    "titleEn": "Cross-Role Conflict Resolution & ADRs (DEC-01..12)",
                    "detailAr": "حسم التعارضات بين الأدوار وتوثيق المعمارية المستهدفة (`TO_BE_ARCHITECTURE.md`) وبوابات الإنتاج.",
                    "detailEn": "Resolves inter-role conflicts into formal ADRs and target architecture specifications."
                },
                {
                    "step": "03",
                    "titleAr": "إصلاح المونوريبو ومرونة الاتصال (Monorepo Remediation)",
                    "titleEn": "Monorepo Execution & Offline/Retry Resilience",
                    "detailAr": "تطبيق التسعير الذري، وفصل الدفع، وطوابير Outbox، ومديري المزامنة والتعافي في تطبيقات Flutter الخمسة.",
                    "detailEn": "Implements atomic booking pricing, outbox queues, `OfflineSyncManager`, and `ErrorRecoveryService` across the 5 apps."
                }
            ],
            "systemBoundariesAr": "تتخاطب تطبيقات Flutter الخمسة مع مشاريع Supabase متعددة (عيادات، مختبر، صيدلية) وخدمة Cloudinary للأصول مع عزل الصلاحيات عبر RLS.",
            "systemBoundariesEn": "Five Flutter apps communicate with domain-partitioned Supabase backends (Clinic, Lab, Pharmacy) and Cloudinary asset storage under strict RLS controls."
        },
        "technologies": [
            "Flutter / Dart",
            "Supabase (PostgreSQL, RLS, Edge Functions)",
            "BLoC / Cubit State Management",
            "Offline Outbox & Connectivity Streams",
            "Cloudinary Signed Asset Pipeline",
            "Rust (FigCraft Desktop Controller)",
            "Architectural Governance & ADR Framework"
        ],
        "challenges": [
            {
                "id": "ENA-CH-1",
                "type": "verified_fix",
                "titleAr": "حماية العمليات الطبية من الضياع عند انقطاع الشبكة ومنع عواصف إعادة المحاولة",
                "titleEn": "Preventing Offline Action Loss & Retry Storms Across Healthcare Apps",
                "problemAr": "إلغاء الحجز أو تحديث الحالة أثناء انقطاع الإنترنت على هاتف الطبيب أو المريض أو المختبر كان يفشل فوريًا أو يسبب تزامنًا متكررًا غير منضبط عند عودة الاتصال.",
                "problemEn": "Booking cancellations or lab status updates during mobile network drops either failed outright or risked synchronized retry storms upon reconnection.",
                "whyImportantAr": "في التطبيقات الطبية، بقاء حجز ملغى كأنه نشط أو ضياع تحديث المختبر يربك جدول العيادة والمريض.",
                "whyImportantEn": "In clinical workflows, an unpropagated booking cancellation or lost lab update directly disrupts doctor schedules and patient care.",
                "solutionAr": "تطوير `OfflineSyncManager` بعلامة قفل `_isSyncing` يراقب `InternetConnectionChecker` ويفرغ الطابور المحلي ثم يعيد جدولة العمليات التي فشلت فقط، مع بناء `ErrorRecoveryService` في تطبيق المختبر بـ Exponential Backoff وعشوائية Jitter (0.8..1.2).",
                "solutionEn": "Implemented `OfflineSyncManager` with `_isSyncing` mutex guards and partial-failure re-queueing on connectivity restoration, paired with `ErrorRecoveryService` using jittered exponential backoff (0.8x–1.2x) for socket/503/504 errors.",
                "proofRef": "enaya_monorepo/apps/doctor_app/lib/core/services/offline_sync_manager.dart:22-90 & enaya_monorepo/apps/laboratory_app/lib/core/services/error_recovery_service.dart:29-68",
                "impactAr": "اتساق نهائي مضمون (Eventual Consistency) للعمليات المعلقة واستقرار الخادم ضد الأخطاء الشبكية العابرة.",
                "impactEn": "Guaranteed eventual consistency for offline mutations and resilient protection against transient gateway timeouts.",
                "lessonAr": "إفراغ الطابور المحلي ثم إعادة إدراج العناصر الفاشلة فقط تحت قفل تزامن يمنع تكرار التنفيذ والسباقات.",
                "lessonEn": "Atomic queue drain followed by selective re-insertion under a sync lock prevents both duplicate execution and infinite retry loops."
            },
            {
                "id": "ENA-CH-2",
                "type": "preventive_design",
                "titleAr": "حوكمة التدقيق متعدد الأدوار وإلزامية الدليل قبل إعادة هيكلة المونوريبو",
                "titleEn": "Evidence-Gated 12-Role Audit Governance Prior to Monorepo Refactoring",
                "problemAr": "إعادة بناء أو إصلاح منظومة كبيرة تضم 5 تطبيقات مباشرةً بدون فصل الحقائق عن الظنون يؤدي إلى كسر عقود البيانات بين التطبيقات.",
                "problemEn": "Refactoring a 5-app multi-backend system without separating verified code facts from assumptions breaks cross-app data contracts.",
                "whyImportantAr": "تجنب هدم مكونات تعمل بنجاح وضمان توافق الأمان (RLS) والهوية (SSO) وتجربة المستخدم قبل كتابة الكود.",
                "whyImportantEn": "Prevents destructive regressions and aligns Security, Identity, Database, and Mobile schemas before code changes.",
                "solutionAr": "بناء خط تدقيق مهيكل في `D:\\enaya_ai_audit_workspace` يصنف كل ملاحظة إلى (`Observed fact`, `Inferred risk`, `Unknown`, `Recommendation`) ويحسم القرارات في `DEC-01..DEC-12` قبل تنفيذ سلسلة commits الإصلاحية في `enaya_monorepo`.",
                "solutionEn": "Designed a structured governance pipeline enforcing strict epistemic labels (`Observed fact` vs. `Inferred risk`) and binding decisions (`DEC-01..DEC-12`) prior to monorepo remediation commits.",
                "proofRef": "README.md:7-37, MANIFEST.md:1-90 & enaya_monorepo commits 07c9431..08208b8",
                "impactAr": "إنجاز إصلاحات تطبيقات المريض والصيدلية والمختبر والإدارة بسجل تتبع واضح لكل قرار هندسي.",
                "impactEn": "Clean, auditable remediation commits across all 5 applications with zero undocumented architectural assumptions.",
                "lessonAr": "تقييد الذكاء الاصطناعي والفرق الهندسية بقوالب أدلة صارمة يحول التدقيق من آراء عامة إلى وثائق هندسية قابلة للتنفيذ.",
                "lessonEn": "Constraining architectural audits with strict evidence schemas transforms vague reviews into executable engineering blueprints."
            }
        ],
        "evidence": [
            {
                "claimId": "ENA-01",
                "claimAr": "مدير مزامنة العمليات غير المتصلة OfflineSyncManager في تطبيقي الطبيب والمريض مع إعادة جدولة الفشل الجزئي",
                "claimEn": "OfflineSyncManager in Doctor & Patient apps monitoring connectivity changes and re-queueing failed actions",
                "relationType": "EXTRACTED",
                "evidencePath": "enaya_monorepo/apps/doctor_app/lib/core/services/offline_sync_manager.dart",
                "lineOrSymbol": "Lines 8-90 (OfflineSyncManager.startMonitoring, syncOfflineQueue)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "ENA-02",
                "claimAr": "خدمة التعافي من الأخطاء ErrorRecoveryService في تطبيق المختبر بـ Exponential Backoff وJitter عشوائي",
                "claimEn": "ErrorRecoveryService in Laboratory app implementing exponential backoff with randomized jitter (0.8..1.2x)",
                "relationType": "EXTRACTED",
                "evidencePath": "enaya_monorepo/apps/laboratory_app/lib/core/services/error_recovery_service.dart",
                "lineOrSymbol": "Lines 15-69 (ErrorRecoveryService.executeWithRetry)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "ENA-03",
                "claimAr": "أكثر من 90 وثيقة حوكمة ومعمارية وتدقيق RLS ومصفوفات فشل في MANIFEST.md",
                "claimEn": "90+ structured engineering artifacts covering AS-IS/TO-BE architecture, RLS review, and failure matrices",
                "relationType": "EXTRACTED",
                "evidencePath": "MANIFEST.md",
                "lineOrSymbol": "Lines 1-90 (00_governance..05_final_docs)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "ENA-04",
                "claimAr": "سلسلة Commits إصلاحية موثقة عبر تطبيقات المريض والصيدلية والمختبر ولوحة الإدارة",
                "claimEn": "Verified git remediation commits across Patient, Pharmacy, Laboratory, and System Admin apps",
                "relationType": "EXTRACTED",
                "evidencePath": "enaya_monorepo/.git",
                "lineOrSymbol": "Commits 07c9431, a87d911, 7b0efb5, 4f1f721, e9651f7, 08208b8",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            }
        ],
        "screenshots": [
            {
                "src": "/media/projects/enaya-ai-workspace/enaya-ecosystem-architecture.svg",
                "altAr": "مخطط معمارية منظومة عناية الطبية (5 تطبيقات Flutter) ومزامنة الطوابير وحوكمة التدقيق",
                "altEn": "Enaya Healthcare 5-app Flutter monorepo, offline sync, and 12-role audit governance diagram",
                "captionAr": "رسم معماري توضيحي (`Illustrative Architecture Diagram`) يبين ترابط تطبيقات عناية الخمسة وطبقات المزامنة والتعافي وحوكمة القرارات.",
                "captionEn": "Illustrative architecture diagram mapping the 5 Flutter apps, OfflineSyncManager, ErrorRecoveryService, and 12-role governance flow.",
                "kind": "architecture_diagram",
                "width": 1200,
                "height": 540
            }
        ],
        "results": [
            {
                "metric": "5 Flutter Apps",
                "labelAr": "تطبيقات متكاملة في المونوريبو (المريض، الطبيب، المختبر، الصيدلية، الإدارة)",
                "labelEn": "Unified healthcare applications inside enaya_monorepo",
                "sourceRef": "enaya_monorepo/.git commits 07c9431..08208b8"
            },
            {
                "metric": "90+ Artifacts",
                "labelAr": "وثيقة معمارية وتدقيق أمني وسجل قرارات (ADR) مفهرسة في MANIFEST.md",
                "labelEn": "Governance, RLS audit, and target architecture specs in MANIFEST.md",
                "sourceRef": "MANIFEST.md:1-90"
            },
            {
                "metric": "12 Roles",
                "labelAr": "أدوار تدقيق هندسية متخصصة بمراجعات متقاطعة وإسناد إلزامي للأسطر",
                "labelEn": "Specialist engineering audit roles with cross-review conflict resolution",
                "sourceRef": "MANIFEST.md:21-44"
            },
            {
                "metric": "0.8x – 1.2x",
                "labelAr": "معامل العشوائية (Jitter) في إعادة المحاولة التصاعدية لحماية الخادم",
                "labelEn": "Jitter multiplier on exponential backoff retries for transient faults",
                "sourceRef": "error_recovery_service.dart:50-56"
            }
        ],
        "skillsProven": [
            "Multi-App Flutter Monorepo Architecture",
            "Offline-First Synchronization & Outbox Pattern",
            "Fault-Tolerant Networking (Exponential Backoff & Jitter)",
            "Supabase Multi-Tenant Security & RLS Auditing",
            "Technical Governance & Architecture Decision Records (ADRs)"
        ],
        "reviewFlags": [
            "Confirm personal role vs. team scope across enaya_monorepo",
            "Confirm which mobile UI screens can be captured with synthetic demo patient data for public display"
        ],
        "graphStats": {
            "totalFiles": 4700,
            "totalMb": 674.83,
            "nodes": 11456,
            "edges": 17367
        },
        "updatedAt": "2026-11-19"
    },
    {
        "slug": "phone-commander",
        "titleAr": "Phone Commander — أتمتة الهاتف بالرؤية الحاسوبية",
        "titleEn": "Phone Commander — Mobile Vision Automation",
        "summaryAr": "تطبيق Flutter وأندرويد أصيل (Kotlin) يجمع بين محرك مطابقة قوالب بصري فائق السرعة (ZNCC) بدون استنزاف للذاكرة (Zero GC Churn) وخدمة Accessibility مع بوابة ترخيص أصلية (NativeLicenseGate) وسجل عمليات حي.",
        "summaryEn": "Hybrid Flutter and native Android (Kotlin) automation platform pairing a custom thread-local, zero-GC-churn ZNCC computer vision engine and ML Kit OCR with an autonomous state-machine loop and native license verification.",
        "valuePropositionAr": "تنفيذ أتمتة بصرية مستمرة على أجهزة أندرويد بعتبات ثقة مضبوطة (86%–92%) وبدون استنزاف ذاكرة المعالج (Zero GC Churn) مع مراقبة حية من داخل واجهة Flutter.",
        "valuePropositionEn": "Delivers long-running on-device visual automation on Android using configured 86%–92% ZNCC confidence thresholds, zero per-frame bitmap heap churn, and live Flutter console telemetry.",
        "category": ["mobile", "AI", "automation"],
        "status": "functional",
        "visibility": "published",
        "featured": False,
        "featuredOrder": 5,
        "role": {
            "ar": "تطوير أنظمة أندرويد الأصيلة (Kotlin) والرؤية الحاسوبية وواجهة Flutter",
            "en": "Android Native (Kotlin), Computer Vision & Flutter Systems Engineering"
        },
        "audience": {
            "ar": "المستخدمون الذين يحتاجون أتمتة بصرية ذكية تعمل لفترات طويلة على الهاتف دون انهيار الذاكرة أو استنزاف البطارية.",
            "en": "Users requiring continuous, battery-efficient on-device visual automation on Android with deterministic recovery."
        },
        "problem": {
            "ar": "محركات الأتمتة التقليدية على الهواتف تنشئ وتدمر صور Bitmap بحجم ~8MB في كل إطار مما يسبب تشنج الهاتف وانهيار التطبيق (`OutOfMemory` / `Recycled Bitmap Crash`)، كما أن الاعتماد على نقرات عمياء بإحداثيات ثابتة يوقع النظام في حلقات لا نهائية عند تغير حالة الشاشة.",
            "en": "Conventional mobile screen automation allocates ~8MB bitmaps every frame — causing severe GC stutter and recycled-bitmap crashes — while blind hardcoded coordinate taps trap the device in infinite UI loops."
        },
        "solution": {
            "ar": "بناء محرك مطابقة قوالب `TemplateMatcher.kt` بخوارزمية ZNCC يستخدم ذاكرة محلية لكل خيط (`ThreadLocal ReusableScaleBuffer`) وإزاحات صفوف محسوبة مسبقًا (`offsetsForStride`) لتصفير تخصيص الذاكرة في كل إطار، ودمجه مع آلة حالة ذكية (`AutomationEngine.kt`) وGoogle ML Kit OCR وبث اللوجز لحظيًا لواجهة Flutter.",
            "en": "Built a custom ZNCC `TemplateMatcher.kt` utilizing `ThreadLocal` `ReusableScaleBuffer` and precalculated `offsetsForStride` arrays for zero per-frame GC churn, driving a 5,264-line state machine (`AutomationEngine.kt`) with ML Kit OCR, SQLite session sync, and real-time Flutter MethodChannel logs."
        },
        "manualVsAutomated": {
            "ar": "بدلًا من النقر الافتراضي الأعمى عند فشل الرصد، يلتزم المحرك بعتبات ثقة صارمة (86%–92%) داخل نطاق آمن (Safe ROI)، ويستخدم أمر الرجوع النظامي `GLOBAL_ACTION_BACK` عند الطوارئ، ويصغّر التطبيق تلقائيًا لتوفير البطارية إذا تجاوز الانتظار 15 دقيقة.",
            "en": "Replaces blind fallback taps with strict 86%–92% ZNCC confidence gates inside a Safe ROI boundary, system `GLOBAL_ACTION_BACK` recovery, and automatic battery-saving app minimization during waits exceeding 15 minutes."
        },
        "capabilities": [
            {
                "ar": "محرك ZNCC متعدد المقاييس ومتوازي الخيوط بصفر تخصيص ذاكرة لكل إطار (`ReusableScaleBuffer` + `PreparedTemplate`).",
                "en": "Multi-scale parallel ZNCC template matcher with zero per-frame heap allocation (`ReusableScaleBuffer` + `PreparedTemplate`)."
            },
            {
                "ar": "آلة حالة ذاتية (`AutomationEngine.kt` — 5,264 سطرًا) تدير أولويات المهام، طوابير SQLite، وتوفير البطارية أثناء الانتظار الطويل.",
                "en": "Autonomous 5,264-line Kotlin state machine managing task priorities, SQLite queue synchronization, and long-wait battery minimization."
            },
            {
                "ar": "تكامل ثنائي بين الرؤية الحاسوبية (CV) وقراءة النصوص (Google ML Kit OCR) مع حظر النقرات العشوائية.",
                "en": "Dual Computer Vision (ZNCC) and Google ML Kit OCR pipeline enforcing a zero-hardcoded-tap policy."
            },
            {
                "ar": "بوابة ترخيص مزدوجة (`NativeLicenseGate.kt` + Supabase) مع بث حي لسجل العمليات والإحداثيات إلى واجهة Flutter.",
                "en": "Native + Supabase licensing gate (`NativeLicenseGate.kt`) and real-time `MethodChannel` telemetry streaming to Flutter."
            }
        ],
        "architecture": {
            "overviewAr": "تتكون المعمارية من واجهة تحكم وترخيص مبنية بـ Flutter تتواصل عبر `MethodChannel` مع طبقة أندرويد أصيلة (Kotlin) تضم خدمات التقاط الشاشة، ومحرك الرؤية الحاسوبية ZNCC، ومحلل النصوص OCR، وآلة الحالة الرئيسية.",
            "overviewEn": "Hybrid architecture pairing a Flutter control/licensing UI with a high-performance native Kotlin service layer housing `ScreenCaptureService`, `TemplateMatcher` (ZNCC), `ScreenTextRecognizer` (ML Kit), and `AutomationEngine`.",
            "pipelineSteps": [
                {
                    "step": "01",
                    "titleAr": "التقاط الإطار وإعادة تدوير الذاكرة (Frame Capture & ThreadLocal Buffer)",
                    "titleEn": "ScreenCaptureService & ThreadLocal Buffer Reuse",
                    "detailAr": "تحجيم منطقة الفحص الصافية (Safe ROI) داخل `ReusableScaleBuffer` دون إنشاء كائنات Bitmap جديدة.",
                    "detailEn": "Downscales the Safe ROI into a thread-local `ReusableScaleBuffer` without allocating new Bitmaps or IntArrays."
                },
                {
                    "step": "02",
                    "titleAr": "الفحص البصري المتوازي وقراءة النصوص (Parallel ZNCC + ML Kit OCR)",
                    "titleEn": "Multi-Scale ZNCC Matching & ML Kit OCR Verification",
                    "detailAr": "مطابقة القوالب المفرغة عبر إزاحات البكسل المحسوبة مسبقًا بعتبات ثقة 86%–92% مع تحقق OCR للنصوص والأوقات.",
                    "detailEn": "Scans pre-normalized templates using cached row-stride offsets at 86%–92% thresholds alongside OCR timer parsing."
                },
                {
                    "step": "03",
                    "titleAr": "اتخاذ القرار ومزامنة SQLite (State Machine & Queue Sync)",
                    "titleEn": "Priority State Machine, Gesture Dispatch & SQLite Sync",
                    "detailAr": "تنفيذ الإيماءة المؤكدة أو التراجع الآمن `GLOBAL_ACTION_BACK`، وتحديث حالة الجلسات في SQLite وبث السجل لواجهة Flutter.",
                    "detailEn": "Dispatches verified gestures or `GLOBAL_ACTION_BACK`, updates local SQLite session state, and streams telemetry to Flutter."
                }
            ],
            "systemBoundariesAr": "يعمل بالكامل على جهاز أندرويد محليًا عبر `AccessibilityService` و`MediaProjection`، ويتصل بـ Supabase للتحقق من صلاحية الترخيص فقط.",
            "systemBoundariesEn": "Executes 100% on-device via Android `AccessibilityService` and `MediaProjection`, connecting externally only to Supabase for license validation."
        },
        "technologies": [
            "Flutter / Dart",
            "Kotlin (Android Native)",
            "Custom ZNCC Computer Vision",
            "Google ML Kit OCR",
            "Android AccessibilityService & MediaProjection",
            "SQLite Local Sync",
            "Supabase Auth & Licensing"
        ],
        "challenges": [
            {
                "id": "PHC-CH-1",
                "type": "verified_fix",
                "titleAr": "تصفير استنزاف الذاكرة (Zero GC Churn) ومنع انهيار Bitmap Recycled أثناء المسح المتوازي",
                "titleEn": "Eliminating 8MB/Frame GC Churn & Bitmap Recycling Crashes in Parallel CV Scanning",
                "problemAr": "فحص الشاشة المستمر بمقاييس متعددة في خيوط متوازية كان يستهلك ~8MB لكل إطار ويسبب انهيارًا مفاجئًا عند محاولة قراءة Bitmap تم تحريرها.",
                "problemEn": "Continuous multi-scale template scanning across worker threads allocated ~8MB per frame and triggered fatal `recycled bitmap` exceptions during lifecycle transitions.",
                "whyImportantAr": "تطبيقات الأتمتة الخلفية على الهواتف يجب أن تعمل لساعات دون رفع حرارة الجهاز أو إيقاف الخدمة من نظام أندرويد.",
                "whyImportantEn": "On-device background automation must run for hours without thermal throttling, GC pauses, or Android OS process kills.",
                "solutionAr": "تصميم `ReusableScaleBuffer` محلي لكل خيط (`ThreadLocal`) يعيد استخدام مصفوفة البكسلات وBitmap التحجيم، مع حساب إزاحات الصفوف مرة واحدة لكل عرض شاشة (`offsetsForStride`)، وتأمين دورة حياة الـ Bitmap في الـ Commit `50927ed`.",
                "solutionEn": "Implemented `ThreadLocal` `ReusableScaleBuffer` reusing pixel arrays and scaling bitmaps, cached 1D pixel offsets via `offsetsForStride(stride)`, and hardened bitmap/service lifecycle checks in commit `50927ed`.",
                "proofRef": "android/app/src/main/kotlin/com/sys/display/assist/cv/TemplateMatcher.kt:27-85 & git commit 50927ed",
                "impactAr": "أداء بصري فائق السرعة بدون تخصيص ذاكرة متكرر واستقرار كامل للجلسات الطويلة.",
                "impactEn": "Zero per-frame heap allocation overhead during template scans and elimination of bitmap lifecycle crashes.",
                "lessonAr": "في معالجة الصور الحية على الهواتف، هيكلة البيانات في مصفوفات بدائية متصلة وإعادة تدوير المخازن المحلية للخيوط أهم من تحسين المعادلة الرياضية وحدها.",
                "lessonEn": "In mobile real-time computer vision, contiguous primitive arrays and thread-local buffer reuse matter more than algorithmic tweaks alone."
            },
            {
                "id": "PHC-CH-2",
                "type": "verified_fix",
                "titleAr": "منع إحياء الجلسات المنتهية في SQLite وكسر حلقة تبديل الخريطة اللانهائية",
                "titleEn": "Fixing SQLite Session Resurrection & Breaking Infinite Map-Toggle Loops",
                "problemAr": "ظهور بطاقات مهام مكررة وإعادة تفعيل جلسات مكتملة في قاعدة البيانات المحلية، إضافة إلى نقرة انتظار أسفل يسار الشاشة كانت تضغط بالخطأ على زر تبديل العاصمة/الخريطة.",
                "problemEn": "Completed sessions were occasionally resurrected in SQLite causing duplicate dispatches, while an idle bottom-left tap overlapped the map toggle button.",
                "whyImportantAr": "نقرة واحدة خاطئة في حلقة الأتمتة كفيلة بإخراج المحرك من الشاشة المستهدفة وإدخاله في دوران لا نهائي.",
                "whyImportantEn": "A single misplaced coordinate in an autonomous loop can derail state tracking into an infinite toggle cycle.",
                "solutionAr": "ضبط مطابقة اكتمال المسيرة ومنع إحياء الجلسات المنتهية في SQLite (`d5dc166`)، وحذف نقرة الانتظار أسفل اليسار (`a52ed58`) مع توثيق خطة الحظر التام للنقرات الافتراضية (`AUTOMATION_UPGRADE_PLAN.md`).",
                "solutionEn": "Hardened SQLite march completion matching and session state finality (`d5dc166`), removed the bottom-left idle tap (`a52ed58`), and instituted a zero-hardcoded-tap policy (`AUTOMATION_UPGRADE_PLAN.md`).",
                "proofRef": "phone_commander/.git commits d5dc166, a52ed58 & AUTOMATION_UPGRADE_PLAN.md:10-44",
                "impactAr": "تزامن دقيق للطوابير النشطة واختفاء حلقات التبديل العشوائي للشاشة.",
                "impactEn": "Deterministic queue tracking and complete elimination of unintended map-toggle loops.",
                "lessonAr": "كل نقرة في نظام أتمتة بصري يجب أن تكون مشروطة برصد مؤكد (CV/OCR)؛ النقرات الاحتياطية العمياء تخلق أعطالًا أصعب من الفشل الصريح.",
                "lessonEn": "Every interaction in a visual automation loop must be gated by positive CV/OCR detection; blind fallback taps create failure modes worse than explicit retries."
            }
        ],
        "evidence": [
            {
                "claimId": "PHC-01",
                "claimAr": "محرك مطابقة القوالب ZNCC بصفر استنزاف للذاكرة عبر ReusableScaleBuffer وoffsetsForStride",
                "claimEn": "Zero-GC-churn ZNCC TemplateMatcher using ThreadLocal ReusableScaleBuffer and precalculated stride offsets",
                "relationType": "EXTRACTED",
                "evidencePath": "android/app/src/main/kotlin/com/sys/display/assist/cv/TemplateMatcher.kt",
                "lineOrSymbol": "Lines 15-85 (PreparedTemplate, ReusableScaleBuffer)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "PHC-02",
                "claimAr": "محرك الأتمتة الرئيسي (5,264 سطرًا) مع آلة حالة التحالف وتصغير التطبيق لتوفير البطارية",
                "claimEn": "5,264-line AutomationEngine with AllianceFlowStep state machine and battery-saving auto-minimize",
                "relationType": "EXTRACTED",
                "evidencePath": "android/app/src/main/kotlin/com/sys/display/assist/engine/AutomationEngine.kt",
                "lineOrSymbol": "Lines 63-95 (AllianceFlowStep, longWaitMinimizeEnabled)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "PHC-03",
                "claimAr": "إصلاحات موثقة في Git لمنع انهيار Bitmap Recycled ومنع تكرار الجلسات في SQLite",
                "claimEn": "Verified git commits resolving bitmap recycling crashes, SQLite queue resurrection, and map toggle loops",
                "relationType": "EXTRACTED",
                "evidencePath": "phone_commander/.git",
                "lineOrSymbol": "Commits 50927ed, d5dc166, a52ed58, 41c9490",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "PHC-04",
                "claimAr": "مصفوفة عتبات الرصد البصري (86%–92%) وهيكل بث السجلات الحية لواجهة Flutter",
                "claimEn": "Calibrated 86%–92% ZNCC detection threshold matrix and real-time Flutter MethodChannel log schema",
                "relationType": "EXTRACTED",
                "evidencePath": "AUTOMATION_UPGRADE_PLAN.md",
                "lineOrSymbol": "Lines 10-86 (Hardcoded tap audit, AutomationLogPayload, Thresholds Matrix)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            }
        ],
        "screenshots": [
            {
                "src": "/media/projects/phone-commander/cv-safe-roi-zones.webp",
                "altAr": "تحديد منطقة الفحص البصري الصافية (Safe ROI) باللون الأخضر لعزل أشرطة الواجهة عن مساحة الخريطة",
                "altEn": "Computer-vision Safe ROI green boundary isolating playable map area from HUD overlays (privacy-sanitized)",
                "captionAr": "لقطة تشخيصية لمنطقة الفحص الصافية (`Safe ROI` — بعد طمس الإحداثيات والدردشة) التي يحصر فيها محرك ZNCC البحث لتسريع الأداء ومنع الرصد الخاطئ.",
                "captionEn": "Diagnostic view of the green Safe ROI boundary (with player coordinates and chat redacted) restricting ZNCC scanning to avoid HUD false positives.",
                "kind": "diagnostic_output",
                "width": 1400,
                "height": 630
            },
            {
                "src": "/media/projects/phone-commander/zncc-vision-architecture.svg",
                "altAr": "مخطط معمارية محرك الرؤية الحاسوبية ZNCC وآلة الحالة وبث السجلات إلى Flutter",
                "altEn": "Phone Commander Zero-GC ZNCC computer vision and Flutter telemetry architecture diagram",
                "captionAr": "مخطط معماري يوضح دورة الإطار من `ReusableScaleBuffer` حتى مطابقة ZNCC المتوازية ومزامنة SQLite.",
                "captionEn": "Architectural diagram showing zero-GC frame scaling, parallel ZNCC matching, SQLite queue sync, and Flutter MethodChannel streaming.",
                "kind": "architecture_diagram",
                "width": 1200,
                "height": 540
            }
        ],
        "results": [
            {
                "metric": "0 MB/Frame",
                "labelAr": "تخصيص ذاكرة جديدة لكل إطار بفضل إعادة استخدام المخازن المحلية للخيوط",
                "labelEn": "Per-frame bitmap heap allocation eliminated via ThreadLocal ReusableScaleBuffer",
                "sourceRef": "TemplateMatcher.kt:62-85"
            },
            {
                "metric": "0.86 – 0.92",
                "labelAr": "عتبات الثقة المضبوطة في خوارزمية ZNCC لقبول المطابقة البصرية",
                "labelEn": "Configured ZNCC confidence thresholds gating UI template matches",
                "sourceRef": "AUTOMATION_UPGRADE_PLAN.md:76-85"
            },
            {
                "metric": "5,264 Lines",
                "labelAr": "حجم محرك آلة الحالة الذاتية والتعافي من الأخطاء في Kotlin",
                "labelEn": "Autonomous state-machine and error recovery implementation in AutomationEngine.kt",
                "sourceRef": "AutomationEngine.kt:1-5264"
            },
            {
                "metric": "> 15 Min",
                "labelAr": "عتبة تصغير التطبيق التلقائي لتوفير البطارية والحرارة أثناء الانتظار الطويل",
                "labelEn": "Auto-minimize threshold saving battery and thermal load during long waits",
                "sourceRef": "AutomationEngine.kt:89-95"
            }
        ],
        "skillsProven": [
            "Real-Time Mobile Computer Vision (Custom ZNCC & OCR)",
            "Low-Level Memory & GC Optimization (ThreadLocal Buffers)",
            "Native Android Accessibility & MediaProjection Engineering",
            "Flutter-to-Native MethodChannel Bridge & Telemetry",
            "Autonomous State-Machine & Crash Recovery Design"
        ],
        "reviewFlags": [
            "Confirm personal role attribution",
            "Local phone_commander.db and .env excluded from public bundle"
        ],
        "graphStats": {
            "totalFiles": 389,
            "totalMb": 38.49,
            "nodes": 1704,
            "edges": 3056
        },
        "updatedAt": "2026-11-19"
    },
    {
        "slug": "remix-sole-marketplace",
        "titleAr": "متجر سول للأحذية (SOLE)",
        "titleEn": "SOLE Footwear Marketplace",
        "summaryAr": "تطبيق تجارة إلكترونية وكتالوج رقمي ثنائي اللغة (React 19 + Express + Supabase + Cloudinary) يحوّل أرشيف صور الاستوديو إلى متجر سريع مع لوحة إدارة، فحص Magic Bytes للصور، وحماية ضد حقن PostgREST وPath Traversal.",
        "summaryEn": "Full-stack footwear marketplace (React 19, Express, TypeScript, Supabase, Cloudinary) transforming studio photo archives into a high-speed storefront with an admin panel, binary Magic-Byte upload validation, PostgREST injection guards, and offline static fallback.",
        "valuePropositionAr": "تحويل مجلدات صور المنتجات الملتقطة بالكاميرا أو واتساب تلقائيًا إلى متجر إلكتروني أنيق وسريع ومحصن أمنيًا مع استمرارية عمل حتى عند انقطاع قاعدة البيانات.",
        "valuePropositionEn": "Automatically normalizes raw studio/WhatsApp image folders into an editorial footwear storefront with binary upload security and static JSON fallback resilience.",
        "category": ["web", "API", "security"],
        "status": "production",
        "visibility": "published",
        "featured": True,
        "featuredOrder": 3,
        "role": {
            "ar": "تطوير Full-Stack TypeScript وتحصين أمن تطبيقات الويب",
            "en": "Full-Stack TypeScript & Web Application Security Engineering"
        },
        "audience": {
            "ar": "العلامات التجارية ومتاجر الأحذية والأزياء التي تملك أرشيف صور ضخمًا وتريد واجهة عرض وبيع سريعة وسهلة الإدارة.",
            "en": "Footwear and fashion retailers with large studio photo archives seeking a fast, low-friction digital catalog and admin suite."
        },
        "problem": {
            "ar": "رفع مئات الصور مباشرة من الهاتف أو واتساب (`IMG-20261029-WA0019`) داخل مجلدات مختلطة العربية والإنجليزية (`Y3فاشون`) ينتج أسماء منتجات مشوهة، كما أن قراءة Cloudinary مباشرة مع كل زائر يستهلك حصة الـ API، وقبول رفع الملفات بالامتداد فقط يفتح ثغرات XSS ورفع ملفات خبيثة.",
            "en": "Uploading hundreds of raw WhatsApp/camera photos (`IMG-20261029-WA0019`) in fused Arabic/Latin folders (`Y3فاشون`) creates messy product titles, while live Cloudinary scans on visitor traffic exhaust API quotas and naive file uploads invite spoofed SVG/EXE attacks."
        },
        "solution": {
            "ar": "بناء محرك تطبيع لغوي ثنائي اللغة يحول أسماء ملفات الكاميرا والمجلدات تلقائيًا إلى عناوين أنيقة (`Y3 فاشون · موديل 0019`)، وفصل حركة الزوار لتقرأ من Supabase مع ملف احتياطي `catalog-fallback.json` وصور Cloudinary متجاوبة (`srcset`)، وتحصين الخادم بفحص البايتات السحرية (`Magic Bytes`) ومنع حقن PostgREST.",
            "en": "Built a bilingual lexical normalizer turning raw camera filenames into clean editorial titles (`Y3 فاشون · موديل 0019`), decoupled public visitor traffic from Cloudinary Admin API scans via Supabase + `catalog-fallback.json`, and hardened the Express API with binary Magic-Byte inspection and PostgREST injection filters."
        },
        "manualVsAutomated": {
            "ar": "بدلًا من إعادة تسمية 506 صورة يدويًا وضغطها في برامج التصميم، يستورد النظام المجلدات ويولّد عناوين عربية/إنجليزية نظيفة وروابط `f_auto,q_auto` متعددة الأحجام تلقائيًا.",
            "en": "Eliminates manual renaming and resizing across 506 studio photos by automatically formatting bilingual titles and generating responsive `f_auto,q_auto` `srcset` URLs."
        },
        "capabilities": [
            {
                "ar": "وحدة أمان خادم شاملة (`src/server/security.ts`) تفحص البايتات السحرية (Magic Bytes) وتمنع ملفات SVG/HTML/EXE المنتحلة وحقن PostgREST وPath Traversal.",
                "en": "Hardened security module (`src/server/security.ts`) validating binary Magic Bytes (blocking spoofed SVG/HTML/EXE), PostgREST identifiers, and Cloudinary paths."
            },
            {
                "ar": "مطبّع أسماء ذكي للعربية والإنجليزية (`src/utils/catalog.ts`) يفصل النصوص الملتصقة ويعالج تسميات صور واتساب.",
                "en": "Bilingual slug and filename normalizer (`src/utils/catalog.ts`) splitting fused Arabic/Latin strings and formatting WhatsApp image codes."
            },
            {
                "ar": "عزل كامل لزيارات المتجر العام عن Cloudinary Admin API عبر `fetchSupabasePublicCatalog` وملف `catalog-fallback.json`.",
                "en": "Zero-Cloudinary-scan public catalog loading via Supabase active categories with automatic fallback to `public/catalog-fallback.json`."
            },
            {
                "ar": "مكون صور متجاوب (`OptimizedImage.tsx`) يولّد `srcset` بأحجام 400w–1200w وصيغ WebP/AVIF التلقائية.",
                "en": "Responsive image pipeline (`OptimizedImage.tsx`) generating 400w–1200w Cloudinary `f_auto,q_auto` transformation `srcset` attributes."
            }
        ],
        "architecture": {
            "overviewAr": "تطبيق Full-Stack موحد يعمل بـ React 19 وVite 8 في الواجهة، وخادم Express 4 في الخلفية يُحزم عبر `esbuild` ليعمل كدالة Serverless على Vercel (`api/index.js`) مع قاعدة بيانات Supabase وCloudinary CDN.",
            "overviewEn": "Unified Full-Stack TypeScript architecture running React 19 + Tailwind CSS 4 on the client and an Express 4 API bundled via `esbuild` into a Vercel Serverless entrypoint (`api/index.js`), backed by Supabase and Cloudinary.",
            "pipelineSteps": [
                {
                    "step": "01",
                    "titleAr": "استيراد وتطبيع أرشيف الاستوديو (Studio Ingestion & Normalization)",
                    "titleEn": "Admin Cloudinary Ingestion & Bilingual Normalization",
                    "detailAr": "استبعاد مجلدات العينات (`samples`)، وفصل الحروف العربية عن اللاتينية، وتحويل رموز الكاميرا إلى أسماء موديلات منظمة.",
                    "detailEn": "Filters out starter sample folders, splits fused Arabic/English labels, and converts camera IDs into clean model names."
                },
                {
                    "step": "02",
                    "titleAr": "بوابة الأمان والتحقق الثنائي (Magic-Byte & PostgREST Security Gate)",
                    "titleEn": "Binary Magic-Byte & PostgREST Security Validation",
                    "detailAr": "فحص التوقيع الثنائي للملفات المرفوعة، وتطهير النصوص من محارف التحكم، والتحقق من حدود الأسعار ومعرفات UUID.",
                    "detailEn": "Verifies JPEG/PNG/WebP magic bytes, blocks PostgREST control characters, and enforces strict price/UUID bounds."
                },
                {
                    "step": "03",
                    "titleAr": "العرض السريع والمرونة الاحتياطية (Supabase Public Catalog & Fallback)",
                    "titleEn": "High-Speed Storefront Delivery & Static Fallback",
                    "detailAr": "تقديم الكتالوج العام من Supabase مباشرة (أو من `catalog-fallback.json` عند الطوارئ) مع صور CDN متجاوبة.",
                    "detailEn": "Serves public catalog queries from Supabase RLS tables (or `catalog-fallback.json`) with responsive Cloudinary CDN transforms."
                }
            ],
            "systemBoundariesAr": "يتعامل الزوار فقط مع واجهة القراءة العامة وروابط الصور المحسنة، بينما تُعزل عمليات المزامنة والرفع خلف مصادقة الإدارة وفحوص `security.ts`.",
            "systemBoundariesEn": "Public traffic interacts strictly with read-only Supabase/fallback endpoints and Cloudinary CDN URLs; admin mutations are gated by session auth and `security.ts` validators."
        },
        "technologies": [
            "React 19",
            "TypeScript",
            "Express 4",
            "Tailwind CSS 4",
            "Vite 8 + esbuild",
            "Supabase (PostgreSQL + RLS)",
            "Cloudinary CDN & Admin API",
            "Node.js Native Test Runner"
        ],
        "challenges": [
            {
                "id": "SOL-CH-1",
                "type": "preventive_design",
                "titleAr": "فحص البايتات السحرية (Magic Bytes) للصور ومنع حقن فلاتر PostgREST واختراق المسارات",
                "titleEn": "Binary Magic-Byte Upload Verification & PostgREST Filter Injection Hardening",
                "problemAr": "قبول الصور بناءً على امتداد `.jpg` أو `Content-Type` يسمح برفع ملفات SVG تحتوي على `<script>` أو ملفات تنفيذية `MZ`، كما أن تمرير معرفات الدخول دون تصفية يسمح بحقن شروط إضافية في فلاتر PostgREST.",
                "problemEn": "Validating uploads solely by `.jpg` extension or MIME header allows XSS-laden SVGs or Windows `.exe` binaries (`MZ`) to slip through, while raw login identifiers can inject operators into PostgREST filter strings.",
                "whyImportantAr": "حماية لوحة إدارة المتجر وقاعدة البيانات ومجلدات السحابة من ثغرات XSS ورفع الملفات الخبيثة وتجاوز الصلاحيات.",
                "whyImportantEn": "Protects the merchant admin panel, database queries, and cloud storage paths against stored XSS, malicious binaries, and filter tampering.",
                "solutionAr": "كتابة وحدة `src/server/security.ts` للتحقق من البايتات السحرية الفعلية (`0xFF 0xD8 0xFF` لـ JPEG و`0x89 0x50 0x4E 0x47` لـ PNG)، وحظر الفواصل والأقواس وعلامات الاقتباس في `isValidLoginIdentifier`، ومنع `..` في مسارات Cloudinary، وإثباتها باختبارات `security.test.ts`.",
                "solutionEn": "Implemented `validateImageUploadBuffer` checking raw binary signatures while rejecting `<svg`/`<html`/`MZ` payloads, `isValidLoginIdentifier` blocking PostgREST metacharacters, and `isValidCloudinaryFolder` blocking path traversal — all verified in `security.test.ts`.",
                "proofRef": "src/server/security.ts:18-95 & src/server/security.test.ts:13-95",
                "impactAr": "صد 100% لملفات SVG/HTML/EXE المنتحلة وهجمات حقن الفلاتر واختراق المسارات في الاختبارات الآلية.",
                "impactEn": "100% automated test rejection of spoofed SVG/HTML/EXE buffers, SQL/PostgREST filter payloads, and `../` traversal strings.",
                "lessonAr": "أمن رفع الملفات يبدأ من قراءة البايتات الأولى للذاكرة (`Buffer`)، وليس من metadata يرسلها المتصفح.",
                "lessonEn": "Upload security must inspect the first bytes of the binary buffer, never browser-supplied filenames or MIME headers."
            },
            {
                "id": "SOL-CH-2",
                "type": "verified_fix",
                "titleAr": "تطبيع أسماء صور الكاميرا وواتساب المختلطة وفصل الزوار عن استهلاك حصص Cloudinary API",
                "titleEn": "Bilingual Camera Filename Normalization & Decoupling Public Traffic from Cloudinary Quotas",
                "problemAr": "أرشيف الصور الفعلي للمتجر (506 صورة في 15 مجلدًا) يحتوي أسماء مثل `IMG-20261029-WA0019` ومجلدات مثل `Y3فاشون` و`عرض ال150`، وكان استدعاء Cloudinary Admin API عند تصفح الزوار يهدد بنفاد حصة الطلبات.",
                "problemEn": "The merchant's 506-image studio archive contained raw WhatsApp filenames (`IMG-20261029-WA0019`) and fused bilingual folder names (`Y3فاشون`, `عرض ال150`), while live Cloudinary Admin scans per visitor risked rate-limit exhaustion.",
                "whyImportantAr": "تحويل أرشيف الصور الخام إلى متجر احترافي فوري دون إجبار التاجر على إدخال 506 منتجًا يدويًا ودون بطء أو توقف للمتجر.",
                "whyImportantEn": "Enables zero-touch onboarding of existing photo archives while keeping public page loads fast and immune to third-party API rate limits.",
                "solutionAr": "بناء دوال `formatCategoryLabel` و`formatProductDisplayName` مع اختبارات وحدة شاملة (`catalog.test.ts`) لتحويل الأسماء تلقائيًا إلى `Y3 فاشون · موديل 0019`، وجعل الزوار يقرؤون من `fetchSupabasePublicCatalog` أو `catalog-fallback.json`.",
                "solutionEn": "Engineered regex normalizers in `src/utils/catalog.ts` tested in `catalog.test.ts`, and restricted public catalog reads to `fetchSupabasePublicCatalog` with automatic fallback to `public/catalog-fallback.json`.",
                "proofRef": "src/utils/catalog.test.ts:32-60 & src/server/catalogService.ts:50-95",
                "impactAr": "عرض 506 منتجًا في 15 مجموعة بتسميات عربية/إنجليزية نظيفة وصفر استهلاك لـ Cloudinary Admin API من زيارات العملاء.",
                "impactEn": "Clean editorial presentation for 506 products across 15 collections with zero live Cloudinary Admin API calls on customer visits.",
                "lessonAr": "فصل مسار استيراد البيانات الإداري (Ingestion) عن مسار القراءة العام (Public Read) يحمي الأداء والتكلفة معًا.",
                "lessonEn": "Separating admin asset ingestion from public read paths protects both latency and third-party API quotas."
            }
        ],
        "evidence": [
            {
                "claimId": "SOL-01",
                "claimAr": "وحدة أمان تفحص البايتات السحرية للصور وتمنع ملفات SVG/HTML/EXE المنتحلة وحقن PostgREST",
                "claimEn": "Security module inspecting image Magic Bytes and blocking spoofed SVG/HTML/EXE, PostgREST injection, and path traversal",
                "relationType": "EXTRACTED",
                "evidencePath": "src/server/security.ts & src/server/security.test.ts",
                "lineOrSymbol": "security.ts:8-95 & security.test.ts:13-95",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "SOL-02",
                "claimAr": "تطبيع ثنائي اللغة لأسماء المجلدات وصور واتساب وتوليد روابط Cloudinary المتجاوبة (srcset)",
                "claimEn": "Bilingual Arabic/English folder & WhatsApp filename normalizer and responsive Cloudinary srcset builder",
                "relationType": "EXTRACTED",
                "evidencePath": "src/utils/catalog.test.ts",
                "lineOrSymbol": "Lines 32-60 (formatCategoryLabel, formatProductDisplayName, buildCloudinarySrcSet)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "SOL-03",
                "claimAr": "قراءة الكتالوج العام من Supabase مباشرة مع ملف احتياطي دون فحص Cloudinary الحي للزوار",
                "claimEn": "Public catalog isolation querying Supabase active categories with static fallback and zero live Cloudinary scans",
                "relationType": "EXTRACTED",
                "evidencePath": "src/server/catalogService.ts",
                "lineOrSymbol": "Lines 22-95 (getPublicSiteSettings, fetchSupabasePublicCatalog)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            }
        ],
        "screenshots": [
            {
                "src": "/media/projects/remix-sole-marketplace/storefront-catalog.webp",
                "altAr": "واجهة متجر سول (SOLE) تعرض 506 موديل أحذية موزعة على 15 قسمًا بتصميم عصري",
                "altEn": "SOLE Footwear Marketplace storefront displaying 506 curated silhouettes across 15 bilingual collections",
                "captionAr": "لقطة شاشة فعلية لواجهة المتجر (`SOLE Digital Archive`): عرض 506 منتجًا في 15 مجموعة مع فلترة فورية وتسميات عربية/إنجليزية مطبّعة.",
                "captionEn": "Real storefront screenshot (`SOLE Digital Archive`) showcasing 506 normalized products across 15 collections with instant filtering.",
                "kind": "real_screenshot",
                "width": 1400,
                "height": 875
            },
            {
                "src": "/media/projects/remix-sole-marketplace/security-architecture.svg",
                "altAr": "مخطط معمارية متجر سول وبوابة فحص البايتات السحرية وعزل الكتالوج العام",
                "altEn": "SOLE Marketplace full-stack architecture and Magic-Byte security diagram",
                "captionAr": "مخطط معماري يوضح طبقات الأمان (`security.ts`) وتطبيع الكتالوج وعزل الزوار عن فحص Cloudinary المباشر.",
                "captionEn": "Architecture diagram illustrating Magic-Byte upload filtering, PostgREST injection guards, bilingual normalization, and Supabase/fallback catalog delivery.",
                "kind": "architecture_diagram",
                "width": 1200,
                "height": 540
            }
        ],
        "results": [
            {
                "metric": "506 Products",
                "labelAr": "منتجًا حقيقيًا تم استيرادها وتطبيع أسمائها عبر 15 قسمًا",
                "labelEn": "Studio products ingested and normalized across 15 collections",
                "sourceRef": "public/catalog-fallback.json & storefront screenshot"
            },
            {
                "metric": "0 Live Scans",
                "labelAr": "استدعاءات Cloudinary Admin API أثناء تصفح الزوار بفضل طبقة Supabase والملف الاحتياطي",
                "labelEn": "Cloudinary Admin API calls triggered by public visitors",
                "sourceRef": "src/server/catalogService.ts:50-54"
            },
            {
                "metric": "100% Blocked",
                "labelAr": "منع كامل لملفات SVG/HTML/EXE المزيفة وحقن فلاتر PostgREST في اختبارات الوحدة",
                "labelEn": "Spoofed SVG/HTML/EXE uploads and PostgREST injection payloads rejected in tests",
                "sourceRef": "src/server/security.test.ts:13-95"
            },
            {
                "metric": "400w – 1200w",
                "labelAr": "توليد تلقائي لروابط صور Cloudinary المتجاوبة (srcset) بصيغ f_auto,q_auto",
                "labelEn": "Responsive Cloudinary srcset transformations (f_auto,q_auto)",
                "sourceRef": "src/utils/catalog.test.ts:46-59"
            }
        ],
        "skillsProven": [
            "Full-Stack TypeScript (React 19 + Express + Vercel Serverless)",
            "Web Application Security (Magic-Byte Validation & Injection Prevention)",
            "Bilingual Arabic/English Text & Slug Normalization",
            "Media CDN Optimization (Responsive Cloudinary srcset)",
            "High-Availability Fallback Architecture"
        ],
        "reviewFlags": [
            "Confirm personal role attribution",
            ".env file inside archive excluded from public build"
        ],
        "graphStats": {
            "totalFiles": 51,
            "totalMb": 9.81,
            "nodes": 320,
            "edges": 848
        },
        "updatedAt": "2026-11-19"
    },
    {
        "slug": "gmail-options-suite",
        "titleAr": "منظومة أتمتة المتصفح المتعددة",
        "titleEn": "Multi-Slot Browser Automation Suite",
        "summaryAr": "منصة أتمتة بايثون معيارية مستقلة مع لوحة إدارة، تدير سلوتات متصفح متوازية معزولة كليًا (BrowserContext + Proxy Locking + Humanization) وتتعامل مع حالات الفشل والتصنيف الذري للملفات.",
        "summaryEn": "Modular standalone Python browser automation suite with an admin panel, managing isolated multi-slot Camoufox/Playwright contexts, proxy locking, Bezier humanization, thread-safe atomic result routing, and deep forensic stealth auditing.",
        "valuePropositionAr": "تشغيل مهام متصفح متوازية بعزل 100% للجلسات والبروكسيات مع تحديث ذري آمن للملفات وتدقيق جنائي عميق لسطح الكشف.",
        "valuePropositionEn": "Executes concurrent browser workflows with 100% session/proxy isolation, thread-safe atomic state persistence, and forensic anti-detection auditing.",
        "category": ["automation", "desktop", "CLI", "security"],
        "status": "functional",
        "visibility": "published",
        "featured": False,
        "featuredOrder": 6,
        "role": {
            "ar": "تصميم معمارية الأتمتة والتدقيق الجنائي للمتصفحات",
            "en": "Automation Systems Architecture & Browser Forensics Analysis"
        },
        "audience": {
            "ar": "فرق هندسة الأتمتة واختبار الأنظمة التي تحتاج تشغيل جلسات متصفح متعددة دون تداخل في الكوكيز أو البروكسيات.",
            "en": "Automation engineering teams needing isolated multi-slot browser execution and deterministic failure handling."
        },
        "problem": {
            "ar": "إغلاق الصفحة (`page.close()`) فقط في Playwright يترك الكوكيز والبصمة حية في الجلسة، كما أن تشغيل عدة خيوط متوازية يسبب تصادمًا في سحب البروكسيات أو تلفًا في ملفات الإدخال عند التحديث المتزامن.",
            "en": "Closing only a Playwright `Page` leaks cookies and fingerprint state across runs, while concurrent worker threads risk proxy collisions and corrupted input/output files."
        },
        "solution": {
            "ar": "تصميم مدير سلوتات يدمر `Page` و`BrowserContext` معًا في كتلة `finally` مع قفل البروكسي (`lock_proxy` / `unlock_proxy`)، وبناء `RecoveryFailureHandler` بقفل `threading.Lock()` لحذف السجل المعالج وتصنيفه ذريًا في الوقت الحقيقي، مع إجراء تدقيق جنائي شامل (`camoufox_forensic_audit.md`).",
            "en": "Engineered a slot lifecycle manager enforcing full `Page` + `BrowserContext` destruction and proxy locking in `finally` blocks, a thread-safe `RecoveryFailureHandler` using `threading.Lock()` for atomic file pruning, and a 1,276-line forensic audit of Camoufox/Playwright internals."
        },
        "manualVsAutomated": {
            "ar": "بدلًا من إدارة المتصفحات يدويًا أو فقدان تقدم التشغيل عند حدوث خطأ، يعزل النظام كل سلوت ببصمة وبروكسي مستقلين ويصنف النتائج لحظيًا دون تكرار.",
            "en": "Replaces fragile single-session scripts with isolated per-slot browser contexts, locked proxy rotation, and real-time crash-safe output routing."
        },
        "capabilities": [
            {
                "ar": "عزل كامل للجلسات عبر تدمير `BrowserContext` بعد كل مهمة وتدوير البروكسيات المقفولة.",
                "en": "100% session state teardown destroying both `Page` and `BrowserContext` per task with exclusive proxy locking."
            },
            {
                "ar": "مصنف أخطاء ذري متعدد الخيوط (`RecoveryFailureHandler`) يستخدم `threading.Lock()` لتحديث ملفات الإدخال والمخرجات بأمان.",
                "en": "Thread-safe `RecoveryFailureHandler` using `threading.Lock()` for atomic input pruning and categorized output routing."
            },
            {
                "ar": "محرك محاكاة بشرية (`shared/browser_engine/humanization/`) يشمل منحنيات Bezier للماوس وفيزياء التمرير والكتابة.",
                "en": "Humanization engine implementing cubic Bezier mouse trajectories, typing cadence simulation, and smooth scroll physics."
            },
            {
                "ar": "تقرير تدقيق جنائي عميق (1,276 سطرًا) يفحص 10 إشارات في بروتوكول Playwright وWebRTC وSOCKS5.",
                "en": "1,276-line forensic security audit analyzing 10 protocol, WebRTC, SOCKS5 auth downgrade, and pointer-event signals."
            }
        ],
        "architecture": {
            "overviewAr": "بنية بايثون معيارية مفصولة بالكامل (`83/83` ملفًا تترجم بنجاح بصفر اعتماديات خارجية مكسورة) تضم حزمة السيناريوهات (`scenarios/`)، البنية المشتركة (`shared/browser_engine/`)، ولوحة الإدارة (`admin_panel/`).",
            "overviewEn": "Decoupled modular Python architecture (verified across 83/83 compiled modules with zero broken imports) comprising `scenarios/`, `shared/browser_engine/`, and `admin_panel/`.",
            "pipelineSteps": [
                {
                    "step": "01",
                    "titleAr": "حجز السلوت وقفل البروكسي (Slot & Proxy Lock)",
                    "titleEn": "Slot Allocation & Exclusive Proxy Locking",
                    "detailAr": "سحب بروكسي متاح وقفله للسلوت الحالي لمنع استخدامه من خيط آخر.",
                    "detailEn": "Acquires and locks an available proxy for the active worker slot."
                },
                {
                    "step": "02",
                    "titleAr": "إطلاق السياق المعزول والمحاكاة (Isolated Context & Humanization)",
                    "titleEn": "Fresh BrowserContext Launch & Bezier Humanization",
                    "detailAr": "إنشاء `BrowserContext` جديد ببصمة وأبعاد شاشة مستقلة وتنفيذ خطوات السيناريو بحركة ماوس وكتابة طبيعية.",
                    "detailEn": "Creates a fresh `BrowserContext` with isolated fingerprint settings and executes scenario steps via Bezier mouse/typing helpers."
                },
                {
                    "step": "03",
                    "titleAr": "التصنيف الذري وتدمير الجلسة (Atomic Routing & Teardown)",
                    "titleEn": "Thread-Safe Result Classification & Full Context Teardown",
                    "detailAr": "كتابة النتيجة وحذف السجل من الملف الرئيسي تحت قفل `threading.Lock`، ثم إغلاق الصفحة والسياق وفك قفل البروكسي.",
                    "detailEn": "Atomically logs results and prunes input lines under `threading.Lock`, then destroys `Page` + `BrowserContext` and unlocks the proxy."
                }
            ],
            "systemBoundariesAr": "يعمل محليًا عبر Python وPlaywright/Camoufox مع لوحة إدارة سطح مكتب وتكامل ترخيص، وتم استبعاد ملف `license.key` من الحزمة العامة.",
            "systemBoundariesEn": "Runs locally via Python and Playwright/Camoufox with a desktop admin panel; local `license.key` is strictly excluded from public artifacts."
        },
        "technologies": [
            "Python 3.12+",
            "Playwright",
            "Camoufox (Custom Firefox Engine)",
            "BrowserForge",
            "Thread-Safe File IO (threading.Lock)",
            "Cubic Bezier Humanization",
            "Desktop Admin Panel UI"
        ],
        "challenges": [
            {
                "id": "GML-CH-1",
                "type": "preventive_design",
                "titleAr": "منع تسرب الكوكيز والبصمة بين المهام عبر التدمير الإجباري لـ BrowserContext وقفل البروكسيات",
                "titleEn": "Preventing Cross-Task State Leakage via Mandatory BrowserContext Teardown & Proxy Locks",
                "problemAr": "إغلاق التبويب (`page.close()`) وحده داخل Playwright لا يمسح الكوكيز أو LocalStorage أو إعدادات البروكسي المرتبطة بـ `BrowserContext`.",
                "problemEn": "Calling `page.close()` alone in Playwright preserves cookies, session storage, and proxy bindings inside the parent `BrowserContext`.",
                "whyImportantAr": "أي بقايا جلسة سابقة تؤدي إلى تداخل الحسابات وفشل عزل السلوتات المتوازية.",
                "whyImportantEn": "Leftover context state contaminates subsequent tasks and invalidates multi-slot isolation.",
                "solutionAr": "فرض إغلاق مزدوج في كتلة `finally` (`await page.close()` + `await context.close()` + `unlock_proxy`) مع حماية تحديث ملفات النتائج بقفل `threading.Lock()` في `RecoveryFailureHandler`.",
                "solutionEn": "Enforced mandatory `finally` teardown (`page.close()` + `context.close()` + `unlock_proxy`) paired with `threading.Lock()` atomic file pruning in `RecoveryFailureHandler`.",
                "proofRef": "browser_data_and_slots_report.md:33-86 & scenarios/recovery/failure_handler.py:31-75",
                "impactAr": "عزل 100% بين كل مهمة وأخرى وعدم ضياع أو تكرار أي سجل أثناء التشغيل المتوازي.",
                "impactEn": "100% state isolation between tasks and zero race-condition file corruption across concurrent worker slots.",
                "lessonAr": "في أتمتة المتصفحات، وحدة العزل الحقيقية هي `BrowserContext` وليست الصفحة (`Page`).",
                "lessonEn": "In browser automation architectures, `BrowserContext` — never `Page` — is the true unit of identity and storage isolation."
            },
            {
                "id": "GML-CH-2",
                "type": "possible_risk",
                "titleAr": "التدقيق الجنائي لـ 10 إشارات كشف في تكامل Camoufox وPlaywright",
                "titleEn": "Forensic Audit Uncovering 10 Protocol & Behavioral Detection Signals in Camoufox/Playwright",
                "problemAr": "استخدام محرك متصفح معدل على مستوى C++ قد يظل قابلاً للرصد إذا كانت إعدادات Playwright أو الشبكة تسرب إشارات غير طبيعية.",
                "problemEn": "Even with a C++-patched stealth browser binary, application-layer Playwright configs and proxy handlers can leak automation anomalies.",
                "whyImportantAr": "فهم الفجوات الدقيقة بين طبقة المتصفح وطبقة البروتوكول ضروري لتقييم المخاطر بصدق بدل افتراض التخفي الكامل.",
                "whyImportantEn": "Identifying subtle mismatches between browser internals and protocol configs prevents false confidence in stealth setups.",
                "solutionAr": "إجراء تحليل جنائي شامل موثق في `camoufox_forensic_audit.md` (1,276 سطرًا) كشف 10 مخاطر محددة مثل خفض بروكسي SOCKS5 المحمي بكلمة مرور إلى HTTP، وتعطيل WebRTC كليًا بدل تمويهه، وانخفاض كثافة نقاط حركة الماوس (مصنف بصدق كـ `possible_risk` مرصود بالتدقيق).",
                "solutionEn": "Conducted a 1,276-line forensic audit (`camoufox_forensic_audit.md`) pinpointing 10 concrete risks including silent SOCKS5-with-auth downgrade to HTTP, total WebRTC disabling, Nightly BuildID mismatch, and low mouse step density (transparently classified as `possible_risk`).",
                "proofRef": "camoufox_forensic_audit.md:14-90",
                "impactAr": "خريطة طريق هندسية واضحة لمعالجة ثغرات البروتوكول والسلوك مرتبة حسب الخطورة.",
                "impactEn": "Actionable severity-ranked remediation matrix covering protocol, network, and behavioral layers.",
                "lessonAr": "التدقيق الجنائي الصادق الذي يوثق القيود والمخاطر المكتشفة يبني ثقة هندسية أعلى بكثير من ادعاء الكمال.",
                "lessonEn": "Honest forensic auditing that documents discovered architectural risks builds far greater engineering credibility than claiming perfection."
            }
        ],
        "evidence": [
            {
                "claimId": "GML-01",
                "claimAr": "عزل 100% للجلسات عبر تدمير Page وBrowserContext معًا وفك قفل البروكسي في كتلة finally",
                "claimEn": "100% session isolation destroying both Page and BrowserContext in finally blocks with proxy unlock",
                "relationType": "EXTRACTED",
                "evidencePath": "browser_data_and_slots_report.md",
                "lineOrSymbol": "Lines 33-86 (shared/browser/firefox_engine.py L124-169)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "GML-02",
                "claimAr": "معالج أخطاء ذري متعدد الخيوط RecoveryFailureHandler يحذف السجل المعالج ويصنفه تحت قفل threading.Lock",
                "claimEn": "Thread-safe atomic account line removal and classified failure routing in RecoveryFailureHandler",
                "relationType": "EXTRACTED",
                "evidencePath": "scenarios/recovery/failure_handler.py",
                "lineOrSymbol": "Lines 24-90 (remove_account_from_main_file, handle_result)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "GML-03",
                "claimAr": "تقرير تدقيق جنائي من 1,276 سطرًا يوثق 10 ثغرات بروتوكول وشبكة وسلوك في تكامل Camoufox",
                "claimEn": "1,276-line deep forensic audit of Camoufox 0.4.11 & Playwright 1.49.1 identifying 10 anomalies",
                "relationType": "EXTRACTED",
                "evidencePath": "camoufox_forensic_audit.md",
                "lineOrSymbol": "Lines 1-90 (Executive Summary & 10 Ranked Findings)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "GML-04",
                "claimAr": "فصل معماري مستقل مفحوص عبر 83 ملف بايثون بصفر أخطاء استيراد أو مسارات خارجية",
                "claimEn": "Standalone architectural extraction verified across 83/83 compiled Python files with zero broken imports",
                "relationType": "EXTRACTED",
                "evidencePath": "verification_report.md",
                "lineOrSymbol": "Lines 1-46 (Safety, Compilation & Directory Audit)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            }
        ],
        "screenshots": [
            {
                "src": "/media/projects/gmail-options-suite/slot-isolation-architecture.svg",
                "altAr": "مخطط معمارية عزل سلوتات المتصفح المتوازية وقفل البروكسيات والتصنيف الذري",
                "altEn": "Multi-Slot Browser Engine context isolation, proxy locking, and atomic failure routing diagram",
                "captionAr": "رسم معماري توضيحي (`Illustrative Architecture Diagram`) يوضح دورة حياة السلوت من قفل البروكسي وإنشاء `BrowserContext` حتى التصنيف الذري وتدمير الجلسة.",
                "captionEn": "Illustrative architecture diagram showing slot lifecycle from proxy lock acquisition and fresh `BrowserContext` creation to thread-safe result routing and teardown.",
                "kind": "architecture_diagram",
                "width": 1200,
                "height": 540
            }
        ],
        "results": [
            {
                "metric": "100% Isolated",
                "labelAr": "تدمير كامل لسياق الجلسة والكوكيز وتبديل البروكسي بين كل عملية وأخرى",
                "labelEn": "Complete BrowserContext teardown and proxy rotation between executions",
                "sourceRef": "browser_data_and_slots_report.md:33-61"
            },
            {
                "metric": "83/83 Modules",
                "labelAr": "ملف بايثون مفصول ومترجم بنجاح بصفر اعتماديات خارجية مكسورة",
                "labelEn": "Standalone Python modules compiling cleanly with zero external path leaks",
                "sourceRef": "verification_report.md:17-19"
            },
            {
                "metric": "10 Findings",
                "labelAr": "إشارات بروتوكول وسلوك موثقة في تقرير التدقيق الجنائي (1,276 سطرًا)",
                "labelEn": "Protocol and behavioral anomalies documented in the 1,276-line forensic audit",
                "sourceRef": "camoufox_forensic_audit.md:16-28"
            },
            {
                "metric": "Atomic Lock",
                "labelAr": "حذف وتصنيف ذري للسجلات المعالجة عبر threading.Lock لمنع التضارب",
                "labelEn": "Thread-safe atomic input pruning and output routing via threading.Lock",
                "sourceRef": "scenarios/recovery/failure_handler.py:31-75"
            }
        ],
        "skillsProven": [
            "Browser Internals & Protocol Forensics (Playwright / Camoufox)",
            "Concurrent Session Isolation & Resource Locking",
            "Thread-Safe File Persistence & Crash Recovery",
            "Modular Python Architecture & Dependency Decoupling"
        ],
        "reviewFlags": [
            "Confirm personal role attribution",
            "license.key excluded from public bundle"
        ],
        "graphStats": {
            "totalFiles": 272,
            "totalMb": 2.91,
            "nodes": 1757,
            "edges": 4374
        },
        "updatedAt": "2026-11-19"
    },
    {
        "slug": "rok-vision-controller",
        "titleAr": "محرك معايرة الشاشات عبر ADB",
        "titleEn": "Universal ADB Screen Controller",
        "summaryAr": "أداة تحكم بايثون عبر `uiautomator2` وADB تحل مشكلة اختلاف أبعاد ونسب الشاشات (16:9، 20:9، الأجهزة اللوحية) عبر خوارزمية تحويل إحداثيات مرتكزة على نقاط الإرساء (`ScreenScaler`).",
        "summaryEn": "Python ADB automation controller using `uiautomator2` that solves multi-device aspect-ratio drift (16:9, 19.5:9, 20:9, tablets) via an anchor-based geometric coordinate transformer (`ScreenScaler`).",
        "valuePropositionAr": "تشغيل نفس سيناريو التحكم عبر ADB على أي هاتف أو جهاز لوحي مهما اختلفت دقة الشاشة أو نسبة العرض إلى الارتفاع دون إعادة معايرة يدوية.",
        "valuePropositionEn": "Runs ADB UI automation accurately across arbitrary screen resolutions and aspect ratios (16:9, 19.5:9, 20:9, tablets) without per-device coordinate recalibration.",
        "category": ["automation", "CLI"],
        "status": "functional",
        "visibility": "published",
        "featured": False,
        "featuredOrder": 7,
        "role": {
            "ar": "تطوير خوارزمية التحويل الهندسي وأتمتة ADB",
            "en": "Geometric UI Scaling & ADB Automation Engineering"
        },
        "audience": {
            "ar": "مطورو أتمتة الهواتف واختبار الواجهات الأفقية عبر أجهزة ومحاكي أندرويد متعددة الأحجام.",
            "en": "Mobile automation engineers testing or running landscape UI workflows across diverse Android viewports."
        },
        "problem": {
            "ar": "النسب المئوية البسيطة `(X%, Y%)` تنحرف عن مواقع الأزرار عند الانتقال من شاشة 16:9 إلى شاشة هاتف عريضة 20:9 (2400x1080)، لأن محركات الواجهات الأفقية تحجّم العناصر نسبةً لارتفاع الشاشة فقط وتثبتها في زوايا الشاشة.",
            "en": "Flat `(X%, Y%)` screen percentages miss button targets when moving between 16:9 tablets and 20:9 phones (2400x1080), because landscape UI engines scale elements by screen height (`H`) while pinning HUD clusters to viewport corners."
        },
        "solution": {
            "ar": "تطوير فئة `ScreenScaler` في `rok_universal_controller.py` التي تقفل معامل التحجيم على ارتفاع الشاشة (`scale = h / 1080.0`) وتحسب الإحداثيات نسبةً إلى 5 نقاط إرساء (`center`, `bottom_left`, `top_left`, `bottom_center`, `top_right`) مع فرض الاتجاه الأفقي تلقائيًا.",
            "en": "Built `ScreenScaler` in `rok_universal_controller.py` locking the scale factor to screen height (`scale = h / 1080.0`) and projecting reference coordinates from 5 semantic HUD anchors (`center`, `bottom_left`, `top_left`, `bottom_center`, `top_right`)."
        },
        "manualVsAutomated": {
            "ar": "بدلًا من قياس وحفظ جدول إحداثيات منفصل لكل جهاز، يُعرّف العنصر مرة واحدة على الشاشة المرجعية (2400x1080) مع نقطة إرسائه، ويتكفل `ScreenScaler` بحساب الموقع الدقيق على أي شاشة.",
            "en": "Eliminates per-device coordinate tables by defining each UI element once in 2400x1080 reference space with its anchor tag and transforming coordinates dynamically at runtime."
        },
        "capabilities": [
            {
                "ar": "محول إحداثيات هندسي (`ScreenScaler`) يدعم 5 مناطق إرساء (`center`, `bottom_left`, `top_left`, `bottom_center`, `top_right`).",
                "en": "Anchor-based geometric coordinate transformer (`ScreenScaler`) supporting 5 viewport anchor zones."
            },
            {
                "ar": "تطبيع تلقائي للاتجاه الأفقي (`w = max(raw_w, raw_h)`, `h = min(raw_w, raw_h)`) عبر `uiautomator2`.",
                "en": "Automatic landscape orientation normalization (`w = max(raw_w, raw_h)`) on ADB connection."
            },
            {
                "ar": "جدول شبكة ديناميكي ثنائي الأعمدة (`CHAR_GRID_CONFIG`) للتنقل بين الشخصيات مع التمرير التلقائي.",
                "en": "Dynamic 2-column character grid geometry (`CHAR_GRID_CONFIG`) with scroll-adjusted row targeting."
            },
            {
                "ar": "تأخير زمني عشوائي يحاكي السلوك البشري (5.0 إلى 10.0 ثوانٍ) بين النقرات المتتالية.",
                "en": "Human-like randomized post-click delay envelope (5.0s–10.0s) with live cycle countdowns."
            }
        ],
        "architecture": {
            "overviewAr": "يتكون المشروع من نسختين توثقان تطور الحل الهندسي: `rok_controller.py` (النسب المئوية المباشرة) و`rok_universal_controller.py` (التحويل الهندسي المعتمد على نقاط الإرساء `ScreenScaler`).",
            "overviewEn": "Demonstrates clear architectural evolution from `rok_controller.py` (flat percentage ratios) to `rok_universal_controller.py` (anchor-aware `ScreenScaler` geometric projection).",
            "pipelineSteps": [
                {
                    "step": "01",
                    "titleAr": "الاتصال عبر ADB وتطبيع الأبعاد (ADB Connect & Landscape Lock)",
                    "titleEn": "ADB Connection & Landscape Dimension Normalization",
                    "detailAr": "الاتصال بالجهاز عبر `uiautomator2` وقراءة أبعاد النافذة مع ضمان `w > h`.",
                    "detailEn": "Connects via `uiautomator2` and enforces landscape width/height ordering."
                },
                {
                    "step": "02",
                    "titleAr": "التحويل الهندسي بنقاط الإرساء (Anchor-Based Projection)",
                    "titleEn": "Height-Locked Anchor Coordinate Transformation",
                    "detailAr": "حساب `scale = h / 1080.0` وإسقاط الإحداثيات المرجعية من الزاوية أو المركز المرتبط بالعنصر.",
                    "detailEn": "Computes `scale = h / 1080.0` and projects `(ref_x, ref_y)` relative to the element's semantic anchor."
                },
                {
                    "step": "03",
                    "titleAr": "تنفيذ الدورة متعددة الشخصيات (Multi-Character Loop)",
                    "titleEn": "Automated Multi-Character Cycle & Humanized Delays",
                    "detailAr": "التبديل الاختياري بين الشخصيات وتنفيذ خطوات البحث والجمع الأربع بفاصل زمني عشوائي.",
                    "detailEn": "Iterates across characters and executes the 4-step gathering flow with randomized human delays."
                }
            ],
            "systemBoundariesAr": "أداة CLI خفيفة تعمل عبر Python وADB مباشرة دون تعديل ملفات التطبيق المستهدف.",
            "systemBoundariesEn": "Lightweight Python CLI communicating strictly over standard Android Debug Bridge (`uiautomator2`)."
        },
        "technologies": [
            "Python 3.13",
            "uiautomator2",
            "ADB (Android Debug Bridge)",
            "Geometric Viewport Scaling"
        ],
        "challenges": [
            {
                "id": "ROK-CH-1",
                "type": "verified_fix",
                "titleAr": "معالجة انحراف الإحداثيات عبر نسب الشاشات المختلفة بالانتقال إلى التحجيم المرتكز على الزوايا",
                "titleEn": "Eliminating Multi-Device Aspect-Ratio Drift via Height-Locked Anchor Scaling",
                "problemAr": "في النسخة الأولى (`rok_controller.py`)، كانت الإحداثيات النسبية `(X_ratio, Y_ratio)` تعمل على شاشة واحدة لكنها تنحرف أفقيًا على الشاشات الأعوص أو الأجهزة اللوحية.",
                "problemEn": "In `rok_controller.py`, flat `(X_ratio, Y_ratio)` coordinates worked on the calibration device but drifted horizontally on wider or narrower aspect ratios.",
                "whyImportantAr": "توفير أداة تعمل فورًا على أي هاتف أو محاكي دون مطالبة المستخدم بقياس البكسلات يدويًا.",
                "whyImportantEn": "Allows the controller to run out-of-the-box on any phone, tablet, or emulator without manual pixel hunting.",
                "solutionAr": "بناء `ScreenScaler` في `rok_universal_controller.py` لفصل معامل التحجيم (`self.h / 1080.0`) عن نقطة ارتكاز كل عنصر (`center`, `bottom_left`, `top_left`, `bottom_center`, `top_right`).",
                "solutionEn": "Implemented `ScreenScaler` in `rok_universal_controller.py:5-63` decoupling height-proportional scale (`self.h / 1080.0`) from the 5 viewport anchor origins.",
                "proofRef": "rok_controller.py:21-63 vs rok_universal_controller.py:5-95",
                "impactAr": "تطابق دقيق لمواقع النقر عبر شاشات 16:9 و19.5:9 و20:9 والأجهزة اللوحية.",
                "impactEn": "Exact button hit accuracy across 16:9, 19.5:9, 20:9, and tablet aspect ratios.",
                "lessonAr": "واجهات التطبيقات الأفقية لا تتمدد خطيًا في الاتجاهين؛ محاكاة نظام الإرساء (Anchoring) الخاص بمحرك الواجهة هو الحل الهندسي الصحيح.",
                "lessonEn": "Landscape UIs do not stretch linearly on both axes; mirroring the UI engine's own anchor-pinning model is the only mathematically sound scaling approach."
            }
        ],
        "evidence": [
            {
                "claimId": "ROK-01",
                "claimAr": "فئة ScreenScaler تحول إحداثيات 2400x1080 بمعامل ارتفاع الشاشة و5 نقاط إرساء",
                "claimEn": "ScreenScaler class transforming 2400x1080 coordinates via height-locked scale and 5 HUD anchors",
                "relationType": "EXTRACTED",
                "evidencePath": "rok_universal_controller.py",
                "lineOrSymbol": "Lines 5-63 (ScreenScaler.get_coords)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            },
            {
                "claimId": "ROK-02",
                "claimAr": "فرض الاتجاه الأفقي تلقائيًا وتأخير عشوائي 5–10 ثوانٍ بين النقرات",
                "claimEn": "Automatic landscape orientation enforcement and randomized 5s–10s post-click delay",
                "relationType": "EXTRACTED",
                "evidencePath": "rok_controller.py",
                "lineOrSymbol": "Lines 84-95 (RoKController.__init__)",
                "confidence": "HIGH",
                "visibility": "public",
                "verificationStatus": "verified"
            }
        ],
        "screenshots": [
            {
                "src": "/media/projects/rok-vision-controller/anchor-screen-scaler.svg",
                "altAr": "مخطط تقني يوضح خوارزمية ScreenScaler ونقاط الإرساء الخمس عبر أبعاد الشاشات",
                "altEn": "Technical diagram of ScreenScaler height-locked coordinate projection across 5 viewport anchors",
                "captionAr": "رسم تقني توضيحي (`Illustrative Technical Diagram`) يشرح كيف تحافظ خوارزمية `ScreenScaler` على دقة الإحداثيات عند تغير نسبة أبعاد الشاشة.",
                "captionEn": "Illustrative technical diagram demonstrating how `ScreenScaler` preserves button accuracy across 16:9 and 20:9 aspect ratios.",
                "kind": "architecture_diagram",
                "width": 1200,
                "height": 540
            }
        ],
        "results": [
            {
                "metric": "5 Anchors",
                "labelAr": "نقاط إرساء هندسية (المركز والأركان) لمعالجة اختلاف نسب الشاشات",
                "labelEn": "Semantic viewport anchors handling aspect-ratio variance",
                "sourceRef": "rok_universal_controller.py:27-62"
            },
            {
                "metric": "2400x1080",
                "labelAr": "الفضاء المرجعي الموحد المحول ديناميكيًا بمعامل ارتفاع الشاشة",
                "labelEn": "Reference coordinate space dynamically scaled by h / 1080.0",
                "sourceRef": "rok_universal_controller.py:11-21"
            },
            {
                "metric": "5.0s – 10.0s",
                "labelAr": "نطاق التأخير العشوائي بين النقرات لمحاكاة التفاعل الطبيعي",
                "labelEn": "Randomized humanization delay envelope between ADB taps",
                "sourceRef": "rok_controller.py:84-86"
            },
            {
                "metric": "16:9 – 20:9",
                "labelAr": "دعم مختلف نسب العرض إلى الارتفاع للهواتف والأجهزة اللوحية دون انحراف",
                "labelEn": "Aspect-ratio compatibility across phones and tablets without drift",
                "sourceRef": "rok_universal_controller.py:5-26"
            }
        ],
        "skillsProven": [
            "ADB & uiautomator2 Device Automation",
            "Geometric UI Coordinate Transformation (Anchor Scaling)",
            "Iterative Refactoring from Fixed Scripts to Universal Engines"
        ],
        "reviewFlags": [
            "Confirm personal role attribution",
            "Raw game profile screenshots in D:\\rok excluded from public display to protect account privacy"
        ],
        "graphStats": {
            "totalFiles": 16,
            "totalMb": 14.65,
            "nodes": 64,
            "edges": 108
        },
        "updatedAt": "2026-11-19"
    },
    {
        "slug": "draft-internal-sandbox",
        "titleAr": "[مسودة داخلية] مشروع تجريبي لاختبار عزل المسودات عن البناء العام",
        "titleEn": "[Internal Draft] Sandbox Project Verifying Draft Exclusion from Public Build",
        "summaryAr": "سجل اختباري بحالة visibility=draft للتأكد من أن محرك Astro لا ينشر المسودات للعامة.",
        "summaryEn": "Verification fixture with visibility=draft ensuring the Astro build strictly excludes unpublished drafts from public routes.",
        "valuePropositionAr": "اختبار آلي لفلترة المسودات.",
        "valuePropositionEn": "Automated draft filtering verification fixture.",
        "category": ["other"],
        "status": "prototype",
        "visibility": "draft",
        "featured": False,
        "featuredOrder": 99,
        "role": {"ar": "اختبار", "en": "Test"},
        "audience": {"ar": "اختبار", "en": "Test"},
        "problem": {"ar": "اختبار", "en": "Test"},
        "solution": {"ar": "اختبار", "en": "Test"},
        "manualVsAutomated": {"ar": "اختبار", "en": "Test"},
        "capabilities": [{"ar": "اختبار", "en": "Test"}],
        "architecture": {
            "overviewAr": "اختبار",
            "overviewEn": "Test",
            "pipelineSteps": [
                {"step": "01", "titleAr": "اختبار", "titleEn": "Test", "detailAr": "اختبار", "detailEn": "Test"}
            ],
            "systemBoundariesAr": "اختبار",
            "systemBoundariesEn": "Test"
        },
        "technologies": ["Test"],
        "challenges": [
            {
                "id": "DRF-1",
                "type": "unverified_story",
                "titleAr": "اختبار",
                "titleEn": "Test",
                "problemAr": "اختبار",
                "problemEn": "Test",
                "whyImportantAr": "اختبار",
                "whyImportantEn": "Test",
                "solutionAr": "اختبار",
                "solutionEn": "Test",
                "proofRef": "Test",
                "impactAr": "اختبار",
                "impactEn": "Test",
                "lessonAr": "اختبار",
                "lessonEn": "Test"
            }
        ],
        "evidence": [
            {
                "claimId": "DRF-01",
                "claimAr": "اختبار",
                "claimEn": "Test",
                "relationType": "INFERRED",
                "evidencePath": "test",
                "lineOrSymbol": "L1",
                "confidence": "LOW",
                "visibility": "private",
                "verificationStatus": "unverified"
            }
        ],
        "screenshots": [
            {
                "src": "/media/projects/rok-vision-controller/anchor-screen-scaler.svg",
                "altAr": "اختبار",
                "altEn": "Test",
                "captionAr": "اختبار",
                "captionEn": "Test",
                "kind": "illustrative_demo",
                "width": 1200,
                "height": 540
            }
        ],
        "results": [
            {"metric": "0", "labelAr": "اختبار", "labelEn": "Test", "sourceRef": "test"}
        ],
        "skillsProven": ["Test"],
        "reviewFlags": ["Draft fixture — must never appear in public build"],
        "graphStats": {"totalFiles": 1, "totalMb": 0.01, "nodes": 1, "edges": 0},
        "updatedAt": "2026-11-19"
    }
]


def main():
    for item in PROJECTS_CONTENT:
        out_path = CONTENT_DIR / f"{item['slug']}.json"
        out_path.write_text(json.dumps(item, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Wrote content collection entry: {out_path.name} (visibility={item['visibility']}, featured={item['featured']})")


if __name__ == "__main__":
    main()
