# pathElement  Question mark   
Element functions can be customized with set and show rules.
    Warning  the path function is deprecated, use curve instead; it will be removed in Typst null

Source: https://typst.app/docs/reference/visualize/path/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Visualize](/docs/reference/visualize/)
- ![](/assets/icons/16-chevron-right.svg)
- [Path](/docs/reference/visualize/path/)

# `path`Element Question mark Element functions can be customized with `set` and `show` rules. Warning the `path` function is deprecated, use `curve` instead; it will be removed in Typst null

A path through a list of points, connected by Bézier curves.

## Example

```typst
#path(
  fill: blue.lighten(80%),
  stroke: blue,
  closed: true,
  (0pt, 50pt),
  (100%, 50pt),
  ((50%, 0pt), (40pt, 0pt)),
)
```

![Preview](/assets/docs/fHH_90d6MEksjFQh_gCkDwAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

path(

[fill:](#parameters-fill) [none](/docs/reference/foundations/none/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[tiling](/docs/reference/visualize/tiling/),[fill-rule:](#parameters-fill-rule) [str](/docs/reference/foundations/str/),[stroke:](#parameters-stroke) [none](/docs/reference/foundations/none/)[auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[stroke](/docs/reference/visualize/stroke/)[tiling](/docs/reference/visualize/tiling/)[dictionary](/docs/reference/foundations/dictionary/),[closed:](#parameters-closed) [bool](/docs/reference/foundations/bool/),[..](#parameters-vertices)[array](/docs/reference/foundations/array/),

) -> [content](/docs/reference/foundations/content/)

### `fill` [none](/docs/reference/foundations/none/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [tiling](/docs/reference/visualize/tiling/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How to fill the path.

When setting a fill, the default stroke disappears. To create a
rectangle with both fill and stroke, you have to configure both.

Default: `none`

### `fill-rule` [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The drawing rule used to fill the path.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
// We use `.with` to get a new
// function that has the common
// arguments pre-applied.
#let star = path.with(
  fill: red,
  closed: true,
  (25pt, 0pt),
  (10pt, 50pt),
  (50pt, 20pt),
  (0pt, 20pt),
  (40pt, 50pt),
)

#star(fill-rule: "non-zero")
#star(fill-rule: "even-odd")
```

![Preview](/assets/docs/MJEOUf62l7aK0PG-Hl3HKgAAAAAAAAAA.png)

| Variant | Details |
| --- | --- |
| `"non-zero"` | Specifies that "inside" is computed by a non-zero sum of signed edge crossings. |
| `"even-odd"` | Specifies that "inside" is computed by an odd number of edge crossings. |

Default: `"non-zero"`

### `stroke` [none](/docs/reference/foundations/none/) or [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [stroke](/docs/reference/visualize/stroke/) or [tiling](/docs/reference/visualize/tiling/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How to [stroke](/docs/reference/visualize/stroke/ "stroke") the path.

Can be set to `none` to disable the stroke or to `auto` for a
stroke of `1pt` black if and only if no fill is given.

Default: `auto`

### `closed` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether to close this path with one last Bézier curve. This curve will
take into account the adjacent control points. If you want to close
with a straight line, simply add one last point that's the same as the
start point.

Default: `false`

### `vertices` [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The vertices of the path.

Each vertex can be defined in 3 ways:

- A regular point, as given to the [`line`](/docs/reference/visualize/line/ "`line`") or [`polygon`](/docs/reference/visualize/polygon/ "`polygon`") function.
- An array of two points, the first being the vertex and the second
  being the control point. The control point is expressed relative to
  the vertex and is mirrored to get the second control point. The given
  control point is the one that affects the curve coming *into* this
  vertex (even for the first point). The mirrored control point affects
  the curve going out of this vertex.
- An array of three points, the first being the vertex and the next
  being the control points (control point for curves coming in and out,
  respectively).

[![←](/assets/icons/16-chevron-right.svg)

LinePrevious page](/docs/reference/visualize/line/) [![→](/assets/icons/16-chevron-right.svg)

PolygonNext page](/docs/reference/visualize/polygon/)