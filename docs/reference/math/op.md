# opElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/math/op/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Math](/docs/reference/math/)
- ![](/assets/icons/16-chevron-right.svg)
- [Text Operator](/docs/reference/math/op/)

# `op`Element Question mark Element functions can be customized with `set` and `show` rules.

A text operator in an equation.

## Example

```
$ tan x = (sin x)/(cos x) $
$ op("custom",
     limits: #true)_(n->oo) n $
```

![Preview](/assets/docs/n9yefElmfwTi92ejfLzhZwAAAAAAAAAA.png)

## Predefined Operators

Typst predefines the operators `arccos`, `arcsin`, `arctan`, `arg`, `cos`,
`cosh`, `cot`, `coth`, `csc`, `csch`, `ctg`, `deg`, `det`, `dim`, `exp`,
`gcd`, `lcm`, `hom`, `id`, `im`, `inf`, `ker`, `lg`, `lim`, `liminf`,
`limsup`, `ln`, `log`, `max`, `min`, `mod`, `Pr`, `sec`, `sech`, `sin`,
`sinc`, `sinh`, `sup`, `tan`, `tanh`, `tg` and `tr`.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

math.op(

[content](/docs/reference/foundations/content/),[limits:](#parameters-limits) [bool](/docs/reference/foundations/bool/),

) -> [content](/docs/reference/foundations/content/)

### `text` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The operator's text.

### `limits` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether the operator should show attachments as limits in display mode.

Default: `false`

[![←](/assets/icons/16-chevron-right.svg)

StylesPrevious page](/docs/reference/math/styles/) [![→](/assets/icons/16-chevron-right.svg)

Under/OverNext page](/docs/reference/math/underover/)