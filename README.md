# Typst Context for Claude

A local markdown mirror of the [Typst documentation](https://typst.app/docs/), scraped for Claude to use for accurate Typst writing.

## What's Included

- **`docs/`** - Complete Typst documentation converted to markdown
  - `syntax-cheatsheet.md` - Quick reference for Typst syntax
  - `reference/` - Full function and type reference (200+ pages)
  - `guides/` - User guides including LaTeX migration
  - `tutorial/` - Getting started tutorials
- **`scrape_typst_docs.py`** - Python scraper to regenerate the docs
- **`CLAUDE.md`** - LLM context file for AI assistants working with Typst

## Usage

### Using the Documentation

The `docs/` folder contains markdown versions of the official Typst documentation. Use it for:
- Offline reference
- Providing context to LLMs/AI coding assistants
- Quick searching with grep/ripgrep

### Regenerating the Docs

To scrape a fresh copy of the documentation:

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the scraper
python scrape_typst_docs.py
```

The scraper respects rate limits (0.5s between requests) and will output to the `docs/` directory.

## LLM Context

The `CLAUDE.md` file provides context for AI assistants to understand Typst syntax. It includes:
- Key differences between Typst and LaTeX
- Common syntax patterns
- Function reference pointers

This is useful when using AI coding assistants to help write Typst documents.

## License

The scraper code is provided as-is. The scraped documentation is from [Typst](https://typst.app/) - see their [licensing terms](https://github.com/typst/typst/blob/main/LICENSE).
