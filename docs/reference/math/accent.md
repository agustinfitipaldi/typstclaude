# accentElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/math/accent/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Math](/docs/reference/math/)
- ![](/assets/icons/16-chevron-right.svg)
- [Accent](/docs/reference/math/accent/)

# `accent`Element Question mark Element functions can be customized with `set` and `show` rules.

Attaches an accent to a base.

## Example

```
$grave(a) = accent(a, `)$ \
$arrow(a) = accent(a, arrow)$ \
$tilde(a) = accent(a, \u{0303})$
```

![Preview](/assets/docs/wdLZED2cvtXKAU75vKtAKwAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

math.accent(

[content](/docs/reference/foundations/content/),[str](/docs/reference/foundations/str/)[content](/docs/reference/foundations/content/),[size:](#parameters-size) [relative](/docs/reference/layout/relative/),[dotless:](#parameters-dotless) [bool](/docs/reference/foundations/bool/),

) -> [content](/docs/reference/foundations/content/)

### `base` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The base to which the accent is applied. May consist of multiple
letters.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$arrow(A B C)$
```

![Preview](/assets/docs/aVpZuZcTglBCvF8kbjxN7AAAAAAAAAAA.png)

### `accent` [str](/docs/reference/foundations/str/) or [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The accent to apply to the base.

Supported accents include:

| Accent | Name | Codepoint |
| --- | --- | --- |
| Grave | `grave` | `` ` `` |
| Acute | `acute` | `´` |
| Circumflex | `hat` | `^` |
| Tilde | `tilde` | `~` |
| Macron | `macron` | `¯` |
| Dash | `dash` | `‾` |
| Breve | `breve` | `˘` |
| Dot | `dot` | `.` |
| Double dot, Diaeresis | `dot.double`, `diaer` | `¨` |
| Triple dot | `dot.triple` | `⃛` |
| Quadruple dot | `dot.quad` | `⃜` |
| Circle | `circle` | `∘` |
| Double acute | `acute.double` | `˝` |
| Caron | `caron` | `ˇ` |
| Right arrow | `arrow`, `->` | `→` |
| Left arrow | `arrow.l`, `<-` | `←` |
| Left/Right arrow | `arrow.l.r` | `↔` |
| Right harpoon | `harpoon` | `⇀` |
| Left harpoon | `harpoon.lt` | `↼` |

### `size` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The size of the accent, relative to the width of the base.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$dash(A, size: #150%)$
```

![Preview](/assets/docs/hq6LNtuIDgNQA24Un_9aIgAAAAAAAAAA.png)

Default: `100% + 0pt`

### `dotless` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether to remove the dot on top of lowercase i and j when adding a top
accent.

This enables the `dtls` OpenType feature.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$hat(dotless: #false, i)$
```

![Preview](/assets/docs/c53-GzmofkeD49EdBDqftgAAAAAAAAAA.png)

Default: `true`

[![←](/assets/icons/16-chevron-right.svg)

MathPrevious page](/docs/reference/math/) [![→](/assets/icons/16-chevron-right.svg)

AttachNext page](/docs/reference/math/attach/)