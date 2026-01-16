# lineElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/visualize/line/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Visualize](/docs/reference/visualize/)
- ![](/assets/icons/16-chevron-right.svg)
- [Line](/docs/reference/visualize/line/)

# `line`Element Question mark Element functions can be customized with `set` and `show` rules.

A line from one point to another.

## Example

```typst
#set page(height: 100pt)

#line(length: 100%)
#line(end: (50%, 50%))
#line(
  length: 4cm,
  stroke: 2pt + maroon,
)
```

![Preview](/assets/docs/IBdLCKW0h9kNWs6W_8DKAwAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

line(

[start:](#parameters-start) [array](/docs/reference/foundations/array/),[end:](#parameters-end) [none](/docs/reference/foundations/none/)[array](/docs/reference/foundations/array/),[length:](#parameters-length) [relative](/docs/reference/layout/relative/),[angle:](#parameters-angle) [angle](/docs/reference/layout/angle/),[stroke:](#parameters-stroke) [length](/docs/reference/layout/length/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[stroke](/docs/reference/visualize/stroke/)[tiling](/docs/reference/visualize/tiling/)[dictionary](/docs/reference/foundations/dictionary/),

) -> [content](/docs/reference/foundations/content/)

### `start` [array](/docs/reference/foundations/array/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The start point of the line.

Must be an array of exactly two relative lengths.

Default: `(0% + 0pt, 0% + 0pt)`

### `end` [none](/docs/reference/foundations/none/) or [array](/docs/reference/foundations/array/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The point where the line ends.

Default: `none`

### `length` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The line's length. This is only respected if `end` is `none`.

Default: `0% + 30pt`

### `angle` [angle](/docs/reference/layout/angle/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The angle at which the line points away from the origin. This is only
respected if `end` is `none`.

Default: `0deg`

### `stroke` [length](/docs/reference/layout/length/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [stroke](/docs/reference/visualize/stroke/) or [tiling](/docs/reference/visualize/tiling/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How to [stroke](/docs/reference/visualize/stroke/ "stroke") the line.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set line(length: 100%)
#stack(
  spacing: 1em,
  line(stroke: 2pt + red),
  line(stroke: (paint: blue, thickness: 4pt, cap: "round")),
  line(stroke: (paint: blue, thickness: 1pt, dash: "dashed")),
  line(stroke: (paint: blue, thickness: 1pt, dash: ("dot", 2pt, 4pt, 2pt))),
)
```

![Preview](/assets/docs/Shwqpl9XrWkg6A1XzBok6AAAAAAAAAAA.png)

Default: `1pt + black`

[![←](/assets/icons/16-chevron-right.svg)

ImagePrevious page](/docs/reference/visualize/image/) [![→](/assets/icons/16-chevron-right.svg)

PathNext page](/docs/reference/visualize/path/)