# مصفوفة المهارات والأدلة التقنية (`docs/skills-evidence-matrix.md`)

> لا تعتمد هذه المصفوفة على سرد أسماء اللغات والمكتبات المثبتة، بل تربط كل قدرة هندسية بالقرارات البرمجية والاختبارات والملفات التي تبرهن عليها عبر المشاريع السبعة.

## 1. تصميم خطوط إنتاج الذكاء الاصطناعي والمترجمات الرسومية المحكومة بالعقود
- **الشرح بلغة العميل:** تحويل العمليات الإبداعية والإنتاجية المعقدة (مثل إنتاج الفيديو، الدبلجة، وتحليل النصوص) إلى خطوط إنتاج آلية موثوقة لا تتلف المخرجات السابقة وتفحص جودة عملها ذاتيًا.
- **التفسير التقني:** بناء خط إنتاج من 13 مرحلة (`PIPELINE_CONTRACTS.md`) ومترجم رسومي من 10 مراحل (`ecgc_compiler.py`) يترجم `aion.scene_graph.v2` إلى مشاريع EffectCraft GPU وفيديوهات MP4، مع مدقق ثوابت (`audit_scene_graph`) يفحص تباين الإضاءة (`_hex_luma`)، وحدود التوقيت، وانحراف الصوت/الصورة (<0.35s)، مع قفل برمجي (`PermissionError`) لحماية المشروع المرجعي الذهبي.
- **المشاريع الداعمة:** `image-to-animate`, `school-timetable`
- **الأدلة المرجعية (`EXTRACTED` / `verified`):**
  - `E:\image_to_animate\PIPELINE_CONTRACTS.md` (الأسطر 9–36)
  - `E:\image_to_animate\core\aion\ecgc_compiler.py` (الأسطر 1–85)
  - `E:\image_to_animate\core\aion\contracts.py` (الأسطر 46–90: `_hex_luma`, `audit_scene_graph`)
  - `E:\image_to_animate\V5_GOLD_REGRESSION_RCA_AR.md` (الأسطر 15–90)
- **مستوى الثقة:** `HIGH`

---

## 2. الاستمثال الرياضي (OR-Tools CP-SAT) والإصلاح الذكي القابل للتفسير
- **الشرح بلغة العميل:** حل مشكلات الجدولة وتوزيع الموارد المستحيلة يدويًا في ثوانٍ بصفر تضارب، مع شرح واضح للمستخدم عند إجراء أي تعديل يدوي والبدائل المتاحة دون هدم الجدول.
- **التفسير التقني:** صياغة قيود خطية (`Linear Gap Formulations`) في Google OR-Tools CP-SAT مسبوقة بمحلل جدوى رياضي (`FeasibilityAnalyzer` لمنع فخ الاستحالة المعكوس `Inverted Pigeonhole`)، ومتبوعة بمدقق مستقل بدون ثقة مسبقة (`ScheduleValidator`) ومحرك إصلاح موضعي (`MoveLessonCommand` + `LocalRepairEngine`) يعرض سلسلة الحصص المزاحة مع حفظ `is_pinned` في SQLite.
- **المشاريع الداعمة:** `school-timetable`
- **الأدلة المرجعية (`EXTRACTED` / `verified`):**
  - `E:\جدول_مدرسة\README.md` (الأسطر 10–36 و80–90: 36 اختبار Pytest + اختبار ضغط 600 حصة)
  - `E:\جدول_مدرسة\CHANGE_IMPACT_BEFORE_AFTER.md` (الأسطر 12–90)
  - `E:\جدول_مدرسة\خطة_إصلاح_وتطوير_منظومة_القيود_الشاملة.md` (الأسطر 34–74)
  - `E:\جدول_مدرسة\src\school_scheduler\ai_studio\api_server.py` (الأسطر 1–76)
- **مستوى الثقة:** `HIGH`

---

## 3. الرؤية الحاسوبية الفورية على الهواتف (Zero-GC ZNCC) والتحويل الهندسي للأبعاد
- **الشرح بلغة العميل:** بناء أنظمة تفهم محتوى الشاشة بصريًا وتعمل لساعات طويلة على مختلف الهواتف والأجهزة اللوحية دون استنزاف البطارية أو انهيار التطبيق أو الانحراف عن الأزرار.
- **التفسير التقني:** تنفيذ خوارزمية `Zero-Mean Normalized Cross-Correlation (ZNCC)` في Kotlin باستخدام مخازن محلية للخيوط (`ThreadLocal ReusableScaleBuffer`) وإزاحات صفوف محسوبة مسبقًا (`offsetsForStride`) لتفادي تخصيص ~8MB في كل إطار، مع خوارزمية `ScreenScaler` في بايثون التي تقفل التحجيم على الارتفاع (`h / 1080.0`) عبر 5 نقاط إرساء هندسية.
- **المشاريع الداعمة:** `phone-commander`, `rok-vision-controller`, `image-to-animate`
- **الأدلة المرجعية (`EXTRACTED` / `verified`):**
  - `D:\app_access\phone_commander\android\app\src\main\kotlin\com\sys\display\assist\cv\TemplateMatcher.kt` (الأسطر 15–85)
  - `D:\app_access\phone_commander\android\app\src\main\kotlin\com\sys\display\assist\engine\AutomationEngine.kt` (الأسطر 63–95 + Commit `50927ed`)
  - `D:\rok\rok_universal_controller.py` (الأسطر 5–63: `ScreenScaler.get_coords`)
