#!/usr/bin/env python3
"""
Builds a self-contained version of the TrueHealthic landing page.
Downloads all external CSS, images, and fonts, then inlines/localizes them.
"""

import os
import re
import hashlib
import urllib.request
import urllib.error
import ssl
from pathlib import Path

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"
CSS_DIR = ASSETS_DIR / "css"
IMG_DIR = ASSETS_DIR / "img"
FONT_DIR = ASSETS_DIR / "fonts"
JS_DIR = ASSETS_DIR / "js"
INPUT_FILE = BASE_DIR / "source.html"
OUTPUT_FILE = BASE_DIR / "index.html"

ORIGIN = "https://truehealthic.com"

for d in [CSS_DIR, IMG_DIR, FONT_DIR, JS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

downloaded_cache = {}

def resolve_url(url):
    clean = url.strip()
    if clean.startswith("//"):
        clean = "https:" + clean
    elif clean.startswith("/"):
        clean = ORIGIN + clean
    return clean if clean.startswith("http") else None

def download_file(url, dest_dir, prefix=""):
    if url in downloaded_cache:
        return downloaded_cache[url]
    try:
        clean_url = resolve_url(url)
        if not clean_url:
            return None

        ext = ""
        url_path = clean_url.split("?")[0]
        if "." in url_path.split("/")[-1]:
            ext = "." + url_path.split("/")[-1].split(".")[-1]
            if len(ext) > 6:
                ext = ""

        url_hash = hashlib.md5(clean_url.encode()).hexdigest()[:12]
        filename = f"{prefix}{url_hash}{ext}"
        dest_path = dest_dir / filename

        if dest_path.exists():
            rel = os.path.relpath(dest_path, BASE_DIR)
            downloaded_cache[url] = rel
            return rel

        req = urllib.request.Request(clean_url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as response:
            data = response.read()
            dest_path.write_bytes(data)
            rel = os.path.relpath(dest_path, BASE_DIR)
            downloaded_cache[url] = rel
            print(f"  ✓ {rel} ({len(data):,}b)")
            return rel
    except Exception as e:
        print(f"  ✗ {url[:80]}... ({e})")
        return None

def process_css_urls(css_content, css_url_base):
    def replace_css_url(match):
        url = match.group(1).strip("'\"")
        if url.startswith("data:"):
            return match.group(0)
        if url.startswith("//"):
            full_url = "https:" + url
        elif url.startswith("/"):
            full_url = ORIGIN + url
        elif url.startswith("http"):
            full_url = url
        elif css_url_base:
            full_url = css_url_base.rsplit("/", 1)[0] + "/" + url
        else:
            return match.group(0)

        lower = full_url.lower()
        if any(ext in lower for ext in ['.woff', '.woff2', '.ttf', '.eot', '.otf']):
            local = download_file(full_url, FONT_DIR, "font_")
        else:
            local = download_file(full_url, IMG_DIR, "css_")

        if local:
            rel_from_css = local.replace("assets/", "")
            return "url('../" + rel_from_css + "')" if "assets/" in local else "url('" + local + "')"
        return match.group(0)

    return re.sub(r'url\(([^)]+)\)', replace_css_url, css_content)

def download_and_inline_css(html):
    print("\n📦 Processing CSS...")
    def replace_link(match):
        tag = match.group(0)
        href_match = re.search(r'href=["\']([^"\']+)["\']', tag)
        if not href_match:
            return tag
        href = href_match.group(1)
        if 'stylesheet' not in tag and '.css' not in href:
            return tag

        url = resolve_url(href)
        if not url:
            return tag

        # Skip checkout/prefetch CSS
        if any(skip in url for skip in ['checkout-web', 'prefetch', 'preload']):
            return ''

        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, context=ctx, timeout=15) as response:
                css_content = response.read().decode('utf-8', errors='replace')
            css_content = process_css_urls(css_content, url)
            print(f"  ✓ Inlined CSS: {url[:80]}...")
            return f"<style>/* {url[:60]} */\n{css_content}</style>"
        except Exception as e:
            print(f"  ✗ CSS: {url[:80]}... ({e})")
            return tag

    html = re.sub(r'<link[^>]*(?:rel=["\']stylesheet["\']|\.css)[^>]*/?>', replace_link, html, flags=re.IGNORECASE)
    return html

def download_images(html):
    print("\n🖼️  Processing images...")
    def replace_src(match):
        attr = match.group(1)
        url = match.group(2)
        if url.startswith("data:") or not url.strip():
            return match.group(0)
        local = download_file(url, IMG_DIR, "img_")
        if local:
            return f'{attr}="{local}"'
        return match.group(0)

    html = re.sub(r'((?:data-)?src(?:set)?)=["\']([^"\']+)["\']', replace_src, html)

    def replace_bg_url(match):
        url = match.group(1).strip("'\"")
        if url.startswith("data:"):
            return match.group(0)
        local = download_file(url, IMG_DIR, "bg_")
        if local:
            return f"background-image: url('{local}')"
        return match.group(0)

    html = re.sub(r'background-image:\s*url\(([^)]+)\)', replace_bg_url, html)

    def replace_bg_shorthand(match):
        prefix = match.group(1)
        url = match.group(2).strip("'\"")
        suffix = match.group(3)
        if url.startswith("data:"):
            return match.group(0)
        local = download_file(url, IMG_DIR, "bg_")
        if local:
            return f"background:{prefix}url('{local}'){suffix}"
        return match.group(0)

    html = re.sub(r'background:([^;]*?)url\(([^)]+)\)([^;]*)', replace_bg_shorthand, html)
    return html

def download_scripts(html):
    print("\n📜 Processing scripts...")
    def replace_script(match):
        tag = match.group(0)
        src_match = re.search(r'src=["\']([^"\']+)["\']', tag)
        if not src_match:
            return tag
        url = src_match.group(1)
        resolved = resolve_url(url)
        if not resolved:
            return tag

        # Keep essential scripts (jQuery, Bootstrap, Slick, etc), skip tracking
        tracking = [
            'googletagmanager', 'google-analytics', 'doubleclick', 'facebook.net',
            'fbevents', 'clarity.ms', 'klaviyo', 'trekkie', 'trackcollect',
            'wetracked', 'optimonk', 'pixel', 'beacon', 'config-security',
            'shop.app/checkouts', 'shopify.com/proxy', 'web-pixels',
            'consent-tracking', 'perf-kit', 'shop_events_listener',
            'chrome-extension', 'triplewhale', 'alia-prod', 'aimerce',
            'aftersell', 'intelligems', 'monorail', 'vitals.js',
            'td.js', 'amz.js', 'pixelate', 'adnabu'
        ]
        if any(t in resolved.lower() for t in tracking):
            return ''

        local = download_file(url, JS_DIR, "js_")
        if local:
            return tag.replace(src_match.group(0), f'src="{local}"')
        return tag

    html = re.sub(r'<script[^>]*src=["\'][^"\']+["\'][^>]*>(?:</script>)?', replace_script, html, flags=re.IGNORECASE)
    return html

def download_favicons(html):
    print("\n🔖 Processing favicons...")
    def replace_fav(match):
        tag = match.group(0)
        href_match = re.search(r'href=["\']([^"\']+)["\']', tag)
        if not href_match:
            return tag
        local = download_file(href_match.group(1), IMG_DIR, "fav_")
        if local:
            return tag.replace(href_match.group(0), f'href="{local}"')
        return tag

    html = re.sub(r'<link[^>]*rel=["\'](?:icon|shortcut icon|apple-touch-icon)["\'][^>]*>', replace_fav, html, flags=re.IGNORECASE)
    return html

def clean_tracking(html):
    print("\n🧹 Cleaning tracking...")
    # Remove inline tracking scripts
    html = re.sub(r'<script[^>]*>\s*(?:window\.dataLayer|function gtag|gtag\(|fbq\(|clarity\(|window\.ShopifyAnalytics|_learnq|__st\.).*?</script>', '', html, flags=re.IGNORECASE | re.DOTALL)
    # Remove tracking noscripts
    html = re.sub(r'<noscript[^>]*>.*?(?:facebook|google|clarity).*?</noscript>', '', html, flags=re.IGNORECASE | re.DOTALL)
    # Remove browser extension artifacts
    html = re.sub(r'<script[^>]*bis_use[^>]*>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<script[^>]*data-dynamic-id[^>]*>.*?</script>', '', html, flags=re.DOTALL)
    # Remove prefetch/preconnect for tracking
    html = re.sub(r'<link[^>]*(?:prefetch|preconnect|dns-prefetch)[^>]*(?:monorail|shop\.app|config-security|clarity|facebook|google-analytics|klaviyo)[^>]*/?>', '', html, flags=re.IGNORECASE)
    return html

def fix_relative_urls(html):
    print("\n🔗 Fixing relative URLs...")
    html = re.sub(r'href="(/(?!Users)[^"]*)"', f'href="{ORIGIN}\\1"', html)
    return html

def main():
    print("=" * 60)
    print("🏗️  Building self-contained TrueHealthic page")
    print("=" * 60)

    html = INPUT_FILE.read_text(encoding='utf-8', errors='replace')
    print(f"\n📄 Source: {len(html):,} chars")

    html = clean_tracking(html)
    html = download_and_inline_css(html)
    html = download_scripts(html)
    html = download_images(html)
    html = download_favicons(html)
    html = fix_relative_urls(html)

    OUTPUT_FILE.write_text(html, encoding='utf-8')

    total = sum(1 for _ in ASSETS_DIR.rglob("*") if _.is_file())
    print(f"\n{'=' * 60}")
    print(f"✅ Done! {OUTPUT_FILE}")
    print(f"   Assets: {total} | Size: {OUTPUT_FILE.stat().st_size:,} bytes")
    print(f"{'=' * 60}")

if __name__ == "__main__":
    main()
