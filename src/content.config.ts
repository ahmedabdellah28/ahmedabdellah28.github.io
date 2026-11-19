import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const bilingualText = z.object({
  ar: z.string().min(1),
  en: z.string().min(1),
});

const evidenceItemSchema = z.object({
  claimId: z.string().min(1),
  claimAr: z.string().min(1),
  claimEn: z.string().min(1),
  relationType: z.enum(['EXTRACTED', 'INFERRED']),
  evidencePath: z.string().min(1),
  lineOrSymbol: z.string().min(1),
  confidence: z.enum(['HIGH', 'MEDIUM', 'LOW']),
  visibility: z.enum(['public', 'private']),
  verificationStatus: z.enum(['verified', 'unverified']),
});

const challengeItemSchema = z.object({
  id: z.string().min(1),
  type: z.enum(['verified_fix', 'preventive_design', 'possible_risk', 'unverified_story']),
  titleAr: z.string().min(1),
  titleEn: z.string().min(1),
  problemAr: z.string().min(1),
  problemEn: z.string().min(1),
  whyImportantAr: z.string().min(1),
  whyImportantEn: z.string().min(1),
  solutionAr: z.string().min(1),
  solutionEn: z.string().min(1),
  proofRef: z.string().min(1),
  impactAr: z.string().min(1),
  impactEn: z.string().min(1),
  lessonAr: z.string().min(1),
  lessonEn: z.string().min(1),
});

const screenshotItemSchema = z.object({
  src: z.string().min(1),
  altAr: z.string().min(1),
  altEn: z.string().min(1),
  captionAr: z.string().min(1),
  captionEn: z.string().min(1),
  kind: z.enum(['real_screenshot', 'architecture_diagram', 'illustrative_demo', 'diagnostic_output']),
  width: z.number().int().positive(),
  height: z.number().int().positive(),
});

const projectsCollection = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/projects' }),
  schema: z.object({
    slug: z.string().min(1),
    titleAr: z.string().min(1),
    titleEn: z.string().min(1),
    summaryAr: z.string().min(1),
    summaryEn: z.string().min(1),
    valuePropositionAr: z.string().min(1),
    valuePropositionEn: z.string().min(1),
    humanCategoryAr: z.string().optional(),
    humanCategoryEn: z.string().optional(),
    struggleAr: z.string().optional(),
    struggleEn: z.string().optional(),
    triumphAr: z.string().optional(),
    triumphEn: z.string().optional(),
    category: z.array(
      z.enum([
        'web',
        'desktop',
        'mobile',
        'CLI',
        'API',
        'automation',
        'AI',
        'media',
        'architecture',
        'security',
        'library',
        'other',
      ])
    ).min(1),
    status: z.enum(['production', 'functional', 'prototype', 'in_progress', 'concept', 'unknown']),
    visibility: z.enum(['published', 'review', 'draft', 'private']),
    featured: z.boolean().default(false),
    featuredOrder: z.number().int().default(99),
    role: bilingualText,
    audience: bilingualText,
    problem: bilingualText,
    solution: bilingualText,
    manualVsAutomated: bilingualText,
    capabilities: z.array(bilingualText).min(1),
    architecture: z.object({
      overviewAr: z.string().min(1),
      overviewEn: z.string().min(1),
      pipelineSteps: z.array(
        z.object({
          step: z.string(),
          titleAr: z.string(),
          titleEn: z.string(),
          detailAr: z.string(),
          detailEn: z.string(),
        })
      ).min(1),
      systemBoundariesAr: z.string().min(1),
      systemBoundariesEn: z.string().min(1),
    }),
    technologies: z.array(z.string()).min(1),
    challenges: z.array(challengeItemSchema).min(1),
    evidence: z.array(evidenceItemSchema).min(1),
    screenshots: z.array(screenshotItemSchema).min(1),
    results: z.array(
      z.object({
        metric: z.string().min(1),
        labelAr: z.string().min(1),
        labelEn: z.string().min(1),
        sourceRef: z.string().min(1),
      })
    ).min(1),
    skillsProven: z.array(z.string()).min(1),
    reviewFlags: z.array(z.string()),
    graphStats: z.object({
      totalFiles: z.number().int(),
      totalMb: z.number(),
      nodes: z.number().int(),
      edges: z.number().int(),
    }),
    updatedAt: z.string().min(1),
  }),
});

export const collections = {
  projects: projectsCollection,
};
