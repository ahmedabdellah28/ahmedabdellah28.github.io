# Ahmed Abdellah | Single-scroll portfolio

بورتفوليو احمد عبداللاه بصفحة واحدة قابلة للتمرير لكل لغة، مبني بـ Astro مع محتوى عربي RTL وإنجليزي LTR.

## العرض

- `/ar/`: الصفحة العربية.
- `/en/`: الصفحة الإنجليزية.
- الرئيسية، الأعمال، الخبرات، عنّي، والتواصل أقسام داخل نفس الصفحة.
- تفاصيل المشاريع والصور والمراجع تفتح داخل الصفحة بعناصر `details` الأصلية، وتعمل دون JavaScript.
- روابط الصفحات السابقة تتحول تلقائيًا إلى القسم أو المشروع الموافق. لا توجد صفحات محتوى منفصلة في تجربة التنقل الجديدة.
- `/sitemap.xml` يحتوي على نسختي اللغة فقط. ملفات المسارات القديمة موجودة لحماية الروابط السابقة، وليست صفحات محتوى إضافية.

## التشغيل والفحص

```sh
npm ci
npm run dev
npm run build
npm run test:qa
npm run preview
```

فحص Python يتحقق من بنية النسختين، الروابط الداخلية، الصور المحلية، مسارات التحويل، واستبعاد المشاريع غير المنشورة. لا يدعي قياس سرعة التحميل أو مراجعة بصرية أو اختبار كل الروابط الخارجية. يلزم فحص المتصفح بعد أي تعديل بصري، وعلى الموبايل أيضًا.

## تعديل المحتوى

- `src/pages/[locale]/index.astro`: تصميم الصفحة والنصوص العامة والقائمة.
- `src/content/projects/*.json`: بيانات المشاريع الأصلية، الصور، النتائج، القرارات، والمراجع. يعرض الموقع فقط `visibility: published`، والمراجع ذات `visibility: public`.
- `src/config/site.ts`: الهوية وقنوات التواصل. لا تضف بريدًا أو هاتفًا تخمينيًا. النسخة الحالية تعرض رابط GitHub الموجود فقط، ولا تعرض فورم لا يستقبل الرسائل.
- `public/media/`: الصور الأصلية.
- `src/pages/[locale]/about.astro` والملفات المشابهة: تحويلات الروابط القديمة إلى أقسام الصفحة.

أسماء المشاريع والأرقام والمراجع محفوظة من المصدر الأصلي. المراجع الداخلية ليست روابط إلى مستودعات عامة بالضرورة، ولا تعني إجراء تدقيق مستقل جديد.

## GitHub Pages

سير النشر الموجود في `.github/workflows/deploy.yml` يبني المشروع عند تحديث فرع `main` أو التشغيل اليدوي. يجب أن تكون إعدادات Pages في المستودع متوافقة مع مصدر GitHub Actions. نجاح البناء المحلي لا يثبت نجاح النشر. تحقق من نتيجة التشغيل ومن الصفحة المنشورة بعد الرفع. لا تغيّر خصوصية المستودع لحل مشكلة نشر دون قرار صاحبه.

## Dependency maintenance

The existing dependency lock is unchanged by the single-page redesign. A November 21, 2026 `npm audit` reported six affected package groups, including Astro and Sharp. A separate, tested framework upgrade is recommended. The critical Astro image advisory requires processing an untrusted AVIF image: https://github.com/advisories/GHSA-26w7-cxv4-gfx2 . This portfolio currently emits static HTML and references local media with ordinary image tags; it does not provide a visitor image-upload or runtime image-processing endpoint. That limits the observed exposure for this deployment, but does not clear the dependency findings or replace a security review. Reassess before introducing uploads, SSR, untrusted CMS content, or image optimization.
