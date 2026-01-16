# boxElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/layout/box/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Box](/docs/reference/layout/box/)

# `box`Element Question mark Element functions can be customized with `set` and `show` rules.

An inline-level container that sizes content.

All elements except inline math, text, and boxes are block-level and cannot
occur inside of a [paragraph](/docs/reference/model/par/). The box function can be used to
integrate such elements into a paragraph. Boxes take the size of their
contents by default but can also be sized explicitly.

## Example

```typst
Refer to the docs
#box(
  height: 9pt,
  image("docs.svg")
)
for more information.
```

![Preview](/assets/docs/eB9NAzu2xk-O1miffozwKQAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

box(

[width:](#parameters-width) [auto](/docs/reference/foundations/auto/)[relative](/docs/reference/layout/relative/)[fraction](/docs/reference/layout/fraction/),[height:](#parameters-height) [auto](/docs/reference/foundations/auto/)[relative](/docs/reference/layout/relative/),[baseline:](#parameters-baseline) [relative](/docs/reference/layout/relative/),[fill:](#parameters-fill) [none](/docs/reference/foundations/none/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[tiling](/docs/reference/visualize/tiling/),[stroke:](#parameters-stroke) [none](/docs/reference/foundations/none/)[length](/docs/reference/layout/length/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[stroke](/docs/reference/visualize/stroke/)[tiling](/docs/reference/visualize/tiling/)[dictionary](/docs/reference/foundations/dictionary/),[radius:](#parameters-radius) [relative](/docs/reference/layout/relative/)[dictionary](/docs/reference/foundations/dictionary/),[inset:](#parameters-inset) [relative](/docs/reference/layout/relative/)[dictionary](/docs/reference/foundations/dictionary/),[outset:](#parameters-outset) [relative](/docs/reference/layout/relative/)[dictionary](/docs/reference/foundations/dictionary/),[clip:](#parameters-clip) [bool](/docs/reference/foundations/bool/),[none](/docs/reference/foundations/none/)[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `width` [auto](/docs/reference/foundations/auto/) or [relative](/docs/reference/layout/relative/) or [fraction](/docs/reference/layout/fraction/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The width of the box.

Boxes can have [fractional](/docs/reference/layout/fraction/) widths, as the example below
demonstrates.

*Note:* Currently, only boxes and only their widths might be fractionally
sized within paragraphs. Support for fractionally sized images, shapes,
and more might be added in the future.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
Line in #box(width: 1fr, line(length: 100%)) between.
```

![Preview](/assets/docs/dzJroqkPcQ8j1yD6nZSE0AAAAAAAAAAA.png)

Default: `auto`

### `height` [auto](/docs/reference/foundations/auto/) or [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The height of the box.

Default: `auto`

### `baseline` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

An amount to shift the box's baseline by.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
Image: #box(baseline: 40%, image("tiger.jpg", width: 2cm)).
```

![Preview](/assets/docs/jNZmXcLZQWKojb5Yhz3uEQAAAAAAAAAA.png)

Default: `0% + 0pt`

### `fill` [none](/docs/reference/foundations/none/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [tiling](/docs/reference/visualize/tiling/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The box's background color. See the
[rectangle's documentation](/docs/reference/visualize/rect/#parameters-fill) for more details.

Default: `none`

### `stroke` [none](/docs/reference/foundations/none/) or [length](/docs/reference/layout/length/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [stroke](/docs/reference/visualize/stroke/) or [tiling](/docs/reference/visualize/tiling/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The box's border color. See the
[rectangle's documentation](/docs/reference/visualize/rect/#parameters-stroke) for more details.

Default: `(:)`

### `radius` [relative](/docs/reference/layout/relative/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How much to round the box's corners. See the
[rectangle's documentation](/docs/reference/visualize/rect/#parameters-radius) for more details.

Default: `(:)`

### `inset` [relative](/docs/reference/layout/relative/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How much to pad the box's content.

This can be a single length for all sides or a dictionary of lengths
for individual sides. When passing a dictionary, it can contain the
following keys in order of precedence: `top`, `right`, `bottom`, `left`
(controlling the respective cell sides), `x`, `y` (controlling vertical
and horizontal insets), and `rest` (covers all insets not styled by
other dictionary entries). All keys are optional; omitted keys will use
their previously set value, or the default value if never set.

[Relative lengths](/docs/reference/layout/relative/) for this parameter are relative to the box
size excluding [outset](/docs/reference/layout/box/#parameters-outset). Note that relative insets and
outsets are different from relative [widths](/docs/reference/layout/box/#parameters-width) and
[heights](/docs/reference/layout/box/#parameters-height), which are relative to the container.

*Note:* When the box contains text, its exact size depends on the
current [text edges](/docs/reference/text/text/#parameters-top-edge).

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#rect(inset: 0pt)[Tight]
```

![Preview](/assets/docs/GVDpvIL_te6KlSASD3i2EQAAAAAAAAAA.png)

Default: `(:)`

### `outset` [relative](/docs/reference/layout/relative/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How much to expand the box's size without affecting the layout.

This can be a single length for all sides or a dictionary of lengths for
individual sides. [Relative lengths](/docs/reference/layout/relative/) for this parameter are
relative to the box size excluding outset. See the documentation for
[inset](/docs/reference/layout/box/#parameters-inset) above for further details.

This is useful to prevent padding from affecting line layout. For a
generalized version of the example below, see the documentation for the
[raw text's block parameter](/docs/reference/text/raw/#parameters-block).

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
An inline
#box(
  fill: luma(235),
  inset: (x: 3pt, y: 0pt),
  outset: (y: 3pt),
  radius: 2pt,
)[rectangle].
```

![Preview](/assets/docs/68KQkm_HskMy1aDAbQWYdwAAAAAAAAAA.png)

Default: `(:)`

### `clip` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether to clip the content inside the box.

Clipping is useful when the box's content is larger than the box itself,
as any content that exceeds the box's bounds will be hidden.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#box(
  width: 50pt,
  height: 50pt,
  clip: true,
  image("tiger.jpg", width: 100pt, height: 100pt)
)
```

![Preview](/assets/docs/RAY1IirASCSdH0pM4209bwAAAAAAAAAA.png)

Default: `false`

### `body` [none](/docs/reference/foundations/none/) or [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The contents of the box.

Default: `none`

[![←](/assets/icons/16-chevron-right.svg)

BlockPrevious page](/docs/reference/layout/block/) [![→](/assets/icons/16-chevron-right.svg)

Column BreakNext page](/docs/reference/layout/colbreak/)