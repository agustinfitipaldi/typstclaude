# curveElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/visualize/curve/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Visualize](/docs/reference/visualize/)
- ![](/assets/icons/16-chevron-right.svg)
- [Curve](/docs/reference/visualize/curve/)

# `curve`Element Question mark Element functions can be customized with `set` and `show` rules.

A curve consisting of movements, lines, and Bézier segments.

At any point in time, there is a conceptual pen or cursor.

- Move elements move the cursor without drawing.
- Line/Quadratic/Cubic elements draw a segment from the cursor to a new
  position, potentially with control point for a Bézier curve.
- Close elements draw a straight or smooth line back to the start of the
  curve or the latest preceding move segment.

For layout purposes, the bounding box of the curve is a tight rectangle
containing all segments as well as the point `(0pt, 0pt)`.

Positions may be specified absolutely (i.e. relatively to `(0pt, 0pt)`),
or relative to the current pen/cursor position, that is, the position where
the previous segment ended.

Bézier curve control points can be skipped by passing `none` or
automatically mirrored from the preceding segment by passing `auto`.

## Example

```typst
#curve(
  fill: blue.lighten(80%),
  stroke: blue,
  curve.move((0pt, 50pt)),
  curve.line((100pt, 50pt)),
  curve.cubic(none, (90pt, 0pt), (50pt, 0pt)),
  curve.close(),
)
```

