# نظام التصميم والهوية البصرية (`docs/design/DESIGN_SYSTEM.md`)

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
