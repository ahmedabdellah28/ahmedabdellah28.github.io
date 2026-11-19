# البورتفوليو الهندسي ثنائي اللغة — Graph-First Engineering Portfolio (`ahmed-abdellah.github.io`)

موقع بورتفوليو شخصي إنتاجي باللغتين العربية (`RTL`) والإنجليزية (`LTR`) مبني بتقنيات **Astro 5 (Static Site Generation - SSG) + TypeScript + Tailwind CSS 4 + Content Collections**، ومُجهّز للنشر المجاني التلقائي على **GitHub Pages** (`https://ahmed-abdellah.github.io`) دون أي اعتماد على خادم خلفي دائم (Zero Backend) أو خدمات مدفوعة.

---

## 1. النشر على GitHub Pages (`ahmed-abdellah.github.io`)

تم إعداد المشروع ليعمل كمستودع عام نظيف ومفصول تمامًا عن مجلدات المشاريع الأصلية وعن ذاكرة التحليل الداخلية (`.portfolio-intelligence/`).

### الخطوة 1: إنشاء المستودع على GitHub
1. أنشئ مستودعًا عامًا جديدًا (Public Repository) باسم:
   **`ahmed-abdellah.github.io`**
   تحت حسابك `https://github.com/ahmed-abdellah`.

### الخطوة 2: تفعيل GitHub Pages عبر GitHub Actions
1. من إعدادات المستودع على GitHub، افتح **Settings → Pages**.
2. تحت قسم **Build and deployment → Source**، اختر:
   **`GitHub Actions`** (بدلًا من Deploy from a branch).

### الخطوة 3: رفع مجلد `portfolio/` فقط إلى المستودع العام
لضمان فصل المستودع المنشور عن أي ملفات داخلية أو مشاريع خاصة، ارفع محتويات مجلد `portfolio/` مباشرةً إلى الفرع `main`:

```powershell
cd d:\بورتفيليو\portfolio

git init
git branch -M main
git add .

# تحقق قبل الرفع من عدم وجود أي ملفات داخلية أو حساسة (محمية بـ .gitignore):
git status

git commit -m "feat: initial Astro SSG portfolio release for GitHub Pages"
git remote add origin https://github.com/ahmed-abdellah/ahmed-abdellah.github.io.git
git push -u origin main
```

بمجرد الدفع (`git push`) إلى الفرع `main`، سيعمل ملف، [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) تلقائيًا باستخدام الإجراء الرسمي **`withastro/action@v3`** و**`actions/deploy-pages@v4`**، ويُنشر الموقع على:
- العربي (الافتراضي): `https://ahmed-abdellah.github.io/ar/`
- الإنجليزي: `https://ahmed-abdellah.github.io/en/`
- خريطة الموقع: `https://ahmed-abdellah.github.io/sitemap.xml`

---

## 2. ربط دومين مستقل لاحقًا (Custom Domain Setup)

الموقع مجهّز مسبقًا لربط أي دومين مخصص (مثل `ahmedabdellah.dev` أو `portfolio.yourdomain.com`) في خطوتين دون إعادة هيكلة الكود:

1. **تفعيل ملف `CNAME`:**
   - أعد تسمية الملف [`public/CNAME.example`](public/CNAME.example) إلى `public/CNAME` وضع بداخله اسم النطاق الجديد في سطر واحد:
     ```text
     portfolio.yourdomain.com
     ```
2. **تحديث عنوان الموقع الأساسي (`PUBLIC_SITE_URL`):**
   - إما بتعديل `SITE_URL` في [`astro.config.mjs`](astro.config.mjs)، أو بإضافة متغير بيئة `PUBLIC_SITE_URL=https://portfolio.yourdomain.com` في إعدادات GitHub Actions (`Settings → Secrets and variables → Actions → Variables`).
3. **إعداد سجلات DNS لدى مزود الدومين:**
   - للنطاق الجذري (`Apex Domain`): أضف سجلات `A` تشير إلى عناوين GitHub Pages الرسمية (`185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`).
   - للنطاق الفرعي (`Subdomain`): أضف سجل `CNAME` يشير إلى `ahmed-abdellah.github.io`.
   - فعّل خيار **Enforce HTTPS** من إعدادات GitHub Pages.

