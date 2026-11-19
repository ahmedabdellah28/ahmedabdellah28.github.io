export interface EngineeringStrength {
  id: string;
  domain: 'ai_media' | 'optimization' | 'computer_vision' | 'distributed_resilience' | 'security_fullstack' | 'automation_forensics';
  titleAr: string;
  titleEn: string;
  clientExplanationAr: string;
  clientExplanationEn: string;
  technicalExplanationAr: string;
  technicalExplanationEn: string;
  supportingProjects: string[];
  proofTypeAr: string;
  proofTypeEn: string;
  evidenceRefs: string[];
  confidence: 'HIGH' | 'MEDIUM';
}

export const ENGINEERING_STRENGTHS: EngineeringStrength[] = [
  {
    id: 'contract-driven-ai-compilers',
    domain: 'ai_media',
    titleAr: 'تصميم خطوط إنتاج الذكاء الاصطناعي والمترجمات الرسومية المحكومة بالعقود',
    titleEn: 'Contract-Driven AI Pipelines & Multi-Stage Media Compilers',
    clientExplanationAr:
      'تحويل العمليات الإبداعية والإنتاجية المعقدة (مثل إنتاج الفيديو، الدبلجة، وتحليل النصوص) إلى خطوط إنتاج آلية موثوقة لا تتلف المخرجات السابقة وتفحص جودة عملها ذاتيًا.',
    clientExplanationEn:
      'Transforming complex creative and document workflows into deterministic, self-verifying pipelines that isolate each run and guarantee broadcast-ready outputs.',
    technicalExplanationAr:
      'بناء خط إنتاج من 13 مرحلة (`PIPELINE_CONTRACTS.md`) ومترجم رسومي من 10 مراحل (`ecgc_compiler.py`) مع مدقق ثوابت (`audit_scene_graph`) يفحص تباين الإضاءة (`_hex_luma`)، وحدود التوقيت، وانحراف الصوت/الصورة (<0.35s)، مع حماية المشاريع الذهبية بـ `PermissionError` وعزل كل تشغيل في `exports/runs/<run_id>/`.',
    technicalExplanationEn:
      'Engineered a 13-stage contract-gated pipeline and 10-stage Scene Graph V2 compiler (`ecgc_compiler.py`) with automated invariant auditing (`audit_scene_graph`), luma contrast checks (`_hex_luma`), RMS voice-ducking audio mixing, and write-protected golden reference baselines.',
    supportingProjects: ['image-to-animate', 'school-timetable'],
    proofTypeAr: 'كود مصدري + عقود JSON Schema + تحقيق جنائي (RCA) + مخرجات QA مرندرة',
    proofTypeEn: 'Source Code + JSON Schema Contracts + Forensic RCA + Rendered QA Contact Sheets',
    evidenceRefs: [
      'image-to-animate :: PIPELINE_CONTRACTS.md:9-36',
      'image-to-animate :: core/aion/ecgc_compiler.py:1-85',
      'image-to-animate :: core/aion/contracts.py:46-90',
      'image-to-animate :: V5_GOLD_REGRESSION_RCA_AR.md:15-90',
    ],
    confidence: 'HIGH',
  },
  {
    id: 'mathematical-optimization-cpsat',
    domain: 'optimization',
    titleAr: 'الاستمثال الرياضي (CP-SAT) والإصلاح الذكي القابل للتفسير (Explainable Smart Repair)',
    titleEn: 'Mathematical Constraint Optimization (OR-Tools CP-SAT) & Explainable Repair',
    clientExplanationAr:
      'حل مشكلات الجدولة وتوزيع الموارد المستحيلة يدويًا في ثوانٍ بصفر تضارب، مع شرح واضح للمستخدم عند إجراء أي تعديل يدوي والبدائل المتاحة دون هدم الجدول.',
    clientExplanationEn:
      'Solving resource scheduling problems in seconds with zero conflicts, while providing transparent before/after causal explanations when users make manual adjustments.',
    technicalExplanationAr:
      'صياغة قيود خطية (`Linear Gap Formulations`) في Google OR-Tools CP-SAT مسبوقة بمحلل جدوى رياضي (`FeasibilityAnalyzer` لمنع فخ الاستحالة المعكوس `Inverted Pigeonhole`)، ومتبوعة بمدقق مستقل بدون ثقة مسبقة (`ScheduleValidator`) ومحرك إصلاح موضعي (`MoveLessonCommand` + `LocalRepairEngine`) يعرض سلسلة الحصص المزاحة مع حفظ `is_pinned` في SQLite.',
    technicalExplanationEn:
      'Formulated linear-gap CP-SAT models preceded by pre-solve mathematical feasibility checks (`FeasibilityAnalyzer`), verified by an independent zero-trust `ScheduleValidator`, and paired with a minimal-perturbation repair call chain (`MoveLessonCommand`) surfacing displaced lesson diffs.',
    supportingProjects: ['school-timetable'],
    proofTypeAr: 'محرك CP-SAT + 36 اختبار Pytest + اختبار ضغط (600 حصة) + تدقيق سلسلة الاستدعاء',
    proofTypeEn: 'CP-SAT Solver + 36 Pytest Suite + 600-Period Stress Test + Call-Chain Diff Audit',
    evidenceRefs: [
      'school-timetable :: README.md:10-36 & 80-90',
      'school-timetable :: CHANGE_IMPACT_BEFORE_AFTER.md:12-90',
      'school-timetable :: خطة_إصلاح_وتطوير_منظومة_القيود_الشاملة.md:34-74',
      'school-timetable :: src/school_scheduler/ai_studio/api_server.py:1-76',
    ],
    confidence: 'HIGH',
  },
  {
    id: 'realtime-cv-memory-optimization',
    domain: 'computer_vision',
    titleAr: 'الرؤية الحاسوبية الفورية على الهواتف (ZNCC) وتحسين الذاكرة والتحويل الهندسي للأبعاد',
    titleEn: 'On-Device Computer Vision (Zero-GC ZNCC) & Anchor-Based Viewport Scaling',
    clientExplanationAr:
      'بناء أنظمة تفهم محتوى الشاشة بصريًا وتعمل لساعات طويلة على مختلف الهواتف والأجهزة اللوحية دون استنزاف البطارية أو انهيار التطبيق أو الانحراف عن الأزرار.',
    clientExplanationEn:
      'Building visual recognition engines that run continuously across phones and tablets without memory crashes, battery drain, or aspect-ratio coordinate drift.',
    technicalExplanationAr:
      'تنفيذ خوارزمية `Zero-Mean Normalized Cross-Correlation (ZNCC)` في Kotlin باستخدام مخازن محلية للخيوط (`ThreadLocal ReusableScaleBuffer`) وإزاحات صفوف محسوبة مسبقًا (`offsetsForStride`) لتفادي تخصيص ~8MB في كل إطار، مع خوارزمية `ScreenScaler` في بايثون التي تقفل التحجيم على الارتفاع (`h / 1080.0`) عبر 5 نقاط إرساء هندسية.',
    technicalExplanationEn:
      'Implemented parallel ZNCC template matching in Kotlin using `ThreadLocal` `ReusableScaleBuffer` and cached 1D row-stride pixel offsets (`offsetsForStride`) to eliminate ~8MB/frame GC churn, complemented by height-locked 5-anchor geometric projection (`ScreenScaler`) for aspect-ratio independence.',
    supportingProjects: ['phone-commander', 'rok-vision-controller', 'image-to-animate'],
    proofTypeAr: 'كود Kotlin/Python مصدري + سجلات إصلاح Git + لقطات تشخيص ROI البصرية',
    proofTypeEn: 'Kotlin/Python Source + Verified Git Stability Commits + CV ROI Diagnostic Outputs',
    evidenceRefs: [
      'phone-commander :: TemplateMatcher.kt:15-85',
      'phone-commander :: AutomationEngine.kt:63-95 & git commit 50927ed',
      'rok-vision-controller :: rok_universal_controller.py:5-63 (ScreenScaler)',
      'image-to-animate :: asset_sheet_extractor_v2_output/preview_diagnostics.png',
    ],
    confidence: 'HIGH',
  },
  {
    id: 'offline-resilience-distributed-sync',
    domain: 'distributed_resilience',
    titleAr: 'هندسة الاعتمادية، مزامنة الطوابير غير المتصلة (Offline Outbox)، والتعافي من الفشل',
    titleEn: 'Offline-First Outbox Synchronization, Jittered Backoff & State Recovery',
    clientExplanationAr:
      'ضمان عدم ضياع بيانات المستخدم أو عملياته الحرجة عند انقطاع الإنترنت أو حدوث خطأ مفاجئ، مع استئناف العمل تلقائيًا بهدوء فور استقرار الاتصال.',
    clientExplanationEn:
      'Preventing lost user transactions during network drops or crashes, automatically recovering and syncing pending work once connectivity returns.',
    technicalExplanationAr:
      'بناء `OfflineSyncManager` في Flutter لمراقبة تغير حالة الشبكة وتفريغ طابور العمليات مع إعادة جدولة الفشل الجزئي فقط تحت قفل تزامن، وبناء `ErrorRecoveryService` بـ Exponential Backoff وعامل Jitter عشوائي (`0.8 + random * 0.4`)، واستخدام `threading.Lock()` للحذف والتصنيف الذري في بايثون، ومنع إحياء جلسات SQLite المنتهية.',
    technicalExplanationEn:
      'Designed `OfflineSyncManager` with mutex-guarded queue draining and selective failure re-insertion, `ErrorRecoveryService` with jittered exponential backoff for transient 503/504/socket faults, `threading.Lock()` atomic file pruning in `RecoveryFailureHandler`, and SQLite session deduplication.',
    supportingProjects: ['enaya-ai-workspace', 'gmail-options-suite', 'phone-commander', 'remix-sole-marketplace'],
    proofTypeAr: 'خدمات Dart/Python مصدرية + التزامات Git إصلاحية + ملفات Fallback احتياطية',
    proofTypeEn: 'Dart/Python Service Implementations + Git Remediation Commits + Static JSON Fallbacks',
    evidenceRefs: [
      'enaya-ai-workspace :: offline_sync_manager.dart:8-90',
      'enaya-ai-workspace :: error_recovery_service.dart:15-69',
      'gmail-options-suite :: scenarios/recovery/failure_handler.py:24-90',
      'phone-commander :: git commit d5dc166',
      'remix-sole-marketplace :: src/server/catalogService.ts:32-95',
    ],
    confidence: 'HIGH',
  },
  {
    id: 'app-security-fullstack-hardening',
    domain: 'security_fullstack',
    titleAr: 'تحصين تطبيقات الويب والـ APIs، فحص البايتات السحرية (Magic Bytes)، وحماية قواعد البيانات',
    titleEn: 'Application Security Hardening, Binary Magic-Byte Validation & RLS Governance',
    clientExplanationAr:
      'حماية المتاجر والمنصات السحابية من رفع الملفات الخبيثة، واختراق المسارات، والتلاعب ببيانات المستخدمين أو استنزاف حصص الخدمات السحابية.',
    clientExplanationEn:
      'Protecting web platforms and cloud APIs against malicious file uploads, query injection, path traversal, and third-party API quota exhaustion.',
    technicalExplanationAr:
      'فحص التوقيع الثنائي الفعلي (`Magic Bytes`) للصور المرفوعة ورفض ملفات SVG/HTML/EXE المنتحلة في `validateImageUploadBuffer`، ومنع محارف حقن PostgREST في `isValidLoginIdentifier`، وحظر `..` في مسارات Cloudinary، وعزل خوارزميات الحل خلف `LicenseManager` في FastAPI، وتدقيق سياسات Supabase RLS.',
    technicalExplanationEn:
      'Enforced binary Magic-Byte header verification rejecting spoofed SVG/HTML/EXE uploads, strict PostgREST filter metacharacter blocking, path traversal rejection, license-gated FastAPI endpoints (`_require_license`), and multi-tenant Supabase RLS policy reviews.',
    supportingProjects: ['remix-sole-marketplace', 'enaya-ai-workspace', 'school-timetable'],
    proofTypeAr: 'وحدة أمان TypeScript + اختبارات وحدة أمنية (security.test.ts) + وثائق تدقيق RLS',
    proofTypeEn: 'TypeScript Security Module + Automated Security Unit Tests + Supabase RLS Audit Docs',
    evidenceRefs: [
      'remix-sole-marketplace :: src/server/security.ts:8-95',
      'remix-sole-marketplace :: src/server/security.test.ts:13-95',
      'school-timetable :: src/school_scheduler/ai_studio/api_server.py:62-76',
      'enaya-ai-workspace :: 05_final_docs/RLS_POLICY_REVIEW.md',
    ],
    confidence: 'HIGH',
  },
  {
    id: 'arabic-rtl-engineering-bilingual-ux',
    domain: 'automation_forensics',
    titleAr: 'هندسة العربية وRTL المتقدمة، وتطبيع البيانات المختلطة، والتدقيق الجنائي للأنظمة',
    titleEn: 'Advanced Arabic/RTL Engineering, Bilingual Lexical Normalization & Systems Forensics',
    clientExplanationAr:
      'تقديم تجربة عربية وإنجليزية أصلية وسليمة 100% في الواجهات وملفات PDF والفيديوهات والمتاجر، حتى عندما تكون البيانات المدخلة غير منظمة أو مختلطة اللغات.',
    clientExplanationEn:
      'Delivering native Arabic RTL and English experiences across web UIs, print-ready A4 PDFs, motion graphics, and e-commerce catalogs — even from messy bilingual inputs.',
    technicalExplanationAr:
      'تطوير مطبّع نصوص ثنائي اللغة يفصل الحروف العربية الملتصقة باللاتينية والأرقام ويعالج أسماء ملفات واتساب (`formatCategoryLabel`, `formatProductDisplayName`)، وتشكيل النصوص العربية ثنائية الاتجاه في تقارير PDF عبر `arabic-reshaper` و`python-bidi`، وضبط اتجاه الكشف الحركي للنصوص في `ecgc_compiler.py`، وإجراء تحقيقات جنائية موثقة للأعطال.',
    technicalExplanationEn:
      'Built bilingual lexical normalizers (`formatCategoryLabel`, `formatProductDisplayName`) with unit tests, Arabic bidirectional shaping (`arabic-reshaper` + `python-bidi`) in ReportLab PDF exporters, RTL kinetic typography in `ecgc_compiler.py`, and deep forensic audit reports (`camoufox_forensic_audit.md`, `V5_GOLD_REGRESSION_RCA_AR.md`).',
    supportingProjects: ['remix-sole-marketplace', 'school-timetable', 'image-to-animate', 'gmail-options-suite'],
    proofTypeAr: 'اختبارات تطبيع ثنائية اللغة (catalog.test.ts) + مصدرات PDF عربية + تقارير تدقيق جنائي',
    proofTypeEn: 'Bilingual Unit Tests (catalog.test.ts) + RTL PDF Exporters + Forensic Audit Reports',
    evidenceRefs: [
      'remix-sole-marketplace :: src/utils/catalog.test.ts:32-45',
      'school-timetable :: README.md:30-33 (arabic-reshaper + python-bidi)',
      'image-to-animate :: core/aion/ecgc_compiler.py:47-50 (is_rtl_text)',
      'gmail-options-suite :: camoufox_forensic_audit.md:1-90',
    ],
    confidence: 'HIGH',
  },
];
