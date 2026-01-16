# toml

Source: https://typst.app/docs/reference/data-loading/toml/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Data Loading](/docs/reference/data-loading/)
- ![](/assets/icons/16-chevron-right.svg)
- [TOML](/docs/reference/data-loading/toml/)

# `toml`

Reads structured data from a TOML file.

The file must contain a valid TOML table. The TOML values will be converted
into corresponding Typst values as listed in the [table below](#conversion).

The function returns a dictionary representing the TOML table.

The TOML file in the example consists of a table with the keys `title`,
`version`, and `authors`.

## Example

```typst
#let details = toml("details.toml")

Title: #details.title \
Version: #details.version \
Authors: #(details.authors
  .join(", ", last: " and "))
```

![Preview](/assets/docs/f26frHBWUfr7bIomQ1qwWAAAAAAAAAAA.png)

## Conversion details

First of all, TOML documents are tables. Other values must be put in a table
to be encoded or decoded.

| TOML value | Converted into Typst |
| --- | --- |
| string | [`str`](/docs/reference/foundations/str/ "`str`") |
| integer | [`int`](/docs/reference/foundations/int/ "`int`") |
| float | [`float`](/docs/reference/foundations/float/ "`float`") |
| boolean | [`bool`](/docs/reference/foundations/bool/ "`bool`") |
| datetime | [`datetime`](/docs/reference/foundations/datetime/ "`datetime`") |
| array | [`array`](/docs/reference/foundations/array/ "`array`") |
| table | [`dictionary`](/docs/reference/foundations/dictionary/ "`dictionary`") |

| Typst value | Converted into TOML |
| --- | --- |
| types that can be converted from TOML | corresponding TOML value |
| `none` | ignored |
| [`bytes`](/docs/reference/foundations/bytes/ "`bytes`") | string via [`repr`](/docs/reference/foundations/repr/ "`repr`") |
| [`symbol`](/docs/reference/foundations/symbol/ "`symbol`") | string |
| [`content`](/docs/reference/foundations/content/ "`content`") | a table describing the content |
| other types ([`length`](/docs/reference/layout/length/ "`length`"), etc.) | string via [`repr`](/docs/reference/foundations/repr/ "`repr`") |

### Notes

- Be aware that TOML integers larger than 263-1 or smaller
  than -263 cannot be represented losslessly in Typst, and an
  error will be thrown according to the
  [specification](https://toml.io/en/v1.0.0#integer).
- Bytes are not encoded as TOML arrays for performance and readability
  reasons. Consider using [`cbor.encode`](/docs/reference/data-loading/cbor/#definitions-encode "`cbor.encode`") for binary data.
- The `repr` function is [for debugging purposes only](/docs/reference/foundations/repr/#debugging-only),
  and its output is not guaranteed to be stable across Typst versions.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

toml(

[str](/docs/reference/foundations/str/)[bytes](/docs/reference/foundations/bytes/)

) -> [dictionary](/docs/reference/foundations/dictionary/)

### `source` [str](/docs/reference/foundations/str/) or [bytes](/docs/reference/foundations/bytes/) Required Positional Question mark Positional parameters are specified in order, without names.

A [path](/docs/reference/syntax/#paths) to a TOML file or raw TOML bytes.

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `decode` Warning `toml.decode` is deprecated, directly pass bytes to `toml` instead; it will be removed in Typst 0.15.0

Reads structured data from a TOML string/bytes.

toml.decode(

[str](/docs/reference/foundations/str/)[bytes](/docs/reference/foundations/bytes/)

) -> [dictionary](/docs/reference/foundations/dictionary/)

#### `data` [str](/docs/reference/foundations/str/) or [bytes](/docs/reference/foundations/bytes/) Required Positional Question mark Positional parameters are specified in order, without names.

TOML data.

### `encode`

Encodes structured data into a TOML string.

toml.encode(

[dictionary](/docs/reference/foundations/dictionary/),[pretty:](#definitions-encode-pretty) [bool](/docs/reference/foundations/bool/),

) -> [str](/docs/reference/foundations/str/)

#### `value` [dictionary](/docs/reference/foundations/dictionary/) Required Positional Question mark Positional parameters are specified in order, without names.

Value to be encoded.

TOML documents are tables. Therefore, only dictionaries are suitable.

#### `pretty` [bool](/docs/reference/foundations/bool/)

Whether to pretty-print the resulting TOML.

Default: `true`

[![←](/assets/icons/16-chevron-right.svg)

ReadPrevious page](/docs/reference/data-loading/read/) [![→](/assets/icons/16-chevron-right.svg)

XMLNext page](/docs/reference/data-loading/xml/)