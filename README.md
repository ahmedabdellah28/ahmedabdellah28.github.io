# بورتفوليو أحمد عبد الله الهندسي — Ahmed Abdellah Engineering Portfolio (`ahmedabdellah28.github.io`)

موقع بورتفوليو شخصي إنتاجي باللغتين العربية (`RTL`) والإنجليزية (`LTR`) مبني بتقنيات **Astro 5 (Static Site Generation - SSG) + TypeScript + Tailwind CSS 4 + Content Collections**، ومُجهّز للنشر المجاني على **GitHub Pages** (`https://ahmedabdellah28.github.io`).

---

## 1. الروابط الرسمية

- **الموقع العام (العربية — RTL):** `https://ahmedabdellah28.github.io/ar/`
- **النسخة الإنجليزية (English — LTR):** `https://ahmedabdellah28.github.io/en/`
- **خريطة الموقع (`Sitemap`):** `https://ahmedabdellah28.github.io/sitemap.xml`
- **مستودع GitHub:** `https://github.com/ahmedabdellah28/ahmedabdellah28.github.io`

---

## 2. التشغيل والاختبار المحلي (Local Development & QA)

> على جهاز التطوير الحالي، إذا لم يكن `node` في متغير `PATH` للجلسة، أضفه أولًا:
> ```powershell
> $env:PATH = "C:\\Users\\loper\\AppData\\Local\\hermes\\tools\\node-26.7.0-win32-x64;" + $env:PATH
> ```

```powershell
cd d:\بورتفيليو\portfolio

# 1. تثبيت الحزم
npm install

# 2. تشغيل خادم التطوير المحلي
npm run dev

# 3. بناء النسخة الإنتاجية الثابتة في dist/
npm run build

# 4. تشغيل فحوص البناء والأمان وSEO (226 فحصًا آليًا)
python scripts/qa_verify_build.py

# 5. تشغيل اختبارات المتصفح التفاعلية عبر Playwright والتقاط صور المقارنة (33 اختبارًا)
python scripts/playwright_e2e_audit.py
```

---

## 3. تعديل بيانات التواصل والهوية (`src/config/site.ts`)

تُدار جميع إعدادات الهوية والنطاق الأساسي (`SITE_URL = 'https://ahmedabdellah28.github.io'`) وقنوات التواصل من ملف واحد فقط: [`src/config/site.ts`](src/config/site.ts).

لتفعيل بريد عمل مباشر أو خدمة نماذج خارجية (مثل Formspree) في صفحة التواصل:
```ts
contact: {
  email: 'your-real-email@domain.com',
  emailStatus: 'verified',
  formEndpoint: 'https://formspree.io/f/your_public_form_id', // اختياري بدون أي مفتاح سري
  github: 'https://github.com/ahmedabdellah28',
  linkedin: 'https://linkedin.com/in/...',
  domain: SITE_URL,
}
```

---

## 4. الوثائق الهندسية وتقارير التدقيق (`docs/`)

- [`docs/audit/PORTFOLIO_AUDIT_V2.md`](docs/audit/PORTFOLIO_AUDIT_V2.md) — جدول أخطاء `P0/P1/P2` وحالة إصلاحها والتحقق منها.
- [`docs/audit/BEFORE_AFTER.md`](docs/audit/BEFORE_AFTER.md) — مقارنة التغييرات البصرية والهيكلية وروابط صور `before/` و`after/`.
- [`docs/design/DESIGN_SYSTEM.md`](docs/design/DESIGN_SYSTEM.md) — نظام التصميم، الخلفية الداكنة الثابتة المستوحاة من جرادينت صورة البروفايل، التباين، والخطوط.
- [`docs/design/MOTION_GUIDELINES.md`](docs/design/MOTION_GUIDELINES.md) — نظام الحركة الهادئة ودعم `prefers-reduced-motion`.
- [`docs/audit/QA_REPORT.md`](docs/audit/QA_REPORT.md) — نتائج اختبارات البناء (`226/226`) وPlaywright (`33/33`).
- [`docs/audit/OWNER_DECISIONS.md`](docs/audit/OWNER_DECISIONS.md) — البيانات الاختيارية التي تنتظر مدخلات المالك (مثل البريد العام).

---

## 5. النشر على GitHub Pages

يعمل ملف [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) باستخدام الإجراء الرسمي `withastro/action@v3` و`actions/deploy-pages@v4` عند الدفع إلى الفرع `main`:

```powershell
cd d:\بورتفيليو\portfolio
git add .
git commit -m "feat: redesign portfolio with fixed portrait dark gradient and V2 audit fixes"
git push origin main
```
