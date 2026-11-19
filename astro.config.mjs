import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import tailwindcss from '@tailwindcss/vite';

// Default target: GitHub Pages user domain (https://ahmed-abdellah.github.io)
// Can be overridden via PUBLIC_SITE_URL environment variable when attaching a custom domain.
const SITE_URL = process.env.PUBLIC_SITE_URL || 'https://ahmedabdellah28.github.io';
const BASE_PATH = process.env.PUBLIC_BASE_PATH || undefined;

export default defineConfig({
  site: SITE_URL,
  base: BASE_PATH,
  output: 'static',
  trailingSlash: 'ignore',
  integrations: [mdx()],
  vite: {
    plugins: [tailwindcss()],
  },
  i18n: {
    defaultLocale: 'ar',
    locales: ['ar', 'en'],
    routing: {
      prefixDefaultLocale: true,
      redirectToDefaultLocale: false,
    },
  },
});
