# colbreakElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/layout/colbreak/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Column Break](/docs/reference/layout/colbreak/)

# `colbreak`Element Question mark Element functions can be customized with `set` and `show` rules.

Forces a column break.

The function will behave like a [page break](/docs/reference/layout/pagebreak/) when used in a
single column layout or the last column on a page. Otherwise, content after
the column break will be placed in the next column.

## Example

```typst
#set page(columns: 2)
Preliminary findings from our
ongoing research project have
revealed a hitherto unknown
phenomenon of extraordinary
significance.

#colbreak()
Through rigorous experimentation
and analysis, we have discovered
a hitherto uncharacterized process
that defies our current
understanding of the fundamental
laws of nature.
```

![Preview](/assets/docs/MXyldqpQM7MpLi9gC6sPGAAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

colbreak(

[weak:](#parameters-weak) [bool](/docs/reference/foundations/bool/)

) -> [content](/docs/reference/foundations/content/)

### `weak` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

If `true`, the column break is skipped if the current column is
already empty.

Default: `false`

[![←](/assets/icons/16-chevron-right.svg)

BoxPrevious page](/docs/reference/layout/box/) [![→](/assets/icons/16-chevron-right.svg)

ColumnsNext page](/docs/reference/layout/columns/)