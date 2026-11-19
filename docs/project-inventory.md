# فهرس المشاريع البرمجية وحالة الأدلة (`docs/project-inventory.md`)

> تم إنشاء هذا الفهرس باتباع منهجية **Graph-First + Progressive Disclosure** دون تعديل أي ملف في المستودعات الأصلية (`قراءة فقط`).

## جدول الجرد الشامل للمشاريع السبعة

| # | المعرّف (`slug`) | الاسم المقترح (AR / EN) | المسار المصدري | التصنيف | حالة التنفيذ | الملفات (الحجم) | عقد Graphify (العلاقات) | الأدلة الموثقة | العرض في الموقع |
| :-: | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| 1 | `image-to-animate` | محرك AION Studio V6 للموشن جرافيك / AION Studio V6 Motion Engine | `E:\image_to_animate` | `AI`, `media`, `automation`, `CLI` | `production` | 18,242 (`6,693 MB`) | 3,233 (`8,111`) | 4 (`ITA-01..04`) | بارز #1 (`Featured`) |
| 2 | `school-timetable` | نظام الجدول المدرسي الذكي (CP-SAT) / Deterministic School Timetable | `E:\جدول_مدرسة` | `desktop`, `web`, `AI`, `automation` | `production` | 798 (`22.97 MB`) | 5,563 (`16,500`) | 4 (`SCH-01..04`) | بارز #2 (`Featured`) |
| 3 | `enaya-ai-workspace` | منظومة عناية الطبية وحوكمة التدقيق / Enaya Healthcare Monorepo & Audit | `D:\enaya_ai_audit_workspace` | `mobile`, `web`, `architecture`, `AI` | `functional` | 4,700 (`674.83 MB`) | 11,456 (`17,367`)* | 4 (`ENA-01..04`) | بارز #3 (`Featured`) |
| 4 | `phone-commander` | تطبيق Phone Commander (رؤية حاسوبية ZNCC) / Phone Commander Vision Hub | `D:\app_access\phone_commander` | `mobile`, `AI`, `automation` | `functional` | 389 (`38.49 MB`) | 1,704 (`3,056`) | 4 (`PHC-01..04`) | بارز #4 (`Featured`) |
| 5 | `remix-sole-marketplace` | منصة سول (SOLE) لتجارة الأحذية / SOLE Footwear Marketplace | `Downloads\remix-sole...zip` | `web`, `API`, `security` | `production` | 51 (`9.81 MB`) | 320 (`848`) | 3 (`SOL-01..03`) | بارز #5 (`Featured`) |
| 6 | `gmail-options-suite` | منظومة Scenarios & Browser Slots / Multi-Slot Browser Engine | `D:\gmail-options-main\gmail-options-main` | `automation`, `desktop`, `CLI`, `security` | `functional` | 272 (`2.91 MB`) | 1,757 (`4,374`) | 4 (`GML-01..04`) | منشور (`Published`) |
| 7 | `rok-vision-controller` | محرك RoK Universal Controller / Anchor-Based ADB Controller | `D:\rok` | `automation`, `CLI` | `functional` | 16 (`14.65 MB`) | 64 (`108`) | 2 (`ROK-01..02`) | منشور (`Published`) |
| 8 | `draft-internal-sandbox` | عينة اختبار عزل المسودات / Draft Exclusion Test Fixture | داخلي (`src/content/projects/`) | `other` | `prototype` | 1 (`0.01 MB`) | 1 (`0`) | 1 (`DRF-01`) | مخفي (`draft` — مستبعد من البناء) |

*(\* ملاحظة: يضم `enaya-ai-workspace` رسمًا معرفيًا أساسيًا من 11,456 عقدة، وعند دمج استخراج AST الكامل لملفات الكود في `enaya_monorepo` و`figcraft` يبلغ إجمالي العقد المدمجة 47,596 عقدة).*

---

## روابط ملفات الذاكرة والأدلة الداخلية (`.portfolio-intelligence/`)

- **الجرد العام:** `portfolio/.portfolio-intelligence/inventory.json`
- **سجلات الفهرسة:** `portfolio/.portfolio-intelligence/project-index/<slug>.json`
- **الذاكرة الهندسية الدائمة:** `portfolio/.portfolio-intelligence/project-memory/<slug>.md`
- **سجلات الأدلة (`Evidence Manifests`):** `portfolio/.portfolio-intelligence/evidence/<slug>.json`
- **سجلات التدقيق (`Project Audits`):** `portfolio/.portfolio-intelligence/audits/<slug>-audit.json`
