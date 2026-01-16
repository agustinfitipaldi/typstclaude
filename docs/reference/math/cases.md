# casesElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/math/cases/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Math](/docs/reference/math/)
- ![](/assets/icons/16-chevron-right.svg)
- [Cases](/docs/reference/math/cases/)

# `cases`Element Question mark Element functions can be customized with `set` and `show` rules.

A case distinction.

Content across different branches can be aligned with the `&` symbol.

## Example

```
$ f(x, y) := cases(
  1 "if" (x dot y)/2 <= 0,
  2 "if" x "is even",
  3 "if" x in NN,
  4 "else",
) $
```

![Preview](/assets/docs/0X1AFPDieBd9jiawKpc0-AAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

math.cases(

[delim:](#parameters-delim) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/)[symbol](/docs/reference/foundations/symbol/),[reverse:](#parameters-reverse) [bool](/docs/reference/foundations/bool/),[gap:](#parameters-gap) [relative](/docs/reference/layout/relative/),[..](#parameters-children)[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `delim` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/) or [symbol](/docs/reference/foundations/symbol/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The delimiter to use.

Can be a single character specifying the left delimiter, in which case
the right delimiter is inferred. Otherwise, can be an array containing a
left and a right delimiter.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set math.cases(delim: "[")
$ x = cases(1, 2) $
```

![Preview](/assets/docs/bErdOHWWOQLSKtsxtJeY5QAAAAAAAAAA.png)

Default: `("{", "}")`

### `reverse` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether the direction of cases should be reversed.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set math.cases(reverse: true)
$ cases(1, 2) = x $
```

![Preview](/assets/docs/z6AQZKJsH9nM95e6Aw0hGgAAAAAAAAAA.png)

Default: `false`

### `gap` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The gap between branches.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set math.cases(gap: 1em)
$ x = cases(1, 2) $
```

![Preview](/assets/docs/-xscfzRH4Dw6Yi5TCvpkVwAAAAAAAAAA.png)

Default: `0% + 0.2em`

### `children` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The branches of the case distinction.

[![←](/assets/icons/16-chevron-right.svg)

CancelPrevious page](/docs/reference/math/cancel/) [![→](/assets/icons/16-chevron-right.svg)

ClassNext page](/docs/reference/math/class/)