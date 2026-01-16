# padElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/layout/pad/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Padding](/docs/reference/layout/pad/)

# `pad`Element Question mark Element functions can be customized with `set` and `show` rules.

Adds spacing around content.

The spacing can be specified for each side individually, or for all sides at
once by specifying a positional argument.

## Example

```typst
#set align(center)

#pad(x: 16pt, image("typing.jpg"))
_Typing speeds can be
 measured in words per minute._
```

![Preview](/assets/docs/YnvzY3ls2HrcPgokDMxVqwAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

pad(

[left:](#parameters-left) [relative](/docs/reference/layout/relative/),[top:](#parameters-top) [relative](/docs/reference/layout/relative/),[right:](#parameters-right) [relative](/docs/reference/layout/relative/),[bottom:](#parameters-bottom) [relative](/docs/reference/layout/relative/),[x:](#parameters-x) [relative](/docs/reference/layout/relative/),[y:](#parameters-y) [relative](/docs/reference/layout/relative/),[rest:](#parameters-rest) [relative](/docs/reference/layout/relative/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `left` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The padding at the left side.

Default: `0% + 0pt`

### `top` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The padding at the top side.

Default: `0% + 0pt`

### `right` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The padding at the right side.

Default: `0% + 0pt`

### `bottom` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The padding at the bottom side.

Default: `0% + 0pt`

### `x` [relative](/docs/reference/layout/relative/)

A shorthand to set `left` and `right` to the same value.

Default: `0% + 0pt`

### `y` [relative](/docs/reference/layout/relative/)

A shorthand to set `top` and `bottom` to the same value.

Default: `0% + 0pt`

### `rest` [relative](/docs/reference/layout/relative/)

A shorthand to set all four sides to the same value.

Default: `0% + 0pt`

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to pad at the sides.

[![←](/assets/icons/16-chevron-right.svg)

MovePrevious page](/docs/reference/layout/move/) [![→](/assets/icons/16-chevron-right.svg)

PageNext page](/docs/reference/layout/page/)