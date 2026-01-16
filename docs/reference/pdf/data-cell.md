# data-cell

Source: https://typst.app/docs/reference/pdf/data-cell/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [PDF](/docs/reference/pdf/)
- ![](/assets/icons/16-chevron-right.svg)
- [Data Cell](/docs/reference/pdf/data-cell/)

# `data-cell`

Explicitly defines this cell as a data cell.

Each cell in a table is either a header cell or a data cell. By default, all
cells in [`table.header`](/docs/reference/model/table/#definitions-header "`table.header`") are header cells, and all other cells data cells.

If your header contains a cell that is not a header cell, you can use this
function to mark it as a data cell.

The API of this feature is temporary. Hence, calling this function requires
enabling the `a11y-extras` feature flag at the moment. In a future Typst
release, this functionality may move out of the `pdf` module so that tables
in other export targets can contain the same information.

```typst
#show table.cell.where(x: 0): set text(weight: "bold")
#show table.cell.where(x: 1): set text(style: "italic")
#show table.cell.where(x: 1, y: 0): set text(style: "normal")

#table(
  columns: 3,
  align: (left, left, center),

  table.header[Objective][Key Result][Status],

  table.header(
    level: 2,
    table.cell(colspan: 2)[Improve Customer Satisfaction],
    // Status is data for this objective, not a header
    pdf.data-cell[✓ On Track],
  ),
  [], [Increase NPS to 50+], [45],
  [], [Reduce churn to \<5%], [4.2%],

  table.header(
    level: 2,
    table.cell(colspan: 2)[Grow Revenue],
    pdf.data-cell[⚠ At Risk],
  ),
  [], [Achieve \$2M ARR], [\$1.8M],
  [], [Close 50 enterprise deals], [38],
)
```

![Preview](/assets/docs/X9arJEZz96WVLrKt0YGbjQAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

pdf.data-cell(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

### `cell` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The table cell.

This can be content or a call to [`table.cell`](/docs/reference/model/table/#definitions-cell "`table.cell`").

[![←](/assets/icons/16-chevron-right.svg)

AttachPrevious page](/docs/reference/pdf/attach/) [![→](/assets/icons/16-chevron-right.svg)

Header CellNext page](/docs/reference/pdf/header-cell/)