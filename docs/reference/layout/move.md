# moveElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/layout/move/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Move](/docs/reference/layout/move/)

# `move`Element Question mark Element functions can be customized with `set` and `show` rules.

Moves content without affecting layout.

The `move` function allows you to move content while the layout still 'sees'
it at the original positions. Containers will still be sized as if the
content was not moved.

## Example

```typst
#rect(inset: 0pt, fill: gray, move(
  dx: 4pt, dy: 6pt,
  rect(
    inset: 8pt,
    fill: white,
    stroke: black,
    [Abra cadabra]
  )
))
```

![Preview](/assets/docs/asQdhB-KaUubWCFzAxhPdAAAAAAAAAAA.png)

## Accessibility

Moving is transparent to Assistive Technology (AT). Your content will be
read in the order it appears in the source, regardless of any visual
movement. If you need to hide content from AT altogether in PDF export,
consider using [`pdf.artifact`](/docs/reference/pdf/artifact/ "`pdf.artifact`").

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

move(

[dx:](#parameters-dx) [relative](/docs/reference/layout/relative/),[dy:](#parameters-dy) [relative](/docs/reference/layout/relative/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `dx` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The horizontal displacement of the content.

Default: `0% + 0pt`

### `dy` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The vertical displacement of the content.

Default: `0% + 0pt`

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to move.

[![←](/assets/icons/16-chevron-right.svg)

MeasurePrevious page](/docs/reference/layout/measure/) [![→](/assets/icons/16-chevron-right.svg)

PaddingNext page](/docs/reference/layout/pad/)