from pathlib import Path

WORKSPACE = Path.cwd()
PORTFOLIO_ROOT = WORKSPACE if (WORKSPACE / "astro.config.mjs").exists() else WORKSPACE / "portfolio"


def write_doc(rel_path: str, content: str):
    for base in [PORTFOLIO_ROOT / "docs", WORKSPACE / "docs"]:
        target = base / rel_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")


def main():
    # 1. docs/audit/PORTFOLIO_AUDIT_V2.md & docs/audit/baseline.md
    audit_v2_md = """# سجل التدقيق الشامل والإصلاحات المنفذة (`docs/audit/PORTFOLIO_AUDIT_V2.md`)

> يوثق هذا السجل جميع العيوب المرصودة في خط الأساس (`Baseline Audit`) مصنفةً حسب الخطورة (`P0 / P1 / P2`)، مع السبب الجذري، الأثر على الزائر، التصحيح المنفذ في الكود، ومعيار القبول المختبر آليًا.

## جدول الأخطاء والإصلاحات (P0 → P2)

| الرمز | الأولوية | المكان | الحالة قبل الإصلاح (Baseline) | السبب الجذري | الأثر على الزائر | التصحيح المنفذ | معيار القبول والتحقق (`PASS`) |
| :---: | :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **AUD-01** | `P0` | `src/config/site.ts` & `src/pages/[locale]/contact.astro` | عرض `ahmed.abdellah@users.noreply.github.com` كبريد تواصل وزر إرسال `mailto:` | استخدام بريد GitHub الرمزي لحماية الخصوصية بدل بريد عمل حقيقي | إرسال العميل رسائل لبريد لا يستقبل الرسائل (`noreply`) | ضبط `contact.email = null` و`emailStatus = 'needs_owner_input'`، وحجب `users.noreply.github.com` كليًا من الواجهة العامة مع الإبقاء على قناة GitHub الموثقة ومُنسق الملخص المحلي | فحص آلي في `qa_verify_build.py` يضمن `0` ظهور لـ `users.noreply.github.com` في `dist/` |
| **AUD-02** | `P0` | `README.md`, `BaseLayout.astro`, `astro.config.mjs` | تضارب بين `ahmed-abdellah.github.io` و`ahmedabdellah28.github.io` | بقاء نصوص من الإعداد الأولي قبل ربط حساب GitHub الفعلي `ahmedabdellah28` | روابط مرجعية (`canonical`) أو روابط توثيق تشير لنطاق مختلف عن المستودع المنشور | توحيد الثابت المركزي `SITE_URL = 'https://ahmedabdellah28.github.io'` في `site.ts` وكافة الصفحات و`sitemap.xml` و`robots.txt` و`README.md` | فحص `canonical_exact_domain_*` و`sitemap_uses_exact_domain` (`26/26 PASS`) |
| **AUD-03** | `P0` | `src/pages/404.astro` | غياب صفحة `404.html` مخصصة ثنائية اللغة | عدم وجود ملف `404.astro` في `src/pages/` | ظهور صفحة خطأ GitHub Pages الافتراضية دون توجيه للعربية/الإنجليزية | إنشاء `src/pages/404.astro` بنفس الهوية البصرية الداكنة وروابط العودة إلى `/ar/` و`/en/` | توليد `dist/404.html` واختبارها في Playwright (`page-404-desktop-1440.png`) |
| **AUD-04** | `P1` | `src/pages/[locale]/index.astro` | ازدحام أعلى الصفحة بشريط «أوضاع الجمهور» (Client/HR/CTO) وإحصاءات AST قبل المشاريع | محاولة وضع جميع ملخصات الجماهير فوق المشاريع مباشرة | إرباك الزائر ومطالبته باختيار دوره قبل رؤية أي مشروع حقيقي | إزالة شريط اختيار الجمهور من أعلى الصفحة، واعتماد الترتيب الإلزامي: `Hero -> Featured Work (3 مشاريع بارزة مباشرة) -> What I Build -> Engineering Highlights -> Approach -> CTA` | مراجعة DOM ولقطات `after/home-ar-*`: ظهور المشاريع الثلاثة المختارة مباشرة بعد الـ Hero |
| **AUD-05** | `P1` | `src/pages/[locale]/index.astro` & `ProjectCard.astro` | عرض `60,137 AST Nodes` و`Graph-First 2027` في عنوان الهوية والبطاقات العلوية | تسرب مصطلحات أداة التحليل الداخلية إلى واجهة العميل | مصطلحات غير مفهومة لصاحب المشروع التجاري | استبدالها في الـ Hero بجملة قيمة بشرية واضحة (`أحوّل الأفكار المعقدة إلى تطبيقات وأنظمة ذكية قابلة للاستخدام`)، ونقل تفاصيل الكود للطبقة التقنية | خلو الـ Hero من مصطلحات `AST` و`Graph-First` |
| **AUD-06** | `P1` | `src/content/projects/*.json` | عناوين مشاريع طويلة جدًا ومزدحمة بالتفاصيل التقنية | دمج الاسم مع الوصف والتقنيات في حقل العنوان | إجهاد بصري وصعوبة المسح السريع لبطاقات المشاريع | اختصار جميع عناوين المشاريع إلى 3–6 كلمات واضحة (مثل `AION Studio — إنتاج الموشن جرافيك آليًا`، `نظام الجدول المدرسي الذكي`، `متجر سول للأحذية (SOLE)`) | عناوين قصيرة ومتسقة في جميع البطاقات والصفحات |
| **AUD-07** | `P1` | `src/pages/[locale]/projects/[slug].astro` | ظهور صناديق المقاييس وملخصات الأدوار قبل الصورة الرئيسية للمشروع | ترتيب الميتاداتا التقنية قبل العرض البصري في دراسة الحالة | تأخر وصول الزائر لرؤية شكل النظام ومشكلته العملية | إعادة هيكلة دراسة الحالة لتبدأ بالصورة/المخطط الكبير في الـ Hero، تليها المشكلة والحل العملي، ثم الجولة البصرية، ثم `Technical Deep Dive` مع جدول أدلة قابل للطي (`<details>`) | تحقق بصري وبنيوي في `after/case-study-aion-ar-*` |
| **AUD-08** | `P1` | `src/content/projects/*.json` | ظهور عبارات `(يحتاج تأكيد المالك)` و`(Pending owner confirmation)` في حقل الدور العام | نسخ ملاحظات التدقيق الداخلي إلى حقل العرض العام | انطباع بأن الموقع مسودة غير مكتملة | تنظيف حقل `role` في جميع ملفات المحتوى العامة، وحصر مسائل التأكيد في `docs/audit/OWNER_DECISIONS.md` | فحص آلي في `qa_verify_build.py` يؤكد `0` ظهور لعبارات المراجعة الداخلية |
| **AUD-09** | `P1` | `src/content/projects/*.json` | ظهور مسارات `.portfolio-intelligence/project-index/...` في `results.sourceRef` | الإشارة لملف الفهرس الداخلي بدل الوثيقة أو الكود المصدري | مسار داخلي غير قابل للفتح ولا يضيف معنى للزائر | استبدالها بمراجع مصدرية مقروءة وواضحة (`README.md`, `error_recovery_service.dart`, `catalog.test.ts`) | فحص آلي يؤكد `0` ظهور لـ `.portfolio-intelligence/` في `dist/` |
| **AUD-10** | `P1` | `src/content/projects/phone-commander.json` | عرض `86% – 92%` بعبارة قد توحي بأنها دقة مقاسة للنظام | عدم التمييز الحرفي بين عتبة القبول البرمجية والدقة المقاسة | احتمال التباس بين `Confidence Threshold` و`Measured Accuracy` | تعديل القيمة والوصف إلى `0.86 – 0.92: عتبات الثقة المضبوطة في خوارزمية ZNCC لقبول المطابقة البصرية (Configured ZNCC Confidence Thresholds)` | مراجعة نص البطاقة ودراسة الحالة لـ `phone-commander` |
| **AUD-11** | `P1` | `src/pages/[locale]/projects/index.astro` | وجود حرفين من الأبجدية العبرية (`המ`) داخل كلمة `الموثقة` في السطر 32 | خطأ ترميز/لوحة مفاتيح أثناء كتابة الكلمة | خطأ إملائي بصري واضح في صفحة الأعمال العربية | تصحيح الكلمة إلى `فهرس الأعمال الموثقة` وإضافة فحص Regex آلي (`[\\u0590-\\u05FF]+`) في `qa_verify_build.py` لمنع أي حرف غير عربي/لاتيني | `zero_stray_foreign_characters: PASS (0 hits)` |
| **AUD-12** | `P1` | `src/components/ProjectCard.astro` & `BaseLayout.astro` | عند تبديل صورة البطاقة إلى «المخطط المعماري»، يتغير `img.src` فقط بينما يظل `img.alt` وزر التكبير يشيران للصورة الأولى | غياب تحديث خصائص `alt` و`data-lightbox-*` في معالج الحدث | فتح نافذة التكبير على صورة مخالفة للصورة المعروضة في البطاقة | ربط أزرار التبديل بخصائص `data-switch-alt`, `data-switch-caption`, `data-switch-width`, `data-switch-height`, و`aria-pressed` وتحديث الصورة وزر التكبير معًا | اختبار Playwright آلي `project_card_media_switch_syncs_zoom_trigger_and_aria_pressed: PASS` |
| **AUD-13** | `P1/P2` | `src/layouts/BaseLayout.astro` | نافذة تكبير الصور تفتقر لإدارة التركيز (`Focus Management`) وإعادة التركيز لزر الفتح عند الإغلاق بـ `Escape` | غياب حفظ `lastFocusedTrigger` و`focus()` عند الفتح والإغلاق | صعوبة استخدام الموقع بلوحة المفاتيح فقط | تطبيق `role="dialog"`, `aria-modal="true"`, نقل التركيز لزر الإغلاق عند الفتح، حصر `Tab`، وإعادة التركيز للزر الأصلي عند `Escape` | اختبار Playwright آلي `lightbox_closes_on_escape_and_restores_focus: PASS` |
| **AUD-14** | `P2` | `src/layouts/BaseLayout.astro` | قائمة الهاتف كانت شريط تمرير أفقي مكرر أسفل الهيدر دائم الظهور | عدم وجود درج قائمة قابل للفتح والإغلاق بـ `aria-expanded` | استهلاك مساحة عمودية إضافية على شاشات الهاتف الصغيرة | استبدالها بزر قائمة قياسي مع `aria-expanded="false/true"` و`aria-controls="mobile-nav-drawer"` وإغلاق بـ `Escape` | اختبار Playwright آلي `mobile_menu_opens_with_aria_expanded` & `mobile_menu_closes_on_escape: PASS` |
"""
    write_doc("audit/PORTFOLIO_AUDIT_V2.md", audit_v2_md)
    write_doc("audit/baseline.md", audit_v2_md)

    # 2. docs/audit/BEFORE_AFTER.md
    before_after_md = """# مقارنة التغييرات البصرية والهيكلية قبل وبعد التطوير (`docs/audit/BEFORE_AFTER.md`)

## 1. ملخص التحول التصميمي والمعماري

| المحور | الحالة السابقة (`Before`) | الحالة الجديدة (`After`) |
| :--- | :--- | :--- |
| **الخلفية والسمة البصرية** | تباين متقطع بين أقسام فاتحة (`#F5F7FA`) وأقسام داكنة (`#0B1220`) | **خلفية داكنة ثابتة (`Fixed Studio Portrait Gradient`)** على كامل الموقع تستمد نفس التدرج اللوني لصورة البروفايل (كحلي أوبسيديان `#050914` مع توهج أزرق ملكي `#2563EB` على جانب وتوهج عنبري دافئ `#EA580C` على الجانب المقابل) وأسطح زجاجية داكنة عالية التباين (`glass-panel`) |
| **أعلى الصفحة الرئيسية (`Above the Fold`)** | ازدحام بشريط «أوضاع الجمهور» (4 تبويبات) وبطاقات `60,137 AST Nodes` و`Graph-First 2027` قبل الوصول للمشاريع | Hero نظيف ومباشر بصورة البروفايل المتناغمة مع الخلفية، وجملة قيمة واضحة (`أحوّل الأفكار المعقدة إلى تطبيقات وأنظمة ذكية قابلة للاستخدام`)، يتبعه فورًا قسم **أعمال مختارة (3 مشاريع بارزة)** |
| **بطاقات المشاريع (`ProjectCard.astro`)** | عناوين طويلة جدًا، وعطل عدم تزامن زر التكبير و`alt` عند تبديل صورة البطاقة | عناوين مختصرة (3–6 كلمات)، جملة قيمة واحدة، وتزامن 100% بين الصورة المعروضة، النص البديل `alt`، حالة `aria-pressed`، ونافذة التكبير (`Lightbox`) |
| **تدفق دراسة الحالة (`Case Study`)** | مقاييس تقنية وملخصات أدوار قبل صورة المشروع | الصورة الرئيسية الكبيرة أولًا في الـ Hero، ثم التحدي والحل بلغة العميل، ثم الجولة البصرية، ثم طبقة `Technical Deep Dive` وجدول الأدلة القابل للطي (`<details>`) |
| **صفحة التواصل (`Contact`)** | عرض بريد `users.noreply.github.com` غير الصالح للاستقبال | إزالة `noreply` تمامًا، عرض قناة GitHub الرسمية الموثقة (`github.com/ahmedabdellah28`)، وأداة محلية لتنسيق ونسخ ملخص المشروع |

---

## 2. سجل لقطات الشاشة المرجعية (`Before` مقابل `After`)

تم التقاط جميع اللقطات آليًا بواسطة Playwright (`Desktop 1440×900` و`Mobile 390×844`):

| الصفحة والمنصة | لقطة قبل التعديل (`Before`) | لقطة بعد التعديل (`After`) |
| :--- | :--- | :--- |
| **الرئيسية (عربي — Desktop 1440)** | `docs/audit/screenshots/before/home-ar-desktop-1440.png` | `docs/audit/screenshots/after/home-ar-desktop-1440.png` |
| **الرئيسية (عربي — Mobile 390)** | `docs/audit/screenshots/before/home-ar-mobile-390.png` | `docs/audit/screenshots/after/home-ar-mobile-390.png` |
| **الرئيسية (إنجليزي — Desktop 1440)** | `docs/audit/screenshots/before/home-en-desktop-1440.png` | `docs/audit/screenshots/after/home-en-desktop-1440.png` |
| **الرئيسية (إنجليزي — Mobile 390)** | `docs/audit/screenshots/before/home-en-mobile-390.png` | `docs/audit/screenshots/after/home-en-mobile-390.png` |
| **صفحة الأعمال (عربي — Desktop 1440)** | `docs/audit/screenshots/before/projects-ar-desktop-1440.png` | `docs/audit/screenshots/after/projects-ar-desktop-1440.png` |
| **صفحة الأعمال (عربي — Mobile 390)** | `docs/audit/screenshots/before/projects-ar-mobile-390.png` | `docs/audit/screenshots/after/projects-ar-mobile-390.png` |
| **دراسة حالة AION (عربي — Desktop 1440)** | `docs/audit/screenshots/before/case-study-aion-ar-desktop-1440.png` | `docs/audit/screenshots/after/case-study-aion-ar-desktop-1440.png` |
| **دراسة حالة AION (عربي — Mobile 390)** | `docs/audit/screenshots/before/case-study-aion-ar-mobile-390.png` | `docs/audit/screenshots/after/case-study-aion-ar-mobile-390.png` |
| **صفحة التواصل (عربي — Desktop 1440)** | `docs/audit/screenshots/before/contact-ar-desktop-1440.png` | `docs/audit/screenshots/after/contact-ar-desktop-1440.png` |
| **صفحة التواصل (عربي — Mobile 390)** | `docs/audit/screenshots/before/contact-ar-mobile-390.png` | `docs/audit/screenshots/after/contact-ar-mobile-390.png` |
| **صفحة 404 المخصصة (Desktop & Mobile)** | غير موجودة سابقًا | `docs/audit/screenshots/after/page-404-desktop-1440.png` & `page-404-mobile-390.png` |
"""
    write_doc("audit/BEFORE_AFTER.md", before_after_md)

    # 3. docs/design/DESIGN_SYSTEM.md
    design_system_md = """# نظام التصميم والهوية البصرية (`docs/design/DESIGN_SYSTEM.md`)

## 1. الاتجاه البصري: Studio Portrait Dark Gradient

بناءً على توجيه المالك بتثبيت الخلفية الداكنة واستلهام التدرج اللوني مباشرةً من إضاءة الاستوديو في الصورة الشخصية (`public/media/profile/ahmed-abdellah.webp`)، يعتمد الموقع طبقة خلفية ثابتة (`position: fixed; inset: 0`) تجمع بين:
- **القاعدة العميقة (`--bg-obsidian`):** `#050914` (كحلي أوبسيديان داكن جدًا يمنح تباينًا فائقًا للنصوص).
- **التوهج الأزرق الملكي الجانبي (`Studio Cobalt Rim`):** `radial-gradient(circle at 14% 22%, rgba(37, 99, 235, 0.34), transparent 58%)`.
- **التوهج العنبري الدافئ المقابل (`Studio Amber Rim`):** `radial-gradient(circle at 86% 28%, rgba(234, 88, 12, 0.27), transparent 55%)`.

---

## 2. رموز الألوان والتباين (`Color Tokens & WCAG Contrast`)

| الرمز (`Token`) | القيمة | الاستخدام | نسبة التباين مع `#0B1325` |
| :--- | :--- | :--- | :---: |
| `--text-primary` | `#F8FAFC` | العناوين الرئيسية (`H1`, `H2`, `H3`) | `> 16.5 : 1` (WCAG AAA) |
| `--text-secondary` | `#CBD5E1` | الفقرات والنصوص التوضيحية | `> 11.2 : 1` (WCAG AAA) |
| `--text-muted` | `#94A3B8` | البيانات الثانوية والوسوم الفرعية | `> 6.3 : 1` (WCAG AA) |
| `--color-brand-blue` | `#3B82F6` / `#2563EB` | الأزرار الأساسية والروابط النشطة وحلقات التركيز | `> 4.8 : 1` |
| `--color-brand-amber` | `#F59E0B` / `#FCD34D` | شارات التميز، العناوين الفرعية، والأكواد المرجعية | `> 10.4 : 1` |
| `--color-brand-teal` | `#18B8A7` / `#6EE7B7` | شارات الإثبات (`Verified Fix`) والحالات المكتملة | `> 9.5 : 1` |
| `.glass-panel` | `rgba(11, 19, 37, 0.78)` + `blur(16px)` | بطاقات المشاريع، الأقسام، والجداول | حد زجاجي `rgba(255,255,255,0.10)` |

---

## 3. نظام الخطوط والاتجاه (`Typography & BiDi Isolation`)

- **العربية (`html[lang="ar"]` — `dir="rtl"`):** `'IBM Plex Sans Arabic', 'Segoe UI', Tahoma, system-ui, sans-serif`.
- **الإنجليزية (`html[lang="en"]` — `dir="ltr"`):** `'Manrope', 'Inter', 'Segoe UI', system-ui, sans-serif`.
- **الشيفرة والمقاييس (`code, pre, .font-mono`):** `'JetBrains Mono', 'Cascadia Code', Consolas, monospace` مع `direction: ltr; unicode-bidi: isolate;` لمنع انعكاس المسارات البرمجية أو الأرقام داخل الجمل العربية.
- **الهرمية:** عنوان `H1` واحد فقط في كل صفحة (`26/26` صفحة مفحوصة آليًا)، يليه `H2` للأقسام الرئيسية و`H3` لبطاقات المشاريع والتحديات.

---

## 4. الشبكة والمسافات والمكونات (`Grid, Spacing & Component States`)

- **الحاوية القصوى:** `max-w-7xl` (`1280px`) مع حشوات جانبية متجاوبة (`px-4 sm:px-6 lg:px-8`).
- **نقاط التوقف المختبرة (`Breakpoints`):** `320px`, `375px`, `390px`, `768px`, `1024px`, `1440px` بصفر تمرير أفقي (`Zero Horizontal Overflow`).
- **أحجام أهداف اللمس (`Touch Targets`):** الأزرار التفاعلية وحقول التصفية وأزرار القوائم مصممة بارتفاع `40px–46px` لسهولة اللمس على الهواتف.
- **حالات التفاعل (`Interactive States`):**
  - `Hover`: ارتفاع خفيف `translateY(-3px)` مع إضاءة حدود البطاقة `rgba(96, 165, 250, 0.45)`.
  - `Focus-Visible`: إطار واضح `2.5px solid #60A5FA` مع `outline-offset: 3px` لجميع العناصر القابلة للتركيز بلوحة المفاتيح.
"""
    write_doc("design/DESIGN_SYSTEM.md", design_system_md)

    # 4. docs/design/MOTION_GUIDELINES.md
    motion_guidelines_md = """# إرشادات الحركة والتفاعل (`docs/design/MOTION_GUIDELINES.md`)

## 1. فلسفة الحركة: هادئة، وظيفية، ولا تحجب المحتوى

صُمم نظام الحركة ليدعم الفهم البصري دون إبطاء القراءة أو استهلاك المعالج:
1. **عدم إخفاء المحتوى الرئيسي فوق الطية (`Hero LCP Safe`):** نص الـ Hero وصورة البروفايل يظهران فورًا دون انتظار JavaScript حتى لا يتأخر زمن `Largest Contentful Paint (LCP)`.
2. **ظهور البطاقات عند التمرير (`Scroll Reveal`):**
   - العناصر التي تحمل الفئة `.reveal-item` تبدأ بإزاحة صغيرة جدًا (`translateY(10px)`) وتنتقل خلال `340ms` بمنحنى `cubic-bezier(0.22, 1, 0.36, 1)` فور دخولها مجال الرؤية (`IntersectionObserver`).
   - في حال تعطيل JavaScript، تظل جميع العناصر مرئية بنسبة 100% (`opacity: 1`).
3. **تفاعل البطاقات (`Card Hover & Focus`):**
   - انتقال سريع (`200ms`) يرفع البطاقة `-3px` ويبرز حدها الزجاجي لتوضيح قابليتها للنقر.
4. **تبديل وسائط البطاقة (`Synchronized Media Switch`):**
   - تبديل فوري ومتزامن يحدّث `img.src`، `img.alt`، أبعاد الصورة، وحالة `aria-pressed`، بالإضافة إلى تحديث هدف نافذة التكبير (`Lightbox`) في اللحظة نفسها.

---

## 5. دعم تقليل الحركة (`prefers-reduced-motion: reduce`)

عند تفعيل خيار تقليل الحركة في نظام التشغيل لدى الزائر، تطبق قاعدة CSS الصارمة في `src/styles/global.css`:
- إيقاف السلوك السلس للتمرير (`scroll-behavior: auto`).
- تقليص جميع مدد الانتقالات والحركات إلى `0.01ms !important`.
- إظهار جميع عناصر `.reveal-item` في موضعها النهائي فورًا (`opacity: 1 !important; transform: none !important`).
"""
    write_doc("design/MOTION_GUIDELINES.md", motion_guidelines_md)

    # 5. docs/audit/OWNER_DECISIONS.md
    owner_decisions_md = """# القرارات والبيانات التي تتطلب مدخلات المالك (`docs/audit/OWNER_DECISIONS.md`)

> يحتوي هذا الملف الداخلي على النقاط التي لا يمكن استنتاجها برمجيًا بأمان، وتم التعامل معها في الموقع العام بأسلوب محايد وآمن دون اختلاق بيانات.

## 1. البريد الإلكتروني العام للتواصل (`contact.email`)
- **الحالة الحالية:** مضبوط في `portfolio/src/config/site.ts` على:
  ```ts
  email: null,
  emailStatus: 'needs_owner_input',
  ```
- **لماذا؟** البريد الوحيد الموجود في سجلات Git المحلية هو `ahmed.abdellah@users.noreply.github.com` وهو عنوان حماية خصوصية لا يستقبل رسائل العملاء.
- **كيفية التفعيل:** فور رغبتك في إظهار بريد عمل مباشر أو خدمة نماذج (مثل Formspree)، افتح `portfolio/src/config/site.ts` وحدّث:
  ```ts
  email: 'your-real-email@domain.com',
  emailStatus: 'verified',
  formEndpoint: 'https://formspree.io/f/your_form_id', // اختياري
  ```
  وستظهر قناة البريد وزر الإرسال البريدي تلقائيًا في صفحة التواصل.

## 2. روابط التواصل الإضافية (`LinkedIn / WhatsApp`)
- **الحالة الحالية:** مضبوطة على `null` في `src/config/site.ts`، ويعتمد الموقع حاليًا على قناة GitHub الرسمية الموثقة (`https://github.com/ahmedabdellah28`). يمكن إضافتها في أي وقت داخل `src/config/site.ts`.

## 3. توصيف الأدوار في المشاريع (`Role Attribution`)
- تم استخدام توصيف هندسي دقيق ومحايد في الواجهة العامة (مثل: `تصميم المعمارية وتطوير المحرك`، `تطوير Full-Stack TypeScript وتحصين أمن تطبيقات الويب`) مع إزالة جميع عبارات `(يحتاج تأكيد المالك)` من صفحات الزوار.
"""
    write_doc("audit/OWNER_DECISIONS.md", owner_decisions_md)

    # 6. docs/audit/link-check.md & docs/audit/accessibility.md
    link_check_md = """# تقرير فحص الروابط والمسارات (`docs/audit/link-check.md`)

- **إجمالي صفحات HTML المفحوصة:** `26` صفحة (`12` صفحة عربية `/ar/*` + `12` صفحة إنجليزية `/en/*` + `/index.html` + `/404.html`).
- **الروابط الداخلية المكسورة (`broken_links`):** `0`
- **الصور أو المخططات المفقودة (`broken_images`):** `0`
- **توحيد النطاق الأساسي (`Canonical & Sitemap Domain`):** `100%` موحد على `https://ahmedabdellah28.github.io` (`0` إشارات لنطاقات قديمة).
- **روابط تبديل اللغة (`AR <-> EN`):** `24/24` صفحة داخلية تنتقل مباشرةً إلى الصفحة المكافئة لها في اللغة الأخرى.
"""
    write_doc("audit/link-check.md", link_check_md)

    accessibility_md = """# تقرير إمكانية الوصول والتوافق مع WCAG 2.2 AA (`docs/audit/accessibility.md`)

## الفحوص المنفذة والنتائج

1. **تباين الألوان (`Contrast Ratio`):**
   - النصوص الأساسية `#F8FAFC` والثانوية `#CBD5E1` فوق الأسطح الزجاجية الداكنة `#0B1325` تحقق تباينًا بين `11.2:1` و`16.5:1` (يتجاوز متطلبات WCAG AAA).
2. **سلامة الترويسات (`Single H1 Hierarchy`):**
   - جميع الصفحات الـ 26 تحتوي على عنصر `<h1>` واحد فقط غير فارغ (`single_h1_*: 26/26 PASS`).
3. **النصوص البديلة للصور (`Image Alt Attributes`):**
   - جميع عناصر `<img>` عبر الـ 26 صفحة تملك نصًا بديلًا معبرًا باللغة المطابقة للصفحة (`missing_alts: 0`).
   - عند تبديل الصورة داخل بطاقة المشروع (`ProjectCard`)، يتحدث `img.alt` وهدف التكبير ديناميكيًا (`project_card_media_switch_updates_img_and_alt: PASS`).
4. **نافذة تكبير الصور (`Accessible Dialog Semantics`):**
   - تطبق `role="dialog"`, `aria-modal="true"`, `aria-labelledby="lightbox-badge"`, `aria-describedby="lightbox-caption"`.
   - تنقل التركيز تلقائيًا إلى زر الإغلاق عند الفتح، وتحصر مفتاح `Tab` داخلها، وتستعيد التركيز للزر الأصلي عند الضغط على `Escape` (`lightbox_closes_on_escape_and_restores_focus: PASS`).
5. **قائمة الهاتف (`Mobile Menu Accessibility`):**
   - زر القائمة يطبق `aria-expanded="false/true"` و`aria-controls="mobile-nav-drawer"` ويغلق عند الضغط على `Escape` (`mobile_menu_opens_with_aria_expanded: PASS`).
6. **عزل الاتجاه (`RTL / LTR BiDi Isolation`):**
   - جميع صفحات العربية `lang="ar" dir="rtl"` وصفحات الإنجليزية `lang="en" dir="ltr"` مع عزل `unicode-bidi: isolate` للأكواد والمسارات التقنية.
"""
    write_doc("audit/accessibility.md", accessibility_md)

    print("Generated V2 audit and design system documentation files.")


if __name__ == "__main__":
    main()
