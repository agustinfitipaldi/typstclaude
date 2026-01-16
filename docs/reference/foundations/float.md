# float

Source: https://typst.app/docs/reference/foundations/float/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Foundations](/docs/reference/foundations/)
- ![](/assets/icons/16-chevron-right.svg)
- [Float](/docs/reference/foundations/float/)

# float

A floating-point number.

A limited-precision representation of a real number. Typst uses 64 bits to
store floats. Wherever a float is expected, you can also pass an
[integer](/docs/reference/foundations/int/).

You can convert a value to a float with this type's constructor.

NaN and positive infinity are available as `float.nan` and `float.inf`
respectively.

## Example

```typst
#3.14 \
#1e4 \
#(10 / 4)
```

![Preview](/assets/docs/Oh7PyPKhSHHcwVH4CSb0KwAAAAAAAAAA.png)

## Constructor Question mark If a type has a constructor, you can call it like a function to create a new value of the type.

Converts a value to a float.

- Booleans are converted to `0.0` or `1.0`.
- Integers are converted to the closest 64-bit float. For integers with
  absolute value less than `calc.pow(2, 53)`, this conversion is
  exact.
- Ratios are divided by 100%.
- Strings are parsed in base 10 to the closest 64-bit float. Exponential
  notation is supported.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#float(false) \
#float(true) \
#float(4) \
#float(40%) \
#float("2.7") \
#float("1e5")
```

![Preview](/assets/docs/PMa-HqZaL4--FN_1I0OHagAAAAAAAAAA.png)

float(

[bool](/docs/reference/foundations/bool/)[int](/docs/reference/foundations/int/)[float](/docs/reference/foundations/float/)[ratio](/docs/reference/layout/ratio/)[str](/docs/reference/foundations/str/)[decimal](/docs/reference/foundations/decimal/)

) -> [float](/docs/reference/foundations/float/)

#### `value` [bool](/docs/reference/foundations/bool/) or [int](/docs/reference/foundations/int/) or [float](/docs/reference/foundations/float/) or [ratio](/docs/reference/layout/ratio/) or [str](/docs/reference/foundations/str/) or [decimal](/docs/reference/foundations/decimal/) Required Positional Question mark Positional parameters are specified in order, without names.

The value that should be converted to a float.

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `is-nan`

Checks if a float is not a number.

In IEEE 754, more than one bit pattern represents a NaN. This function
returns `true` if the float is any of those bit patterns.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#float.is-nan(0) \
#float.is-nan(1) \
#float.is-nan(float.nan)
```

![Preview](/assets/docs/9jd8hxPcunH7CdCSXWd1dwAAAAAAAAAA.png)

self.is-nan() -> [bool](/docs/reference/foundations/bool/)

### `is-infinite`

Checks if a float is infinite.

Floats can represent positive infinity and negative infinity. This
function returns `true` if the float is an infinity.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#float.is-infinite(0) \
#float.is-infinite(1) \
#float.is-infinite(float.inf)
```

![Preview](/assets/docs/AIoKhvpoq-xeueiSPD9O7gAAAAAAAAAA.png)

self.is-infinite() -> [bool](/docs/reference/foundations/bool/)

### `signum`

Calculates the sign of a floating point number.

- If the number is positive (including `+0.0`), returns `1.0`.
- If the number is negative (including `-0.0`), returns `-1.0`.
- If the number is NaN, returns `float.nan`.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#(5.0).signum() \
#(-5.0).signum() \
#(0.0).signum() \
#float.nan.signum()
```

![Preview](/assets/docs/HHp-pldXJoLbqAEsg_2mmQAAAAAAAAAA.png)

self.signum() -> [float](/docs/reference/foundations/float/)

### `from-bytes`

Interprets bytes as a float.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#float.from-bytes(bytes((0, 0, 0, 0, 0, 0, 240, 63))) \
#float.from-bytes(bytes((63, 240, 0, 0, 0, 0, 0, 0)), endian: "big")
```

![Preview](/assets/docs/TbCinqru71JKOm73kOJYdwAAAAAAAAAA.png)

float.from-bytes(

[bytes](/docs/reference/foundations/bytes/),[endian:](#definitions-from-bytes-endian) [str](/docs/reference/foundations/str/),

) -> [float](/docs/reference/foundations/float/)

#### `bytes` [bytes](/docs/reference/foundations/bytes/) Required Positional Question mark Positional parameters are specified in order, without names.

The bytes that should be converted to a float.

Must have a length of either 4 or 8. The bytes are then
interpreted in [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754)'s
binary32 (single-precision) or binary64 (double-precision) format
depending on the length of the bytes.

#### `endian` [str](/docs/reference/foundations/str/)

The endianness of the conversion.

| Variant | Details |
| --- | --- |
| `"big"` | Big-endian byte order: The highest-value byte is at the beginning of the bytes. |
| `"little"` | Little-endian byte order: The lowest-value byte is at the beginning of the bytes. |

Default: `"little"`

### `to-bytes`

Converts a float to bytes.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#array(1.0.to-bytes(endian: "big")) \
#array(1.0.to-bytes())
```

![Preview](/assets/docs/oyz50tHIOoQRj_5WM6JIbAAAAAAAAAAA.png)

self.to-bytes(

[endian:](#definitions-to-bytes-endian) [str](/docs/reference/foundations/str/),[size:](#definitions-to-bytes-size) [int](/docs/reference/foundations/int/),

) -> [bytes](/docs/reference/foundations/bytes/)

#### `endian` [str](/docs/reference/foundations/str/)

The endianness of the conversion.

| Variant | Details |
| --- | --- |
| `"big"` | Big-endian byte order: The highest-value byte is at the beginning of the bytes. |
| `"little"` | Little-endian byte order: The lowest-value byte is at the beginning of the bytes. |

Default: `"little"`

#### `size` [int](/docs/reference/foundations/int/)

The size of the resulting bytes.

This must be either 4 or 8. The call will return the
representation of this float in either
[IEEE 754](https://en.wikipedia.org/wiki/IEEE_754)'s binary32
(single-precision) or binary64 (double-precision) format
depending on the provided size.

Default: `8`

[![←](/assets/icons/16-chevron-right.svg)

EvaluatePrevious page](/docs/reference/foundations/eval/) [![→](/assets/icons/16-chevron-right.svg)

FunctionNext page](/docs/reference/foundations/function/)