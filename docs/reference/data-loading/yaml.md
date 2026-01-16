# yaml

Source: https://typst.app/docs/reference/data-loading/yaml/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Data Loading](/docs/reference/data-loading/)
- ![](/assets/icons/16-chevron-right.svg)
- [YAML](/docs/reference/data-loading/yaml/)

# `yaml`

Reads structured data from a YAML file.

The file must contain a valid YAML object or array. The YAML values will be
converted into corresponding Typst values as listed in the
[table below](#conversion).

The function returns a dictionary, an array or, depending on the YAML file,
another YAML data type.

The YAML files in the example contain objects with authors as keys,
each with a sequence of their own submapping with the keys
"title" and "published".

## Example

```typst
#let bookshelf(contents) = {
  for (author, works) in contents {
    author
    for work in works [
      - #work.title (#work.published)
    ]
  }
}

#bookshelf(
  yaml("scifi-authors.yaml")
)
```

![Preview](/assets/docs/zhzvOjbNeHnb4ZYJg032GwAAAAAAAAAA.png)

## Conversion details

| YAML value | Converted into Typst |
| --- | --- |
| null-values (`null`, `~` or empty ) | `none` |
| boolean | [`bool`](/docs/reference/foundations/bool/ "`bool`") |
| number | [`float`](/docs/reference/foundations/float/ "`float`") or [`int`](/docs/reference/foundations/int/ "`int`") |
| string | [`str`](/docs/reference/foundations/str/ "`str`") |
| sequence | [`array`](/docs/reference/foundations/array/ "`array`") |
| mapping | [`dictionary`](/docs/reference/foundations/dictionary/ "`dictionary`") |

| Typst value | Converted into YAML |
| --- | --- |
| types that can be converted from YAML | corresponding YAML value |
| [`bytes`](/docs/reference/foundations/bytes/ "`bytes`") | string via [`repr`](/docs/reference/foundations/repr/ "`repr`") |
| [`symbol`](/docs/reference/foundations/symbol/ "`symbol`") | string |
| [`content`](/docs/reference/foundations/content/ "`content`") | a mapping describing the content |
| other types ([`length`](/docs/reference/layout/length/ "`length`"), etc.) | string via [`repr`](/docs/reference/foundations/repr/ "`repr`") |

### Notes

- In most cases, YAML numbers will be converted to floats or integers
  depending on whether they are whole numbers. However, be aware that
  integers larger than 263-1 or smaller than -263 will
  be converted to floating-point numbers, which may result in an
  approximative value.
- Custom YAML tags are ignored, though the loaded value will still be present.
- Bytes are not encoded as YAML sequences for performance and readability
  reasons. Consider using [`cbor.encode`](/docs/reference/data-loading/cbor/#definitions-encode "`cbor.encode`") for binary data.
- The `repr` function is [for debugging purposes only](/docs/reference/foundations/repr/#debugging-only),
  and its output is not guaranteed to be stable across Typst versions.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

yaml(

[str](/docs/reference/foundations/str/)[bytes](/docs/reference/foundations/bytes/)

) -> any

### `source` [str](/docs/reference/foundations/str/) or [bytes](/docs/reference/foundations/bytes/) Required Positional Question mark Positional parameters are specified in order, without names.

A [path](/docs/reference/syntax/#paths) to a YAML file or raw YAML bytes.

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `decode` Warning `yaml.decode` is deprecated, directly pass bytes to `yaml` instead; it will be removed in Typst 0.15.0

Reads structured data from a YAML string/bytes.

yaml.decode(

[str](/docs/reference/foundations/str/)[bytes](/docs/reference/foundations/bytes/)

) -> any

#### `data` [str](/docs/reference/foundations/str/) or [bytes](/docs/reference/foundations/bytes/) Required Positional Question mark Positional parameters are specified in order, without names.

YAML data.

### `encode`

Encode structured data into a YAML string.

yaml.encode(

any

) -> [str](/docs/reference/foundations/str/)

#### `value` any Required Positional Question mark Positional parameters are specified in order, without names.

Value to be encoded.

[![←](/assets/icons/16-chevron-right.svg)

XMLPrevious page](/docs/reference/data-loading/xml/) [![→](/assets/icons/16-chevron-right.svg)

PDFNext page](/docs/reference/pdf/)