![Preview](/assets/docs/9uihNAu_dEPJt6RrdXvspAAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

curve(

[fill:](#parameters-fill) [none](/docs/reference/foundations/none/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[tiling](/docs/reference/visualize/tiling/),[fill-rule:](#parameters-fill-rule) [str](/docs/reference/foundations/str/),[stroke:](#parameters-stroke) [none](/docs/reference/foundations/none/)[auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[stroke](/docs/reference/visualize/stroke/)[tiling](/docs/reference/visualize/tiling/)[dictionary](/docs/reference/foundations/dictionary/),[..](#parameters-components)[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `fill` [none](/docs/reference/foundations/none/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [tiling](/docs/reference/visualize/tiling/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How to fill the curve.

When setting a fill, the default stroke disappears. To create a curve
with both fill and stroke, you have to configure both.

Default: `none`

### `fill-rule` [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The drawing rule used to fill the curve.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
// We use `.with` to get a new
// function that has the common
// arguments pre-applied.
#let star = curve.with(
  fill: red,
  curve.move((25pt, 0pt)),
  curve.line((10pt, 50pt)),
  curve.line((50pt, 20pt)),
  curve.line((0pt, 20pt)),
  curve.line((40pt, 50pt)),
  curve.close(),
)

#star(fill-rule: "non-zero")
#star(fill-rule: "even-odd")
```

![Preview](/assets/docs/MtCGlNFyX7T8BEspWRN1OwAAAAAAAAAA.png)

| Variant | Details |
| --- | --- |
| `"non-zero"` | Specifies that "inside" is computed by a non-zero sum of signed edge crossings. |
| `"even-odd"` | Specifies that "inside" is computed by an odd number of edge crossings. |

Default: `"non-zero"`

### `stroke` [none](/docs/reference/foundations/none/) or [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [stroke](/docs/reference/visualize/stroke/) or [tiling](/docs/reference/visualize/tiling/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How to [stroke](/docs/reference/visualize/stroke/ "stroke") the curve.

Can be set to `none` to disable the stroke or to `auto` for a
stroke of `1pt` black if and only if no fill is given.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#let down = curve.line((40pt, 40pt), relative: true)
#let up = curve.line((40pt, -40pt), relative: true)

#curve(
  stroke: 4pt + gradient.linear(red, blue),
  down, up, down, up, down,
)
```

![Preview](/assets/docs/BuYkNpXtHJIILC395drcRgAAAAAAAAAA.png)

Default: `auto`

### `components` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The components of the curve, in the form of moves, line and Bézier
segment, and closes.

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `move`Element Question mark Element functions can be customized with `set` and `show` rules.

Starts a new curve component.

If no `curve.move` element is passed, the curve will start at
`(0pt, 0pt)`.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#curve(
  fill: blue.lighten(80%),
  fill-rule: "even-odd",
  stroke: blue,
  curve.line((50pt, 0pt)),
  curve.line((50pt, 50pt)),
  curve.line((0pt, 50pt)),
  curve.close(),
  curve.move((10pt, 10pt)),
  curve.line((40pt, 10pt)),
  curve.line((40pt, 40pt)),
  curve.line((10pt, 40pt)),
  curve.close(),
)
```

![Preview](/assets/docs/GVXUaPSBZ9aLOPaKKVQbFgAAAAAAAAAA.png)

curve.move(

[array](/docs/reference/foundations/array/),[relative:](#definitions-move-relative) [bool](/docs/reference/foundations/bool/),

) -> [content](/docs/reference/foundations/content/)

#### `start` [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names.

The starting point for the new component.

#### `relative` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether the coordinates are relative to the previous point.

Default: `false`

### `line`Element Question mark Element functions can be customized with `set` and `show` rules.

Adds a straight line from the current point to a following one.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#curve(
  stroke: blue,
  curve.line((50pt, 0pt)),
  curve.line((50pt, 50pt)),
  curve.line((100pt, 50pt)),
  curve.line((100pt, 0pt)),
  curve.line((150pt, 0pt)),
)
```

![Preview](/assets/docs/h2sK3vEc4wLpSNDc-y8obgAAAAAAAAAA.png)

curve.line(

[array](/docs/reference/foundations/array/),[relative:](#definitions-line-relative) [bool](/docs/reference/foundations/bool/),

) -> [content](/docs/reference/foundations/content/)

#### `end` [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names.

The point at which the line shall end.

#### `relative` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether the coordinates are relative to the previous point.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#curve(
  stroke: blue,
  curve.line((50pt, 0pt), relative: true),
  curve.line((0pt, 50pt), relative: true),
  curve.line((50pt, 0pt), relative: true),
  curve.line((0pt, -50pt), relative: true),
  curve.line((50pt, 0pt), relative: true),
)
```

![Preview](/assets/docs/odTIFGiUZ-tP_5V9hZ1PjwAAAAAAAAAA.png)

Default: `false`

### `quad`Element Question mark Element functions can be customized with `set` and `show` rules.

Adds a quadratic Bézier curve segment from the last point to `end`, using
`control` as the control point.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
// Function to illustrate where the control point is.
#let mark((x, y)) = place(
  dx: x - 1pt, dy: y - 1pt,
  circle(fill: aqua, radius: 2pt),
)

#mark((20pt, 20pt))

#curve(
  stroke: blue,
  curve.move((0pt, 100pt)),
  curve.quad((20pt, 20pt), (100pt, 0pt)),
)
```

![Preview](/assets/docs/ckpS4uyWfB2AMsqGoS9IqQAAAAAAAAAA.png)

curve.quad(

[none](/docs/reference/foundations/none/)[auto](/docs/reference/foundations/auto/)[array](/docs/reference/foundations/array/),[array](/docs/reference/foundations/array/),[relative:](#definitions-quad-relative) [bool](/docs/reference/foundations/bool/),

) -> [content](/docs/reference/foundations/content/)

#### `control` [none](/docs/reference/foundations/none/) or [auto](/docs/reference/foundations/auto/) or [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names.

The control point of the quadratic Bézier curve.

- If `auto` and this segment follows another quadratic Bézier curve,
  the previous control point will be mirrored.
- If `none`, the control point defaults to `end`, and the curve will
  be a straight line.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#curve(
  stroke: 2pt,
  curve.quad((20pt, 40pt), (40pt, 40pt), relative: true),
  curve.quad(auto, (40pt, -40pt), relative: true),
)
```

![Preview](/assets/docs/1H_x4JMwpUyQc8waz51PfQAAAAAAAAAA.png)

#### `end` [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names.

The point at which the segment shall end.

#### `relative` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether the `control` and `end` coordinates are relative to the previous
point.

Default: `false`

### `cubic`Element Question mark Element functions can be customized with `set` and `show` rules.

Adds a cubic Bézier curve segment from the last point to `end`, using
`control-start` and `control-end` as the control points.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
// Function to illustrate where the control points are.
#let handle(start, end) = place(
  line(stroke: red, start: start, end: end)
)

#handle((0pt, 80pt), (10pt, 20pt))
#handle((90pt, 60pt), (100pt, 0pt))

#curve(
  stroke: blue,
  curve.move((0pt, 80pt)),
  curve.cubic((10pt, 20pt), (90pt, 60pt), (100pt, 0pt)),
)
```

![Preview](/assets/docs/elkayc3A9R2TuqA50KBBIgAAAAAAAAAA.png)

curve.cubic(

[none](/docs/reference/foundations/none/)[auto](/docs/reference/foundations/auto/)[array](/docs/reference/foundations/array/),[none](/docs/reference/foundations/none/)[array](/docs/reference/foundations/array/),[array](/docs/reference/foundations/array/),[relative:](#definitions-cubic-relative) [bool](/docs/reference/foundations/bool/),

) -> [content](/docs/reference/foundations/content/)

#### `control-start` [none](/docs/reference/foundations/none/) or [auto](/docs/reference/foundations/auto/) or [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names.

The control point going out from the start of the curve segment.

- If `auto` and this element follows another `curve.cubic` element,
  the last control point will be mirrored. In SVG terms, this makes
  `curve.cubic` behave like the `S` operator instead of the `C` operator.
- If `none`, the curve has no first control point, or equivalently,
  the control point defaults to the curve's starting point.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#curve(
  stroke: blue,
  curve.move((0pt, 50pt)),
  // - No start control point
  // - End control point at `(20pt, 0pt)`
  // - End point at `(50pt, 0pt)`
  curve.cubic(none, (20pt, 0pt), (50pt, 0pt)),
  // - No start control point
  // - No end control point
  // - End point at `(50pt, 0pt)`
  curve.cubic(none, none, (100pt, 50pt)),
)

#curve(
  stroke: blue,
  curve.move((0pt, 50pt)),
  curve.cubic(none, (20pt, 0pt), (50pt, 0pt)),
  // Passing `auto` instead of `none` means the start control point
  // mirrors the end control point of the previous curve. Mirror of
  // `(20pt, 0pt)` w.r.t `(50pt, 0pt)` is `(80pt, 0pt)`.
  curve.cubic(auto, none, (100pt, 50pt)),
)

