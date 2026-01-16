# classElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/math/class/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Math](/docs/reference/math/)
- ![](/assets/icons/16-chevron-right.svg)
- [Class](/docs/reference/math/class/)

# `class`Element Question mark Element functions can be customized with `set` and `show` rules.

Forced use of a certain math class.

This is useful to treat certain symbols as if they were of a different
class, e.g. to make a symbol behave like a relation. The class of a symbol
defines the way it is laid out, including spacing around it, and how its
scripts are attached by default. Note that the latter can always be
overridden using [`limits`](/docs/reference/math/attach/#functions-limits) and [`scripts`](/docs/reference/math/attach/#functions-scripts).

## Example

```typst
#let loves = math.class(
  "relation",
  sym.suit.heart,
)

$x loves y and y loves 5$
```

![Preview](/assets/docs/4-1urHqzMZfIf7fLTw_1MAAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

math.class(

[str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `class` [str](/docs/reference/foundations/str/) Required Positional Question mark Positional parameters are specified in order, without names.

The class to apply to the content.

  ![](/assets/icons/16-chevron-right.svg) View options 

| Variant | Details |
| --- | --- |
| `"normal"` | The default class for non-special things. |
| `"punctuation"` | Punctuation, e.g. a comma. |
| `"opening"` | An opening delimiter, e.g. `(`. |
| `"closing"` | A closing delimiter, e.g. `)`. |
| `"fence"` | A delimiter that is the same on both sides, e.g. `|`. |
| `"large"` | A large operator like `sum`. |
| `"relation"` | A relation like `=` or `prec`. |
| `"unary"` | A unary operator like `not`. |
| `"binary"` | A binary operator like `times`. |
| `"vary"` | An operator that can be both unary or binary like `+`. |

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to which the class is applied.

[![←](/assets/icons/16-chevron-right.svg)

CasesPrevious page](/docs/reference/math/cases/) [![→](/assets/icons/16-chevron-right.svg)

EquationNext page](/docs/reference/math/equation/)