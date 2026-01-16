# alignment

Source: https://typst.app/docs/reference/layout/alignment/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Alignment](/docs/reference/layout/alignment/)

# alignment

Where to align something along an axis.

Possible values are:

- `start`: Aligns at the [start](/docs/reference/layout/direction/#definitions-start) of the [text
  direction](/docs/reference/text/text/#parameters-dir).
- `end`: Aligns at the [end](/docs/reference/layout/direction/#definitions-end) of the [text
  direction](/docs/reference/text/text/#parameters-dir).
- `left`: Align at the left.
- `center`: Aligns in the middle, horizontally.
- `right`: Aligns at the right.
- `top`: Aligns at the top.
- `horizon`: Aligns in the middle, vertically.
- `bottom`: Align at the bottom.

These values are available globally and also in the alignment type's scope,
so you can write either of the following two:

```typst
#align(center)[Hi]
#align(alignment.center)[Hi]
```

![Preview](/assets/docs/ZprGjLBPSUJ5f2a4fil8IAAAAAAAAAAA.png)

## 2D alignments

To align along both axes at the same time, add the two alignments using the
`+` operator. For example, `top + right` aligns the content to the top right
corner.

```typst
#set page(height: 3cm)
#align(center + bottom)[Hi]
```

![Preview](/assets/docs/X3ZrV0nn1RgePWtIVMB4XgAAAAAAAAAA.png)

## Fields

The `x` and `y` fields hold the alignment's horizontal and vertical
components, respectively (as yet another `alignment`). They may be `none`.

```typst
#(top + right).x \
#left.x \
#left.y (none)
```

![Preview](/assets/docs/ecr8JX7jRnRHSrOlOhwwRwAAAAAAAAAA.png)

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `axis`

The axis this alignment belongs to.

- `"horizontal"` for `start`, `left`, `center`, `right`, and `end`
- `"vertical"` for `top`, `horizon`, and `bottom`
- `none` for 2-dimensional alignments

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#left.axis() \
#bottom.axis()
```

![Preview](/assets/docs/OHqui2ES_RRnmxyOZdFWIgAAAAAAAAAA.png)

self.axis() -> [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/)

### `inv`

The inverse alignment.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#top.inv() \
#left.inv() \
#center.inv() \
#(left + bottom).inv()
```

![Preview](/assets/docs/tBAxSGcUdyogNGn2l8Pm_QAAAAAAAAAA.png)

self.inv() -> [alignment](/docs/reference/layout/alignment/)

[![←](/assets/icons/16-chevron-right.svg)

AlignPrevious page](/docs/reference/layout/align/) [![→](/assets/icons/16-chevron-right.svg)

AngleNext page](/docs/reference/layout/angle/)