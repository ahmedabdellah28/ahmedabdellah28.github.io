export const SITE_URL = 'https://ahmedabdellah28.github.io';

export interface SiteOwnerConfig {
  ownerNameAr: string;
  ownerNameEn: string;
  roleTitleAr: string;
  roleTitleEn: string;
  taglineAr: string;
  taglineEn: string;
  heroHeadingAr: string;
  heroHeadingEn: string;
  heroSubheadingAr: string;
  heroSubheadingEn: string;
  contact: {
    email: string | null;
    emailStatus: 'verified' | 'needs_owner_input';
    formEndpoint: string | null;
    whatsapp: string | null;
    github: string;
    linkedin: string | null;
    domain: string;
  };
}

export const SITE_CONFIG: SiteOwnerConfig = {
  ownerNameAr: 'أحمد عبد الله',
  ownerNameEn: 'Ahmed Abdellah',
  roleTitleAr: 'مهندس برمجيات ومعماري أنظمة ذكية وأتمتة',
  roleTitleEn: 'Software Engineer · AI & Automation Systems Architect',
  taglineAr:
    'أحوّل الأفكار المعقدة إلى تطبيقات وأنظمة ذكية قابلة للاستخدام.',
  taglineEn:
    'Turning complex problems into intelligent, usable software and automation systems.',
  heroHeadingAr:
    'أحوّل الأفكار المعقدة إلى تطبيقات وأنظمة ذكية قابلة للاستخدام.',
  heroHeadingEn:
    'Turning Complex Problems into Intelligent, Usable Software & Automation Systems.',
  heroSubheadingAr:
    'أصمّم وأبني تطبيقات ويب وموبايل، ومحركات أتمتة، وأنظمة مدعومة بالذكاء الاصطناعي والرؤية الحاسوبية — بتركيز كامل على الاعتمادية، والسرعة، والقيمة العملية الواضحة.',
  heroSubheadingEn:
    'I architect and build web & mobile applications, deterministic automation engines, and AI/computer-vision workflows designed for real-world reliability and clear business impact.',
  contact: {
    // Strictly null until owner provides a real public inbox (never expose users.noreply.github.com)
    email: null,
    emailStatus: 'needs_owner_input',
    formEndpoint: null,
    whatsapp: null,
    github: 'https://github.com/ahmedabdellah28',
    linkedin: null,
    domain: SITE_URL,
  },
};

export const UI_LABELS = {
  ar: {
    navHome: 'الرئيسية',
    navProjects: 'الأعمال',
    navExpertise: 'الخبرات',
    navAbout: 'عنّي',
    navContact: 'التواصل',
    switchLang: 'English',
    switchLangHref: '/en/',
    heroPrimaryCta: 'شاهد أعمالي',
    heroSecondaryCta: 'تعرّف على خبرتي',
    featuredSectionTitle: 'أعمال مختارة',
    featuredSectionSub:
      'ثلاثة مشاريع متنوعة توضح كيف تتحول المشكلات المعقدة في إنتاج الوسائط، والجدولة الرياضية، والتجارة الإلكترونية إلى أنظمة عملية موثوقة.',
    otherProjectsTitle: 'مشاريع وأنظمة إضافية',
    viewAllProjects: 'عرض جميع المشاريع (7)',
    readCaseStudy: 'استكشف المشروع',
    clientOverviewTab: 'نظرة عامة والقيمة العملية',
    engineeringDeepDiveTab: 'التفاصيل الهندسية والمعمارية',
    challengesTitle: 'ماذا واجهت وكيف حللته؟ (قصص هندسية موثقة)',
    evidenceTitle: 'الأدلة والنتائج الموثقة',
    architectureTitle: 'القرارات المعمارية وتدفق النظام',
    capabilitiesTitle: 'القدرات والوظائف المنفذة',
    resultsTitle: 'مخرجات وقدرات مثبتة',
    ctaProjectHeading: 'هل لديك مشروع أو تحدٍ تقني تريد مناقشته؟',
    ctaProjectBody: 'تصفح قنوات التواصل المتاحة أو جهّز ملخصًا سريعًا لمتطلباتك.',
    ctaProjectBtn: 'تواصل معي',
    statusLabels: {
      production: 'نظام مكتمل وقابل للتشغيل',
      functional: 'نواة وظيفية عاملة',
      prototype: 'نموذج أولي',
      in_progress: 'قيد التطوير',
      concept: 'تصور معماري',
      unknown: 'قيد المراجعة',
    },
    challengeTypeLabels: {
      verified_fix: 'إصلاح موثق بالدليل (Verified Fix)',
      preventive_design: 'تصميم وقائي (Preventive Design)',
      possible_risk: 'مخاطر مرصودة بالتدقيق (Forensic Audit Finding)',
      unverified_story: 'قيد المراجعة',
    },
  },
  en: {
    navHome: 'Home',
    navProjects: 'Work',
    navExpertise: 'Expertise',
    navAbout: 'About',
    navContact: 'Contact',
    switchLang: 'العربية',
    switchLangHref: '/ar/',
    heroPrimaryCta: 'View My Work',
    heroSecondaryCta: 'Explore Expertise',
    featuredSectionTitle: 'Featured Work',
    featuredSectionSub:
      'Three selected systems demonstrating how complex challenges in media production, mathematical scheduling, and e-commerce become reliable products.',
    otherProjectsTitle: 'Additional Systems & Tooling',
    viewAllProjects: 'View All Projects (7)',
    readCaseStudy: 'Explore Case Study',
    clientOverviewTab: 'Overview & Practical Value',
    engineeringDeepDiveTab: 'Technical Deep Dive & Architecture',
    challengesTitle: 'What Went Wrong & How I Solved It',
    evidenceTitle: 'Verified Evidence & Outcomes',
    architectureTitle: 'Architectural Decisions & System Flow',
    capabilitiesTitle: 'Implemented Capabilities & Workflows',
    resultsTitle: 'Verified Capabilities & Outcomes',
    ctaProjectHeading: 'Have a project or engineering challenge to discuss?',
    ctaProjectBody: 'Connect through verified channels or prepare a concise project brief.',
    ctaProjectBtn: 'Get in Touch',
    statusLabels: {
      production: 'Production-Ready System',
      functional: 'Functional Core System',
      prototype: 'Prototype',
      in_progress: 'In Progress',
      concept: 'Architecture Concept',
      unknown: 'Under Review',
    },
    challengeTypeLabels: {
      verified_fix: 'Verified Fix (Code/Git Proven)',
      preventive_design: 'Preventive Architecture Design',
      possible_risk: 'Forensic Audit Finding',
      unverified_story: 'Under Review',
    },
  },
} as const;
