import type { APIRoute } from "astro";
export const GET: APIRoute = ({ site }) => {
  const origin = site?.origin || "https://ahmedabdellah28.github.io";
  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>${origin}/ar/</loc></url><url><loc>${origin}/en/</loc></url></urlset>`;
  return new Response(xml, {
    headers: { "Content-Type": "application/xml; charset=utf-8" },
  });
};
