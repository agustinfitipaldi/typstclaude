# blockElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/layout/block/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Block](/docs/reference/layout/block/)

# `block`Element Question mark Element functions can be customized with `set` and `show` rules.

A block-level container.

Such a container can be used to separate content, size it, and give it a
background or border.

Blocks are also the primary way to control whether text becomes part of a
paragraph or not. See [the paragraph documentation](/docs/reference/model/par/#what-becomes-a-paragraph)
for more details.

## Examples

With a block, you can give a background to content while still allowing it
to break across multiple pages.

```typst
#set page(height: 100pt)
#block(
  fill: luma(230),
  inset: 8pt,
  radius: 4pt,
  lorem(30),
)
```

![Preview](/assets/docs/ANNbdXVxvjEeHE66qUzAcwAAAAAAAAAA.png)
![Preview](/assets/docs/ANNbdXVxvjEeHE66qUzAcwAAAAAAAAAB.png)

Blocks are also useful to force elements that would otherwise be inline to
become block-level, especially when writing show rules.

```typst
#show heading: it => it.body
= Blockless
More text.

#show heading: it => block(it.body)
= Blocky
More text.
```

![Preview](/assets/docs/oxrD9vHAqcb-9gLEkFF_PQAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

block(

[width:](#parameters-width) [auto](/docs/reference/foundations/auto/)[relative](/docs/reference/layout/relative/),[height:](#parameters-height) [auto](/docs/reference/foundations/auto/)[relative](/docs/reference/layout/relative/)[fraction](/docs/reference/layout/fraction/),[breakable:](#parameters-breakable) [bool](/docs/reference/foundations/bool/),[fill:](#parameters-fill) [none](/docs/reference/foundations/none/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[tiling](/docs/reference/visualize/tiling/),[stroke:](#parameters-stroke) [none](/docs/reference/foundations/none/)[length](/docs/reference/layout/length/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[stroke](/docs/reference/visualize/stroke/)[tiling](/docs/reference/visualize/tiling/)[dictionary](/docs/reference/foundations/dictionary/),[radius:](#parameters-radius) [relative](/docs/reference/layout/relative/)[dictionary](/docs/reference/foundations/dictionary/),[inset:](#parameters-inset) [relative](/docs/reference/layout/relative/)[dictionary](/docs/reference/foundations/dictionary/),[outset:](#parameters-outset) [relative](/docs/reference/layout/relative/)[dictionary](/docs/reference/foundations/dictionary/),[spacing:](#parameters-spacing) [relative](/docs/reference/layout/relative/)[fraction](/docs/reference/layout/fraction/),[above:](#parameters-above) [auto](/docs/reference/foundations/auto/)[relative](/docs/reference/layout/relative/)[fraction](/docs/reference/layout/fraction/),[below:](#parameters-below) [auto](/docs/reference/foundations/auto/)[relative](/docs/reference/layout/relative/)[fraction](/docs/reference/layout/fraction/),[clip:](#parameters-clip) [bool](/docs/reference/foundations/bool/),[sticky:](#parameters-sticky) [bool](/docs/reference/foundations/bool/),[none](/docs/reference/foundations/none/)[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `width` [auto](/docs/reference/foundations/auto/) or [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The block's width.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set align(center)
#block(
  width: 60%,
  inset: 8pt,
  fill: silver,
  lorem(10),
)
```

![Preview](/assets/docs/rmTSlZT-FzVZcPQGVLOIiwAAAAAAAAAA.png)

Default: `auto`

### `height` [auto](/docs/reference/foundations/auto/) or [relative](/docs/reference/layout/relative/) or [fraction](/docs/reference/layout/fraction/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The block's height. When the height is larger than the remaining space
on a page and [`breakable`](/docs/reference/layout/block/#parameters-breakable) is `true`, the
block will continue on the next page with the remaining height.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set page(height: 80pt)
#set align(center)
#block(
  width: 80%,
  height: 150%,
  fill: aqua,
)
```

![Preview](/assets/docs/lezx_tGBIjN0y72kerj7yQAAAAAAAAAA.png)
![Preview](/assets/docs/lezx_tGBIjN0y72kerj7yQAAAAAAAAAB.png)

Default: `auto`

### `breakable` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether the block can be broken and continue on the next page.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set page(height: 80pt)
The following block will
jump to its own page.
#block(
  breakable: false,
  lorem(15),
)
```

![Preview](/assets/docs/I4HMzOAjAUbW-RK0a_YVHAAAAAAAAAAA.png)
![Preview](/assets/docs/I4HMzOAjAUbW-RK0a_YVHAAAAAAAAAAB.png)

Default: `true`

### `fill` [none](/docs/reference/foundations/none/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [tiling](/docs/reference/visualize/tiling/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The block's background color. See the
[rectangle's documentation](/docs/reference/visualize/rect/#parameters-fill) for more details.

Default: `none`

### `stroke` [none](/docs/reference/foundations/none/) or [length](/docs/reference/layout/length/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [stroke](/docs/reference/visualize/stroke/) or [tiling](/docs/reference/visualize/tiling/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The block's border color. See the
[rectangle's documentation](/docs/reference/visualize/rect/#parameters-stroke) for more details.

Default: `(:)`

### `radius` [relative](/docs/reference/layout/relative/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How much to round the block's corners. See the
[rectangle's documentation](/docs/reference/visualize/rect/#parameters-radius) for more details.

Default: `(:)`

### `inset` [relative](/docs/reference/layout/relative/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How much to pad the block's content. See the
[box's documentation](/docs/reference/layout/box/#parameters-inset) for more details.

Default: `(:)`

### `outset` [relative](/docs/reference/layout/relative/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How much to expand the block's size without affecting the layout. See
the [box's documentation](/docs/reference/layout/box/#parameters-outset) for more details.

Default: `(:)`

### `spacing` [relative](/docs/reference/layout/relative/) or [fraction](/docs/reference/layout/fraction/)

The spacing around the block. When `auto`, inherits the paragraph
[`spacing`](/docs/reference/model/par/#parameters-spacing).

For two adjacent blocks, the larger of the first block's `above` and the
second block's `below` spacing wins. Moreover, block spacing takes
precedence over paragraph [`spacing`](/docs/reference/model/par/#parameters-spacing).

Note that this is only a shorthand to set `above` and `below` to the
same value. Since the values for `above` and `below` might differ, a
[context](/docs/reference/context/ "context") block only provides access to `block.above` and
`block.below`, not to `block.spacing` directly.

This property can be used in combination with a show rule to adjust the
spacing around arbitrary block-level elements.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set align(center)
#show math.equation: set block(above: 8pt, below: 16pt)

This sum of $x$ and $y$:
$ x + y = z $
A second paragraph.
```

![Preview](/assets/docs/-Z0A6wte5TbEZ6mEwTPvngAAAAAAAAAA.png)

Default: `1.2em`

### `above` [auto](/docs/reference/foundations/auto/) or [relative](/docs/reference/layout/relative/) or [fraction](/docs/reference/layout/fraction/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The spacing between this block and its predecessor.

Default: `auto`

### `below` [auto](/docs/reference/foundations/auto/) or [relative](/docs/reference/layout/relative/) or [fraction](/docs/reference/layout/fraction/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The spacing between this block and its successor.

Default: `auto`

### `clip` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether to clip the content inside the block.

Clipping is useful when the block's content is larger than the block itself,
as any content that exceeds the block's bounds will be hidden.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#block(
  width: 50pt,
  height: 50pt,
  clip: true,
  image("tiger.jpg", width: 100pt, height: 100pt)
)
```

![Preview](/assets/docs/VV4XHW5eLH_lso6MwHK6pQAAAAAAAAAA.png)

Default: `false`

### `sticky` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether this block must stick to the following one, with no break in
between.

This is, by default, set on heading blocks to prevent orphaned headings
at the bottom of the page.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
// Disable stickiness of headings.
#show heading: set block(sticky: false)
#lorem(20)

= Chapter
#lorem(10)
```

![Preview](/assets/docs/9rTrIlbIWN6fRV2-gOoijQAAAAAAAAAA.png)
![Preview](/assets/docs/9rTrIlbIWN6fRV2-gOoijQAAAAAAAAAB.png)

Default: `false`

### `body` [none](/docs/reference/foundations/none/) or [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The contents of the block.

Default: `none`

[![←](/assets/icons/16-chevron-right.svg)

AnglePrevious page](/docs/reference/layout/angle/) [![→](/assets/icons/16-chevron-right.svg)

BoxNext page](/docs/reference/layout/box/)