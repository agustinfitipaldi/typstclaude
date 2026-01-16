# alignElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/layout/align/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Align](/docs/reference/layout/align/)

# `align`Element Question mark Element functions can be customized with `set` and `show` rules.

Aligns content horizontally and vertically.

## Example

Let's start with centering our content horizontally:

```typst
#set page(height: 120pt)
#set align(center)

Centered text, a sight to see \
In perfect balance, visually \
Not left nor right, it stands alone \
A work of art, a visual throne
```

![Preview](/assets/docs/kcNIG-bYA8T9BUDnjCUJGgAAAAAAAAAA.png)

To center something vertically, use *horizon* alignment:

```typst
#set page(height: 120pt)
#set align(horizon)

Vertically centered, \
the stage had entered, \
a new paragraph.
```

![Preview](/assets/docs/y9OO-MSDQIHWsGPc_6pNnAAAAAAAAAAA.png)

## Combining alignments

You can combine two alignments with the `+` operator. Let's also only apply
this to one piece of content by using the function form instead of a set
rule:

```typst
#set page(height: 120pt)
Though left in the beginning ...

#align(right + bottom)[
  ... they were right in the end, \
  and with addition had gotten, \
  the paragraph to the bottom!
]
```

![Preview](/assets/docs/gXaqAMYC8Licj_UCK0JSFgAAAAAAAAAA.png)

## Nested alignment

You can use varying alignments for layout containers and the elements within
them. This way, you can create intricate layouts:

```typst
#align(center, block[
  #set align(left)
  Though centered together \
  alone \
  we \
  are \
  left.
])
```

![Preview](/assets/docs/B6Y-WWFtiUjCHNJ9B8R8vQAAAAAAAAAA.png)

## Alignment within the same line

The `align` function performs block-level alignment and thus always
interrupts the current paragraph. To have different alignment for parts
of the same line, you should use [fractional spacing](/docs/reference/layout/h/) instead:

```
Start #h(1fr) End
```

![Preview](/assets/docs/jlafwbE2ZuISwJPQNRzA3gAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

align(

[alignment](/docs/reference/layout/alignment/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `alignment` [alignment](/docs/reference/layout/alignment/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The [alignment](/docs/reference/layout/alignment/ "alignment") along both axes.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set page(height: 6cm)
#set text(lang: "ar")

مثال
#align(
  end + horizon,
  rect(inset: 12pt)[ركن]
)
```

![Preview](/assets/docs/3176vm6IE_BNfZrVpc9_xAAAAAAAAAAA.png)

Default: `start + top`

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to align.

[![←](/assets/icons/16-chevron-right.svg)

LayoutPrevious page](/docs/reference/layout/) [![→](/assets/icons/16-chevron-right.svg)

AlignmentNext page](/docs/reference/layout/alignment/)