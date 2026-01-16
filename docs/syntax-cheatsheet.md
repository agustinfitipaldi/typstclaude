# Typst Syntax Cheatsheet

CRITICAL: Typst is NOT LaTeX. This is a completely different language.

## Modes

Typst has three syntactical modes:
- **Markup mode** (default): For writing text and using markup syntax
- **Math mode**: Enter with `$...$` (inline) or `$ ... $` (display, with spaces)
- **Code mode**: Enter with `#` prefix

| Switch to | Syntax | Example |
|-----------|--------|---------|
| Code | `#` prefix | `Number: #(1 + 2)` |
| Math | `$...$` | `$x^2$` inline, `$ x^2 $` display |
| Markup | `[..]` in code | `let name = [*Typst!*]` |

---

## Markup Syntax

| Element | Syntax | LaTeX Equivalent |
|---------|--------|------------------|
| Heading | `= Title` | `\section{Title}` |
| Subheading | `== Subtitle` | `\subsection{Subtitle}` |
| Bold | `*bold*` | `\textbf{bold}` |
| Italic | `_italic_` | `\emph{italic}` |
| Bullet list | `- item` | `\begin{itemize}\item` |
| Numbered list | `+ item` | `\begin{enumerate}\item` |
| Term list | `/ Term: desc` | `\begin{description}\item[Term]` |
| Link | `https://url` | `\url{https://url}` |
| Label | `<label>` | `\label{label}` |
| Reference | `@label` | `\ref{label}` |
| Citation | `@key` | `\cite{key}` |
| Raw/code | `` `code` `` | `\texttt{code}` |
| Line break | `\` | `\\` |
| Comment | `// line` or `/* block */` | `% comment` |

---

## Math Mode

| Element | Typst | LaTeX |
|---------|-------|-------|
| Inline math | `$x^2$` | `$x^2$` |
| Display math | `$ x^2 $` (with spaces) | `\[x^2\]` |
| Subscript | `$x_1$` | `$x_1$` |
| Superscript | `$x^2$` | `$x^2$` |
| Fraction | `$(a+b)/c$` | `\frac{a+b}{c}` |
| Square root | `$sqrt(x)$` | `\sqrt{x}` |
| Sum | `$sum_(i=1)^n$` | `\sum_{i=1}^n` |
| Integral | `$integral_a^b$` | `\int_a^b` |
| Greek letters | `$alpha, beta, gamma$` | `\alpha, \beta, \gamma` |
| Text in math | `$"text here"$` | `\text{text here}` |

Note: Delimiters scale automatically in Typst (no `\left`/`\right` needed).

---

## Functions (Code Mode)

Functions are called with `#funcname()` or `#funcname[]` for content arguments.

```typst
// Basic function call
#rect(width: 2cm, height: 1cm)

// With content argument
#underline[underlined text]

// Set rule (applies to rest of document/scope)
#set text(size: 14pt)

// Show rule (transform elements)
#show heading: set text(blue)
```

### Common Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `text()` | Style text | `#set text(font: "Arial", size: 12pt)` |
| `page()` | Page setup | `#set page(margin: 2cm)` |
| `image()` | Insert image | `#image("file.png", width: 50%)` |
| `table()` | Create table | `#table(columns: 3, [A], [B], [C])` |
| `figure()` | Figure with caption | `#figure(image("x.png"), caption: [Text])` |
| `link()` | Hyperlink | `#link("https://url")[text]` |
| `bibliography()` | Bibliography | `#bibliography("refs.bib")` |

---

## Code Mode Syntax

```typst
// Variables
#let x = 5
#let name = "Alice"

// Functions
#let greet(name) = [Hello, #name!]

// Arrays
#let nums = (1, 2, 3)

// Dictionaries
#let person = (name: "Bob", age: 30)

// Conditionals
#if x > 3 [Big] else [Small]

// Loops
#for i in range(5) [Item #i. ]

// Import
#import "file.typ": func
#import "@preview/package:1.0.0"
```

---

## Key Differences from LaTeX

1. **No backslashes**: Use `#` for functions, not `\`
2. **No environments**: Use functions like `#list()`, `#table()` instead of `\begin{}`
3. **No packages to load**: Most features are built-in
4. **Content in brackets**: `[content]` instead of `{content}` for function arguments
5. **Set rules**: `#set text(...)` instead of declarations like `\bfseries`
6. **Auto-scaling delimiters**: No `\left`/`\right` needed in math
7. **Simpler math**: `(a+b)/c` becomes a fraction automatically

---

## Quick Reference: LaTeX to Typst

```
\section{Title}       →  = Title
\textbf{bold}         →  *bold*
\emph{italic}         →  _italic_
\begin{itemize}       →  - item
\begin{enumerate}     →  + item
\cite{key}            →  @key
\ref{label}           →  @label
\frac{a}{b}           →  $(a)/(b)$ or $frac(a,b)$
\sqrt{x}              →  $sqrt(x)$
\sum_{i=1}^{n}        →  $sum_(i=1)^n$
\int_{a}^{b}          →  $integral_a^b$
\left( \right)        →  $()$ (auto-scales)
\includegraphics      →  #image("file.png")
\begin{table}         →  #table(...)
\begin{figure}        →  #figure(...)
```
