#!/usr/bin/env python3
"""
Scrape Typst documentation from typst.app/docs and save as markdown.
"""

import os
import re
import time
from urllib.parse import urljoin, urlparse
from collections import deque

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md, MarkdownConverter


class TypstMarkdownConverter(MarkdownConverter):
    """Custom converter that handles Typst doc-specific HTML patterns."""

    def convert_pre(self, el, text, **kwargs):
        """Convert pre blocks to fenced code blocks with typst language hint."""
        code = el.get_text()
        # Try to detect if it's typst code (has # function calls or = headings)
        lang = "typst" if re.search(r'(^|\n)#|^=+ ', code) else ""
        return f"\n```{lang}\n{code.strip()}\n```\n"


def convert_to_markdown(html_content):
    """Convert HTML to markdown using custom converter."""
    return TypstMarkdownConverter(
        heading_style="atx",
        bullets="-",
        strip=["script", "style", "nav", "footer", "header"]
    ).convert(html_content)


class TypstDocsScraper:
    BASE_URL = "https://typst.app/docs/"

    def __init__(self, output_dir="docs"):
        self.output_dir = output_dir
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "TypstDocsScraper/1.0 (local documentation mirror)"
        })
        self.visited = set()
        self.to_visit = deque()

    def get_page(self, url):
        """Fetch a page with rate limiting."""
        try:
            resp = self.session.get(url, timeout=30)
            resp.raise_for_status()
            time.sleep(0.5)  # Be nice to the server
            return resp.text
        except requests.RequestException as e:
            print(f"  Error fetching {url}: {e}")
            return None

    def extract_nav_links(self, soup):
        """Extract documentation links from navigation."""
        links = set()
        for a in soup.find_all("a", href=True):
            href = a["href"]
            # Only follow docs links
            if href.startswith("/docs/") or href.startswith("https://typst.app/docs/"):
                full_url = urljoin(self.BASE_URL, href)
                # Normalize URL (remove trailing slash inconsistency)
                parsed = urlparse(full_url)
                if parsed.netloc == "typst.app" and parsed.path.startswith("/docs/"):
                    # Remove fragment and query
                    clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                    if not clean_url.endswith("/"):
                        clean_url += "/"
                    links.add(clean_url)
        return links

    def extract_content(self, soup, url):
        """Extract main documentation content from page."""
        # Remove navigation, header, footer, scripts
        for tag in soup.find_all(["nav", "header", "footer", "script", "style"]):
            tag.decompose()

        # Try to find main content area
        main = soup.find("main") or soup.find("article") or soup.find("div", class_="content")

        if not main:
            # Fall back to body
            main = soup.find("body")

        if not main:
            return None, None

        # Get title
        title_tag = soup.find("h1")
        title = title_tag.get_text().strip() if title_tag else ""

        # Convert to markdown
        content = convert_to_markdown(str(main))

        # Clean up excessive whitespace
        content = re.sub(r'\n{3,}', '\n\n', content)

        return title, content.strip()

    def url_to_filepath(self, url):
        """Convert URL to local file path."""
        parsed = urlparse(url)
        path = parsed.path.replace("/docs/", "").strip("/")
        if not path:
            path = "index"
        return os.path.join(self.output_dir, f"{path}.md")

    def save_page(self, url, title, content):
        """Save content to markdown file."""
        filepath = self.url_to_filepath(url)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # Add frontmatter
        full_content = f"# {title}\n\nSource: {url}\n\n---\n\n{content}"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(full_content)

        return filepath

    def scrape(self):
        """Main scraping loop."""
        print(f"Starting Typst docs scrape...")
        print(f"Output directory: {self.output_dir}")

        # Start with main docs page
        self.to_visit.append(self.BASE_URL)

        # Also seed with known important sections
        seed_urls = [
            "https://typst.app/docs/tutorial/",
            "https://typst.app/docs/reference/",
            "https://typst.app/docs/guides/",
            "https://typst.app/docs/reference/syntax/",
            "https://typst.app/docs/reference/styling/",
            "https://typst.app/docs/reference/scripting/",
            "https://typst.app/docs/reference/context/",
            "https://typst.app/docs/reference/foundations/",
            "https://typst.app/docs/reference/model/",
            "https://typst.app/docs/reference/text/",
            "https://typst.app/docs/reference/math/",
            "https://typst.app/docs/reference/symbols/",
            "https://typst.app/docs/reference/layout/",
            "https://typst.app/docs/reference/visualize/",
            "https://typst.app/docs/reference/introspection/",
            "https://typst.app/docs/reference/data-loading/",
        ]
        for url in seed_urls:
            if url not in self.visited:
                self.to_visit.append(url)

        pages_scraped = 0

        while self.to_visit:
            url = self.to_visit.popleft()

            if url in self.visited:
                continue

            self.visited.add(url)
            print(f"Scraping: {url}")

            html = self.get_page(url)
            if not html:
                continue

            soup = BeautifulSoup(html, "lxml")

            # Discover new links
            new_links = self.extract_nav_links(soup)
            for link in new_links:
                if link not in self.visited:
                    self.to_visit.append(link)

            # Extract and save content
            title, content = self.extract_content(soup, url)
            if content:
                filepath = self.save_page(url, title, content)
                pages_scraped += 1
                print(f"  Saved: {filepath}")

        print(f"\nDone! Scraped {pages_scraped} pages.")
        print(f"Visited {len(self.visited)} URLs total.")
        return pages_scraped


def main():
    scraper = TypstDocsScraper(output_dir="docs")
    scraper.scrape()


if __name__ == "__main__":
    main()
