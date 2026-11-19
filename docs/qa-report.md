# تقرير اختبارات الجودة والأمان وجاهزية GitHub Pages (`docs/qa-report.md`)

## 1. ملخص التنفيذ الفعلي للاختبارات

تم بناء الموقع فعليًا عبر `astro build` (SSG) لنطاق `https://ahmed-abdellah.github.io` وتشغيل حزمة الاختبارات الآلية [`portfolio/scripts/qa_verify_build.py`](../scripts/qa_verify_build.py) على مخرجات البناء في `portfolio/dist/`:

- **حالة البناء (`npm run build`):** `PASS` — تم بناء 25 صفحة HTML ثابتة + `sitemap.xml` + `robots.txt` + `.nojekyll` في `1.85s` بصفر أخطاء TypeScript أو Vite.
- **حالة اختبارات التحقق الآلية (`qa_verify_build.py`):** `PASS` — **168 / 168 فحصًا ناجحًا (0 أخطاء)**.

---

## 2. مصفوفة الفحوص المنفذة ونتائجها

| فئة الاختبار | الفحص المنفذ | النتيجة الفعلية | التفاصيل |
| :--- | :--- | :---: | :--- |
| **البناء والمسارات (SSG)** | توليد جميع الصفحات الثنائية اللغة (`/ar/*` و`/en/*`) | `PASS` | 25 صفحة HTML مبنية في `dist/` + `sitemap.xml` + `.nojekyll` |
| **GitHub Actions Workflow** | التحقق من `.github/workflows/deploy.yml` | `PASS` | يستخدم `withastro/action@v3` و`actions/deploy-pages@v4` عند الدفع إلى `main` |
| **النطاق وSEO وOpen Graph** | التحقق من `canonical`، `hreflang="ar"/"en"`، ووسوم `og:*` في كل صفحة | `PASS (25/25)` | جميع الروابط المرجعية و`sitemap.xml` تشير إلى `https://ahmed-abdellah.github.io` |
| **ثنائية اللغة والاتجاه** | التحقق من `lang="ar" dir="rtl"` و`lang="en" dir="ltr"` في كل صفحة | `PASS (24/24)` | جميع صفحات العربية `rtl` وجميع صفحات الإنجليزية `ltr` |
| **تبديل اللغة في الصفحات الداخلية** | التحقق من أن زر تبديل اللغة في كل صفحة داخلية ينقل للصفحة المكافئة (`/ar/projects/X` ↔ `/en/projects/X`) | `PASS (24/24)` | تطابق 100% لمسارات التبديل ثنائية الاتجاه |
| **عزل المسودات (`Draft Exclusion`)** | التأكد من عدم ظهور المشروع التجريبي `draft-internal-sandbox` (`visibility="draft"`) في أي صفحة أو رابط | `PASS` | `draft_leaks: 0` — لم يُبنَ له مسار ولم يظهر في القوائم |
| **عزل الذاكرة والمشاريع الأصلية** | التأكد من عدم تسرب `.portfolio-intelligence/` أو أي فيديوهات أو أرشيفات أو قواعد بيانات إلى `dist/` | `PASS` | `forbidden_binaries_or_videos: 0` |
| **سلامة الصور والنصوص البديلة** | فحص وجود كل ملف صورة `<img src="...">` (WebP/SVG) وحجمه `> 0` ووجود نص بديل `alt` | `PASS` | `broken_images: 0`, `missing_alts: 0` عبر جميع الـ 25 صفحة |
| **سلامة الروابط الداخلية** | فحص جميع روابط `<a href="/...">` والتأكد من وصولها لملفات فعلية في `dist/` | `PASS` | `broken_links: 0` |
| **فحص تسرب الأسرار (`Secret Scan`)** | مسح جميع ملفات `dist/` بحثًا عن مفاتيح API، روابط Cloudinary السرية، أو رمز `OWNER-VIP-2026` | `PASS` | `secret_leaks: 0` |
| **إمكانية الوصول والحركة** | التحقق من وجود قواعد `@media (prefers-reduced-motion: reduce)` و`:focus-visible` في CSS النهائي | `PASS` | مضمنة ومفعلة في حزمة CSS |
| **اختبار محرك الاستيراد والتحديث** | تشغيل `python scripts/ingest_project.py --path "D:\rok" --slug "rok-vision-controller"` | `PASS` | اكتشف تطابق البصمة (`d649d567236d4605`) وتخطى إعادة الفهرسة فورًا |

---

## 3. حالات الحافة المختبرة (`Edge Cases Verified`)

1. **مشروع بلا واجهة رسومية (`CLI / Automation`):** تم اختباره في `gmail-options-suite` و`rok-vision-controller` عبر عرض مخططات معمارية واضحة موسومة بـ `Architecture & Workflow Diagram` دون اختلاق شاشات وهمية.
2. **مشروع داخل أرشيف مضغوط (`.zip`):** تم استخراج `remix-sole-marketplace` في مساحة Staging معزولة للقراءة فقط وفهرسته دون المساس بالملف الأصلي.
3. **مشروع بأسماء مجلدات وملفات عربية:** تم اختباره في `E:\جدول_مدرسة` وفي مسار مساحة العمل `d:\بورتفيليو` مع ضبط ترميز UTF-8.
4. **مشروع متعدد التطبيقات (Monorepo):** تم اختباره في `D:\enaya_ai_audit_workspace` (`enaya_monorepo` + `figcraft` + `00_governance..08_lifecycle`).
