# Roadmap

Source: https://typst.app/docs/roadmap/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Roadmap](/docs/roadmap/)

# Roadmap

This page lists planned features for the Typst language, compiler, library and
web app. Since priorities and development realities change, this roadmap is not
set in stone. Features that are listed here will not necessarily be implemented
and features that will be implemented might be missing here. Moreover, this
roadmap only lists larger, more fundamental features and bugs.

Are you missing something on the roadmap? Typst relies on your feedback as a
user to plan for and prioritize new features. Get started by filing a new issue
on [GitHub](https://github.com/typst/typst/issues) or discuss your feature
request with the [community](https://typst.app/docs/community).

## Language and Compiler

- **Styling**

  - Support for revoking style rules
  - Ancestry selectors (e.g., within)
  - ~~Fix show rule recursion crashes~~
  - ~~Fix show-set issues~~
- **Scripting**

  - Function for debug logging
  - Fix issues with paths being strings
  - Custom types (that work with set and show rules)
  - Type hints
  - Function hoisting (if feasible)
  - ~~Data loading functions~~
  - ~~Support for compiler warnings~~
  - ~~Types as first-class values~~
  - ~~More fields and methods on primitives~~
  - ~~WebAssembly plugins~~
  - ~~Get values of set rules~~
  - ~~Replace locate, etc. with unified context system~~
  - ~~Allow expressions as dictionary keys~~
  - ~~Package management~~
- **Model**

  - Fix issues with numbering patterns
  - Better support for custom referenceable things
  - Enum continuation
  - ~~Richer built-in outline customization~~
  - ~~Support a path or bytes in places that currently only support paths,
    superseding `.decode` scoped functions~~ (not yet released)
  - ~~Bibliography and citation customization via CSL
    (Citation Style Language)~~
  - ~~Relative counters, e.g. for figure numbering per section~~
- **Text**

  - Font fallback warnings
  - Bold, italic, and smallcaps synthesis
  - Variable fonts support
  - Ruby and Warichu
  - Kashida justification
  - ~~Support for basic CJK text layout rules~~
  - ~~Fix SVG font fallback~~
  - ~~Themes for raw text and more/custom syntaxes~~
- **Math**

  - Fix attachment parsing priorities
  - Fix syntactic quirks
  - Fix font handling
  - Provide more primitives
  - Improve equation numbering
  - Big fractions
  - ~~Fix single letter strings~~
- **Layout**

  - Fix issues with list (in particular baselines & alignment)
  - Balanced columns
  - Support for side-floats and other "collision" layouts
  - Drop caps
  - End notes, maybe margin notes
  - Page adjustment from within flow
  - Chained layout regions
  - Better support for more canvas-like layouts
  - Grid-based typesetting
  - Maybe unified layout primitives across normal content and math
  - ~~Character-level justification~~
  - ~~Improve widow & orphan prevention~~
  - ~~Expand floating layout (e.g. over two columns)~~
  - ~~Support for "sticky" blocks that stay with the next one~~
  - ~~Fix footnote issues~~ (not all released yet)
  - ~~Footnotes~~
  - ~~Basic floating layout~~
  - ~~Row span and column span in table~~
  - ~~Per-cell table stroke customization~~
- **Visualize**

  - Arrows
  - Color management
  - ~~PDFs as images~~
  - ~~Better path drawing~~
  - ~~More configurable strokes~~
  - ~~Gradients~~
  - ~~Patterns~~
- **Introspection**

  - Better diagnostics for non-convergence
  - Support for freezing content, so that e.g. numbers in it remain the same
    if it appears multiple times
- **Export**

  - HTML export (in progress)
  - PDF/UA-2 support
  - PDF/X support
  - EPUB export
  - ~~Tagged PDF for Accessibility~~
  - ~~PDF/A support~~
  - ~~PNG export~~
  - ~~SVG export~~
  - ~~Support for transparency in PDF~~
  - ~~Fix issues with SVGs in PDF~~
  - ~~Fix emoji export in PDF~~
  - ~~Selectable text in SVGs in PDF~~
  - ~~Better font subsetting for smaller PDFs~~
- **CLI**

  - Support for downloading fonts on-demand automatically
  - ~~`typst query` for querying document elements~~
  - ~~`typst init` for creating a project from a template~~
  - ~~`typst update` for self-updating the CLI~~
- **Tooling**

  - Autoformatter
  - Documentation generator and doc comments
  - Linter
- **Performance**

  - Reduce memory usage
  - ~~Optimize runtime of optimal paragraph layout~~
  - ~~Parallelize layout engine~~
- **Development**

  - Benchmarking
  - Better contributor documentation

## Web App

- **Editing**

  - Smarter & more action buttons
  - Inline documentation
  - Preview autocomplete entry
  - Color Picker
  - Symbol picker
  - Basic, built-in image editor (cropping, etc.)
  - GUI inspector for editing function calls
  - Cursor in preview
  - ~~Hover tooltips for debugging~~
  - ~~Scroll to cursor position in preview~~
  - ~~Folders in projects~~
  - ~~Outline panel~~
  - ~~More export options~~
  - ~~Preview in a separate window~~
  - ~~Sync literature with Zotero and Mendely~~
  - ~~Paste modal~~
  - ~~Improve panel~~
- **Writing**

  - Word count
  - Structure view
  - Text completion by LLM
  - ~~Spell check~~
- **Collaboration**

  - Change tracking
  - Version history
  - ~~Chat-like comments~~
  - ~~Git integration~~
- **Project management**

  - ~~Drag-and-drop for projects~~~
  - ~~Folders for projects~~
  - ~~LaTeX, Word, Markdown import~~
  - ~~Thumbnails for projects~~
- **Settings**

  - Keyboard shortcuts configuration
  - Better project settings
  - Avatar Cropping
  - ~~System Theme setting~~
- **Other**

  - Mobile improvements
  - Two-Factor Authentication
  - Advanced search in projects
  - Offline PWA
  - ~~Private packages in teams~~
  - ~~LDAP Single sign-on~~
  - ~~Compiler version picker~~
  - ~~Presentation mode~~
  - ~~Support for On-Premises deployment~~
  - ~~Typst Universe~~

[![←](/assets/icons/16-chevron-right.svg)

SearchPrevious page](/docs/web-app/search/) [![→](/assets/icons/16-chevron-right.svg)

CommunityNext page](/docs/community/)