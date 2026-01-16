# panic

Source: https://typst.app/docs/reference/foundations/panic/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Foundations](/docs/reference/foundations/)
- ![](/assets/icons/16-chevron-right.svg)
- [Panic](/docs/reference/foundations/panic/)

# `panic`

Fails with an error.

Arguments are displayed to the user (not rendered in the document) as
strings, converting with `repr` if necessary.

## Example

The code below produces the error `panicked with: "this is wrong"`.

```typst
#panic("this is wrong")
```

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

panic(

[..](#parameters-values)any

)

### `values` any Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The values to panic with and display to the user.

[![←](/assets/icons/16-chevron-right.svg)

NonePrevious page](/docs/reference/foundations/none/) [![→](/assets/icons/16-chevron-right.svg)

PluginNext page](/docs/reference/foundations/plugin/)