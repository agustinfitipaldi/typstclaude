# fracElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/math/frac/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Math](/docs/reference/math/)
- ![](/assets/icons/16-chevron-right.svg)
- [Fraction](/docs/reference/math/frac/)

# `frac`Element Question mark Element functions can be customized with `set` and `show` rules.

A mathematical fraction.

## Example

```
$ 1/2 < (x+1)/2 $
$ ((x+1)) / 2 = frac(a, b) $
```

![Preview](/assets/docs/9RFsr-VSObielPb4Nrr-zQAAAAAAAAAA.png)

## Syntax

This function also has dedicated syntax: Use a slash to turn neighbouring
expressions into a fraction. Multiple atoms can be grouped into a single
expression using round grouping parentheses. Such parentheses are removed
from the output, but you can nest multiple to force them.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

math.frac(

[content](/docs/reference/foundations/content/),[content](/docs/reference/foundations/content/),[style:](#parameters-style) [str](/docs/reference/foundations/str/),

) -> [content](/docs/reference/foundations/content/)

### `num` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The fraction's numerator.

### `denom` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The fraction's denominator.

### `style` [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How the fraction should be laid out.

  ![](/assets/icons/16-chevron-right.svg) View example: Styles 

```
$ frac(x, y, style: "vertical") $
$ frac(x, y, style: "skewed") $
$ frac(x, y, style: "horizontal") $
```

![Preview](/assets/docs/rbvekr5KnstwzqSwIhOMsAAAAAAAAAAA.png)

   ![](/assets/icons/16-chevron-right.svg) View example: Setting the default 

```typst
#set math.frac(style: "skewed")
$ a / b $
```

![Preview](/assets/docs/C3eC2tzND4bLHJCN7QEWBwAAAAAAAAAA.png)

   ![](/assets/icons/16-chevron-right.svg) View example: Handling of grouping parentheses 

```typst
// Grouping parentheses are removed.
#set math.frac(style: "vertical")
$ (a + b) / b $

// Grouping parentheses are removed.
#set math.frac(style: "skewed")
$ (a + b) / b $

// Grouping parentheses are retained.
#set math.frac(style: "horizontal")
$ (a + b) / b $
```

![Preview](/assets/docs/bDgPvzmhmghTI54-coqcPwAAAAAAAAAA.png)

   ![](/assets/icons/16-chevron-right.svg) View example: Different styles in inline vs block equations 

```typst
// This changes the style for inline equations only.
#show math.equation.where(block: false): set math.frac(style: "horizontal")

This $(x-y)/z = 3$ is inline math, and this is block math:
$ (x-y)/z = 3 $
```

![Preview](/assets/docs/kU4oOiEGmQKXIT_3UoYMDwAAAAAAAAAA.png)

| Variant | Details |
| --- | --- |
| `"vertical"` | Stacked numerator and denominator with a bar. |
| `"skewed"` | Numerator and denominator separated by a slash. |
| `"horizontal"` | Numerator and denominator placed inline and parentheses are not absorbed. |

Default: `"vertical"`

[![←](/assets/icons/16-chevron-right.svg)

EquationPrevious page](/docs/reference/math/equation/) [![→](/assets/icons/16-chevron-right.svg)

Left/RightNext page](/docs/reference/math/lr/)