# equationElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/math/equation/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Math](/docs/reference/math/)
- ![](/assets/icons/16-chevron-right.svg)
- [Equation](/docs/reference/math/equation/)

# `equation`Element Question mark Element functions can be customized with `set` and `show` rules.

A mathematical equation.

Can be displayed inline with text or as a separate block. An equation
becomes block-level through the presence of whitespace after the opening
dollar sign and whitespace before the closing dollar sign.

## Example

```typst
#set text(font: "New Computer Modern")

Let $a$, $b$, and $c$ be the side
lengths of right-angled triangle.
Then, we know that:
$ a^2 + b^2 = c^2 $

Prove by induction:
$ sum_(k=1)^n k = (n(n+1)) / 2 $
```

![Preview](/assets/docs/JtxOgQArvspfmmStl8-3_gAAAAAAAAAA.png)

By default, block-level equations will not break across pages. This can be
changed through `show math.equation: set block(breakable: true)`.

## Syntax

This function also has dedicated syntax: Write mathematical markup within
dollar signs to create an equation. Starting and ending the equation with
whitespace lifts it into a separate block that is centered horizontally.
For more details about math syntax, see the
[main math page](/docs/reference/math/).

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

math.equation(

[block:](#parameters-block) [bool](/docs/reference/foundations/bool/),[numbering:](#parameters-numbering) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/)[function](/docs/reference/foundations/function/),[number-align:](#parameters-number-align) [alignment](/docs/reference/layout/alignment/),[supplement:](#parameters-supplement) [none](/docs/reference/foundations/none/)[auto](/docs/reference/foundations/auto/)[content](/docs/reference/foundations/content/)[function](/docs/reference/foundations/function/),[alt:](#parameters-alt) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `block` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether the equation is displayed as a separate block.

Default: `false`

### `numbering` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/) or [function](/docs/reference/foundations/function/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How to number block-level equations. Accepts a
[numbering pattern or function](/docs/reference/model/numbering/) taking a single number.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set math.equation(numbering: "(1)")

We define:
$ phi.alt := (1 + sqrt(5)) / 2 $ <ratio>

With @ratio, we get:
$ F_n = floor(1 / sqrt(5) phi.alt^n) $
```

![Preview](/assets/docs/ICkRN4qFA2wn3VV_dGJcKAAAAAAAAAAA.png)

Default: `none`

### `number-align` [alignment](/docs/reference/layout/alignment/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The alignment of the equation numbering.

By default, the alignment is `end + horizon`. For the horizontal
component, you can use `right`, `left`, or `start` and `end`
of the text direction; for the vertical component, you can use
`top`, `horizon`, or `bottom`.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set math.equation(numbering: "(1)", number-align: bottom)

We can calculate:
$ E &= sqrt(m_0^2 + p^2) \
    &approx 125 "GeV" $
```

![Preview](/assets/docs/EjQKswH-OBAc5Rwhl-7WNQAAAAAAAAAA.png)

Default: `end + horizon`

### `supplement` [none](/docs/reference/foundations/none/) or [auto](/docs/reference/foundations/auto/) or [content](/docs/reference/foundations/content/) or [function](/docs/reference/foundations/function/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

A supplement for the equation.

For references to equations, this is added before the referenced number.

If a function is specified, it is passed the referenced equation and
should return content.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set math.equation(numbering: "(1)", supplement: [Eq.])

We define:
$ phi.alt := (1 + sqrt(5)) / 2 $ <ratio>

With @ratio, we get:
$ F_n = floor(1 / sqrt(5) phi.alt^n) $
```

![Preview](/assets/docs/LsvSGn7Nchg2dddv3zDBtAAAAAAAAAAA.png)

Default: `auto`

### `alt` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

An alternative description of the mathematical equation.

This should describe the full equation in natural language and will be
made available to Assistive Technology. You can learn more in the
[Textual Representations section of the Accessibility
Guide](/docs/guides/accessibility/#textual-representations).

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#math.equation(
  alt: "integral from 1 to infinity of a x squared plus b with respect to x",
  block: true,
  $ integral_1^oo a x^2 + b dif x $,
)
```

![Preview](/assets/docs/0DeRe9uXAIt5WX8U3NPWtQAAAAAAAAAA.png)

Default: `none`

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The contents of the equation.

[![←](/assets/icons/16-chevron-right.svg)

ClassPrevious page](/docs/reference/math/class/) [![→](/assets/icons/16-chevron-right.svg)

FractionNext page](/docs/reference/math/frac/)