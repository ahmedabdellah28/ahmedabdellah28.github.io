# مسائل تحتاج مراجعة المالك والملفات الحساسة المستبعدة (`docs/review-required.md`)

## 1. أسئلة المالك التي لا تعطل التشغيل ولكن يفضل تأكيدها قبل النشر العام

1. **الاسم الشخصي العام (`OWNER_NAME_AR` / `OWNER_NAME_EN`):**
   - ظهر الاسم `Ahmed Abdellah <ahmed.abdellah@users.noreply.github.com>` في سجل Git داخل `E:\image_to_animate\.git`.
   - التزامًا بمبدأ عدم افتراض الهوية العامة دون تصريح، وُضع لقب مهني صادق في `portfolio/src/config/site.ts` (`مهندس برمجيات ومعماري أنظمة ذكية` / `Systems Architect & Creative AI Engineer`) مع علم `ownerNameConfirmed: false`. يمكن تغيير الاسم في سطر واحد داخل `src/config/site.ts`.
2. **قنوات التواصل المباشر (`CONTACT_EMAIL / WHATSAPP / GITHUB / LINKEDIN`):**
   - مضبوطة حاليًا على `null` في `src/config/site.ts` لمنع أي روابط مختلقة. تعرض صفحة التواصل أداة محلية لتحضير ونسخ ملخص المشروع (`Client-Side Project Brief Generator`) دون إيهام الزائر بإرسال نموذج وهمي.
3. **تأكيد الدور الشخصي (`Role Attribution`):**
   - في `enaya-ai-workspace` وباقي المشاريع، تم توصيف الدور التقني المستنتج من الكود مع وسم `needs_owner_confirmation` للتأكد مما إذا كان العمل فرديًا بالكامل أو ضمن فريق.

---

## 2. الملفات الحساسة المستبعدة تلقائيًا من الفهرسة ومن حزمة الموقع العامة

تم حظر واستبعاد جميع الملفات التالية من القراءة العميقة ومن مجلد البناء العام `portfolio/dist/`:

| المشروع | الملفات الحساسة المستبعدة | سبب الاستبعاد |
| :--- | :--- | :--- |
| `image-to-animate` | `.env` (1,169 بايت) | يحتوي مفاتيح البيئة (`GEMINI_API_KEY` وغيرها) |
| `school-timetable` | `school_scheduler.db` (3.78 MB)، ورمز الترخيص الظاهر في أعلى لقطة الشاشة `r4-master-table-rendered.png` | قاعدة بيانات SQLite محلية؛ وتم طمس مربع رمز الترخيص (`OWNER-VIP-2026`) برمجيًا في الصورة المنشورة |
| `enaya-ai-workspace` | `.neural_db`, `.neural_memory`, وأي ملفات `.env` داخل `sources/` | قواعد ذاكرة داخلية وبيانات بيئة |
| `gmail-options-suite` | `license.key` (263 بايت)، `resources/accounts/`, `resources/proxies.txt` | مفتاح ترخيص وملفات حسابات/بروكسيات تشغيلية |
| `phone-commander` | `.env` (618 بايت)، `phone_commander.db` (99 KB)، وإحداثيات اللاعب والدردشة في `roi_visual_zones_new.png` | مفاتيح Supabase وقاعدة بيانات محلية؛ وتم طمس إحداثيات المملكة والدردشة في صورة تشخيص الـ ROI |
| `rok-vision-controller` | لقطات شاشة الحساب الخام (`profile_screen.png`, `characters_screen.png`) | تحتوي أسماء ومعرفات حسابات داخل اللعبة؛ استُبدلت بمخطط هندسي توضيحي لخوارزمية `ScreenScaler` |
| `remix-sole-marketplace` | `.env` داخل ملف الـ ZIP | متغيرات اتصال Supabase وCloudinary الخاصة |

---

## 3. ادعاءات أو قصص لم تُنشر أو صُنفت بوضوح

- **`GML-CH-2` (في `gmail-options-suite`):** النتائج العشر الواردة في `camoufox_forensic_audit.md` صُنفت بصراحة كـ `possible_risk` (مخاطر مرصودة عبر التدقيق الجنائي) ولم تُعرض على أنها إصلاحات منفذة.
- **`draft-internal-sandbox`:** مشروع مسودة (`visibility: "draft"`) أُنشئ خصيصًا لإثبات أن نظام البناء يستبعد المسودات تلقائيًا من كافة الصفحات وملف `sitemap.xml`.
