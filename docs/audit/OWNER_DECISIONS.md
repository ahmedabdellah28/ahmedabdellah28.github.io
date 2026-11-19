# القرارات والبيانات التي تتطلب مدخلات المالك (`docs/audit/OWNER_DECISIONS.md`)

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
