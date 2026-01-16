# placeElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/layout/place/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Place](/docs/reference/layout/place/)

# `place`Element Question mark Element functions can be customized with `set` and `show` rules.

Places content relatively to its parent container.

Placed content can be either overlaid (the default) or floating. Overlaid
content is aligned with the parent container according to the given
[`alignment`](/docs/reference/layout/place/#parameters-alignment), and shown over any other content added so
far in the container. Floating content is placed at the top or bottom of
the container, displacing other content down or up respectively. In both
cases, the content position can be adjusted with [`dx`](/docs/reference/layout/place/#parameters-dx) and
[`dy`](/docs/reference/layout/place/#parameters-dy) offsets without affecting the layout.

The parent can be any container such as a [`block`](/docs/reference/layout/block/ "`block`"), [`box`](/docs/reference/layout/box/ "`box`"),
[`rect`](/docs/reference/visualize/rect/ "`rect`"), etc. A top level `place` call will place content directly
in the text area of the current page. This can be used for absolute
positioning on the page: with a `top + left`
[`alignment`](/docs/reference/layout/place/#parameters-alignment), the offsets `dx` and `dy` will set the
position of the element's top left corner relatively to the top left corner
of the text area. For absolute positioning on the full page including
margins, you can use `place` in [`page.foreground`](/docs/reference/layout/page/#parameters-foreground "`page.foreground`") or [`page.background`](/docs/reference/layout/page/#parameters-background "`page.background`").

## Examples

```typst
#set page(height: 120pt)
Hello, world!

#rect(
  width: 100%,
  height: 2cm,
  place(horizon + right, square()),
)

#place(
  top + left,
  dx: -5pt,
  square(size: 5pt, fill: red),
)
```

![Preview](/assets/docs/b3Ue37sNl2HDpslyo5trfgAAAAAAAAAA.png)

## Effect on the position of other elements

Overlaid elements don't take space in the flow of content, but a `place`
call inserts an invisible block-level element in the flow. This can
affect the layout by breaking the current paragraph. To avoid this,
you can wrap the `place` call in a [`box`](/docs/reference/layout/box/ "`box`") when the call is made
in the middle of a paragraph. The alignment and offsets will then be
relative to this zero-size box. To make sure it doesn't interfere with
spacing, the box should be attached to a word using a word joiner.

For example, the following defines a function for attaching an annotation
to the following word:

```typst
#let annotate(..args) = {
  box(place(..args))
  sym.wj
  h(0pt, weak: true)
}

A placed #annotate(square(), dy: 2pt)
square in my text.
```

![Preview](/assets/docs/QIJqPsAAp5jqe-EB4bZF1gAAAAAAAAAA.png)

The zero-width weak spacing serves to discard spaces between the function
call and the next word.

## Accessibility

Assistive Technology (AT) will always read the placed element at the point
where it logically appears in the document, regardless of where this
function physically moved it. Put its markup where it would make the most
sense in the reading order.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

place(

[auto](/docs/reference/foundations/auto/)[alignment](/docs/reference/layout/alignment/),[scope:](#parameters-scope) [str](/docs/reference/foundations/str/),[float:](#parameters-float) [bool](/docs/reference/foundations/bool/),[clearance:](#parameters-clearance) [length](/docs/reference/layout/length/),[dx:](#parameters-dx) [relative](/docs/reference/layout/relative/),[dy:](#parameters-dy) [relative](/docs/reference/layout/relative/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `alignment` [auto](/docs/reference/foundations/auto/) or [alignment](/docs/reference/layout/alignment/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Relative to which position in the parent container to place the content.

- If `float` is `false`, then this can be any alignment other than `auto`.
- If `float` is `true`, then this must be `auto`, `top`, or `bottom`.

When `float` is `false` and no vertical alignment is specified, the
content is placed at the current position on the vertical axis.

Default: `start`

### `scope` [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Relative to which containing scope something is placed.

The parent scope is primarily used with figures and, for
this reason, the figure function has a mirrored [`scope`
parameter](/docs/reference/model/figure/#parameters-scope). Nonetheless, it can also be more generally
useful to break out of the columns. A typical example would be to
[create a single-column title section](/docs/guides/page-setup/#columns)
in a two-column document.

Note that parent-scoped placement is currently only supported if `float`
is `true`. This may change in the future.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set page(height: 150pt, columns: 2)
#place(
  top + center,
  scope: "parent",
  float: true,
  rect(width: 80%, fill: aqua),
)

#lorem(25)
```

![Preview](/assets/docs/9xhEXBaN2g3N9Vju7GUzFwAAAAAAAAAA.png)

| Variant | Details |
| --- | --- |
| `"column"` | Place into the current column. |
| `"parent"` | Place relative to the parent, letting the content span over all columns. |

Default: `"column"`

### `float` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether the placed element has floating layout.

Floating elements are positioned at the top or bottom of the parent
container, displacing in-flow content. They are always placed in the
in-flow order relative to each other, as well as before any content
following a later [`place.flush`](/docs/reference/layout/place/#definitions-flush "`place.flush`") element.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set page(height: 150pt)
#let note(where, body) = place(
  center + where,
  float: true,
  clearance: 6pt,
  rect(body),
)

#lorem(10)
#note(bottom)[Bottom 1]
#note(bottom)[Bottom 2]
#lorem(40)
#note(top)[Top]
#lorem(10)
```

![Preview](/assets/docs/t5SJ49ulSlCH5SgTOH20JAAAAAAAAAAA.png)
![Preview](/assets/docs/t5SJ49ulSlCH5SgTOH20JAAAAAAAAAAB.png)

Default: `false`

### `clearance` [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The spacing between the placed element and other elements in a floating
layout.

Has no effect if `float` is `false`.

Default: `1.5em`

### `dx` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The horizontal displacement of the placed content.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set page(height: 100pt)
#for x in range(-8, 8) {
  place(center + horizon,
    dx: x * 8pt, dy: x * 4pt,
    text(
      size: calc.root(x + 10, 3) * 6pt,
      fill: color.mix((green, 8 - x), (blue, 8 + x)),
    )[T]
  )
}
```

![Preview](/assets/docs/PKFFaKrabuMqdO4B0YRnNwAAAAAAAAAA.png)

This does not affect the layout of in-flow content.
In other words, the placed content is treated as if it
were wrapped in a [`move`](/docs/reference/layout/move/ "`move`") element.

Default: `0% + 0pt`

### `dy` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The vertical displacement of the placed content.

This does not affect the layout of in-flow content.
In other words, the placed content is treated as if it
were wrapped in a [`move`](/docs/reference/layout/move/ "`move`") element.

Default: `0% + 0pt`

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to place.

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `flush`Element Question mark Element functions can be customized with `set` and `show` rules.

Asks the layout algorithm to place pending floating elements before
continuing with the content.

This is useful for preventing floating figures from spilling
into the next section.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#lorem(15)

#figure(
  rect(width: 100%, height: 50pt),
  placement: auto,
  caption: [A rectangle],
)

#place.flush()

This text appears after the figure.
```

![Preview](/assets/docs/8qp5vfUImMtnXndzjQCsNQAAAAAAAAAA.png)
![Preview](/assets/docs/8qp5vfUImMtnXndzjQCsNQAAAAAAAAAB.png)

place.flush() -> [content](/docs/reference/foundations/content/)

[![←](/assets/icons/16-chevron-right.svg)

Page BreakPrevious page](/docs/reference/layout/pagebreak/) [![→](/assets/icons/16-chevron-right.svg)

RatioNext page](/docs/reference/layout/ratio/)