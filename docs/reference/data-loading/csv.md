# csv

Source: https://typst.app/docs/reference/data-loading/csv/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Data Loading](/docs/reference/data-loading/)
- ![](/assets/icons/16-chevron-right.svg)
- [CSV](/docs/reference/data-loading/csv/)

# `csv`

Reads structured data from a CSV file.

The CSV file will be read and parsed into a 2-dimensional array of strings:
Each row in the CSV file will be represented as an array of strings, and all
rows will be collected into a single array. Header rows will not be
stripped.

## Example

```typst
#let results = csv("example.csv")

#table(
  columns: 2,
  [*Condition*], [*Result*],
  ..results.flatten(),
)
```

![Preview](/assets/docs/wZK4j33X4RoMvhQZsQnpmQAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

csv(

[str](/docs/reference/foundations/str/)[bytes](/docs/reference/foundations/bytes/),[delimiter:](#parameters-delimiter) [str](/docs/reference/foundations/str/),[row-type:](#parameters-row-type) [type](/docs/reference/foundations/type/),

) -> [array](/docs/reference/foundations/array/)

### `source` [str](/docs/reference/foundations/str/) or [bytes](/docs/reference/foundations/bytes/) Required Positional Question mark Positional parameters are specified in order, without names.

A [path](/docs/reference/syntax/#paths) to a CSV file or raw CSV bytes.

### `delimiter` [str](/docs/reference/foundations/str/)

The delimiter that separates columns in the CSV file.
Must be a single ASCII character.

Default: `","`

### `row-type` [type](/docs/reference/foundations/type/)

How to represent the file's rows.

- If set to `array`, each row is represented as a plain array of
  strings.
- If set to `dictionary`, each row is represented as a dictionary
  mapping from header keys to strings. This option only makes sense when
  a header row is present in the CSV file.

Default: `array`

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `decode` Warning `csv.decode` is deprecated, directly pass bytes to `csv` instead; it will be removed in Typst 0.15.0

Reads structured data from a CSV string/bytes.

csv.decode(

[str](/docs/reference/foundations/str/)[bytes](/docs/reference/foundations/bytes/),[delimiter:](#definitions-decode-delimiter) [str](/docs/reference/foundations/str/),[row-type:](#definitions-decode-row-type) [type](/docs/reference/foundations/type/),

) -> [array](/docs/reference/foundations/array/)

#### `data` [str](/docs/reference/foundations/str/) or [bytes](/docs/reference/foundations/bytes/) Required Positional Question mark Positional parameters are specified in order, without names.

CSV data.

#### `delimiter` [str](/docs/reference/foundations/str/)

The delimiter that separates columns in the CSV file.
Must be a single ASCII character.

Default: `","`

#### `row-type` [type](/docs/reference/foundations/type/)

How to represent the file's rows.

- If set to `array`, each row is represented as a plain array of
  strings.
- If set to `dictionary`, each row is represented as a dictionary
  mapping from header keys to strings. This option only makes sense
  when a header row is present in the CSV file.

Default: `array`

[![←](/assets/icons/16-chevron-right.svg)

CBORPrevious page](/docs/reference/data-loading/cbor/) [![→](/assets/icons/16-chevron-right.svg)

JSONNext page](/docs/reference/data-loading/json/)