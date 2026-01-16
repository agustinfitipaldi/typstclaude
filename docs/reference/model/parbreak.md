# parbreakElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/model/parbreak/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Model](/docs/reference/model/)
- ![](/assets/icons/16-chevron-right.svg)
- [Paragraph Break](/docs/reference/model/parbreak/)

# `parbreak`Element Question mark Element functions can be customized with `set` and `show` rules.

A paragraph break.

This starts a new paragraph. Especially useful when used within code like
[for loops](/docs/reference/scripting/#loops). Multiple consecutive
paragraph breaks collapse into a single one.

## Example

```typst
#for i in range(3) {
  [Blind text #i: ]
  lorem(5)
  parbreak()
}
```

![Preview](/assets/docs/Ugn0Cpe50EHdh4tXrmb4YAAAAAAAAAAA.png)

## Syntax

Instead of calling this function, you can insert a blank line into your
markup to create a paragraph break.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

parbreak() -> [content](/docs/reference/foundations/content/)

[![←](/assets/icons/16-chevron-right.svg)

ParagraphPrevious page](/docs/reference/model/par/) [![→](/assets/icons/16-chevron-right.svg)

QuoteNext page](/docs/reference/model/quote/)