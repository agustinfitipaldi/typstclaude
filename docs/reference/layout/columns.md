# columnsElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/layout/columns/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Columns](/docs/reference/layout/columns/)

# `columns`Element Question mark Element functions can be customized with `set` and `show` rules.

Separates a region into multiple equally sized columns.

The `column` function lets you separate the interior of any container into
multiple columns. It will currently not balance the height of the columns.
Instead, the columns will take up the height of their container or the
remaining height on the page. Support for balanced columns is planned for
the future.

When arranging content across multiple columns, use [`colbreak`](/docs/reference/layout/colbreak/)
to explicitly continue in the next column.

## Example

```typst
#columns(2, gutter: 8pt)[
  This text is in the
  first column.

  #colbreak()

  This text is in the
  second column.
]
```

![Preview](/assets/docs/g7s0FDVA18XrIBkGtU4zDQAAAAAAAAAA.png)

## Page-level columns

If you need to insert columns across your whole document, use the `page`
function's [`columns` parameter](/docs/reference/layout/page/#parameters-columns) instead. This will create
the columns directly at the page-level rather than wrapping all of your
content in a layout container. As a result, things like
[pagebreaks](/docs/reference/layout/pagebreak/), [footnotes](/docs/reference/model/footnote/), and [line
numbers](/docs/reference/model/par/#definitions-line) will continue to work as expected. For more information,
also read the [relevant part of the page setup
guide](/docs/guides/page-setup/#columns).

## Breaking out of columns

To temporarily break out of columns (e.g. for a paper's title), use
parent-scoped floating placement:

```typst
#set page(columns: 2, height: 150pt)

#place(
  top + center,
  scope: "parent",
  float: true,
  text(1.4em, weight: "bold")[
    My document
  ],
)

#lorem(40)
```

![Preview](/assets/docs/qNRmHdtNgs8qpE-RUR-XyQAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

columns(

[int](/docs/reference/foundations/int/),[gutter:](#parameters-gutter) [relative](/docs/reference/layout/relative/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `count` [int](/docs/reference/foundations/int/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The number of columns.

Default: `2`

### `gutter` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The size of the gutter space between each column.

Default: `4% + 0pt`

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content that should be layouted into the columns.

[![←](/assets/icons/16-chevron-right.svg)

Column BreakPrevious page](/docs/reference/layout/colbreak/) [![→](/assets/icons/16-chevron-right.svg)

DirectionNext page](/docs/reference/layout/direction/)