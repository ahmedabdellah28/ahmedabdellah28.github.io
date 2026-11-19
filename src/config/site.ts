export interface SiteOwnerConfig {
  ownerNameAr: string;
  ownerNameEn: string;
  ownerNameConfirmed: boolean;
  brandName: string | null;
  taglineAr: string;
  taglineEn: string;
  heroHeadingAr: string;
  heroHeadingEn: string;
  heroSubheadingAr: string;
  heroSubheadingEn: string;
  contact: {
    email: string;
    formEndpoint: string | null;
    whatsapp: string | null;
    github: string;
    linkedin: string | null;
    domain: string;
  };
  stats: {
    projectsAudited: number;
    graphNodesIndexed: number;
    verifiedEvidenceClaims: number;
    coreDomains: number;
  };
}

/**
 * Owner Configuration configured for GitHub Pages (https://ahmed-abdellah.github.io)
 * - Uses zero-backend static mailto: + optional Formspree endpoint (no secret keys in client bundle).
 */
export const SITE_CONFIG: SiteOwnerConfig = {
  ownerNameAr: 'أحمد عبد الله — مهندس برمجيات ومعماري أنظمة ذكية',
  ownerNameEn: 'Ahmed Abdellah — Systems Architect & Creative AI Engineer',
  ownerNameConfirmed: true,
  brandName: null,
  taglineAr:
    'أبني تطبيقات وأنظمة أتمتة وحلولًا مدعومة بالذكاء الاصطناعي، وأحوّل المشكلات المعقدة إلى تجارب عملية واضحة.',
  taglineEn:
    'I build applications, automation engines, and AI-powered systems — turning complex engineering problems into clear, dependable products.',
  heroHeadingAr:
    'أبني تطبيقات وأنظمة أتمتة وحلولًا مدعومة بالذكاء الاصطناعي، وأحوّل المشكلات المعقدة إلى تجارب عملية واضحة.',
  heroHeadingEn:
    'Building deterministic automation, computer-vision engines, and full-stack AI systems backed by verifiable code evidence.',
  heroSubheadingAr:
    'بورتفوليو هندسي مبني مباشرةً من الفحص الجنائي للكود المصدري عبر 7 مشاريع حقيقية (أكثر من 60,000 عقدة برمجية مفهرسة) — يجمع بين وضوح القيمة لصاحب العمل وعمق البرهان التقني لمديري الهندسة.',
  heroSubheadingEn:
    'An evidence-driven engineering portfolio synthesized directly from source-code analysis across 7 systems (60,000+ AST graph nodes indexed) — bridging clear business outcomes for clients with traceable architectural proof for engineering leaders.',
  contact: {
    email: 'ahmed.abdellah@users.noreply.github.com',
    formEndpoint: null, // Optional: e.g. 'https://formspree.io/f/your_form_id' (public endpoint only, no secret keys)
    whatsapp: null,
    github: 'https://github.com/ahmedabdellah28',
    linkedin: null,
    domain: 'https://ahmedabdellah28.github.io',
  },
  stats: {
    projectsAudited: 7,
    graphNodesIndexed: 60137,
    verifiedEvidenceClaims: 24,
    coreDomains: 6,
  },
};

