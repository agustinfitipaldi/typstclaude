# ellipseElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/visualize/ellipse/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Visualize](/docs/reference/visualize/)
- ![](/assets/icons/16-chevron-right.svg)
- [Ellipse](/docs/reference/visualize/ellipse/)

# `ellipse`Element Question mark Element functions can be customized with `set` and `show` rules.

An ellipse with optional content.

## Example

```typst
// Without content.
#ellipse(width: 35%, height: 30pt)

// With content.
#ellipse[
  #set align(center)
  Automatically sized \
  to fit the content.
]
```

![Preview](/assets/docs/u35LFJMn0LDLxUBqOdjmvgAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

ellipse(

[width:](#parameters-width) [auto](/docs/reference/foundations/auto/)[relative](/docs/reference/layout/relative/),[height:](#parameters-height) [auto](/docs/reference/foundations/auto/)[relative](/docs/reference/layout/relative/)[fraction](/docs/reference/layout/fraction/),[fill:](#parameters-fill) [none](/docs/reference/foundations/none/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[tiling](/docs/reference/visualize/tiling/),[stroke:](#parameters-stroke) [none](/docs/reference/foundations/none/)[auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[stroke](/docs/reference/visualize/stroke/)[tiling](/docs/reference/visualize/tiling/)[dictionary](/docs/reference/foundations/dictionary/),[inset:](#parameters-inset) [relative](/docs/reference/layout/relative/)[dictionary](/docs/reference/foundations/dictionary/),[outset:](#parameters-outset) [relative](/docs/reference/layout/relative/)[dictionary](/docs/reference/foundations/dictionary/),[none](/docs/reference/foundations/none/)[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `width` [auto](/docs/reference/foundations/auto/) or [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The ellipse's width, relative to its parent container.

Default: `auto`

### `height` [auto](/docs/reference/foundations/auto/) or [relative](/docs/reference/layout/relative/) or [fraction](/docs/reference/layout/fraction/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The ellipse's height, relative to its parent container.

Default: `auto`

### `fill` [none](/docs/reference/foundations/none/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [tiling](/docs/reference/visualize/tiling/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How to fill the ellipse. See the [rectangle's documentation](/docs/reference/visualize/rect/#parameters-fill)
for more details.

Default: `none`

### `stroke` [none](/docs/reference/foundations/none/) or [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [stroke](/docs/reference/visualize/stroke/) or [tiling](/docs/reference/visualize/tiling/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How to stroke the ellipse. See the
[rectangle's documentation](/docs/reference/visualize/rect/#parameters-stroke) for more details.

Default: `auto`

### `inset` [relative](/docs/reference/layout/relative/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How much to pad the ellipse's content. See the
[box's documentation](/docs/reference/layout/box/#parameters-inset) for more details.

Default: `0% + 5pt`

### `outset` [relative](/docs/reference/layout/relative/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How much to expand the ellipse's size without affecting the layout. See
the [box's documentation](/docs/reference/layout/box/#parameters-outset) for more details.

Default: `(:)`

### `body` [none](/docs/reference/foundations/none/) or [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The content to place into the ellipse.

When this is omitted, the ellipse takes on a default size of at most
`45pt` by `30pt`.

Default: `none`

[![←](/assets/icons/16-chevron-right.svg)

CurvePrevious page](/docs/reference/visualize/curve/) [![→](/assets/icons/16-chevron-right.svg)

GradientNext page](/docs/reference/visualize/gradient/)