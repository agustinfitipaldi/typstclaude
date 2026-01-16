# hElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/layout/h/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Spacing (H)](/docs/reference/layout/h/)

# `h`Element Question mark Element functions can be customized with `set` and `show` rules.

Inserts horizontal spacing into a paragraph.

The spacing can be absolute, relative, or fractional. In the last case, the
remaining space on the line is distributed among all fractional spacings
according to their relative fractions.

## Example

```
First #h(1cm) Second \
First #h(30%) Second
```

![Preview](/assets/docs/8wL-xYLR6Y7MLlpoIuX_vAAAAAAAAAAA.png)

## Fractional spacing

With fractional spacing, you can align things within a line without forcing
a paragraph break (like [`align`](/docs/reference/layout/align/ "`align`") would). Each fractionally sized element
gets space based on the ratio of its fraction to the sum of all fractions.

```
First #h(1fr) Second \
First #h(1fr) Second #h(1fr) Third \
First #h(2fr) Second #h(1fr) Third
```

![Preview](/assets/docs/pBCqhY9Aheurjnzy2VgPBgAAAAAAAAAA.png)

## Mathematical Spacing

In [mathematical formulas](/docs/reference/math/), you can additionally use these
constants to add spacing between elements: `thin` (1/6 em), `med` (2/9 em),
`thick` (5/18 em), `quad` (1 em), `wide` (2 em).

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

h(

[relative](/docs/reference/layout/relative/)[fraction](/docs/reference/layout/fraction/),[weak:](#parameters-weak) [bool](/docs/reference/foundations/bool/),

) -> [content](/docs/reference/foundations/content/)

### `amount` [relative](/docs/reference/layout/relative/) or [fraction](/docs/reference/layout/fraction/) Required Positional Question mark Positional parameters are specified in order, without names.

How much spacing to insert.

### `weak` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

If `true`, the spacing collapses at the start or end of a paragraph.
Moreover, from multiple adjacent weak spacings all but the largest one
collapse.

Weak spacing in markup also causes all adjacent markup spaces to be
removed, regardless of the amount of spacing inserted. To force a space
next to weak spacing, you can explicitly write `#" "` (for a normal
space) or `~` (for a non-breaking space). The latter can be useful to
create a construct that always attaches to the preceding word with one
non-breaking space, independently of whether a markup space existed in
front or not.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#h(1cm, weak: true)
We identified a group of _weak_
specimens that fail to manifest
in most cases. However, when
#h(8pt, weak: true) supported
#h(8pt, weak: true) on both sides,
they do show up.

Further #h(0pt, weak: true) more,
even the smallest of them swallow
adjacent markup spaces.
```

![Preview](/assets/docs/c_7b_9WV6STCF2ERdGhpfQAAAAAAAAAA.png)

Default: `false`

[![←](/assets/icons/16-chevron-right.svg)

SkewPrevious page](/docs/reference/layout/skew/) [![→](/assets/icons/16-chevron-right.svg)

Spacing (V)Next page](/docs/reference/layout/v/)