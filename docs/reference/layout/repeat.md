# repeatElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/layout/repeat/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Repeat](/docs/reference/layout/repeat/)

# `repeat`Element Question mark Element functions can be customized with `set` and `show` rules.

Repeats content to the available space.

This can be useful when implementing a custom index, reference, or outline.

Space may be inserted between the instances of the body parameter, so be
sure to adjust the [`justify`](/docs/reference/layout/repeat/#parameters-justify) parameter accordingly.

Errors if there are no bounds on the available space, as it would create
infinite content.

## Example

```typst
Sign on the dotted line:
#box(width: 1fr, repeat[.])

#set text(10pt)
#v(8pt, weak: true)
#align(right)[
  Berlin, the 22nd of December, 2022
]
```

![Preview](/assets/docs/LGILa4453RB6xoEobzmQcAAAAAAAAAAA.png)

## Accessibility

Repeated content is automatically marked as an [artifact](/docs/reference/pdf/artifact/) and
hidden from Assistive Technology (AT). Do not use this function to create
content that contributes to the meaning of your document.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

repeat(

[content](/docs/reference/foundations/content/),[gap:](#parameters-gap) [length](/docs/reference/layout/length/),[justify:](#parameters-justify) [bool](/docs/reference/foundations/bool/),

) -> [content](/docs/reference/foundations/content/)

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to repeat.

### `gap` [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The gap between each instance of the body.

Default: `0pt`

### `justify` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether to increase the gap between instances to completely fill the
available space.

Default: `true`

[![←](/assets/icons/16-chevron-right.svg)

Relative LengthPrevious page](/docs/reference/layout/relative/) [![→](/assets/icons/16-chevron-right.svg)

RotateNext page](/docs/reference/layout/rotate/)