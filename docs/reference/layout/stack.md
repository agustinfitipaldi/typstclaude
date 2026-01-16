# stackElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/layout/stack/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Stack](/docs/reference/layout/stack/)

# `stack`Element Question mark Element functions can be customized with `set` and `show` rules.

Arranges content and spacing horizontally or vertically.

The stack places a list of items along an axis, with optional spacing
between each item.

## Example

```typst
#stack(
  dir: ttb,
  rect(width: 40pt),
  rect(width: 120pt),
  rect(width: 90pt),
)
```

![Preview](/assets/docs/rblc_gO4o5qSEPJtXD1qPgAAAAAAAAAA.png)

## Accessibility

Stacks do not carry any special semantics. The contents of the stack are
read by Assistive Technology (AT) in the order in which they have been
passed to this function.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

stack(

[dir:](#parameters-dir) [direction](/docs/reference/layout/direction/),[spacing:](#parameters-spacing) [none](/docs/reference/foundations/none/)[relative](/docs/reference/layout/relative/)[fraction](/docs/reference/layout/fraction/),[..](#parameters-children)[relative](/docs/reference/layout/relative/)[fraction](/docs/reference/layout/fraction/)[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `dir` [direction](/docs/reference/layout/direction/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The direction along which the items are stacked. Possible values are:

- `ltr`: Left to right.
- `rtl`: Right to left.
- `ttb`: Top to bottom.
- `btt`: Bottom to top.

You can use the `start` and `end` methods to obtain the initial and
final points (respectively) of a direction, as `alignment`. You can also
use the `axis` method to determine whether a direction is
`"horizontal"` or `"vertical"`. The `inv` method returns a
direction's inverse direction.

For example, `ttb.start()` is `top`, `ttb.end()` is `bottom`,
`ttb.axis()` is `"vertical"` and `ttb.inv()` is equal to `btt`.

Default: `ttb`

### `spacing` [none](/docs/reference/foundations/none/) or [relative](/docs/reference/layout/relative/) or [fraction](/docs/reference/layout/fraction/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Spacing to insert between items where no explicit spacing was provided.

Default: `none`

### `children` [relative](/docs/reference/layout/relative/) or [fraction](/docs/reference/layout/fraction/) or [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The children to stack along the axis.

[![←](/assets/icons/16-chevron-right.svg)

Spacing (V)Previous page](/docs/reference/layout/v/) [![→](/assets/icons/16-chevron-right.svg)

VisualizeNext page](/docs/reference/visualize/)