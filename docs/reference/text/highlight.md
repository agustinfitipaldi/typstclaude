# highlightElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/text/highlight/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Text](/docs/reference/text/)
- ![](/assets/icons/16-chevron-right.svg)
- [Highlight](/docs/reference/text/highlight/)

# `highlight`Element Question mark Element functions can be customized with `set` and `show` rules.

Highlights text with a background color.

## Example

```
This is #highlight[important].
```

![Preview](/assets/docs/QtpA6ir9UWFHeXPRr2gD9AAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

highlight(

[fill:](#parameters-fill) [none](/docs/reference/foundations/none/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[tiling](/docs/reference/visualize/tiling/),[stroke:](#parameters-stroke) [none](/docs/reference/foundations/none/)[length](/docs/reference/layout/length/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[stroke](/docs/reference/visualize/stroke/)[tiling](/docs/reference/visualize/tiling/)[dictionary](/docs/reference/foundations/dictionary/),[top-edge:](#parameters-top-edge) [length](/docs/reference/layout/length/)[str](/docs/reference/foundations/str/),[bottom-edge:](#parameters-bottom-edge) [length](/docs/reference/layout/length/)[str](/docs/reference/foundations/str/),[extent:](#parameters-extent) [length](/docs/reference/layout/length/),[radius:](#parameters-radius) [relative](/docs/reference/layout/relative/)[dictionary](/docs/reference/foundations/dictionary/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `fill` [none](/docs/reference/foundations/none/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [tiling](/docs/reference/visualize/tiling/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The color to highlight the text with.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
This is #highlight(
  fill: blue
)[highlighted with blue].
```

![Preview](/assets/docs/oW--DyYpfs3nP_lZOIl65gAAAAAAAAAA.png)

Default: `rgb("#fffd11a1")`

### `stroke` [none](/docs/reference/foundations/none/) or [length](/docs/reference/layout/length/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [stroke](/docs/reference/visualize/stroke/) or [tiling](/docs/reference/visualize/tiling/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The highlight's border color. See the
[rectangle's documentation](/docs/reference/visualize/rect/#parameters-stroke) for more details.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
This is a #highlight(
  stroke: fuchsia
)[stroked highlighting].
```

![Preview](/assets/docs/VdZlBJnkRgdzR_4L65zKzQAAAAAAAAAA.png)

Default: `(:)`

### `top-edge` [length](/docs/reference/layout/length/) or [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The top end of the background rectangle.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set highlight(top-edge: "ascender")
#highlight[a] #highlight[aib]

#set highlight(top-edge: "x-height")
#highlight[a] #highlight[aib]
```

![Preview](/assets/docs/33w6KWiqvSrMq41iE5ob_QAAAAAAAAAA.png)

| Variant | Details |
| --- | --- |
| `"ascender"` | The font's ascender, which typically exceeds the height of all glyphs. |
| `"cap-height"` | The approximate height of uppercase letters. |
| `"x-height"` | The approximate height of non-ascending lowercase letters. |
| `"baseline"` | The baseline on which the letters rest. |
| `"bounds"` | The top edge of the glyph's bounding box. |

Default: `"ascender"`

### `bottom-edge` [length](/docs/reference/layout/length/) or [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The bottom end of the background rectangle.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set highlight(bottom-edge: "descender")
#highlight[a] #highlight[ap]

#set highlight(bottom-edge: "baseline")
#highlight[a] #highlight[ap]
```

![Preview](/assets/docs/tZTem6RAQXJ8OFzIrL6AnAAAAAAAAAAA.png)

| Variant | Details |
| --- | --- |
| `"baseline"` | The baseline on which the letters rest. |
| `"descender"` | The font's descender, which typically exceeds the depth of all glyphs. |
| `"bounds"` | The bottom edge of the glyph's bounding box. |

Default: `"descender"`

### `extent` [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The amount by which to extend the background to the sides beyond
(or within if negative) the content.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
A long #highlight(extent: 4pt)[background].
```

![Preview](/assets/docs/L2wf2ozgvgMg2iI3FR9LdQAAAAAAAAAA.png)

Default: `0pt`

### `radius` [relative](/docs/reference/layout/relative/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How much to round the highlight's corners. See the
[rectangle's documentation](/docs/reference/visualize/rect/#parameters-radius) for more details.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
Listen #highlight(
  radius: 5pt, extent: 2pt
)[carefully], it will be on the test.
```

![Preview](/assets/docs/MdD0cA7uGh7p2z32380_kAAAAAAAAAAA.png)

Default: `(:)`

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content that should be highlighted.

[![←](/assets/icons/16-chevron-right.svg)

TextPrevious page](/docs/reference/text/) [![→](/assets/icons/16-chevron-right.svg)

Line BreakNext page](/docs/reference/text/linebreak/)