# vElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/layout/v/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Spacing (V)](/docs/reference/layout/v/)

# `v`Element Question mark Element functions can be customized with `set` and `show` rules.

Inserts vertical spacing into a flow of blocks.

The spacing can be absolute, relative, or fractional. In the last case,
the remaining space on the page is distributed among all fractional spacings
according to their relative fractions.

## Example

```typst
#grid(
  rows: 3cm,
  columns: 6,
  gutter: 1fr,
  [A #parbreak() B],
  [A #v(0pt) B],
  [A #v(10pt) B],
  [A #v(0pt, weak: true) B],
  [A #v(40%, weak: true) B],
  [A #v(1fr) B],
)
```

![Preview](/assets/docs/DNC2m_0X9s5xLmHMABxCvgAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

v(

[relative](/docs/reference/layout/relative/)[fraction](/docs/reference/layout/fraction/),[weak:](#parameters-weak) [bool](/docs/reference/foundations/bool/),

) -> [content](/docs/reference/foundations/content/)

### `amount` [relative](/docs/reference/layout/relative/) or [fraction](/docs/reference/layout/fraction/) Required Positional Question mark Positional parameters are specified in order, without names.

How much spacing to insert.

### `weak` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

If `true`, the spacing collapses at the start or end of a flow.
Moreover, from multiple adjacent weak spacings all but the largest one
collapse. Weak spacings will always collapse adjacent paragraph spacing,
even if the paragraph spacing is larger.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
The following theorem is
foundational to the field:
#v(4pt, weak: true)
$ x^2 + y^2 = r^2 $
#v(4pt, weak: true)
The proof is simple:
```

![Preview](/assets/docs/7Xa6Zl_-zWfWaA6gosM_0QAAAAAAAAAA.png)

Default: `false`

[![←](/assets/icons/16-chevron-right.svg)

Spacing (H)Previous page](/docs/reference/layout/h/) [![→](/assets/icons/16-chevron-right.svg)

StackNext page](/docs/reference/layout/stack/)