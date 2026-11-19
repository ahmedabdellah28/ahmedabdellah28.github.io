# كتالوج التحديات والقرارات الهندسية الموثقة (`docs/challenges-catalog.md`)

> يصنف هذا السجل كل مشكلة أو قرار هندسي بصراحة تامة إلى إحدى الفئات الأربع المعتمدة:
> - `verified_fix`: مشكلة موثقة ثم إصلاح مثبت بالكود أو اختبارات الوحدة أو التزامات Git.
> - `preventive_design`: اختيار معماري وقائي مثبت في الكود لمنع فئة كاملة من الأعطال.
> - `possible_risk`: خطر أو قيد تقني تم اكتشافه وتوثيقه عبر التدقيق الجنائي (لا يُدّعى أنه ميزة مكتملة).
> - `unverified_story`: رواية أو فرضية تحتاج تأكيد المالك (لا تُنشر للعامة كإنجاز).

## جدول التحديات المصنفة (13 حالة موثقة)

| الرمز | المشروع | التصنيف | العنوان الملخص | الدليل المرجعي (`File / Line / Commit`) |
| :---: | :--- | :---: | :--- | :--- |
| `ITA-CH-1` | `image-to-animate` | `verified_fix` | إصلاح تسطيح المشاهد، شبحية النص العربي (Ghosting)، وتداخل ~84 مؤثرًا صوتيًا عبر `mix_scene_graph_audio` مع RMS Ducking | `V5_GOLD_REGRESSION_RCA_AR.md:15-90` & `core/aion/ecgc_compiler.py:39-71` |
| `ITA-CH-2` | `image-to-animate` | `preventive_design` | عزل مجلدات التشغيل `exports/runs/<run_id>/` وقفل المشروع المرجعي الذهبي بـ `PermissionError` | `PIPELINE_CONTRACTS.md:27-36` & `core/aion/contracts.py:64-90` |
| `SCH-CH-1` | `school-timetable` | `verified_fix` | توحيد مسار السحب والإفلات والإصلاح الذكي عبر `MoveLessonCommand` مع جدول الحصص المزاحة وحفظ `is_pinned` في SQLite | `CHANGE_IMPACT_BEFORE_AFTER.md:12-90` & `خطة_إصلاح_وتطوير_منظومة_القيود_الشاملة.md:34-64` |
| `SCH-CH-2` | `school-timetable` | `verified_fix` | معالجة فخ الاستحالة الرياضي المعكوس (`Inverted Pigeonhole Trap`) عندما يكون نصاب المعلم أقل من عدد أيام العمل النشطة | `خطة_إصلاح_وتطوير_منظومة_القيود_الشاملة.md:65-70` |
| `ENA-CH-1` | `enaya-ai-workspace` | `verified_fix` | مزامنة طابور العمليات غير المتصلة (`OfflineSyncManager`) والتعافي من أخطاء الشبكة بـ Exponential Backoff + Jitter (`0.8..1.2x`) | `offline_sync_manager.dart:22-90` & `error_recovery_service.dart:29-68` |
| `ENA-CH-2` | `enaya-ai-workspace` | `preventive_design` | حوكمة التدقيق متعدد الأدوار (12 دورًا) وإلزامية إسناد السطر والملف وسجلات القرارات `DEC-01..12` قبل تعديل المونوريبو | `README.md:7-37`, `MANIFEST.md:1-90` & Commit `a87d911` |
| `PHC-CH-1` | `phone-commander` | `verified_fix` | تصفير استنزاف الذاكرة (`~8MB/frame GC Churn`) ومنع انهيار `Recycled Bitmap` عبر `ThreadLocal ReusableScaleBuffer` و`offsetsForStride` | `TemplateMatcher.kt:27-85` & Git Commit `50927ed` |
| `PHC-CH-2` | `phone-commander` | `verified_fix` | منع إحياء جلسات الجمع المنتهية في SQLite وإزالة نقرة الانتظار المسببة لحلقة تبديل الخريطة اللانهائية | Git Commits `d5dc166`, `a52ed58` & `AUTOMATION_UPGRADE_PLAN.md:10-44` |
| `SOL-CH-1` | `remix-sole-marketplace` | `preventive_design` | فحص البايتات السحرية (`Magic Bytes`) لصد ملفات SVG/HTML/EXE المنتحلة ومنع حقن فلاتر PostgREST واختراق المسارات | `src/server/security.ts:18-95` & `src/server/security.test.ts:13-95` |
| `SOL-CH-2` | `remix-sole-marketplace` | `verified_fix` | تطبيع أسماء صور الكاميرا وواتساب المختلطة (`Y3فاشون` / `WA0019`) وفصل زيارات المتجر العام عن استهلاك حصص Cloudinary API | `src/utils/catalog.test.ts:32-60` & `src/server/catalogService.ts:50-95` |
| `GML-CH-1` | `gmail-options-suite` | `preventive_design` | التدمير الإجباري لـ `BrowserContext` مع `Page` في كتلة `finally` وقفل البروكسيات والحذف الذري عبر `threading.Lock()` | `browser_data_and_slots_report.md:33-86` & `scenarios/recovery/failure_handler.py:31-75` |
| `GML-CH-2` | `gmail-options-suite` | `possible_risk` | التدقيق الجنائي لسطح الكشف في تكامل Camoufox/Playwright ورصد 10 ثغرات بروتوكول وشبكة (مثل خفض SOCKS5-auth إلى HTTP) | `camoufox_forensic_audit.md:14-90` |
| `ROK-CH-1` | `rok-vision-controller` | `verified_fix` | الانتقال من النسب المئوية المسطحة إلى التحويل الهندسي المرتكز على ارتفاع الشاشة و5 نقاط إرساء (`ScreenScaler`) | `rok_controller.py:21-63` مقابل `rok_universal_controller.py:5-95` |
