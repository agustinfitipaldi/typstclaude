# emphElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/model/emph/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Model](/docs/reference/model/)
- ![](/assets/icons/16-chevron-right.svg)
- [Emphasis](/docs/reference/model/emph/)

# `emph`Element Question mark Element functions can be customized with `set` and `show` rules.

Emphasizes content by toggling italics.

- If the current [text style](/docs/reference/text/text/#parameters-style) is `"normal"`, this turns it
  into `"italic"`.
- If it is already `"italic"` or `"oblique"`, it turns it back to
  `"normal"`.

## Example

```typst
This is _emphasized._ \
This is #emph[too.]

#show emph: it => {
  text(blue, it.body)
}

This is _emphasized_ differently.
```

![Preview](/assets/docs/p3cGCgaJdrkrScOita7QfgAAAAAAAAAA.png)

## Syntax

This function also has dedicated syntax: To emphasize content, simply
enclose it in underscores (`_`). Note that this only works at word
boundaries. To emphasize part of a word, you have to use the function.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

emph(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to emphasize.

[![←](/assets/icons/16-chevron-right.svg)

DocumentPrevious page](/docs/reference/model/document/) [![→](/assets/icons/16-chevron-right.svg)

FigureNext page](/docs/reference/model/figure/)