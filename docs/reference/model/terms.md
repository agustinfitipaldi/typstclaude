# termsElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/model/terms/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Model](/docs/reference/model/)
- ![](/assets/icons/16-chevron-right.svg)
- [Term List](/docs/reference/model/terms/)

# `terms`Element Question mark Element functions can be customized with `set` and `show` rules.

A list of terms and their descriptions.

Displays a sequence of terms and their descriptions vertically. When the
descriptions span over multiple lines, they use hanging indent to
communicate the visual hierarchy.

## Example

```
/ Ligature: A merged glyph.
/ Kerning: A spacing adjustment
  between two adjacent letters.
```

![Preview](/assets/docs/qjdQTTJFa_RYtcfu42IiawAAAAAAAAAA.png)

## Syntax

This function also has dedicated syntax: Starting a line with a slash,
followed by a term, a colon and a description creates a term list item.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

terms(

[tight:](#parameters-tight) [bool](/docs/reference/foundations/bool/),[separator:](#parameters-separator) [content](/docs/reference/foundations/content/),[indent:](#parameters-indent) [length](/docs/reference/layout/length/),[hanging-indent:](#parameters-hanging-indent) [length](/docs/reference/layout/length/),[spacing:](#parameters-spacing) [auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/),[..](#parameters-children)[content](/docs/reference/foundations/content/)[array](/docs/reference/foundations/array/),

) -> [content](/docs/reference/foundations/content/)

### `tight` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Defines the default [spacing](/docs/reference/model/terms/#parameters-spacing) of the term list. If it is
`false`, the items are spaced apart with
[paragraph spacing](/docs/reference/model/par/#parameters-spacing). If it is `true`, they use
[paragraph leading](/docs/reference/model/par/#parameters-leading) instead. This makes the list more
compact, which can look better if the items are short.

In markup mode, the value of this parameter is determined based on
whether items are separated with a blank line. If items directly follow
each other, this is set to `true`; if items are separated by a blank
line, this is set to `false`. The markup-defined tightness cannot be
overridden with set rules.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
/ Fact: If a term list has a lot
  of text, and maybe other inline
  content, it should not be tight
  anymore.

/ Tip: To make it wide, simply
  insert a blank line between the
  items.
```

![Preview](/assets/docs/skkuR2BgltlCHUy9cPpX7gAAAAAAAAAA.png)

Default: `true`

### `separator` [content](/docs/reference/foundations/content/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The separator between the item and the description.

If you want to just separate them with a certain amount of space, use
`h(2cm, weak: true)` as the separator and replace `2cm` with your
desired amount of space.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set terms(separator: [: ])

/ Colon: A nice separator symbol.
```

![Preview](/assets/docs/xyyblMI8l_99lTt1_p5kWgAAAAAAAAAA.png)

Default: `h(amount: 0.6em, weak: true)`

### `indent` [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The indentation of each item.

Default: `0pt`

### `hanging-indent` [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The hanging indent of the description.

This is in addition to the whole item's `indent`.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set terms(hanging-indent: 0pt)
/ Term: This term list does not
  make use of hanging indents.
```

![Preview](/assets/docs/6yYrKErT2JtRwBRmpS8r5wAAAAAAAAAA.png)

Default: `2em`

### `spacing` [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The spacing between the items of the term list.

If set to `auto`, uses paragraph [`leading`](/docs/reference/model/par/#parameters-leading) for tight
term lists and paragraph [`spacing`](/docs/reference/model/par/#parameters-spacing) for wide
(non-tight) term lists.

Default: `auto`

### `children` [content](/docs/reference/foundations/content/) or [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The term list's children.

When using the term list syntax, adjacent items are automatically
collected into term lists, even through constructs like for loops.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#for (year, product) in (
  "1978": "TeX",
  "1984": "LaTeX",
  "2019": "Typst",
) [/ #product: Born in #year.]
```

![Preview](/assets/docs/wkvQM6jeTkSTRoaT9Y0lSQAAAAAAAAAA.png)

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `item`Element Question mark Element functions can be customized with `set` and `show` rules.

A term list item.

terms.item(

[content](/docs/reference/foundations/content/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `term` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The term described by the list item.

#### `description` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The description of the term.

[![←](/assets/icons/16-chevron-right.svg)

TablePrevious page](/docs/reference/model/table/) [![→](/assets/icons/16-chevron-right.svg)

TitleNext page](/docs/reference/model/title/)