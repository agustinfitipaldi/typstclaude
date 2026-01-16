# rectElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/visualize/rect/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Visualize](/docs/reference/visualize/)
- ![](/assets/icons/16-chevron-right.svg)
- [Rectangle](/docs/reference/visualize/rect/)

# `rect`Element Question mark Element functions can be customized with `set` and `show` rules.

A rectangle with optional content.

## Example

```typst
// Without content.
#rect(width: 35%, height: 30pt)

// With content.
#rect[
  Automatically sized \
  to fit the content.
]
```

![Preview](/assets/docs/uMLkrKs8AmOe9L-qU4CYKgAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

rect(

[width:](#parameters-width) [auto](/docs/reference/foundations/auto/)[relative](/docs/reference/layout/relative/),[height:](#parameters-height) [auto](/docs/reference/foundations/auto/)[relative](/docs/reference/layout/relative/)[fraction](/docs/reference/layout/fraction/),[fill:](#parameters-fill) [none](/docs/reference/foundations/none/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[tiling](/docs/reference/visualize/tiling/),[stroke:](#parameters-stroke) [none](/docs/reference/foundations/none/)[auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[stroke](/docs/reference/visualize/stroke/)[tiling](/docs/reference/visualize/tiling/)[dictionary](/docs/reference/foundations/dictionary/),[radius:](#parameters-radius) [relative](/docs/reference/layout/relative/)[dictionary](/docs/reference/foundations/dictionary/),[inset:](#parameters-inset) [relative](/docs/reference/layout/relative/)[dictionary](/docs/reference/foundations/dictionary/),[outset:](#parameters-outset) [relative](/docs/reference/layout/relative/)[dictionary](/docs/reference/foundations/dictionary/),[none](/docs/reference/foundations/none/)[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `width` [auto](/docs/reference/foundations/auto/) or [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The rectangle's width, relative to its parent container.

Default: `auto`

### `height` [auto](/docs/reference/foundations/auto/) or [relative](/docs/reference/layout/relative/) or [fraction](/docs/reference/layout/fraction/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The rectangle's height, relative to its parent container.

Default: `auto`

### `fill` [none](/docs/reference/foundations/none/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [tiling](/docs/reference/visualize/tiling/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How to fill the rectangle.

When setting a fill, the default stroke disappears. To create a
rectangle with both fill and stroke, you have to configure both.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#rect(fill: blue)
```

![Preview](/assets/docs/Xp0gewyTPs1ard61igAjJAAAAAAAAAAA.png)

Default: `none`

### `stroke` [none](/docs/reference/foundations/none/) or [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [stroke](/docs/reference/visualize/stroke/) or [tiling](/docs/reference/visualize/tiling/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How to stroke the rectangle. This can be:

- `none` to disable stroking
- `auto` for a stroke of `1pt + black` if and only if no fill is
  given.
- Any kind of [stroke](/docs/reference/visualize/stroke/ "stroke")
- A dictionary describing the stroke for each side individually. The
  dictionary can contain the following keys in order of precedence:

  - `top`: The top stroke.
  - `right`: The right stroke.
  - `bottom`: The bottom stroke.
  - `left`: The left stroke.
  - `x`: The horizontal stroke.
  - `y`: The vertical stroke.
  - `rest`: The stroke on all sides except those for which the
    dictionary explicitly sets a size.

  All keys are optional; omitted keys will use their previously set
  value, or the default stroke if never set.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#stack(
  dir: ltr,
  spacing: 1fr,
  rect(stroke: red),
  rect(stroke: 2pt),
  rect(stroke: 2pt + red),
)
```

![Preview](/assets/docs/RNPJxaHVa6js_P-8fJFExAAAAAAAAAAA.png)

Default: `auto`

### `radius` [relative](/docs/reference/layout/relative/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How much to round the rectangle's corners, relative to the minimum of
the width and height divided by two. This can be:

- A relative length for a uniform corner radius.
- A dictionary: With a dictionary, the stroke for each side can be set
  individually. The dictionary can contain the following keys in order
  of precedence:

  - `top-left`: The top-left corner radius.
  - `top-right`: The top-right corner radius.
  - `bottom-right`: The bottom-right corner radius.
  - `bottom-left`: The bottom-left corner radius.
  - `left`: The top-left and bottom-left corner radii.
  - `top`: The top-left and top-right corner radii.
  - `right`: The top-right and bottom-right corner radii.
  - `bottom`: The bottom-left and bottom-right corner radii.
  - `rest`: The radii for all corners except those for which the
    dictionary explicitly sets a size.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set rect(stroke: 4pt)
#rect(
  radius: (
    left: 5pt,
    top-right: 20pt,
    bottom-right: 10pt,
  ),
  stroke: (
    left: red,
    top: yellow,
    right: green,
    bottom: blue,
  ),
)
```

![Preview](/assets/docs/P93tDNSSrvmdfXv2L7MmYQAAAAAAAAAA.png)

Default: `(:)`

### `inset` [relative](/docs/reference/layout/relative/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How much to pad the rectangle's content.
See the [box's documentation](/docs/reference/layout/box/#parameters-inset) for more details.

Default: `0% + 5pt`

### `outset` [relative](/docs/reference/layout/relative/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How much to expand the rectangle's size without affecting the layout.
See the [box's documentation](/docs/reference/layout/box/#parameters-outset) for more details.

Default: `(:)`

### `body` [none](/docs/reference/foundations/none/) or [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The content to place into the rectangle.

When this is omitted, the rectangle takes on a default size of at most
`45pt` by `30pt`.

Default: `none`

[![←](/assets/icons/16-chevron-right.svg)

PolygonPrevious page](/docs/reference/visualize/polygon/) [![→](/assets/icons/16-chevron-right.svg)

SquareNext page](/docs/reference/visualize/square/)