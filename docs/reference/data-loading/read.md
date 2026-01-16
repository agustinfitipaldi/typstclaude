# read

Source: https://typst.app/docs/reference/data-loading/read/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Data Loading](/docs/reference/data-loading/)
- ![](/assets/icons/16-chevron-right.svg)
- [Read](/docs/reference/data-loading/read/)

# `read`

Reads plain text or data from a file.

By default, the file will be read as UTF-8 and returned as a [string](/docs/reference/foundations/str/).

If you specify `encoding: none`, this returns raw [bytes](/docs/reference/foundations/bytes/ "bytes") instead.

## Example

```typst
An example for a HTML file: \
#let text = read("example.html")
#raw(text, block: true, lang: "html")

Raw bytes:
#read("tiger.jpg", encoding: none)
```

![Preview](/assets/docs/W-uLL3HdO8kUwcheKma8dwAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

read(

[str](/docs/reference/foundations/str/),[encoding:](#parameters-encoding) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/),

) -> [str](/docs/reference/foundations/str/)[bytes](/docs/reference/foundations/bytes/)

### `path` [str](/docs/reference/foundations/str/) Required Positional Question mark Positional parameters are specified in order, without names.

Path to a file.

For more details, see the [Paths section](/docs/reference/syntax/#paths).

### `encoding` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/)

The encoding to read the file with.

If set to `none`, this function returns raw bytes.

| Variant | Details |
| --- | --- |
| `"utf8"` | The Unicode UTF-8 encoding. |

Default: `"utf8"`

[![←](/assets/icons/16-chevron-right.svg)

JSONPrevious page](/docs/reference/data-loading/json/) [![→](/assets/icons/16-chevron-right.svg)

TOMLNext page](/docs/reference/data-loading/toml/)