- **مستوى الثقة:** `HIGH`

---

## 4. هندسة الاعتمادية، مزامنة الطوابير غير المتصلة (Offline Outbox)، والتعافي من الفشل
- **الشرح بلغة العميل:** ضمان عدم ضياع بيانات المستخدم أو عملياته الحرجة عند انقطاع الإنترنت أو حدوث خطأ مفاجئ، مع استئناف العمل تلقائيًا بهدوء فور استقرار الاتصال.
- **التفسير التقني:** بناء `OfflineSyncManager` في Flutter لمراقبة تغير حالة الشبكة وتفريغ طابور العمليات مع إعادة جدولة الفشل الجزئي فقط تحت قفل تزامن (`_isSyncing`)، وبناء `ErrorRecoveryService` بـ Exponential Backoff وعامل Jitter عشوائي (`0.8..1.2x`)، واستخدام `threading.Lock()` للحذف والتصنيف الذري في بايثون (`RecoveryFailureHandler`)، ومنع إحياء جلسات SQLite المنتهية (`Commit d5dc166`).
- **المشاريع الداعمة:** `enaya-ai-workspace`, `gmail-options-suite`, `phone-commander`, `remix-sole-marketplace`
- **الأدلة المرجعية (`EXTRACTED` / `verified`):**
  - `D:\enaya_ai_audit_workspace\enaya_monorepo\apps\doctor_app\lib\core\services\offline_sync_manager.dart` (الأسطر 8–90)
  - `D:\enaya_ai_audit_workspace\enaya_monorepo\apps\laboratory_app\lib\core\services\error_recovery_service.dart` (الأسطر 15–69)
  - `D:\gmail-options-main\gmail-options-main\scenarios\recovery\failure_handler.py` (الأسطر 24–90)
- **مستوى الثقة:** `HIGH`

---

## 5. تحصين تطبيقات الويب والـ APIs وفحص البايتات السحرية (Magic Bytes) وحوكمة RLS
- **الشرح بلغة العميل:** حماية المتاجر والمنصات السحابية من رفع الملفات الخبيثة، واختراق المسارات، والتلاعب ببيانات المستخدمين أو استنزاف حصص الخدمات السحابية.
- **التفسير التقني:** فحص التوقيع الثنائي الفعلي (`Magic Bytes`) للصور المرفوعة ورفض ملفات SVG/HTML/EXE المنتحلة في `validateImageUploadBuffer`، ومنع محارف حقن PostgREST في `isValidLoginIdentifier`، وحظر `..` في مسارات Cloudinary، وعزل خوارزميات الحل خلف `LicenseManager` في FastAPI، وتدقيق سياسات Supabase RLS.
- **المشاريع الداعمة:** `remix-sole-marketplace`, `enaya-ai-workspace`, `school-timetable`
- **الأدلة المرجعية (`EXTRACTED` / `verified`):**
  - `remix-sole :: src/server/security.ts` (الأسطر 8–95) و`src/server/security.test.ts` (الأسطر 13–95)
  - `E:\جدول_مدرسة\src\school_scheduler\ai_studio\api_server.py` (الأسطر 62–76: `_require_license`)
  - `D:\enaya_ai_audit_workspace\05_final_docs\RLS_POLICY_REVIEW.md`
- **مستوى الثقة:** `HIGH`

---

## 6. هندسة العربية وRTL المتقدمة وتطبيع البيانات المختلطة والتدقيق الجنائي
- **الشرح بلغة العميل:** تقديم تجربة عربية وإنجليزية أصلية وسليمة 100% في الواجهات وملفات PDF والفيديوهات والمتاجر، حتى عندما تكون البيانات المدخلة غير منظمة أو مختلطة اللغات.
- **التفسير التقني:** تطوير مطبّع نصوص ثنائي اللغة يفصل الحروف العربية الملتصقة باللاتينية والأرقام ويعالج أسماء ملفات واتساب (`formatCategoryLabel`, `formatProductDisplayName`)، وتشكيل النصوص العربية ثنائية الاتجاه في تقارير PDF عبر `arabic-reshaper` و`python-bidi`، وضبط اتجاه الكشف الحركي للنصوص في `ecgc_compiler.py`، وإجراء تحقيقات جنائية موثقة للأعطال.
- **المشاريع الداعمة:** `remix-sole-marketplace`, `school-timetable`, `image-to-animate`, `gmail-options-suite`
- **الأدلة المرجعية (`EXTRACTED` / `verified`):**
  - `remix-sole :: src/utils/catalog.test.ts` (الأسطر 32–45)
  - `E:\جدول_مدرسة\README.md` (الأسطر 30–33)
  - `E:\image_to_animate\core\aion\ecgc_compiler.py` (الأسطر 47–50)
  - `D:\gmail-options-main\gmail-options-main\camoufox_forensic_audit.md` (الأسطر 1–90)
- **مستوى الثقة:** `HIGH`
