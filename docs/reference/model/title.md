# titleElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/model/title/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Model](/docs/reference/model/)
- ![](/assets/icons/16-chevron-right.svg)
- [Title](/docs/reference/model/title/)

# `title`Element Question mark Element functions can be customized with `set` and `show` rules.

A document title.

This should be used to display the main title of the whole document and
should occur only once per document. In contrast, level 1
[headings](/docs/reference/model/heading/) are intended to be used for the top-level sections of
the document.

Note that additional frontmatter (like an author list) that should appear
together with the title does not belong in its body.

In HTML export, this shows as a `h1` element while level 1 headings show
as `h2` elements.

## Example

```typst
#set document(
  title: [Interstellar Mail Delivery]
)

#title()

= Introduction
In recent years, ...
```

![Preview](/assets/docs/UVjmmYHJbHHQ-BVwZ_0XJgAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

title(

[auto](/docs/reference/foundations/auto/)[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

### `body` [auto](/docs/reference/foundations/auto/) or [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The content of the title.

When omitted (or `auto`), this will default to [`document.title`](/docs/reference/model/document/#parameters-title "`document.title`"). In
this case, a document title must have been previously set with
`set document(title: [..])`.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set document(title: "Course ABC, Homework 1")
#title[Homework 1]

...
```

![Preview](/assets/docs/iYp3qRDd5l-8YUm8yheI8QAAAAAAAAAA.png)

Default: `auto`

[![←](/assets/icons/16-chevron-right.svg)

Term ListPrevious page](/docs/reference/model/terms/) [![→](/assets/icons/16-chevron-right.svg)

TextNext page](/docs/reference/text/)