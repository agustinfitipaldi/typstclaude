# tiling

Source: https://typst.app/docs/reference/visualize/tiling/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Visualize](/docs/reference/visualize/)
- ![](/assets/icons/16-chevron-right.svg)
- [Tiling](/docs/reference/visualize/tiling/)

# tiling

A repeating tiling fill.

Typst supports the most common type of tilings, where a pattern is repeated
in a grid-like fashion, covering the entire area of an element that is
filled or stroked. The pattern is defined by a tile size and a body defining
the content of each cell. You can also add horizontal or vertical spacing
between the cells of the tiling.

## Examples

```typst
#let pat = tiling(size: (30pt, 30pt))[
  #place(line(start: (0%, 0%), end: (100%, 100%)))
  #place(line(start: (0%, 100%), end: (100%, 0%)))
]

#rect(fill: pat, width: 100%, height: 60pt, stroke: 1pt)
```

![Preview](/assets/docs/qh0n_b0duBWAckuJURX31gAAAAAAAAAA.png)

Tilings are also supported on text, but only when setting the
[relativeness](/docs/reference/visualize/tiling/#constructor-relative) to either `auto` (the default value) or
`"parent"`. To create word-by-word or glyph-by-glyph tilings, you can
wrap the words or characters of your text in [boxes](/docs/reference/layout/box/) manually or
through a [show rule](/docs/reference/styling/#show-rules).

```typst
#let pat = tiling(
  size: (30pt, 30pt),
  relative: "parent",
  square(
    size: 30pt,
    fill: gradient
      .conic(..color.map.rainbow),
  )
)

#set text(fill: pat)
#lorem(10)
```

![Preview](/assets/docs/HUmJC9zQ02GOf6wgfvJ3LQAAAAAAAAAA.png)

You can also space the elements further or closer apart using the
[`spacing`](/docs/reference/visualize/tiling/#constructor-spacing) feature of the tiling. If the spacing
is lower than the size of the tiling, the tiling will overlap.
If it is higher, the tiling will have gaps of the same color as the
background of the tiling.

```typst
#let pat = tiling(
  size: (30pt, 30pt),
  spacing: (10pt, 10pt),
  relative: "parent",
  square(
    size: 30pt,
    fill: gradient
     .conic(..color.map.rainbow),
  ),
)

#rect(
  width: 100%,
  height: 60pt,
  fill: pat,
)
```

![Preview](/assets/docs/oB89RLsift1GYrLpEi1__gAAAAAAAAAA.png)

## Relativeness

The location of the starting point of the tiling is dependent on the
dimensions of a container. This container can either be the shape that it is
being painted on, or the closest surrounding container. This is controlled
by the `relative` argument of a tiling constructor. By default, tilings
are relative to the shape they are being painted on, unless the tiling is
applied on text, in which case they are relative to the closest ancestor
container.

Typst determines the ancestor container as follows:

- For shapes that are placed at the root/top level of the document, the
  closest ancestor is the page itself.
- For other shapes, the ancestor is the innermost [`block`](/docs/reference/layout/block/ "`block`") or [`box`](/docs/reference/layout/box/ "`box`") that
  contains the shape. This includes the boxes and blocks that are implicitly
  created by show rules and elements. For example, a [`rotate`](/docs/reference/layout/rotate/ "`rotate`") will not
  affect the parent of a gradient, but a [`grid`](/docs/reference/layout/grid/ "`grid`") will.

## Compatibility

This type used to be called `pattern`. The name remains as an alias, but is
deprecated since Typst 0.13.

## Constructor Question mark If a type has a constructor, you can call it like a function to create a new value of the type.

Construct a new tiling.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#let pat = tiling(
  size: (20pt, 20pt),
  relative: "parent",
  place(
    dx: 5pt,
    dy: 5pt,
    rotate(45deg, square(
      size: 5pt,
      fill: black,
    )),
  ),
)

#rect(width: 100%, height: 60pt, fill: pat)
```

![Preview](/assets/docs/mXFm4BMZ6kN7dbjIfJkl9gAAAAAAAAAA.png)

tiling(

[size:](#constructor-size) [auto](/docs/reference/foundations/auto/)[array](/docs/reference/foundations/array/),[spacing:](#constructor-spacing) [array](/docs/reference/foundations/array/),[relative:](#constructor-relative) [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [tiling](/docs/reference/visualize/tiling/)

#### `size` [auto](/docs/reference/foundations/auto/) or [array](/docs/reference/foundations/array/)

The bounding box of each cell of the tiling.

Default: `auto`

#### `spacing` [array](/docs/reference/foundations/array/)

The spacing between cells of the tiling.

Default: `(0pt, 0pt)`

#### `relative` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/)

The [relative placement](#relativeness) of the tiling.

For an element placed at the root/top level of the document, the
parent is the page itself. For other elements, the parent is the
innermost block, box, column, grid, or stack that contains the
element.

| Variant | Details |
| --- | --- |
| `"self"` | Relative to itself (its own bounding box). |
| `"parent"` | Relative to its parent (the parent's bounding box). |

Default: `auto`

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content of each cell of the tiling.

[![←](/assets/icons/16-chevron-right.svg)

StrokePrevious page](/docs/reference/visualize/stroke/) [![→](/assets/icons/16-chevron-right.svg)

IntrospectionNext page](/docs/reference/introspection/)