import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export const GET: APIRoute = async ({ site }) => {
  const origin = site ? site.origin : 'https://ahmed-abdellah.github.io';
  const published = await getCollection('projects', ({ data }) => data.visibility === 'published');
  const locales = ['ar', 'en'];
  const staticPages = ['', '/projects', '/expertise', '/about', '/contact'];

  const urls: string[] = [];
  for (const loc of locales) {
    for (const pg of staticPages) {
      urls.push(`${origin}/${loc}${pg}`);
    }
    for (const proj of published) {
      urls.push(`${origin}/${loc}/projects/${proj.data.slug}`);
    }
  }

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map((u) => `  <url><loc>${u}</loc></url>`).join('\n')}
</urlset>`;

  return new Response(xml, {
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
    },
  });
};
