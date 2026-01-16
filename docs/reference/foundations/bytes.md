# bytes

Source: https://typst.app/docs/reference/foundations/bytes/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Foundations](/docs/reference/foundations/)
- ![](/assets/icons/16-chevron-right.svg)
- [Bytes](/docs/reference/foundations/bytes/)

# bytes

A sequence of bytes.

This is conceptually similar to an array of [integers](/docs/reference/foundations/int/) between `0`
and `255`, but represented much more efficiently. You can iterate over it
using a [for loop](/docs/reference/scripting/#loops).

You can convert

- a [string](/docs/reference/foundations/str/) or an [array](/docs/reference/foundations/array/ "array") of integers to bytes with the [`bytes`](/docs/reference/foundations/bytes/ "`bytes`")
  constructor
- bytes to a string with the [`str`](/docs/reference/foundations/str/ "`str`") constructor, with UTF-8 encoding
- bytes to an array of integers with the [`array`](/docs/reference/foundations/array/ "`array`") constructor

When [reading](/docs/reference/data-loading/read/) data from a file, you can decide whether to load it
as a string or as raw bytes.

```typst
#bytes((123, 160, 22, 0)) \
#bytes("Hello 😃")

#let data = read(
  "rhino.png",
  encoding: none,
)

// Magic bytes.
#array(data.slice(0, 4)) \
#str(data.slice(1, 4))
```

![Preview](/assets/docs/sJtYFgVyQkDZELEHje5ywwAAAAAAAAAA.png)

## Constructor Question mark If a type has a constructor, you can call it like a function to create a new value of the type.

Converts a value to bytes.

- Strings are encoded in UTF-8.
- Arrays of integers between `0` and `255` are converted directly. The
  dedicated byte representation is much more efficient than the array
  representation and thus typically used for large byte buffers (e.g. image
  data).

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#bytes("Hello 😃") \
#bytes((123, 160, 22, 0))
```

![Preview](/assets/docs/PlfVajGmfDLMY6p8X4S3BwAAAAAAAAAA.png)

bytes(

[str](/docs/reference/foundations/str/)[bytes](/docs/reference/foundations/bytes/)[array](/docs/reference/foundations/array/)

) -> [bytes](/docs/reference/foundations/bytes/)

#### `value` [str](/docs/reference/foundations/str/) or [bytes](/docs/reference/foundations/bytes/) or [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names.

The value that should be converted to bytes.

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `len`

The length in bytes.

self.len() -> [int](/docs/reference/foundations/int/)

### `at`

Returns the byte at the specified index. Returns the default value if
the index is out of bounds or fails with an error if no default value
was specified.

self.at(

[int](/docs/reference/foundations/int/),[default:](#definitions-at-default) any,

) -> any

#### `index` [int](/docs/reference/foundations/int/) Required Positional Question mark Positional parameters are specified in order, without names.

The index at which to retrieve the byte.

#### `default` any

A default value to return if the index is out of bounds.

### `slice`

Extracts a subslice of the bytes. Fails with an error if the start or
end index is out of bounds.

self.slice(

[int](/docs/reference/foundations/int/),[none](/docs/reference/foundations/none/)[int](/docs/reference/foundations/int/),[count:](#definitions-slice-count) [int](/docs/reference/foundations/int/),

) -> [bytes](/docs/reference/foundations/bytes/)

#### `start` [int](/docs/reference/foundations/int/) Required Positional Question mark Positional parameters are specified in order, without names.

The start index (inclusive).

#### `end` [none](/docs/reference/foundations/none/) or [int](/docs/reference/foundations/int/) Positional Question mark Positional parameters are specified in order, without names.

The end index (exclusive). If omitted, the whole slice until the end
is extracted.

Default: `none`

#### `count` [int](/docs/reference/foundations/int/)

The number of items to extract. This is equivalent to passing
`start + count` as the `end` position. Mutually exclusive with
`end`.

[![←](/assets/icons/16-chevron-right.svg)

BooleanPrevious page](/docs/reference/foundations/bool/) [![→](/assets/icons/16-chevron-right.svg)

CalculationNext page](/docs/reference/foundations/calc/)