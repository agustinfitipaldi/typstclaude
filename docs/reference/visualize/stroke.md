# stroke

Source: https://typst.app/docs/reference/visualize/stroke/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Visualize](/docs/reference/visualize/)
- ![](/assets/icons/16-chevron-right.svg)
- [Stroke](/docs/reference/visualize/stroke/)

# stroke

Defines how to draw a line.

A stroke has a *paint* (a solid color or gradient), a *thickness,* a line
*cap,* a line *join,* a *miter limit,* and a *dash* pattern. All of these
values are optional and have sensible defaults.

## Example

```typst
#set line(length: 100%)
#stack(
  spacing: 1em,
  line(stroke: 2pt + red),
  line(stroke: (paint: blue, thickness: 4pt, cap: "round")),
  line(stroke: (paint: blue, thickness: 1pt, dash: "dashed")),
  line(stroke: 2pt + gradient.linear(..color.map.rainbow)),
)
```

![Preview](/assets/docs/3NofubbwIllodsFawlNd8wAAAAAAAAAA.png)

## Simple strokes

You can create a simple solid stroke from a color, a thickness, or a
combination of the two. Specifically, wherever a stroke is expected you can
pass any of the following values:

- A length specifying the stroke's thickness. The color is inherited,
  defaulting to black.
- A color to use for the stroke. The thickness is inherited, defaulting to
  `1pt`.
- A stroke combined from color and thickness using the `+` operator as in
  `2pt + red`.

For full control, you can also provide a [dictionary](/docs/reference/foundations/dictionary/ "dictionary") or a `stroke` object
to any function that expects a stroke. The dictionary's keys may include any
of the parameters for the constructor function, shown below.

## Fields

On a stroke object, you can access any of the fields listed in the
constructor function. For example, `(2pt + blue).thickness` is `2pt`.
Meanwhile, `stroke(red).cap` is `auto` because it's unspecified. Fields
set to `auto` are inherited.

## Constructor Question mark If a type has a constructor, you can call it like a function to create a new value of the type.

Converts a value to a stroke or constructs a stroke with the given
parameters.

