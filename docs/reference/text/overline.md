# overlineElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/text/overline/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Text](/docs/reference/text/)
- ![](/assets/icons/16-chevron-right.svg)
- [Overline](/docs/reference/text/overline/)

# `overline`Element Question mark Element functions can be customized with `set` and `show` rules.

Adds a line over text.

## Example

```typst
#overline[A line over text.]
```

![Preview](/assets/docs/BQmJqK4pMIkZOu3QEFxsZAAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

overline(

[stroke:](#parameters-stroke) [auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[stroke](/docs/reference/visualize/stroke/)[tiling](/docs/reference/visualize/tiling/)[dictionary](/docs/reference/foundations/dictionary/),[offset:](#parameters-offset) [auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/),[extent:](#parameters-extent) [length](/docs/reference/layout/length/),[evade:](#parameters-evade) [bool](/docs/reference/foundations/bool/),[background:](#parameters-background) [bool](/docs/reference/foundations/bool/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `stroke` [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [stroke](/docs/reference/visualize/stroke/) or [tiling](/docs/reference/visualize/tiling/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How to [stroke](/docs/reference/visualize/stroke/ "stroke") the line.

If set to `auto`, takes on the text's color and a thickness defined in
the current font.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(fill: olive)
#overline(
  stroke: green.darken(20%),
  offset: -12pt,
  [The Forest Theme],
)
```

![Preview](/assets/docs/jXEAZxd9NFnCtgcbDVlzIQAAAAAAAAAA.png)

Default: `auto`

### `offset` [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The position of the line relative to the baseline. Read from the font
tables if `auto`.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#overline(offset: -1.2em)[
  The Tale Of A Faraway Line II
]
```

![Preview](/assets/docs/AUBIhMOFPefmpe2mV6TTrgAAAAAAAAAA.png)

Default: `auto`

### `extent` [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The amount by which to extend the line beyond (or within if negative)
the content.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set overline(extent: 4pt)
#set underline(extent: 4pt)
#overline(underline[Typography Today])
```

![Preview](/assets/docs/11dFhng73-PPcouY1kGuxAAAAAAAAAAA.png)

Default: `0pt`

### `evade` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether the line skips sections in which it would collide with the
glyphs.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#overline(
  evade: false,
  offset: -7.5pt,
  stroke: 1pt,
  extent: 3pt,
  [Temple],
)
```

![Preview](/assets/docs/4typb8n1rt84GcGKwEvmQAAAAAAAAAAA.png)

Default: `true`

### `background` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether the line is placed behind the content it overlines.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set overline(stroke: (thickness: 1em, paint: maroon, cap: "round"))
#overline(background: true)[This is stylized.] \
#overline(background: false)[This is partially hidden.]
```

![Preview](/assets/docs/J1qF0GrkgS3hBoWTovrZ_AAAAAAAAAAA.png)

Default: `false`

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to add a line over.

[![←](/assets/icons/16-chevron-right.svg)

LowercasePrevious page](/docs/reference/text/lower/) [![→](/assets/icons/16-chevron-right.svg)

Raw Text / CodeNext page](/docs/reference/text/raw/)