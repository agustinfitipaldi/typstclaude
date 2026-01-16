# repr

Source: https://typst.app/docs/reference/foundations/repr/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Foundations](/docs/reference/foundations/)
- ![](/assets/icons/16-chevron-right.svg)
- [Representation](/docs/reference/foundations/repr/)

# `repr`

Returns the string representation of a value.

When inserted into content, most values are displayed as this representation
in monospace with syntax-highlighting. The exceptions are `none`,
integers, floats, strings, content, and functions.

## Example

```typst
#none vs #repr(none) \
#"hello" vs #repr("hello") \
#(1, 2) vs #repr((1, 2)) \
#[*Hi*] vs #repr([*Hi*])
```

![Preview](/assets/docs/hOvQAQDTPr3WAVu4x8HkgwAAAAAAAAAA.png)

## For debugging purposes only

This function is for debugging purposes. Its output should not be considered
stable and may change at any time.

To be specific, having the same `repr` does not guarantee that values are
equivalent, and `repr` is not a strict inverse of [`eval`](/docs/reference/foundations/eval/ "`eval`"). In the following
example, for readability, the [`length`](/docs/reference/layout/length/ "`length`") is rounded to two significant
digits and the parameter list and body of the
[unnamed `function`](/docs/reference/foundations/function/#unnamed) are omitted.

```typst
#assert(2pt / 3 < 0.67pt)
#repr(2pt / 3)

#repr(x => x + 1)
```

![Preview](/assets/docs/OPJv8SaHrjC0v3UloOTb0wAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

repr(

any

) -> [str](/docs/reference/foundations/str/)

### `value` any Required Positional Question mark Positional parameters are specified in order, without names.

The value whose string representation to produce.

[![←](/assets/icons/16-chevron-right.svg)

RegexPrevious page](/docs/reference/foundations/regex/) [![→](/assets/icons/16-chevron-right.svg)

SelectorNext page](/docs/reference/foundations/selector/)