---

## 3. التشغيل والتطوير المحلي (Local Development)

> ملاحظة على جهاز التطوير الحالي: إذا لم يكن `node` مضافًا إلى متغير `PATH` في جلستك، أضف مسار Node المحلي أولًا:
> ```powershell
> $env:PATH = "C:\\Users\\loper\\AppData\\Local\\hermes\\tools\\node-26.7.0-win32-x64;" + $env:PATH
> ```

```powershell
cd portfolio

# 1. تثبيت الحزم
npm install

# 2. تشغيل خادم التطوير المحلي
npm run dev

# 3. بناء النسخة الثابتة (SSG) في dist/
npm run build

# 4. تشغيل جناح اختبارات الجودة والأمان وGitHub Pages (165 فحصًا آليًا)
npm run test:qa
```

---

## 4. تحديث بيانات التواصل ونموذج المراسلة بدون Backend

يعمل نموذج التواصل في [`src/pages/[locale]/contact.astro`](src/pages/%5Blocale%5D/contact.astro) بدون أي خادم خلفي:
- **الوضع الافتراضي المجاني (100% Static):** يولّد رابط `mailto:` منسقًا يفتح تطبيق البريد الإلكتروني لدى الزائر بالعنوان والملخص الكامل، مع زر نسخ فوري إلى الحافظة.
- **ربط خدمة نماذج خارجية مجانية (اختياري مثل Formspree):**
  افتح [`src/config/site.ts`](src/config/site.ts) وضع رابط النموذج العام في `formEndpoint`:
  ```ts
  contact: {
    email: 'your-real-email@domain.com',
    formEndpoint: 'https://formspree.io/f/your_public_form_id', // لا يوضع أي مفتاح سري هنا
    github: 'https://github.com/ahmed-abdellah',
    linkedin: 'https://linkedin.com/in/...',
    domain: 'https://ahmed-abdellah.github.io',
  }
  ```

---

## 5. إضافة مشروع جديد أو تحديث مشروع حالي (Graph-First Ingestion)

تتم عملية تحليل المشاريع محليًا فقط قبل الدفع إلى GitHub:

```powershell
cd portfolio
python scripts/ingest_project.py --path "D:\\path\\to\\new_project" --slug "my-new-system" --title-ar "عنوان المشروع" --title-en "Project Title"
```

1. يفحص السكربت المشروع محليًا (` قراءة فقط`) ويحفظ الفهرس في `.portfolio-intelligence/` (المستبعد بواسطة `.gitignore` فلا يُرفع أبدًا إلى GitHub).
2. ينشئ مسودة في `src/content/projects/my-new-system.json` بحالة `"visibility": "review"` ومخطط SVG معماري في `public/media/projects/my-new-system/`.
3. بعد مراجعة المحتوى وتغيير الحالة إلى `"visibility": "published"`، شغّل `npm run build && npm run test:qa` ثم ارفع التحديث إلى `main` ليُنشر تلقائيًا.

---

## 6. قواعد الأمان والأداء المطبقة في المستودع العام

- **عزل المشاريع الأصلية والأسرار:** يمنع [`.gitignore`](.gitignore) رفع `.portfolio-intelligence/`، و`graphify-out/`، وملفات `.env*`، وقواعد البيانات `*.db` / `*.sqlite`، والمفاتيح `*.key`.
- **ضغط الصور والتحميل الكسول:** جميع لقطات الشاشة مضغوطة بصيغة `WebP` عالية الكفاءة مع مخططات `SVG` متجهية خفيفة، وتستخدم جميع الصور غير المرئية فوق الطية `loading="lazy"` و`decoding="async"`.
- **حظر ملفات الفيديو الكبيرة:** يمنع [`.gitignore`](.gitignore) رفع ملفات `*.mp4` / `*.mov` / `*.zip` إلى المستودع؛ يُستعاض عنها بلوحات الفحص المرندرة (`QA Contact Sheets`) أو تضمين خارجي (YouTube / Vimeo / Cloudflare Stream) عند الحاجة.
