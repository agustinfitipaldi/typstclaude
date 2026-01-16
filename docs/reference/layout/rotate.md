# rotateElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/layout/rotate/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Rotate](/docs/reference/layout/rotate/)

# `rotate`Element Question mark Element functions can be customized with `set` and `show` rules.

Rotates content without affecting layout.

Rotates an element by a given angle. The layout will act as if the element
was not rotated unless you specify `reflow: true`.

## Example

```typst
#stack(
  dir: ltr,
  spacing: 1fr,
  ..range(16)
    .map(i => rotate(24deg * i)[X]),
)
```

![Preview](/assets/docs/KRNlJxFzPXxwMsKBe0vSFQAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

rotate(

[angle](/docs/reference/layout/angle/),[origin:](#parameters-origin) [alignment](/docs/reference/layout/alignment/),[reflow:](#parameters-reflow) [bool](/docs/reference/foundations/bool/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `angle` [angle](/docs/reference/layout/angle/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The amount of rotation.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#rotate(-1.571rad)[Space!]
```

![Preview](/assets/docs/_kx75fW11u8TY_Zj6luytwAAAAAAAAAA.png)

Default: `0deg`

### `origin` [alignment](/docs/reference/layout/alignment/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The origin of the rotation.

If, for instance, you wanted the bottom left corner of the rotated
element to stay aligned with the baseline, you would set it to `bottom + left` instead.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(spacing: 8pt)
#let square = square.with(width: 8pt)

#box(square())
#box(rotate(30deg, origin: center, square()))
#box(rotate(30deg, origin: top + left, square()))
#box(rotate(30deg, origin: bottom + right, square()))
```

![Preview](/assets/docs/ZzBCk0ymiIeT5xo4XXc-8QAAAAAAAAAA.png)

Default: `center + horizon`

### `reflow` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether the rotation impacts the layout.

If set to `false`, the rotated content will retain the bounding box of
the original content. If set to `true`, the bounding box will take the
rotation of the content into account and adjust the layout accordingly.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
Hello #rotate(90deg, reflow: true)[World]!
```

![Preview](/assets/docs/i8AMp2vxmKn3Nn0wwA1Z0wAAAAAAAAAA.png)

Default: `false`

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to rotate.

[![←](/assets/icons/16-chevron-right.svg)

RepeatPrevious page](/docs/reference/layout/repeat/) [![→](/assets/icons/16-chevron-right.svg)

ScaleNext page](/docs/reference/layout/scale/)