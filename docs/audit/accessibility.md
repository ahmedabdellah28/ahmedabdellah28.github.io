# تقرير إمكانية الوصول والتوافق مع WCAG 2.2 AA (`docs/audit/accessibility.md`)

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
