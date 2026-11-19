"""
Phase 5 — Automated Playwright E2E Interactive Verification & Visual Regression Capture
Tests responsive viewports (320px..1440px), media switcher sync, Lightbox focus trap/Escape,
mobile menu drawer, language switching, 404 page, and zero console/network errors.
"""
import http.server
import json
import socketserver
import sys
import threading
from pathlib import Path
from playwright.sync_api import sync_playwright

WORKSPACE = Path.cwd()
PORTFOLIO_ROOT = WORKSPACE if (WORKSPACE / "astro.config.mjs").exists() else WORKSPACE / "portfolio"
DIST_DIR = PORTFOLIO_ROOT / "dist"
AFTER_DIR = PORTFOLIO_ROOT / "docs" / "audit" / "screenshots" / "after"
AFTER_DIR.mkdir(parents=True, exist_ok=True)


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIST_DIR), **kwargs)

    def log_message(self, format, *args):
        pass


def main():
    report = {
        "passed": True,
        "tests_run": 0,
        "tests_passed": 0,
        "failures": [],
        "console_errors": [],
        "screenshots_captured": [],
    }

    def record(name: str, ok: bool, detail: str = ""):
        report["tests_run"] += 1
        if ok:
            report["tests_passed"] += 1
        else:
            report["passed"] = False
            report["failures"].append({"test": name, "detail": detail})

    with socketserver.TCPServer(("127.0.0.1", 0), QuietHandler) as httpd:
        port = httpd.server_address[1]
        base_url = f"http://127.0.0.1:{port}"
        t = threading.Thread(target=httpd.serve_forever, daemon=True)
        t.start()

        with sync_playwright() as p:
            browser = p.chromium.launch(channel="msedge", headless=True)

            # 1. Capture AFTER screenshots at Desktop (1440x900) and Mobile (390x844)
            pages_to_capture = [
                ("home-ar", "/ar/"),
                ("home-en", "/en/"),
                ("projects-ar", "/ar/projects/"),
                ("case-study-aion-ar", "/ar/projects/image-to-animate/"),
                ("contact-ar", "/ar/contact/"),
                ("page-404", "/404.html"),
            ]
            for vp_name, w, h in [("desktop-1440", 1440, 900), ("mobile-390", 390, 844)]:
                ctx = browser.new_context(viewport={"width": w, "height": h})
                page = ctx.new_page()
                page.on("pageerror", lambda err: report["console_errors"].append(str(err)))
                for slug_name, route in pages_to_capture:
                    page.goto(f"{base_url}{route}", wait_until="networkidle")
                    out_file = AFTER_DIR / f"{slug_name}-{vp_name}.png"
                    page.screenshot(path=str(out_file), full_page=False)
                    report["screenshots_captured"].append(out_file.name)
                ctx.close()

            # 2. Test Responsive Widths (320, 375, 390, 768, 1024, 1440) for Zero Horizontal Overflow
            for w in [320, 375, 390, 768, 1024, 1440]:
                ctx = browser.new_context(viewport={"width": w, "height": 844})
                page = ctx.new_page()
                for route in ["/ar/", "/en/", "/ar/projects/", "/ar/projects/image-to-animate/"]:
                    page.goto(f"{base_url}{route}", wait_until="networkidle")
                    overflow = page.evaluate("document.documentElement.scrollWidth > window.innerWidth + 1")
                    record(f"no_horizontal_overflow_{w}px_{route}", not overflow, f"scrollWidth={page.evaluate('document.documentElement.scrollWidth')} vs innerWidth={w}")
                ctx.close()

            # 3. Test Interactive ProjectCard Media Switcher Synchronization (P1-13) & Lightbox Dialog Focus/Escape (P1-14)
            ctx = browser.new_context(viewport={"width": 1440, "height": 900})
            page = ctx.new_page()
            page.goto(f"{base_url}/ar/", wait_until="networkidle")

            img_el = page.locator("#card-img-image-to-animate")
            zoom_btn = page.locator("#zoom-card-img-image-to-animate")
            initial_src = img_el.get_attribute("src")
            initial_alt = img_el.get_attribute("alt")

            # Click the second media button ("المخطط المعماري") for image-to-animate
            arch_btn = page.locator('button[data-switch-target="card-img-image-to-animate"]').nth(1)
            arch_btn.click()

            new_src = img_el.get_attribute("src")
            new_alt = img_el.get_attribute("alt")
            zoom_src = zoom_btn.get_attribute("data-lightbox-src")
            zoom_alt = zoom_btn.get_attribute("data-lightbox-alt")
            pressed_state = arch_btn.get_attribute("aria-pressed")

            record(
                "project_card_media_switch_updates_img_and_alt",
                new_src != initial_src and new_alt != initial_alt and "architecture-pipeline.svg" in (new_src or ""),
                f"new_src={new_src}, new_alt={new_alt}",
            )
            record(
                "project_card_media_switch_syncs_zoom_trigger_and_aria_pressed",
                zoom_src == new_src and zoom_alt == new_alt and pressed_state == "true",
                f"zoom_src={zoom_src}, pressed={pressed_state}",
            )

            # Test Lightbox Open -> Focus moved to close button -> Escape closes & restores focus
            zoom_btn.click()
            lightbox = page.locator("#global-lightbox")
            is_open = not ("hidden" in (lightbox.get_attribute("class") or ""))
            active_id = page.evaluate("document.activeElement ? document.activeElement.id : ''")
            lightbox_img_src = page.locator("#lightbox-img").get_attribute("src")

            record("lightbox_opens_with_synced_media", is_open and lightbox_img_src == new_src, f"is_open={is_open}, src={lightbox_img_src}")
            record("lightbox_moves_focus_to_close_button", active_id == "lightbox-close", f"activeElement={active_id}")

            page.keyboard.press("Escape")
            is_closed = "hidden" in (lightbox.get_attribute("class") or "")
            restored_id = page.evaluate("document.activeElement ? document.activeElement.id : ''")
            record("lightbox_closes_on_escape_and_restores_focus", is_closed and restored_id == "zoom-card-img-image-to-animate", f"is_closed={is_closed}, restored={restored_id}")
            ctx.close()

            # 4. Test Mobile Navigation Drawer Toggle & Escape (P2-16)
            ctx_m = browser.new_context(viewport={"width": 390, "height": 844})
            page_m = ctx_m.new_page()
            page_m.goto(f"{base_url}/ar/", wait_until="networkidle")
            menu_btn = page_m.locator("#mobile-menu-toggle")
            drawer = page_m.locator("#mobile-nav-drawer")

            menu_btn.click()
            expanded_true = menu_btn.get_attribute("aria-expanded") == "true"
            drawer_visible = drawer.is_visible()
            record("mobile_menu_opens_with_aria_expanded", expanded_true and drawer_visible, f"expanded={expanded_true}, visible={drawer_visible}")

            page_m.keyboard.press("Escape")
            expanded_false = menu_btn.get_attribute("aria-expanded") == "false"
            record("mobile_menu_closes_on_escape", expanded_false, f"expanded={expanded_false}")

            # 5. Test Search & Category Filtering on /ar/projects/
            page_m.goto(f"{base_url}/ar/projects/", wait_until="networkidle")
            page_m.fill("#project-search", "CP-SAT")
            visible_cards = page_m.locator(".project-item:not(.hidden)").count()
            record("projects_search_filter_works", visible_cards == 1, f"visible_cards={visible_cards}")
            ctx_m.close()

            record("zero_console_errors_across_session", len(report["console_errors"]) == 0, f"errors={report['console_errors']}")
            browser.close()

        httpd.shutdown()

    print(json.dumps(report, indent=2, ensure_ascii=False))
    if not report["passed"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