Note that in most cases you do not need to convert values to strokes in
order to use them, as they will be converted automatically. However,
this constructor can be useful to ensure a value has all the fields of a
stroke.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#let my-func(x) = {
    x = stroke(x) // Convert to a stroke
    [Stroke has thickness #x.thickness.]
}
#my-func(3pt) \
#my-func(red) \
#my-func(stroke(cap: "round", thickness: 1pt))
```

![Preview](/assets/docs/oulcXDNcpunCSxVvCPXMJQAAAAAAAAAA.png)

stroke(

[auto](/docs/reference/foundations/auto/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[tiling](/docs/reference/visualize/tiling/),[auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/),[auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/),[auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/),[none](/docs/reference/foundations/none/)[auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/)[dictionary](/docs/reference/foundations/dictionary/),[auto](/docs/reference/foundations/auto/)[float](/docs/reference/foundations/float/),

) -> [stroke](/docs/reference/visualize/stroke/)

#### `paint` [auto](/docs/reference/foundations/auto/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [tiling](/docs/reference/visualize/tiling/) Required Positional Question mark Positional parameters are specified in order, without names.

The color or gradient to use for the stroke.

If set to `auto`, the value is inherited, defaulting to `black`.

#### `thickness` [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/) Required Positional Question mark Positional parameters are specified in order, without names.

The stroke's thickness.

If set to `auto`, the value is inherited, defaulting to `1pt`.

#### `cap` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/) Required Positional Question mark Positional parameters are specified in order, without names.

How the ends of the stroke are rendered.

If set to `auto`, the value is inherited, defaulting to `"butt"`.

| Variant | Details |
| --- | --- |
| `"butt"` | Square stroke cap with the edge at the stroke's end point. |
| `"round"` | Circular stroke cap centered at the stroke's end point. |
| `"square"` | Square stroke cap centered at the stroke's end point. |

#### `join` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/) Required Positional Question mark Positional parameters are specified in order, without names.

How sharp turns are rendered.

If set to `auto`, the value is inherited, defaulting to `"miter"`.

| Variant | Details |
| --- | --- |
| `"miter"` | Segments are joined with sharp edges. Sharp bends exceeding the miter limit are bevelled instead. |
| `"round"` | Segments are joined with circular corners. |
| `"bevel"` | Segments are joined with a bevel (a straight edge connecting the butts of the joined segments). |

#### `dash` [none](/docs/reference/foundations/none/) or [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/) or [dictionary](/docs/reference/foundations/dictionary/) Required Positional Question mark Positional parameters are specified in order, without names.

The dash pattern to use. This can be:

- One of the predefined patterns:
  - `"solid"` or `none`
  - `"dotted"`
  - `"densely-dotted"`
  - `"loosely-dotted"`
  - `"dashed"`
  - `"densely-dashed"`
  - `"loosely-dashed"`
  - `"dash-dotted"`
  - `"densely-dash-dotted"`
  - `"loosely-dash-dotted"`
- An [array](/docs/reference/foundations/array/ "array") with alternating lengths for dashes and gaps. You can
  also use the string `"dot"` for a length equal to the line
  thickness.
- A [dictionary](/docs/reference/foundations/dictionary/ "dictionary") with the keys `array` (same as the array above),
  and `phase` (of type [length](/docs/reference/layout/length/ "length")), which defines where in the pattern
  to start drawing.

If set to `auto`, the value is inherited, defaulting to `none`.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set line(length: 100%, stroke: 2pt)
#stack(
  spacing: 1em,
  line(stroke: (dash: "dashed")),
  line(stroke: (dash: (10pt, 5pt, "dot", 5pt))),
  line(stroke: (dash: (array: (10pt, 5pt, "dot", 5pt), phase: 10pt))),
)
```

![Preview](/assets/docs/P38gFluKZcw64WdZR85nHgAAAAAAAAAA.png)

   ![](/assets/icons/16-chevron-right.svg) View options 

| Variant | Details |
| --- | --- |
| `"solid"` |  |
| `"dotted"` |  |
| `"densely-dotted"` |  |
| `"loosely-dotted"` |  |
| `"dashed"` |  |
| `"densely-dashed"` |  |
| `"loosely-dashed"` |  |
| `"dash-dotted"` |  |
| `"densely-dash-dotted"` |  |
| `"loosely-dash-dotted"` |  |

#### `miter-limit` [auto](/docs/reference/foundations/auto/) or [float](/docs/reference/foundations/float/) Required Positional Question mark Positional parameters are specified in order, without names.

Number at which protruding sharp bends are rendered with a bevel
instead or a miter join. The higher the number, the sharper an angle
can be before it is bevelled. Only applicable if `join` is
`"miter"`.

Specifically, the miter limit is the maximum ratio between the
corner's protrusion length and the stroke's thickness.

If set to `auto`, the value is inherited, defaulting to `4.0`.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#let items = (
  curve.move((15pt, 0pt)),
  curve.line((0pt, 30pt)),
  curve.line((30pt, 30pt)),
  curve.line((10pt, 20pt)),
)

#set curve(stroke: 6pt + blue)
#stack(
  dir: ltr,
  spacing: 1cm,
  curve(stroke: (miter-limit: 1), ..items),
  curve(stroke: (miter-limit: 4), ..items),
  curve(stroke: (miter-limit: 5), ..items),
)
```

![Preview](/assets/docs/M4GKlDFgR3DSEV3Y5EXCaQAAAAAAAAAA.png)

[![←](/assets/icons/16-chevron-right.svg)

SquarePrevious page](/docs/reference/visualize/square/) [![→](/assets/icons/16-chevron-right.svg)

TilingNext page](/docs/reference/visualize/tiling/)