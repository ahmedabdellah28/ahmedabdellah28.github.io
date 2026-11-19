"""
Phase I & V2 Audit — Automated Quality Assurance, Security, Accessibility & GitHub Pages Suite
Verifies all Definition of Done (§13) criteria against the built static site in portfolio/dist/.
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

WORKSPACE = Path.cwd()
PORTFOLIO_ROOT = WORKSPACE if (WORKSPACE / "astro.config.mjs").exists() else WORKSPACE / "portfolio"
DIST_DIR = PORTFOLIO_ROOT / "dist"


class PageInspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.html_lang = None
        self.html_dir = None
        self.canonical = None
        self.hreflangs = {}
        self.og_tags = {}
        self.images = []
        self.links = []
        self.headings = []
        self.has_backdrop = False
        self.has_dialog = False
        self.has_mobile_toggle = False
        self.switch_buttons = []
        self._in_h1 = False
        self._h1_text = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        cls = attr_dict.get("class", "")
        if "studio-portrait-backdrop" in cls:
            self.has_backdrop = True
        if attr_dict.get("role") == "dialog" and attr_dict.get("aria-modal") == "true":
            self.has_dialog = True
        if attr_dict.get("id") == "mobile-menu-toggle" and "aria-expanded" in attr_dict:
            self.has_mobile_toggle = True
        if "data-switch-target" in attr_dict:
            self.switch_buttons.append(attr_dict)

        if tag == "html":
            self.html_lang = attr_dict.get("lang")
            self.html_dir = attr_dict.get("dir")
        elif tag == "link":
            rel = attr_dict.get("rel", "")
            if rel == "canonical":
                self.canonical = attr_dict.get("href")
            elif rel == "alternate" and attr_dict.get("hreflang"):
                self.hreflangs[attr_dict["hreflang"]] = attr_dict.get("href")
        elif tag == "meta":
            prop = attr_dict.get("property", "")
            if prop.startswith("og:"):
                self.og_tags[prop] = attr_dict.get("content", "")
        elif tag == "img":
            self.images.append({
                "src": attr_dict.get("src", ""),
                "alt": attr_dict.get("alt", ""),
                "loading": attr_dict.get("loading", ""),
            })
        elif tag == "a":
            self.links.append(attr_dict.get("href", ""))
        elif tag == "h1":
            self._in_h1 = True
            self._h1_text = []

    def handle_endtag(self, tag):
        if tag == "h1" and self._in_h1:
            self._in_h1 = False
            self.headings.append("".join(self._h1_text).strip())

    def handle_data(self, data):
        if self._in_h1:
            self._h1_text.append(data)


SECRET_OR_FORBIDDEN_TEXT_PATTERNS = [
    r"AIzaSy[A-Za-z0-9_-]{33}",
    r"cloudinary://[0-9]+:[A-Za-z0-9_-]+@",
    r"OWNER-VIP-2026",
    r"SUPABASE_SERVICE_ROLE_KEY\s*=\s*['\"]eyJ",
    r"-----BEGIN (RSA |EC )?PRIVATE KEY-----",
    r"users\.noreply\.github\.com",
    r"ahmed-abdellah\.github\.io",
    r"\.portfolio-intelligence/",
    r"بحاجة لتأكيد",
    r"يحتاج تأكيد المالك",
    r"Pending owner confirmation",
    r"needs_owner_confirmation",
]

FORBIDDEN_EXTS = {".mp4", ".mov", ".avi", ".mkv", ".zip", ".rar", ".7z", ".db", ".sqlite", ".sqlite3", ".key", ".pem"}


def resolve_dist_link(href: str) -> bool:
    if not href or href.startswith(("#", "mailto:", "tel:", "http://", "https://")):
        return True
    clean = href.split("#")[0].split("?")[0]
    if not clean.startswith("/"):
        return True
    candidate_dir = DIST_DIR / clean.lstrip("/") / "index.html"
    candidate_file = DIST_DIR / clean.lstrip("/")
    return candidate_dir.exists() or candidate_file.exists()


def run_qa_suite() -> dict:
    results = {
        "passed": True,
        "total_checks": 0,
        "passed_checks": 0,
        "failed_checks": [],
        "metrics": {},
    }

    def check(name: str, condition: bool, detail: str = ""):
        results["total_checks"] += 1
        if condition:
            results["passed_checks"] += 1
        else:
            results["passed"] = False
            results["failed_checks"].append({"check": name, "detail": detail})

    check("dist_exists", DIST_DIR.exists(), f"{DIST_DIR} exists")

    html_files = sorted(list(DIST_DIR.rglob("*.html")))
    css_files = sorted(list(DIST_DIR.rglob("*.css")))
    check("page_count_26_html", len(html_files) == 26, f"Found {len(html_files)} HTML pages (including 404.html)")
    check("page_404_exists", (DIST_DIR / "404.html").exists(), "404.html exists")
    check("sitemap_exists", (DIST_DIR / "sitemap.xml").exists(), "sitemap.xml exists")
    check("robots_exists", (DIST_DIR / "robots.txt").exists(), "robots.txt exists")
    check("nojekyll_exists", (DIST_DIR / ".nojekyll").exists(), ".nojekyll exists in dist/")

    wf_path = PORTFOLIO_ROOT / ".github" / "workflows" / "deploy.yml"
    check("gh_pages_workflow_exists", wf_path.exists(), f"{wf_path} exists")
    if wf_path.exists():
        wf_text = wf_path.read_text(encoding="utf-8")
        check("gh_pages_uses_withastro_action", "withastro/action@v3" in wf_text, "Uses official withastro/action@v3")
        check("gh_pages_triggers_on_main", "branches: [main]" in wf_text, "Triggers on main branch")
        check("gh_pages_deploy_action", "actions/deploy-pages@v4" in wf_text, "Uses actions/deploy-pages@v4")

    sitemap_text = (DIST_DIR / "sitemap.xml").read_text(encoding="utf-8") if (DIST_DIR / "sitemap.xml").exists() else ""
    check(
        "sitemap_uses_exact_domain",
        "https://ahmedabdellah28.github.io/ar" in sitemap_text
        and "https://ahmedabdellah28.github.io/en" in sitemap_text
        and "ahmed-abdellah.github.io" not in sitemap_text,
        "sitemap.xml strictly uses https://ahmedabdellah28.github.io",
    )

    check(
        "no_draft_project_route",
        not (DIST_DIR / "ar" / "projects" / "draft-internal-sandbox").exists()
        and not (DIST_DIR / "en" / "projects" / "draft-internal-sandbox").exists(),
        "draft-internal-sandbox must not be generated in dist/",
    )
    check(
        "no_portfolio_intelligence_in_dist",
        not (DIST_DIR / ".portfolio-intelligence").exists(),
        ".portfolio-intelligence must not be copied to dist/",
    )

    forbidden_files = [
        f.relative_to(DIST_DIR).as_posix()
        for f in DIST_DIR.rglob("*")
        if f.is_file() and (f.suffix.lower() in FORBIDDEN_EXTS or f.name.startswith(".env"))
    ]
    check("zero_forbidden_binaries_or_videos_in_dist", len(forbidden_files) == 0, f"Forbidden files: {forbidden_files}")

    broken_images = []
    missing_alts = []
    broken_links = []
    forbidden_text_hits = []
    stray_char_hits = []
    draft_mentions = []
    unsynced_switch_btns = []

    for hf in html_files:
        rel = hf.relative_to(DIST_DIR).as_posix()
        content = hf.read_text(encoding="utf-8")

        if "draft-internal-sandbox" in content:
            draft_mentions.append(rel)

        for pat in SECRET_OR_FORBIDDEN_TEXT_PATTERNS:
            if re.search(pat, content):
                forbidden_text_hits.append((rel, pat))

        if re.search(r"[\u0590-\u05FF]+", content):
            stray_char_hits.append(rel)

        parser = PageInspector()
        parser.feed(content)

        check(f"studio_backdrop_{rel}", parser.has_backdrop, f"studio-portrait-backdrop present in {rel}")
        check(
            f"canonical_exact_domain_{rel}",
            bool(parser.canonical and parser.canonical.startswith("https://ahmedabdellah28.github.io/")),
            f"Canonical={parser.canonical}",
        )
        check(
            f"hreflang_bilingual_{rel}",
            "ar" in parser.hreflangs and "en" in parser.hreflangs,
            f"hreflangs={list(parser.hreflangs.keys())}",
        )
        check(
            f"og_tags_{rel}",
            bool(parser.og_tags.get("og:title") and parser.og_tags.get("og:description")),
            f"og_tags={list(parser.og_tags.keys())}",
        )
        check(f"single_h1_{rel}", len(parser.headings) == 1 and bool(parser.headings[0]), f"H1 count={len(parser.headings)}")

        if rel.startswith("ar/") or rel.startswith("en/"):
            check(f"accessible_dialog_and_menu_{rel}", parser.has_dialog and parser.has_mobile_toggle, f"dialog={parser.has_dialog}, menu={parser.has_mobile_toggle}")

        for sb in parser.switch_buttons:
            if not (sb.get("data-switch-alt") and sb.get("data-switch-caption") and "aria-pressed" in sb):
                unsynced_switch_btns.append(rel)

        if rel.startswith("ar/"):
            check(f"lang_dir_{rel}", parser.html_lang == "ar" and parser.html_dir == "rtl", f"lang={parser.html_lang}, dir={parser.html_dir}")
            expected_en = "/en/" + rel[len("ar/"):].replace("index.html", "")
            has_switch = any(l.rstrip("/") == expected_en.rstrip("/") for l in parser.links)
            check(f"i18n_switch_{rel}", has_switch, f"Expected switch link to {expected_en}")
        elif rel.startswith("en/"):
            check(f"lang_dir_{rel}", parser.html_lang == "en" and parser.html_dir == "ltr", f"lang={parser.html_lang}, dir={parser.html_dir}")
            expected_ar = "/ar/" + rel[len("en/"):].replace("index.html", "")
            has_switch = any(l.rstrip("/") == expected_ar.rstrip("/") for l in parser.links)
            check(f"i18n_switch_{rel}", has_switch, f"Expected switch link to {expected_ar}")

        for img in parser.images:
            src = img["src"]
            if not img["alt"].strip():
                missing_alts.append((rel, src))
            img_file = DIST_DIR / src.lstrip("/")
            if not img_file.exists() or img_file.stat().st_size == 0:
                broken_images.append((rel, src))

        for lnk in parser.links:
            if not resolve_dist_link(lnk):
                broken_links.append((rel, lnk))

    check("zero_draft_mentions_in_html", len(draft_mentions) == 0, f"Draft mentions: {draft_mentions}")
    check("zero_broken_images", len(broken_images) == 0, f"Broken images: {broken_images}")
    check("zero_missing_image_alts", len(missing_alts) == 0, f"Missing alts: {missing_alts}")
    check("zero_broken_internal_links", len(broken_links) == 0, f"Broken links: {broken_links}")
    check("zero_forbidden_or_internal_text_leaks", len(forbidden_text_hits) == 0, f"Forbidden text hits: {forbidden_text_hits}")
    check("zero_stray_foreign_characters", len(stray_char_hits) == 0, f"Stray char hits: {stray_char_hits}")
    check("synchronized_project_card_media_buttons", len(unsynced_switch_btns) == 0, f"Unsynced buttons: {unsynced_switch_btns}")

    all_css = "\n".join(cf.read_text(encoding="utf-8") for cf in css_files)
    check("css_prefers_reduced_motion", "prefers-reduced-motion" in all_css, "prefers-reduced-motion present in CSS")
    check("css_focus_visible", "focus-visible" in all_css, "focus-visible present in CSS")
    check("css_studio_portrait_backdrop", "studio-portrait-backdrop" in all_css, "studio-portrait-backdrop present in CSS")

    results["metrics"] = {
        "target_domain": "https://ahmedabdellah28.github.io",
        "html_pages_verified": len(html_files),
        "css_bundles_verified": len(css_files),
        "broken_images": len(broken_images),
        "missing_alts": len(missing_alts),
        "broken_links": len(broken_links),
        "forbidden_or_internal_text_leaks": len(forbidden_text_hits),
        "stray_foreign_chars": len(stray_char_hits),
        "draft_leaks": len(draft_mentions),
        "forbidden_binaries_or_videos": len(forbidden_files),
    }
    return results


if __name__ == "__main__":
    res = run_qa_suite()
    print(json.dumps(res, indent=2, ensure_ascii=False))
    if not res["passed"]:
        sys.exit(1)
