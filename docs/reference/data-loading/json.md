# json

Source: https://typst.app/docs/reference/data-loading/json/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Data Loading](/docs/reference/data-loading/)
- ![](/assets/icons/16-chevron-right.svg)
- [JSON](/docs/reference/data-loading/json/)

# `json`

Reads structured data from a JSON file.

The file must contain a valid JSON value, such as object or array. The JSON
values will be converted into corresponding Typst values as listed in the
[table below](#conversion).

The function returns a dictionary, an array or, depending on the JSON file,
another JSON data type.

The JSON files in the example contain objects with the keys `temperature`,
`unit`, and `weather`.

## Example

```typst
#let forecast(day) = block[
  #box(square(
    width: 2cm,
    inset: 8pt,
    fill: if day.weather == "sunny" {
      yellow
    } else {
      aqua
    },
    align(
      bottom + right,
      strong(day.weather),
    ),
  ))
  #h(6pt)
  #set text(22pt, baseline: -8pt)
  #day.temperature °#day.unit
]

#forecast(json("monday.json"))
#forecast(json("tuesday.json"))
```

![Preview](/assets/docs/9TGGThvdnznDbVRRo5-HsgAAAAAAAAAA.png)

## Conversion details

| JSON value | Converted into Typst |
| --- | --- |
| `null` | `none` |
| bool | [`bool`](/docs/reference/foundations/bool/ "`bool`") |
| number | [`float`](/docs/reference/foundations/float/ "`float`") or [`int`](/docs/reference/foundations/int/ "`int`") |
| string | [`str`](/docs/reference/foundations/str/ "`str`") |
| array | [`array`](/docs/reference/foundations/array/ "`array`") |
| object | [`dictionary`](/docs/reference/foundations/dictionary/ "`dictionary`") |

| Typst value | Converted into JSON |
| --- | --- |
| types that can be converted from JSON | corresponding JSON value |
| [`bytes`](/docs/reference/foundations/bytes/ "`bytes`") | string via [`repr`](/docs/reference/foundations/repr/ "`repr`") |
| [`symbol`](/docs/reference/foundations/symbol/ "`symbol`") | string |
| [`content`](/docs/reference/foundations/content/ "`content`") | an object describing the content |
| other types ([`length`](/docs/reference/layout/length/ "`length`"), etc.) | string via [`repr`](/docs/reference/foundations/repr/ "`repr`") |

### Notes

- In most cases, JSON numbers will be converted to floats or integers
  depending on whether they are whole numbers. However, be aware that
  integers larger than 263-1 or smaller than -263 will
  be converted to floating-point numbers, which may result in an
  approximative value.
- Bytes are not encoded as JSON arrays for performance and readability
  reasons. Consider using [`cbor.encode`](/docs/reference/data-loading/cbor/#definitions-encode "`cbor.encode`") for binary data.
- The `repr` function is [for debugging purposes only](/docs/reference/foundations/repr/#debugging-only),
  and its output is not guaranteed to be stable across Typst versions.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

json(

[str](/docs/reference/foundations/str/)[bytes](/docs/reference/foundations/bytes/)

) -> any

### `source` [str](/docs/reference/foundations/str/) or [bytes](/docs/reference/foundations/bytes/) Required Positional Question mark Positional parameters are specified in order, without names.

A [path](/docs/reference/syntax/#paths) to a JSON file or raw JSON bytes.

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `decode` Warning `json.decode` is deprecated, directly pass bytes to `json` instead; it will be removed in Typst 0.15.0

Reads structured data from a JSON string/bytes.

json.decode(

[str](/docs/reference/foundations/str/)[bytes](/docs/reference/foundations/bytes/)

) -> any

#### `data` [str](/docs/reference/foundations/str/) or [bytes](/docs/reference/foundations/bytes/) Required Positional Question mark Positional parameters are specified in order, without names.

JSON data.

### `encode`

Encodes structured data into a JSON string.

json.encode(

any,[pretty:](#definitions-encode-pretty) [bool](/docs/reference/foundations/bool/),

) -> [str](/docs/reference/foundations/str/)

#### `value` any Required Positional Question mark Positional parameters are specified in order, without names.

Value to be encoded.

#### `pretty` [bool](/docs/reference/foundations/bool/)

Whether to pretty print the JSON with newlines and indentation.

Default: `true`

[![←](/assets/icons/16-chevron-right.svg)

CSVPrevious page](/docs/reference/data-loading/csv/) [![→](/assets/icons/16-chevron-right.svg)

ReadNext page](/docs/reference/data-loading/read/)