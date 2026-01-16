# header-cell

Source: https://typst.app/docs/reference/pdf/header-cell/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [PDF](/docs/reference/pdf/)
- ![](/assets/icons/16-chevron-right.svg)
- [Header Cell](/docs/reference/pdf/header-cell/)

# `header-cell`

Explicitly defines a cell as a header cell.

Header cells help users of Assistive Technology (AT) understand and navigate
complex tables. When your table is correctly marked up with header cells, AT
can announce the relevant header information on-demand when entering a cell.

By default, Typst will automatically mark all cells within [`table.header`](/docs/reference/model/table/#definitions-header "`table.header`")
as header cells. They will apply to the columns below them. You can use that
function's [`level`](/docs/reference/model/table/#definitions-header-level) parameter to make header cells
labelled by other header cells.

The `pdf.header-cell` function allows you to indicate that a cell is a
header cell in the following additional situations:

- You have a **header column** in which each cell applies to its row. In
  that case, you pass `"row"` as an argument to the [`scope`
  parameter](/docs/reference/pdf/header-cell/#parameters-scope) to indicate that the header cell
  applies to the row.
- You have a cell in [`table.header`](/docs/reference/model/table/#definitions-header "`table.header`"), for example at the very start, that
  labels both its row and column. In that case, you pass `"both"` as an
  argument to the [`scope`](/docs/reference/pdf/header-cell/#parameters-scope) parameter.
- You have a header cell in a row not containing other header cells. In that
  case, you can use this function to mark it as a header cell.

The API of this feature is temporary. Hence, calling this function requires
enabling the `a11y-extras` feature flag at the moment. In a future Typst
release, this functionality may move out of the `pdf` module so that tables
in other export targets can contain the same information.

```typst
#show table.cell.where(x: 0): set text(weight: "medium")
#show table.cell.where(y: 0): set text(weight: "bold")

#table(
  columns: 3,
  align: (start, end, end),

  table.header(
    // Top-left cell: Labels both the nutrient rows
    // and the serving size columns.
    pdf.header-cell(scope: "both")[Nutrient],
    [Per 100g],
    [Per Serving],
  ),

  // First column cells are row headers
  pdf.header-cell(scope: "row")[Calories],
  [250 kcal], [375 kcal],
  pdf.header-cell(scope: "row")[Protein],
  [8g], [12g],
  pdf.header-cell(scope: "row")[Fat],
  [12g], [18g],
  pdf.header-cell(scope: "row")[Carbs],
  [30g], [45g],
)
```

![Preview](/assets/docs/QfmsuzSQVT1unTcb1epxjwAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

pdf.header-cell(

[level:](#parameters-level) [int](/docs/reference/foundations/int/),[scope:](#parameters-scope) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `level` [int](/docs/reference/foundations/int/)

The nesting level of this header cell.

Default: `1`

### `scope` [str](/docs/reference/foundations/str/)

What track of the table this header cell applies to.

| Variant | Details |
| --- | --- |
| `"both"` | The header cell refers to both the row and the column. |
| `"column"` | The header cell refers to the column. |
| `"row"` | The header cell refers to the row. |

Default: `"column"`

### `cell` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The table cell.

This can be content or a call to [`table.cell`](/docs/reference/model/table/#definitions-cell "`table.cell`").

[![←](/assets/icons/16-chevron-right.svg)

Data CellPrevious page](/docs/reference/pdf/data-cell/) [![→](/assets/icons/16-chevron-right.svg)

Table SummaryNext page](/docs/reference/pdf/table-summary/)