export const UI_LABELS = {
  ar: {
    navHome: 'الرئيسية',
    navProjects: 'المشاريع ودراسات الحالة',
    navExpertise: 'الخبرات والأدلة التقنية',
    navAbout: 'منهجية العمل',
    navContact: 'التواصل',
    switchLang: 'English',
    switchLangHref: '/en/',
    heroPrimaryCta: 'استكشف المشاريع البارزة',
    heroSecondaryCta: 'مصفوفة المهارات والأدلة',
    featuredSectionTitle: 'مشاريع مختارة بعناية — القيمة العملية والبرهان الهندسي',
    featuredSectionSub:
      'تم اختيار هذه الأنظمة الخمسة بناءً على اكتمال التنفيذ، عمق القرارات المعمارية، وتنوع المجالات بين الذكاء الاصطناعي، الاستمثال الرياضي، الرؤية الحاسوبية، والتطبيقات المتكاملة.',
    otherProjectsTitle: 'أعمال وأنظمة إضافية',
    viewAllProjects: 'تصفح جميع المشاريع (7)',
    readCaseStudy: 'دراسة الحالة والأدلة',
    clientOverviewTab: 'نظرة العميل والقيمة العملية',
    engineeringDeepDiveTab: 'التعمق الهندسي والمعمارية',
    challengesTitle: 'قصص التحديات والقرارات الهندسية الموثقة',
    evidenceTitle: 'سجل الأدلة البرمجية (Evidence Manifest)',
    architectureTitle: 'معمارية النظام وتدفق البيانات',
    capabilitiesTitle: 'القدرات والوظائف الأساسية',
    resultsTitle: 'النتائج المثبتة في المشروع',
    ctaProjectHeading: 'هل تبحث عن نظام مشابه أو حل لمشكلة معقدة؟',
    ctaProjectBody: 'ناقش معي متطلبات مشروعك وكيف يمكن تصميم حل موثوق وقابل للتوسع.',
    ctaProjectBtn: 'تواصل لمناقشة الحل',
    statusLabels: {
      production: 'إنتاجي / جاهز للتشغيل',
      functional: 'وظيفي مكتمل النواة',
      prototype: 'نموذج أولي',
      in_progress: 'قيد التطوير',
      concept: 'تصور معماري',
      unknown: 'قيد المراجعة',
    },
    challengeTypeLabels: {
      verified_fix: 'إصلاح موثق بالدليل (Verified Fix)',
      preventive_design: 'تصميم وقائي (Preventive Design)',
      possible_risk: 'خطر مرصود بالتدقيق (Forensic Risk Audit)',
      unverified_story: 'يحتاج تأكيد المالك',
    },
  },
  en: {
    navHome: 'Home',
    navProjects: 'Projects & Case Studies',
    navExpertise: 'Expertise & Proof Matrix',
    navAbout: 'Methodology & About',
    navContact: 'Contact',
    switchLang: 'العربية',
    switchLangHref: '/ar/',
    heroPrimaryCta: 'Explore Featured Case Studies',
    heroSecondaryCta: 'Skills & Evidence Matrix',
    featuredSectionTitle: 'Featured Engineering Systems — Business Value & Technical Proof',
    featuredSectionSub:
      'Selected across 7 audited codebases based on implementation completeness, architectural depth, automated verification suites, and domain diversity.',
    otherProjectsTitle: 'Additional Systems & Tooling',
    viewAllProjects: 'Browse All Projects (7)',
    readCaseStudy: 'Case Study & Evidence',
    clientOverviewTab: 'Client Overview & Business Value',
    engineeringDeepDiveTab: 'Engineering Deep Dive & Architecture',
    challengesTitle: 'Verified Engineering Challenges & Decisions',
    evidenceTitle: 'Traceable Code Evidence Manifest',
    architectureTitle: 'System Architecture & Pipeline Flow',
    capabilitiesTitle: 'Core Capabilities & Workflows',
    resultsTitle: 'Proven Engineering Outcomes',
    ctaProjectHeading: 'Need a similar system or facing a complex engineering bottleneck?',
    ctaProjectBody: 'Discuss your architecture, automation, or product requirements directly.',
    ctaProjectBtn: 'Discuss Your Solution',
    statusLabels: {
      production: 'Production-Ready',
      functional: 'Functional Core',
      prototype: 'Prototype',
      in_progress: 'In Progress',
      concept: 'Architecture Concept',
      unknown: 'Under Review',
    },
    challengeTypeLabels: {
      verified_fix: 'Verified Fix (Code/Git Proven)',
      preventive_design: 'Preventive Architecture Design',
      possible_risk: 'Forensic Risk Discovery',
      unverified_story: 'Needs Owner Confirmation',
    },
  },
} as const;
