# frameElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/html/frame/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [HTML](/docs/reference/html/)
- ![](/assets/icons/16-chevron-right.svg)
- [Frame](/docs/reference/html/frame/)

# `frame`Element Question mark Element functions can be customized with `set` and `show` rules.

An element that lays out its content as an inline SVG.

Sometimes, converting Typst content to HTML is not desirable. This can be
the case for plots and other content that relies on positioning and styling
to convey its message.

This function allows you to use the Typst layout engine that would also be
used for PDF, SVG, and PNG export to render a part of your document exactly
how it would appear when exported in one of these formats. It embeds the
content as an inline SVG.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

html.frame(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content that shall be laid out.

[![←](/assets/icons/16-chevron-right.svg)

ElemPrevious page](/docs/reference/html/elem/) [![→](/assets/icons/16-chevron-right.svg)

Typed HTMLNext page](/docs/reference/html/typed/)