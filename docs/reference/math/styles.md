# Styles

Source: https://typst.app/docs/reference/math/styles/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Math](/docs/reference/math/)
- ![](/assets/icons/16-chevron-right.svg)
- [Styles](/docs/reference/math/styles/)

# Styles

Alternate letterforms within formulas.

These functions are distinct from the [`text`](/docs/reference/text/text/ "`text`") function because math fonts
contain multiple variants of each letter.

## Functions

### `upright`

Upright (non-italic) font style in math.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ upright(A) != A $
```

![Preview](/assets/docs/I3XzlEtlEFD5Cw96srS1ngAAAAAAAAAA.png)

math.upright(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to style.

### `italic`

Italic font style in math.

For roman letters and greek lowercase letters, this is already the default.

math.italic(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to style.

### `bold`

Bold font style in math.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ bold(A) := B^+ $
```

![Preview](/assets/docs/8-9k5ChF2PO13_x1ipPkAAAAAAAAAAAA.png)

math.bold(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to style.

[![←](/assets/icons/16-chevron-right.svg)

StretchPrevious page](/docs/reference/math/stretch/) [![→](/assets/icons/16-chevron-right.svg)

Text OperatorNext page](/docs/reference/math/op/)