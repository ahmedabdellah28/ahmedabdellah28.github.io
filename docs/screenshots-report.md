# تقرير الوسائط البصرية ولقطات الشاشة (`docs/screenshots-report.md`)

> يوثق هذا التقرير مصدر كل صورة أو مخطط معماري في `portfolio/public/media/projects/`، وما تم تطهيره لحماية الخصوصية، والتمييز الصريح بين اللقطات الفعلية والرسوم المعمارية التوضيحية.

## جدول الأصول البصرية المنشورة (12 أصلًا بصريًا)

| # | المشروع | ملف الوسائط في الموقع | النوع (`kind`) | المصدر الأصلي وكيفية الحصول عليه | معالجة الخصوصية والتحسين |
| :-: | :--- | :--- | :---: | :--- | :--- |
| 1 | `image-to-animate` | `qa-contact-sheet.webp` | `real_screenshot` | مخرج الفحص الفعلي `projects/mehmed_the_conqueror_ar/.../qa/creative_contact_sheet.png` | خالٍ من البيانات الحساسة؛ حُوّل إلى WebP (`1400x618`) |
| 2 | `image-to-animate` | `storyboard-extractor-diagnostics.webp` | `diagnostic_output` | مخرج تشخيص الرؤية الحاسوبية `asset_sheet_extractor_v2_output/preview_diagnostics.png` | خالٍ من البيانات الحساسة؛ حُوّل إلى WebP (`1400x933`) |
| 3 | `image-to-animate` | `architecture-pipeline.svg` | `architecture_diagram` | مولّد برمجيًا من عقود `PIPELINE_CONTRACTS.md` و`ecgc_compiler.py` | مخطط معماري متجهي (`1200x540`) |
| 4 | `school-timetable` | `master-schedule-ui.webp` | `real_screenshot` | لقطة واجهة التطبيق الفعلية `ai_studio_app/.../r4-master-table-rendered.png` | **تم طمس مربع كود الاشتراك (`OWNER-VIP-2026`)** في الركن العلوي الأيسر وتحويلها إلى WebP (`1400x875`) |
| 5 | `school-timetable` | `architecture-cpsat.svg` | `architecture_diagram` | مولّد برمجيًا من `README.md` و`CHANGE_IMPACT_BEFORE_AFTER.md` | مخطط معماري متجهي (`1200x540`) |
| 6 | `enaya-ai-workspace` | `enaya-ecosystem-architecture.svg` | `architecture_diagram` | رسم معماري توضيحي مبني على `MANIFEST.md` والتطبيقات الخمسة في `enaya_monorepo` | موسوم بوضوح كـ `Illustrative Architecture Diagram`؛ لا يعرض أي بيانات مرضى |
| 7 | `gmail-options-suite` | `slot-isolation-architecture.svg` | `architecture_diagram` | رسم معماري توضيحي مبني على `browser_data_and_slots_report.md` و`failure_handler.py` | مشروع CLI/أتمتة؛ موسوم كـ `Illustrative Architecture Diagram` |
| 8 | `phone-commander` | `cv-safe-roi-zones.webp` | `diagnostic_output` | صورة تشخيص منطقة الفحص البصري `D:\app_access\phone_commander\roi_visual_zones_new.png` | **تم طمس إحداثيات المملكة ومربع الدردشة السفلي** لحماية الخصوصية وتحويلها إلى WebP (`1400x630`) |
| 9 | `phone-commander` | `zncc-vision-architecture.svg` | `architecture_diagram` | مولّد برمجيًا من `TemplateMatcher.kt` و`AUTOMATION_UPGRADE_PLAN.md` | مخطط معماري متجهي (`1200x540`) |
| 10 | `rok-vision-controller` | `anchor-screen-scaler.svg` | `architecture_diagram` | رسم تقني توضيحي لخوارزمية `ScreenScaler` من `rok_universal_controller.py` | استُبعدت صور الحساب الخام (`profile_screen.png`) لحماية خصوصية اللاعب، واستُبدلت بمخطط هندسي موسوم بوضوح |
| 11 | `remix-sole-marketplace` | `storefront-catalog.webp` | `real_screenshot` | لقطة واجهة المتجر الفعلية `.aistudio/artifacts/.../media_1793358406131_a8bb0909.png` | خالية من الأسرار؛ تعرض 506 منتجًا في 15 قسمًا بصيغة WebP (`1400x875`) |
| 12 | `remix-sole-marketplace` | `security-architecture.svg` | `architecture_diagram` | مولّد برمجيًا من `src/server/security.ts` و`catalogService.ts` | مخطط معماري متجهي (`1200x540`) |

---

## لماذا لم يتم تشغيل الخوادم الحية لالتقاط صور إضافية؟
- التزامًا بمبدأ الأمان رقم 6 («لا تشغّل سكربتات مجهولة أو تثبّت تبعيات أو تتصل بخدمات خارجية دون إذن مناسب»)، وبما أن المستودعات تحتوي بالفعل على لقطات تحقق عالية الدقة ومخرجات تشخيص بصرية حقيقية، فقد اعتمدنا الأصول الموثوقة الموجودة بعد تطهيرها من أي بيانات خاصة، وأضفنا إليها مخططات معمارية متجهية (SVG) عالية الوضوح لكل مشروع.
