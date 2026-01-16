# cbor

Source: https://typst.app/docs/reference/data-loading/cbor/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Data Loading](/docs/reference/data-loading/)
- ![](/assets/icons/16-chevron-right.svg)
- [CBOR](/docs/reference/data-loading/cbor/)

# `cbor`

Reads structured data from a CBOR file.

The file must contain a valid CBOR serialization. The CBOR values will be
converted into corresponding Typst values as listed in the
[table below](#conversion).

The function returns a dictionary, an array or, depending on the CBOR file,
another CBOR data type.

## Conversion details

| CBOR value | Converted into Typst |
| --- | --- |
| integer | [`int`](/docs/reference/foundations/int/ "`int`") (or [`float`](/docs/reference/foundations/float/ "`float`")) |
| bytes | [`bytes`](/docs/reference/foundations/bytes/ "`bytes`") |
| float | [`float`](/docs/reference/foundations/float/ "`float`") |
| text | [`str`](/docs/reference/foundations/str/ "`str`") |
| bool | [`bool`](/docs/reference/foundations/bool/ "`bool`") |
| null | `none` |
| array | [`array`](/docs/reference/foundations/array/ "`array`") |
| map | [`dictionary`](/docs/reference/foundations/dictionary/ "`dictionary`") |

| Typst value | Converted into CBOR |
| --- | --- |
| types that can be converted from CBOR | corresponding CBOR value |
| [`symbol`](/docs/reference/foundations/symbol/ "`symbol`") | text |
| [`content`](/docs/reference/foundations/content/ "`content`") | a map describing the content |
| other types ([`length`](/docs/reference/layout/length/ "`length`"), etc.) | text via [`repr`](/docs/reference/foundations/repr/ "`repr`") |

### Notes

- Be aware that CBOR integers larger than 263-1 or smaller than
  -263 will be converted to floating point numbers, which may
  result in an approximative value.
- CBOR tags are not supported, and an error will be thrown.
- The `repr` function is [for debugging purposes only](/docs/reference/foundations/repr/#debugging-only),
  and its output is not guaranteed to be stable across Typst versions.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

cbor(

[str](/docs/reference/foundations/str/)[bytes](/docs/reference/foundations/bytes/)

) -> any

### `source` [str](/docs/reference/foundations/str/) or [bytes](/docs/reference/foundations/bytes/) Required Positional Question mark Positional parameters are specified in order, without names.

A [path](/docs/reference/syntax/#paths) to a CBOR file or raw CBOR bytes.

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `decode` Warning `cbor.decode` is deprecated, directly pass bytes to `cbor` instead; it will be removed in Typst 0.15.0

Reads structured data from CBOR bytes.

cbor.decode(

[bytes](/docs/reference/foundations/bytes/)

) -> any

#### `data` [bytes](/docs/reference/foundations/bytes/) Required Positional Question mark Positional parameters are specified in order, without names.

CBOR data.

### `encode`

Encode structured data into CBOR bytes.

cbor.encode(

any

) -> [bytes](/docs/reference/foundations/bytes/)

#### `value` any Required Positional Question mark Positional parameters are specified in order, without names.

Value to be encoded.

[![←](/assets/icons/16-chevron-right.svg)

Data LoadingPrevious page](/docs/reference/data-loading/) [![→](/assets/icons/16-chevron-right.svg)

CSVNext page](/docs/reference/data-loading/csv/)