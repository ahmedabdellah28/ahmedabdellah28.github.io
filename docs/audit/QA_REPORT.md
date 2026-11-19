# تقرير اختبارات الجودة والأمان والتحقق التفاعلي (`docs/audit/QA_REPORT.md`)

## 1. ملخص النتائج الحقيقية المنفذة

تم تنفيذ مستويين من الاختبارات الآلية الفعلية على النسخة المبنية في `portfolio/dist/`:

1. **اختبارات البناء، الروابط، الأمان، وSEO (`python scripts/qa_verify_build.py`):**
   - **النتيجة:** **`226 / 226 PASS` (0 أخطاء)**.
   - **الصفحات المبنية:** `26` صفحة HTML ثابتة (شاملة `404.html`) + `sitemap.xml` + `robots.txt` + `.nojekyll`.
2. **اختبارات المتصفح الحقيقي التفاعلية ولقطات الشاشة (`python scripts/playwright_e2e_audit.py` عبر `Chromium / Edge Headless`):**
   - **النتيجة:** **`33 / 33 PASS` (0 أخطاء، و0 أخطاء في Console المتصفح)**.
   - **المقاسات المختبرة لعدم وجود تمرير أفقي (`Zero Horizontal Overflow`):** `320px`, `375px`, `390px`, `768px`, `1024px`, `1440px` عبر العربية (`RTL`) والإنجليزية (`LTR`).

---

## 2. مصفوفة الاختبارات التفصيلية

| فئة الاختبار | أداة التنفيذ | الفحص المنفذ | النتيجة |
| :--- | :--- | :--- | :---: |
| **البناء الثابت (Astro SSG)** | `npm run build` | ترجمة جميع مسارات `/ar/*`, `/en/*`, `/404.html`, `/sitemap.xml` | `PASS (1.9s)` |
| **توحيد النطاق (`SITE_URL`)** | `qa_verify_build.py` | التأكد من أن جميع روابط `canonical`, `og:url`, و`sitemap.xml` تشير حصريًا إلى `https://ahmedabdellah28.github.io` وعدم بقاء `ahmed-abdellah.github.io` | `PASS (26/26)` |
| **حجب بريد `noreply` والمسارات الداخلية** | `qa_verify_build.py` | التأكد من عدم ظهور `users.noreply.github.com` أو `.portfolio-intelligence/` أو عبارات `(يحتاج تأكيد المالك)` في أي صفحة عامة | `PASS (0 leaks)` |
| **تدقيق النص العربي (`Unicode Audit`)** | `qa_verify_build.py` | فحص خلو جميع الصفحات من أي أحرف غير عربية/لاتينية دخيلة (`[\\u0590-\\u05FF]+`) | `PASS (0 hits)` |
| **هيكل العناوين (`Single H1`)** | `qa_verify_build.py` | التحقق من وجود `<h1>` واحد فقط غير فارغ في كل صفحة | `PASS (26/26)` |
| **سلامة الصور والروابط** | `qa_verify_build.py` | التحقق من وجود كافة ملفات الصور (`WebP/SVG`)، نصوص `alt`، وصحة كافة الروابط الداخلية | `PASS (0 broken)` |
| **تزامن وسائط بطاقة المشروع** | `playwright_e2e_audit.py` | النقر على زر «المخطط المعماري» في البطاقة والتحقق من تحديث `img.src`، `img.alt`، `aria-pressed="true"`، وهدف زر التكبير `data-lightbox-src` معًا | `PASS` |
| **نافذة التكبير وإدارة التركيز (`Dialog Focus`)** | `playwright_e2e_audit.py` | فتح نافذة التكبير، التحقق من انتقال التركيز إلى `#lightbox-close`، ثم الضغط على `Escape` والتحقق من إغلاق النافذة وعودة التركيز لزر الفتح الأصلي | `PASS` |
| **قائمة الهاتف (`Mobile Menu Drawer`)** | `playwright_e2e_audit.py` | فتح القائمة عند عرض `390px`، التحقق من `aria-expanded="true"` وظهور القائمة، ثم إغلاقها بـ `Escape` | `PASS` |
| **البحث والتصفية الفورية** | `playwright_e2e_audit.py` | إدخال `CP-SAT` في حقل البحث بصفحة `/ar/projects/` والتحقق من تصفية البطاقات بدقة | `PASS` |
| **التجاوب وعدم وجود تمرير أفقي** | `playwright_e2e_audit.py` | قياس `scrollWidth <= innerWidth` عند `320px, 375px, 390px, 768px, 1024px, 1440px` | `PASS (24/24)` |

---

## 3. ملاحظة حول قياسات الأداء (`Performance & Core Web Vitals`)

- جميع صفحات الموقع مبنية كملفات HTML ثابتة (`Astro Static Output`) بدون أطر عمل ثقيلة في المتصفح (Zero React/Vue client hydration)، مع حزمة CSS موحدة (`~34 KB`) وصور `WebP` مضغوطة ومخططات `SVG` متجهية، وصورة Hero محملة بـ `loading="eager" fetchpriority="high"` لسرعة `LCP`، مع `loading="lazy"` لصور أسفل الطية.
- التزامًا بقاعدة عدم ادعاء أرقام Lighthouse معملية أو ميدانية غير مقاسة، نوثق هنا نتائج فحوص البناء وPlaywright الفعلية المنفذة أعلاه (`226/226` + `33/33`).
