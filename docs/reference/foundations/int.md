# int

Source: https://typst.app/docs/reference/foundations/int/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Foundations](/docs/reference/foundations/)
- ![](/assets/icons/16-chevron-right.svg)
- [Integer](/docs/reference/foundations/int/)

# int

A whole number.

The number can be negative, zero, or positive. As Typst uses 64 bits to
store integers, integers cannot be smaller than `-9223372036854775808` or
larger than `9223372036854775807`. Integer literals are always positive,
so a negative integer such as `-1` is semantically the negation `-` of the
positive literal `1`. A positive integer greater than the maximum value and
a negative integer less than or equal to the minimum value cannot be
represented as an integer literal, and are instead parsed as a `float`.
The minimum integer value can still be obtained through integer arithmetic.

The number can also be specified as hexadecimal, octal, or binary by
starting it with a zero followed by either `x`, `o`, or `b`.

You can convert a value to an integer with this type's constructor.

## Example

```typst
#(1 + 2) \
#(2 - 5) \
#(3 + 4 < 8)

#0xff \
#0o10 \
#0b1001
```

![Preview](/assets/docs/wfpxRJDZrNeGDA3RjEgFJgAAAAAAAAAA.png)

## Constructor Question mark If a type has a constructor, you can call it like a function to create a new value of the type.

Converts a value to an integer. Raises an error if there is an attempt
to produce an integer larger than the maximum 64-bit signed integer
or smaller than the minimum 64-bit signed integer.

- Booleans are converted to `0` or `1`.
- Floats and decimals are rounded to the next 64-bit integer towards zero.
- Strings are parsed in base 10.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#int(false) \
#int(true) \
#int(2.7) \
#int(decimal("3.8")) \
#(int("27") + int("4"))
```

![Preview](/assets/docs/4vDM_wHvGAGqziHd9y2LQQAAAAAAAAAA.png)

int(

[bool](/docs/reference/foundations/bool/)[int](/docs/reference/foundations/int/)[float](/docs/reference/foundations/float/)[str](/docs/reference/foundations/str/)[decimal](/docs/reference/foundations/decimal/)

) -> [int](/docs/reference/foundations/int/)

#### `value` [bool](/docs/reference/foundations/bool/) or [int](/docs/reference/foundations/int/) or [float](/docs/reference/foundations/float/) or [str](/docs/reference/foundations/str/) or [decimal](/docs/reference/foundations/decimal/) Required Positional Question mark Positional parameters are specified in order, without names.

The value that should be converted to an integer.

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `signum`

Calculates the sign of an integer.

- If the number is positive, returns `1`.
- If the number is negative, returns `-1`.
- If the number is zero, returns `0`.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#(5).signum() \
#(-5).signum() \
#(0).signum()
```

![Preview](/assets/docs/Vicm2VF6Z98sgjNZQYlaBgAAAAAAAAAA.png)

self.signum() -> [int](/docs/reference/foundations/int/)

### `bit-not`

Calculates the bitwise NOT of an integer.

For the purposes of this function, the operand is treated as a signed
integer of 64 bits.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#4.bit-not() \
#(-1).bit-not()
```

![Preview](/assets/docs/3AYO-p6E-z3VLH4vNyWEKgAAAAAAAAAA.png)

self.bit-not() -> [int](/docs/reference/foundations/int/)

### `bit-and`

Calculates the bitwise AND between two integers.

For the purposes of this function, the operands are treated as signed
integers of 64 bits.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#128.bit-and(192)
```

![Preview](/assets/docs/knwTrW-Xbj5sqbcdza7ewgAAAAAAAAAA.png)

self.bit-and(

[int](/docs/reference/foundations/int/)

) -> [int](/docs/reference/foundations/int/)

#### `rhs` [int](/docs/reference/foundations/int/) Required Positional Question mark Positional parameters are specified in order, without names.

The right-hand operand of the bitwise AND.

### `bit-or`

Calculates the bitwise OR between two integers.

For the purposes of this function, the operands are treated as signed
integers of 64 bits.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#64.bit-or(32)
```

![Preview](/assets/docs/zaVKMztfj-8VIfbLXeJFUAAAAAAAAAAA.png)

self.bit-or(

[int](/docs/reference/foundations/int/)

) -> [int](/docs/reference/foundations/int/)

#### `rhs` [int](/docs/reference/foundations/int/) Required Positional Question mark Positional parameters are specified in order, without names.

The right-hand operand of the bitwise OR.

### `bit-xor`

Calculates the bitwise XOR between two integers.

For the purposes of this function, the operands are treated as signed
integers of 64 bits.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#64.bit-xor(96)
```

![Preview](/assets/docs/KUPqsOL5IXWcGSfAhFpL6wAAAAAAAAAA.png)

self.bit-xor(

[int](/docs/reference/foundations/int/)

) -> [int](/docs/reference/foundations/int/)

