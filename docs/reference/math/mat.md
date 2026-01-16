# matElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/math/mat/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Math](/docs/reference/math/)
- ![](/assets/icons/16-chevron-right.svg)
- [Matrix](/docs/reference/math/mat/)

# `mat`Element Question mark Element functions can be customized with `set` and `show` rules.

A matrix.

The elements of a row should be separated by commas, while the rows
themselves should be separated by semicolons. The semicolon syntax merges
preceding arguments separated by commas into an array. You can also use this
special syntax of math function calls to define custom functions that take
2D data.

Content in cells can be aligned with the [`align`](/docs/reference/math/mat/#parameters-align)
parameter, or content in cells that are in the same row can be aligned with
the `&` symbol.

## Example

```
$ mat(
  1, 2, ..., 10;
  2, 2, ..., 10;
  dots.v, dots.v, dots.down, dots.v;
  10, 10, ..., 10;
) $
```

![Preview](/assets/docs/yiSilYGQ1wRBpIK3ON349AAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

math.mat(

[delim:](#parameters-delim) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/)[symbol](/docs/reference/foundations/symbol/),[align:](#parameters-align) [alignment](/docs/reference/layout/alignment/),[augment:](#parameters-augment) [none](/docs/reference/foundations/none/)[int](/docs/reference/foundations/int/)[dictionary](/docs/reference/foundations/dictionary/),[gap:](#parameters-gap) [relative](/docs/reference/layout/relative/),[row-gap:](#parameters-row-gap) [relative](/docs/reference/layout/relative/),[column-gap:](#parameters-column-gap) [relative](/docs/reference/layout/relative/),[..](#parameters-rows)[array](/docs/reference/foundations/array/),

) -> [content](/docs/reference/foundations/content/)

### `delim` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/) or [symbol](/docs/reference/foundations/symbol/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The delimiter to use.

Can be a single character specifying the left delimiter, in which case
the right delimiter is inferred. Otherwise, can be an array containing a
left and a right delimiter.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set math.mat(delim: "[")
$ mat(1, 2; 3, 4) $
```

![Preview](/assets/docs/CpCAX34oIjWq-jvec_NKoQAAAAAAAAAA.png)

Default: `("(", ")")`

### `align` [alignment](/docs/reference/layout/alignment/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The horizontal alignment that each cell should have.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set math.mat(align: right)
$ mat(-1, 1, 1; 1, -1, 1; 1, 1, -1) $
```

![Preview](/assets/docs/X3QXNtgXqEVUQfvJRQOPRwAAAAAAAAAA.png)

Default: `center`

### `augment` [none](/docs/reference/foundations/none/) or [int](/docs/reference/foundations/int/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Draws augmentation lines in a matrix.

- `none`: No lines are drawn.
- A single number: A vertical augmentation line is drawn
  after the specified column number. Negative numbers start from the end.
- A dictionary: With a dictionary, multiple augmentation lines can be
  drawn both horizontally and vertically. Additionally, the style of the
  lines can be set. The dictionary can contain the following keys:
  - `hline`: The offsets at which horizontal lines should be drawn.
    For example, an offset of `2` would result in a horizontal line
    being drawn after the second row of the matrix. Accepts either an
    integer for a single line, or an array of integers
    for multiple lines. Like for a single number, negative numbers start from the end.
  - `vline`: The offsets at which vertical lines should be drawn.
    For example, an offset of `2` would result in a vertical line being
    drawn after the second column of the matrix. Accepts either an
    integer for a single line, or an array of integers
    for multiple lines. Like for a single number, negative numbers start from the end.
  - `stroke`: How to [stroke](/docs/reference/visualize/stroke/) the line. If set to `auto`,
    takes on a thickness of 0.05 em and square line caps.

  ![](/assets/icons/16-chevron-right.svg) View example: Basic usage 

```
$ mat(1, 0, 1; 0, 1, 2; augment: #2) $
// Equivalent to:
$ mat(1, 0, 1; 0, 1, 2; augment: #(-1)) $
```

![Preview](/assets/docs/4iip0Z9ppDA0SxnJHJihkQAAAAAAAAAA.png)

   ![](/assets/icons/16-chevron-right.svg) View example: Customizing the augmentation line 

```
$ mat(0, 0, 0; 1, 1, 1; augment: #(hline: 1, stroke: 2pt + green)) $
```

![Preview](/assets/docs/3PHAJpsviSZ-Rqtb3sBd4AAAAAAAAAAA.png)

Default: `none`

### `gap` [relative](/docs/reference/layout/relative/)

The gap between rows and columns.

This is a shorthand to set `row-gap` and `column-gap` to the same value.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set math.mat(gap: 1em)
$ mat(1, 2; 3, 4) $
```

![Preview](/assets/docs/kaypJSdE1P1lOWZ-cMMpyAAAAAAAAAAA.png)

Default: `0% + 0pt`

### `row-gap` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The gap between rows.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set math.mat(row-gap: 1em)
$ mat(1, 2; 3, 4) $
```

![Preview](/assets/docs/YNVJ8uCnPvrs8e0YkWIQFgAAAAAAAAAA.png)

Default: `0% + 0.2em`

### `column-gap` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The gap between columns.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set math.mat(column-gap: 1em)
$ mat(1, 2; 3, 4) $
```

![Preview](/assets/docs/tKmrTRxYwVIL8x7N4tnRyQAAAAAAAAAA.png)

Default: `0% + 0.5em`

### `rows` [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

An array of arrays with the rows of the matrix.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#let data = ((1, 2, 3), (4, 5, 6))
#let matrix = math.mat(..data)
$ v := matrix $
```

![Preview](/assets/docs/N-7caJ4FsPlOdlVrUrNk9gAAAAAAAAAA.png)

[![←](/assets/icons/16-chevron-right.svg)

Left/RightPrevious page](/docs/reference/math/lr/) [![→](/assets/icons/16-chevron-right.svg)

PrimesNext page](/docs/reference/math/primes/)