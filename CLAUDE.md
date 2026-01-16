# Typst Documentation Project

## Typst Documentation Reference

When writing or helping with Typst code, **ALWAYS** reference the local documentation in `./docs/` before answering. Typst is a modern typesetting language that is completely different from LaTeX.

### Quick Reference Files

- `./docs/syntax-cheatsheet.md` - Core syntax patterns and LaTeX-to-Typst mapping
- `./docs/guides/for-latex-users.md` - Comprehensive LaTeX migration guide
- `./docs/reference/syntax.md` - Full syntax reference
- `./docs/reference/` - Complete function/type documentation (200+ pages)

### CRITICAL: Typst is NOT LaTeX

Before writing ANY Typst code, internalize these differences:

| Concept | LaTeX | Typst |
|---------|-------|-------|
| Headings | `\section{Title}` | `= Title` |
| Bold | `\textbf{text}` | `*text*` |
| Italic | `\emph{text}` | `_text_` |
| Bullet list | `\begin{itemize}\item` | `- item` |
| Numbered list | `\begin{enumerate}\item` | `+ item` |
| Functions | `\command{arg}` | `#command(arg)` or `#command[content]` |
| Math | `$x^2$`, `\[x^2\]` | `$x^2$` (inline), `$ x^2 $` (display) |
| Fractions | `\frac{a}{b}` | `$(a)/(b)$` or `$frac(a,b)$` |
| References | `\ref{label}` | `@label` |
| Citations | `\cite{key}` | `@key` |
| Comments | `% comment` | `// comment` or `/* block */` |

### Common Patterns

```typst
// Set rules (apply defaults)
#set page(margin: 2cm)
#set text(font: "Arial", size: 11pt)
#set par(justify: true)

// Show rules (transform elements)
#show heading: set text(blue)

// Functions with content
#figure(
  image("diagram.png", width: 80%),
  caption: [A diagram]
)

// Lists
- First item
- Second item
  - Nested item

// Math
$ integral_0^infinity e^(-x^2) dif x = sqrt(pi)/2 $
```

### Function Lookup

For any Typst function, check:
1. `./docs/reference/foundations/` - Core types (str, int, array, etc.)
2. `./docs/reference/text/` - Text formatting functions
3. `./docs/reference/layout/` - Layout functions (page, grid, etc.)
4. `./docs/reference/model/` - Document elements (heading, list, table, etc.)
5. `./docs/reference/math/` - Math functions
6. `./docs/reference/visualize/` - Graphics (image, rect, circle, etc.)

### When in Doubt

1. Check `./docs/syntax-cheatsheet.md` first
2. Search the appropriate reference folder
3. Remember: NO backslashes, NO `\begin{}`/`\end{}`, functions use `#`
