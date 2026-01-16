# underlineElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/text/underline/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Text](/docs/reference/text/)
- ![](/assets/icons/16-chevron-right.svg)
- [Underline](/docs/reference/text/underline/)

# `underline`Element Question mark Element functions can be customized with `set` and `show` rules.

Underlines text.

## Example

```
This is #underline[important].
```

![Preview](/assets/docs/xV-Fy8zwdVIfyHyOpdk_9AAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

underline(

[stroke:](#parameters-stroke) [auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[stroke](/docs/reference/visualize/stroke/)[tiling](/docs/reference/visualize/tiling/)[dictionary](/docs/reference/foundations/dictionary/),[offset:](#parameters-offset) [auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/),[extent:](#parameters-extent) [length](/docs/reference/layout/length/),[evade:](#parameters-evade) [bool](/docs/reference/foundations/bool/),[background:](#parameters-background) [bool](/docs/reference/foundations/bool/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `stroke` [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [stroke](/docs/reference/visualize/stroke/) or [tiling](/docs/reference/visualize/tiling/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How to [stroke](/docs/reference/visualize/stroke/ "stroke") the line.

If set to `auto`, takes on the text's color and a thickness defined in
the current font.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
Take #underline(
  stroke: 1.5pt + red,
  offset: 2pt,
  [care],
)
```

![Preview](/assets/docs/tbLKc9iYaghdhC9NcJaJOQAAAAAAAAAA.png)

Default: `auto`

### `offset` [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The position of the line relative to the baseline, read from the font
tables if `auto`.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#underline(offset: 5pt)[
  The Tale Of A Faraway Line I
]
```

![Preview](/assets/docs/p2tUWXcYq-E_ZbDtwzCDrAAAAAAAAAAA.png)

Default: `auto`

### `extent` [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The amount by which to extend the line beyond (or within if negative)
the content.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#align(center,
  underline(extent: 2pt)[Chapter 1]
)
```

![Preview](/assets/docs/tbT2BOLPtcXW-alQPb8q6wAAAAAAAAAA.png)

Default: `0pt`

### `evade` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether the line skips sections in which it would collide with the
glyphs.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
This #underline(evade: true)[is great].
This #underline(evade: false)[is less great].
```

![Preview](/assets/docs/PaJc2qUpoh1s97E6NZYz0QAAAAAAAAAA.png)

Default: `true`

### `background` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether the line is placed behind the content it underlines.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set underline(stroke: (thickness: 1em, paint: maroon, cap: "round"))
#underline(background: true)[This is stylized.] \
#underline(background: false)[This is partially hidden.]
```

![Preview](/assets/docs/W98M7AlnFoSVnlt9g5bIsAAAAAAAAAAA.png)

Default: `false`

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to underline.

[![←](/assets/icons/16-chevron-right.svg)

TextPrevious page](/docs/reference/text/text/) [![→](/assets/icons/16-chevron-right.svg)

UppercaseNext page](/docs/reference/text/upper/)