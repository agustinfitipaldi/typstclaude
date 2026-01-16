# Math

Source: https://typst.app/docs/reference/math/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Math](/docs/reference/math/)

# Math

Typst has special [syntax](/docs/reference/syntax/#math) and library functions to typeset
mathematical formulas. Math formulas can be displayed inline with text or as
separate blocks. They will be typeset into their own block if they start and end
with at least one space (e.g. `$ x^2 $`).

## Variables

In math, single letters are always displayed as is. Multiple letters, however,
are interpreted as variables and functions. To display multiple letters
verbatim, you can place them into quotes and to access single letter variables,
you can use the [hash syntax](/docs/reference/scripting/#expressions).

```typst
$ A = pi r^2 $
$ "area" = pi dot "radius"^2 $
$ cal(A) :=
    { x in RR | x "is natural" } $
#let x = 5
$ #x < 17 $
```

![Preview](/assets/docs/hSTnanxnhN2cMLti2SpIlwAAAAAAAAAA.png)

## Symbols

Math mode makes a wide selection of [symbols](/docs/reference/symbols/sym/) like `pi`,
`dot`, or `RR` available. Many mathematical symbols are available in different
variants. You can select between different variants by applying
[modifiers](/docs/reference/foundations/symbol/) to the symbol. Typst further recognizes a number of
shorthand sequences like `=>` that approximate a symbol. When such a shorthand
exists, the symbol's documentation lists it.

```
$ x < y => x gt.eq.not y $
```

![Preview](/assets/docs/3QjDlBq8e4sckxD76_cbbgAAAAAAAAAA.png)

## Line Breaks

Formulas can also contain line breaks. Each line can contain one or multiple
*alignment points* (`&`) which are then aligned.

```
$ sum_(k=0)^n k
    &= 1 + ... + n \
    &= (n(n+1)) / 2 $
```

![Preview](/assets/docs/4Y4RfouYZm3Jgju-7W3SZAAAAAAAAAAA.png)

## Function calls

Math mode supports special function calls without the hash prefix. In these
"math calls", the argument list works a little differently than in code:

- Within them, Typst is still in "math mode". Thus, you can write math directly
  into them, but need to use hash syntax to pass code expressions (except for
  strings, which are available in the math syntax).
- They support positional and named arguments, as well as argument spreading.
- They don't support trailing content blocks.
- They provide additional syntax for 2-dimensional argument lists. The semicolon
  (`;`) merges preceding arguments separated by commas into an array argument.

```
$ frac(a^2, 2) $
$ vec(1, 2, delim: "[") $
$ mat(1, 2; 3, 4) $
$ mat(..#range(1, 5).chunks(2)) $
$ lim_x =
    op("lim", limits: #true)_x $
```

![Preview](/assets/docs/oE5_WV4ra9YujrIbz2OgQgAAAAAAAAAA.png)

To write a verbatim comma or semicolon in a math call, escape it with a
backslash. The colon on the other hand is only recognized in a special way if
directly preceded by an identifier, so to display it verbatim in those cases,
you can just insert a space before it.

Functions calls preceded by a hash are normal code function calls and not
affected by these rules.

## Alignment

When equations include multiple *alignment points* (`&`), this creates blocks of
alternatingly right- and left-aligned columns. In the example below, the
expression `(3x + y) / 7` is right-aligned and `= 9` is left-aligned. The word
"given" is also left-aligned because `&&` creates two alignment points in a row,
alternating the alignment twice. `& &` and `&&` behave exactly the same way.
Meanwhile, "multiply by 7" is right-aligned because just one `&` precedes it.
Each alignment point simply alternates between right-aligned/left-aligned.

```
$ (3x + y) / 7 &= 9 && "given" \
  3x + y &= 63 & "multiply by 7" \
  3x &= 63 - y && "subtract y" \
  x &= 21 - y/3 & "divide by 3" $
```

![Preview](/assets/docs/8SM9qVyRZ_Elks_C9882dAAAAAAAAAAA.png)

## Math fonts

You can set the math font by with a [show-set rule](/docs/reference/styling/#show-rules) as
demonstrated below. Note that only special OpenType math fonts are suitable for
typesetting maths.

```typst
#show math.equation: set text(font: "Fira Math")
$ sum_(i in NN) 1 + i $
```

![Preview](/assets/docs/qG9Xcf2X5Ju0E76URIxfZgAAAAAAAAAA.png)

## Math module

All math functions are part of the `math` [module](/docs/reference/scripting/#modules), which
is available by default in equations. Outside of equations, they can be accessed
with the `math.` prefix.

## Accessibility

To make math accessible, you must provide alternative descriptions of equations
in natural language using the [`alt` parameter of
`math.equation`](/docs/reference/math/equation/#parameters-alt). For more information, see the [Textual
Representations section of the Accessibility
Guide](/docs/guides/accessibility/#textual-representations).

```typst
#math.equation(
  alt: "d S equals delta q divided by T",
  block: true,
  $ dif S = (delta q) / T $,
)
```

![Preview](/assets/docs/INZOUOsDY6s763dtPOwR3AAAAAAAAAAA.png)

In the future, Typst will automatically make equations without alternative
descriptions accessible in HTML and PDF 2.0 export.

## Definitions

- [`accent`](/docs/reference/math/accent/)  Attaches an accent to a base.
- [attach](/docs/reference/math/attach/)  Subscript, superscripts, and limits.
- [`binom`](/docs/reference/math/binom/)  A binomial expression.
- [`cancel`](/docs/reference/math/cancel/)  Displays a diagonal line over a part of an equation.
- [`cases`](/docs/reference/math/cases/)  A case distinction.
- [`class`](/docs/reference/math/class/)  Forced use of a certain math class.
- [`equation`](/docs/reference/math/equation/)  A mathematical equation.
- [`frac`](/docs/reference/math/frac/)  A mathematical fraction.
- [lr](/docs/reference/math/lr/)  Delimiter matching.
- [`mat`](/docs/reference/math/mat/)  A matrix.
- [`op`](/docs/reference/math/op/)  A text operator in an equation.
- [`primes`](/docs/reference/math/primes/)  Grouped primes.
- [roots](/docs/reference/math/roots/)  Square and non-square roots.
- [sizes](/docs/reference/math/sizes/)  Forced size styles for expressions within formulas.
- [`stretch`](/docs/reference/math/stretch/)  Stretches a glyph.
- [styles](/docs/reference/math/styles/)  Alternate letterforms within formulas.
- [underover](/docs/reference/math/underover/)  Delimiters above or below parts of an equation.
- [variants](/docs/reference/math/variants/)  Alternate typefaces within formulas.
- [`vec`](/docs/reference/math/vec/)  A column vector.

[![←](/assets/icons/16-chevron-right.svg)

UppercasePrevious page](/docs/reference/text/upper/) [![→](/assets/icons/16-chevron-right.svg)

AccentNext page](/docs/reference/math/accent/)