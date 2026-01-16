# length

Source: https://typst.app/docs/reference/layout/length/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Length](/docs/reference/layout/length/)

# length

A size or distance, possibly expressed with contextual units.

Typst supports the following length units:

- Points: `72pt`
- Millimeters: `254mm`
- Centimeters: `2.54cm`
- Inches: `1in`
- Relative to font size: `2.5em`

You can multiply lengths with and divide them by integers and floats.

## Example

```typst
#rect(width: 20pt)
#rect(width: 2em)
#rect(width: 1in)

#(3em + 5pt).em \
#(20pt).em \
#(40em + 2pt).abs \
#(5em).abs
```

![Preview](/assets/docs/gpwKHS7y2wIB7BIxGEXoMwAAAAAAAAAA.png)

## Fields

- `abs`: A length with just the absolute component of the current length
  (that is, excluding the `em` component).
- `em`: The amount of `em` units in this length, as a [float](/docs/reference/foundations/float/ "float").

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `pt`

Converts this length to points.

Fails with an error if this length has non-zero `em` units (such as
`5em + 2pt` instead of just `2pt`). Use the `abs` field (such as in
`(5em + 2pt).abs.pt()`) to ignore the `em` component of the length (thus
converting only its absolute component).

self.pt() -> [float](/docs/reference/foundations/float/)

### `mm`

Converts this length to millimeters.

Fails with an error if this length has non-zero `em` units. See the
[`pt`](/docs/reference/layout/length/#definitions-pt) method for more details.

self.mm() -> [float](/docs/reference/foundations/float/)

### `cm`

Converts this length to centimeters.

Fails with an error if this length has non-zero `em` units. See the
[`pt`](/docs/reference/layout/length/#definitions-pt) method for more details.

self.cm() -> [float](/docs/reference/foundations/float/)

### `inches`

Converts this length to inches.

Fails with an error if this length has non-zero `em` units. See the
[`pt`](/docs/reference/layout/length/#definitions-pt) method for more details.

self.inches() -> [float](/docs/reference/foundations/float/)

### `to-absolute`

Resolve this length to an absolute length.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(size: 12pt)
#context [
  #(6pt).to-absolute() \
  #(6pt + 10em).to-absolute() \
  #(10em).to-absolute()
]

#set text(size: 6pt)
#context [
  #(6pt).to-absolute() \
  #(6pt + 10em).to-absolute() \
  #(10em).to-absolute()
]
```

![Preview](/assets/docs/O8f4mxTZz-ziS7eclGAyvgAAAAAAAAAA.png)

self.to-absolute() -> [length](/docs/reference/layout/length/)

[![←](/assets/icons/16-chevron-right.svg)

LayoutPrevious page](/docs/reference/layout/layout/) [![→](/assets/icons/16-chevron-right.svg)

MeasureNext page](/docs/reference/layout/measure/)