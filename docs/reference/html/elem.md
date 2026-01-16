# elemElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/html/elem/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [HTML](/docs/reference/html/)
- ![](/assets/icons/16-chevron-right.svg)
- [Elem](/docs/reference/html/elem/)

# `elem`Element Question mark Element functions can be customized with `set` and `show` rules.

An HTML element that can contain Typst content.

Typst's HTML export automatically generates the appropriate tags for most
elements. However, sometimes, it is desirable to retain more control. For
example, when using Typst to generate your blog, you could use this function
to wrap each article in an `<article>` tag.

Typst is aware of what is valid HTML. A tag and its attributes must form
syntactically valid HTML. Some tags, like `meta` do not accept content.
Hence, you must not provide a body for them. We may add more checks in the
future, so be sure that you are generating valid HTML when using this
function.

Normally, Typst will generate `html`, `head`, and `body` tags for you. If
you instead create them with this function, Typst will omit its own tags.

```typst
#html.elem("div", attrs: (style: "background: aqua"))[
  A div with _Typst content_ inside!
]
```

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

html.elem(

[str](/docs/reference/foundations/str/),[attrs:](#parameters-attrs) [dictionary](/docs/reference/foundations/dictionary/),[none](/docs/reference/foundations/none/)[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `tag` [str](/docs/reference/foundations/str/) Required Positional Question mark Positional parameters are specified in order, without names.

The element's tag.

### `attrs` [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The element's HTML attributes.

Default: `(:)`

### `body` [none](/docs/reference/foundations/none/) or [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The contents of the HTML element.

The body can be arbitrary Typst content.

Default: `none`

[![←](/assets/icons/16-chevron-right.svg)

HTMLPrevious page](/docs/reference/html/) [![→](/assets/icons/16-chevron-right.svg)

FrameNext page](/docs/reference/html/frame/)