#### `rhs` [int](/docs/reference/foundations/int/) Required Positional Question mark Positional parameters are specified in order, without names.

The right-hand operand of the bitwise XOR.

### `bit-lshift`

Shifts the operand's bits to the left by the specified amount.

For the purposes of this function, the operand is treated as a signed
integer of 64 bits. An error will occur if the result is too large to
fit in a 64-bit integer.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#33.bit-lshift(2) \
#(-1).bit-lshift(3)
```

![Preview](/assets/docs/kIVISyJsbGpK3k_fu59O2AAAAAAAAAAA.png)

self.bit-lshift(

[int](/docs/reference/foundations/int/)

) -> [int](/docs/reference/foundations/int/)

#### `shift` [int](/docs/reference/foundations/int/) Required Positional Question mark Positional parameters are specified in order, without names.

The amount of bits to shift. Must not be negative.

### `bit-rshift`

Shifts the operand's bits to the right by the specified amount.
Performs an arithmetic shift by default (extends the sign bit to the left,
such that negative numbers stay negative), but that can be changed by the
`logical` parameter.

For the purposes of this function, the operand is treated as a signed
integer of 64 bits.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#64.bit-rshift(2) \
#(-8).bit-rshift(2) \
#(-8).bit-rshift(2, logical: true)
```

![Preview](/assets/docs/gebaB-CZOzDtnvfjDfjtTgAAAAAAAAAA.png)

self.bit-rshift(

[int](/docs/reference/foundations/int/),[logical:](#definitions-bit-rshift-logical) [bool](/docs/reference/foundations/bool/),

) -> [int](/docs/reference/foundations/int/)

#### `shift` [int](/docs/reference/foundations/int/) Required Positional Question mark Positional parameters are specified in order, without names.

The amount of bits to shift. Must not be negative.

Shifts larger than 63 are allowed and will cause the return value to
saturate. For non-negative numbers, the return value saturates at
`0`, while, for negative numbers, it saturates at `-1` if
`logical` is set to `false`, or `0` if it is `true`. This
behavior is consistent with just applying this operation multiple
times. Therefore, the shift will always succeed.

#### `logical` [bool](/docs/reference/foundations/bool/)

Toggles whether a logical (unsigned) right shift should be performed
instead of arithmetic right shift.
If this is `true`, negative operands will not preserve their sign
bit, and bits which appear to the left after the shift will be
`0`. This parameter has no effect on non-negative operands.

Default: `false`

### `from-bytes`

Converts bytes to an integer.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#int.from-bytes(bytes((0, 0, 0, 0, 0, 0, 0, 1))) \
#int.from-bytes(bytes((1, 0, 0, 0, 0, 0, 0, 0)), endian: "big")
```

![Preview](/assets/docs/I0LPQ0WUii0fthcD20cosAAAAAAAAAAA.png)

int.from-bytes(

[bytes](/docs/reference/foundations/bytes/),[endian:](#definitions-from-bytes-endian) [str](/docs/reference/foundations/str/),[signed:](#definitions-from-bytes-signed) [bool](/docs/reference/foundations/bool/),

) -> [int](/docs/reference/foundations/int/)

#### `bytes` [bytes](/docs/reference/foundations/bytes/) Required Positional Question mark Positional parameters are specified in order, without names.

The bytes that should be converted to an integer.

Must be of length at most 8 so that the result fits into a 64-bit
signed integer.

#### `endian` [str](/docs/reference/foundations/str/)

The endianness of the conversion.

| Variant | Details |
| --- | --- |
| `"big"` | Big-endian byte order: The highest-value byte is at the beginning of the bytes. |
| `"little"` | Little-endian byte order: The lowest-value byte is at the beginning of the bytes. |

Default: `"little"`

#### `signed` [bool](/docs/reference/foundations/bool/)

Whether the bytes should be treated as a signed integer. If this is
`true` and the most significant bit is set, the resulting number
will negative.

Default: `true`

### `to-bytes`

Converts an integer to bytes.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#array(10000.to-bytes(endian: "big")) \
#array(10000.to-bytes(size: 4))
```

![Preview](/assets/docs/FF7gGW4eVOEhYjIZXy8BIgAAAAAAAAAA.png)

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

The size in bytes of the resulting bytes (must be at least zero). If
the integer is too large to fit in the specified size, the
conversion will truncate the remaining bytes based on the
endianness. To keep the same resulting value, if the endianness is
big-endian, the truncation will happen at the rightmost bytes.
Otherwise, if the endianness is little-endian, the truncation will
happen at the leftmost bytes.

Be aware that if the integer is negative and the size is not enough
to make the number fit, when passing the resulting bytes to
`int.from-bytes`, the resulting number might be positive, as the
most significant bit might not be set to 1.

Default: `8`

[![←](/assets/icons/16-chevron-right.svg)

FunctionPrevious page](/docs/reference/foundations/function/) [![→](/assets/icons/16-chevron-right.svg)

LabelNext page](/docs/reference/foundations/label/)