#curve(
  stroke: blue,
  curve.move((0pt, 50pt)),
  curve.cubic(none, (20pt, 0pt), (50pt, 0pt)),
  // `(80pt, 0pt)` is the same as `auto` in this case.
  curve.cubic((80pt, 0pt), none, (100pt, 50pt)),
)
```

![Preview](/assets/docs/rD-0pSdPBxWpH9Nie4wy3QAAAAAAAAAA.png)

#### `control-end` [none](/docs/reference/foundations/none/) or [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names.

The control point going into the end point of the curve segment.

If set to `none`, the curve has no end control point, or equivalently,
the control point defaults to the curve's end point.

#### `end` [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names.

The point at which the curve segment shall end.

#### `relative` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether the `control-start`, `control-end`, and `end` coordinates are
relative to the previous point.

Default: `false`

### `close`Element Question mark Element functions can be customized with `set` and `show` rules.

Closes the curve by adding a segment from the last point to the start of the
curve (or the last preceding `curve.move` point).

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
// We define a function to show the same shape with
// both closing modes.
#let shape(mode: "smooth") = curve(
  fill: blue.lighten(80%),
  stroke: blue,
  curve.move((0pt, 50pt)),
  curve.line((100pt, 50pt)),
  curve.cubic(auto, (90pt, 0pt), (50pt, 0pt)),
  curve.close(mode: mode),
)

#shape(mode: "smooth")
#shape(mode: "straight")
```

![Preview](/assets/docs/APT5DqIW1xBK6IZvS6enJgAAAAAAAAAA.png)

curve.close(

[mode:](#definitions-close-mode) [str](/docs/reference/foundations/str/)

) -> [content](/docs/reference/foundations/content/)

#### `mode` [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How to close the curve.

| Variant | Details |
| --- | --- |
| `"smooth"` | Closes the curve with a smooth segment that takes into account the control point opposite the start point. |
| `"straight"` | Closes the curve with a straight line. |

Default: `"smooth"`

[![←](/assets/icons/16-chevron-right.svg)

ColorPrevious page](/docs/reference/visualize/color/) [![→](/assets/icons/16-chevron-right.svg)

EllipseNext page](/docs/reference/visualize/ellipse/)