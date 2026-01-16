# vecElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/math/vec/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Math](/docs/reference/math/)
- ![](/assets/icons/16-chevron-right.svg)
- [Vector](/docs/reference/math/vec/)

# `vec`Element Question mark Element functions can be customized with `set` and `show` rules.

A column vector.

Content in the vector's elements can be aligned with the
[`align`](/docs/reference/math/vec/#parameters-align) parameter, or the `&` symbol.

This function is for typesetting vector components. To typeset a symbol that
represents a vector, [`arrow`](/docs/reference/math/accent/) and [`bold`](/docs/reference/math/styles/#functions-bold) are
commonly used.

## Example

```
$ vec(a, b, c) dot vec(1, 2, 3)
    = a + 2b + 3c $
```

![Preview](/assets/docs/LnRm06lLMggD8fCQZdA66QAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

math.vec(

[delim:](#parameters-delim) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/)[symbol](/docs/reference/foundations/symbol/),[align:](#parameters-align) [alignment](/docs/reference/layout/alignment/),[gap:](#parameters-gap) [relative](/docs/reference/layout/relative/),[..](#parameters-children)[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `delim` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/) or [symbol](/docs/reference/foundations/symbol/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The delimiter to use.

Can be a single character specifying the left delimiter, in which case
the right delimiter is inferred. Otherwise, can be an array containing a
left and a right delimiter.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set math.vec(delim: "[")
$ vec(1, 2) $
```

![Preview](/assets/docs/5LFZJ9d25bljXFp6kARHcgAAAAAAAAAA.png)

Default: `("(", ")")`

### `align` [alignment](/docs/reference/layout/alignment/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The horizontal alignment that each element should have.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set math.vec(align: right)
$ vec(-1, 1, -1) $
```

![Preview](/assets/docs/ZtHlp9Y4zEtz53Ydf5unLAAAAAAAAAAA.png)

Default: `center`

### `gap` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The gap between elements.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set math.vec(gap: 1em)
$ vec(1, 2) $
```

![Preview](/assets/docs/uiK2bQUKjIzcO3IGp7RZPwAAAAAAAAAA.png)

Default: `0% + 0.2em`

### `children` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The elements of the vector.

[![←](/assets/icons/16-chevron-right.svg)

VariantsPrevious page](/docs/reference/math/variants/) [![→](/assets/icons/16-chevron-right.svg)

SymbolsNext page](/docs/reference/symbols/)