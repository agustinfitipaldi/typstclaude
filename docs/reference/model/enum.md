# enumElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/model/enum/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Model](/docs/reference/model/)
- ![](/assets/icons/16-chevron-right.svg)
- [Numbered List](/docs/reference/model/enum/)

# `enum`Element Question mark Element functions can be customized with `set` and `show` rules.

A numbered list.

Displays a sequence of items vertically and numbers them consecutively.

## Example

```typst
Automatically numbered:
+ Preparations
+ Analysis
+ Conclusions

Manually numbered:
2. What is the first step?
5. I am confused.
+  Moving on ...

Multiple lines:
+ This enum item has multiple
  lines because the next line
  is indented.

Function call.
#enum[First][Second]
```

![Preview](/assets/docs/HrnJ1mRKvbXNf6U4DmZCaAAAAAAAAAAA.png)

You can easily switch all your enumerations to a different numbering style
with a set rule.

```typst
#set enum(numbering: "a)")

+ Starting off ...
+ Don't forget step two
```

![Preview](/assets/docs/hFb68a8DC-Rvf_eMOYtVMwAAAAAAAAAA.png)

You can also use [`enum.item`](/docs/reference/model/enum/#definitions-item "`enum.item`") to programmatically customize the number of
each item in the enumeration:

```typst
#enum(
  enum.item(1)[First step],
  enum.item(5)[Fifth step],
  enum.item(10)[Tenth step]
)
```

![Preview](/assets/docs/uRQbjXrkv7FwltBxluVMMAAAAAAAAAAA.png)

## Syntax

This functions also has dedicated syntax:

- Starting a line with a plus sign creates an automatically numbered
  enumeration item.
- Starting a line with a number followed by a dot creates an explicitly
  numbered enumeration item.

Enumeration items can contain multiple paragraphs and other block-level
content. All content that is indented more than an item's marker becomes
part of that item.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

enum(

[tight:](#parameters-tight) [bool](/docs/reference/foundations/bool/),[numbering:](#parameters-numbering) [str](/docs/reference/foundations/str/)[function](/docs/reference/foundations/function/),[start:](#parameters-start) [auto](/docs/reference/foundations/auto/)[int](/docs/reference/foundations/int/),[full:](#parameters-full) [bool](/docs/reference/foundations/bool/),[reversed:](#parameters-reversed) [bool](/docs/reference/foundations/bool/),[indent:](#parameters-indent) [length](/docs/reference/layout/length/),[body-indent:](#parameters-body-indent) [length](/docs/reference/layout/length/),[spacing:](#parameters-spacing) [auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/),[number-align:](#parameters-number-align) [alignment](/docs/reference/layout/alignment/),[..](#parameters-children)[content](/docs/reference/foundations/content/)[array](/docs/reference/foundations/array/),

) -> [content](/docs/reference/foundations/content/)

### `tight` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Defines the default [spacing](/docs/reference/model/enum/#parameters-spacing) of the enumeration. If it
is `false`, the items are spaced apart with
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
+ If an enum has a lot of text, and
  maybe other inline content, it
  should not be tight anymore.

+ To make an enum wide, simply
  insert a blank line between the
  items.
```

![Preview](/assets/docs/CGCi1WYCPLux25Xc9ZWwDQAAAAAAAAAA.png)

Default: `true`

### `numbering` [str](/docs/reference/foundations/str/) or [function](/docs/reference/foundations/function/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How to number the enumeration. Accepts a
[numbering pattern or function](/docs/reference/model/numbering/).

If the numbering pattern contains multiple counting symbols, they apply
to nested enums. If given a function, the function receives one argument
if `full` is `false` and multiple arguments if `full` is `true`.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set enum(numbering: "1.a)")
+ Different
+ Numbering
  + Nested
  + Items
+ Style

#set enum(numbering: n => super[#n])
+ Superscript
+ Numbering!
```

![Preview](/assets/docs/b_5poTPc-SH9hcwOp4TcbAAAAAAAAAAA.png)

Default: `"1."`

### `start` [auto](/docs/reference/foundations/auto/) or [int](/docs/reference/foundations/int/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Which number to start the enumeration with.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#enum(
  start: 3,
  [Skipping],
  [Ahead],
)
```

![Preview](/assets/docs/NqaMIUfLtrq2fhf9xChjagAAAAAAAAAA.png)

Default: `auto`

### `full` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether to display the full numbering, including the numbers of
all parent enumerations.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set enum(numbering: "1.a)", full: true)
+ Cook
  + Heat water
  + Add ingredients
+ Eat
```

![Preview](/assets/docs/ecL0fn92ARx_6xbLZYFkVAAAAAAAAAAA.png)

Default: `false`

### `reversed` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether to reverse the numbering for this enumeration.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set enum(reversed: true)
+ Coffee
+ Tea
+ Milk
```

![Preview](/assets/docs/VSjdcG97Wx9ICEbyU02BLAAAAAAAAAAA.png)

Default: `false`

### `indent` [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The indentation of each item.

Default: `0pt`

### `body-indent` [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The space between the numbering and the body of each item.

Default: `0.5em`

### `spacing` [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The spacing between the items of the enumeration.

If set to `auto`, uses paragraph [`leading`](/docs/reference/model/par/#parameters-leading) for tight
enumerations and paragraph [`spacing`](/docs/reference/model/par/#parameters-spacing) for wide
(non-tight) enumerations.

Default: `auto`

### `number-align` [alignment](/docs/reference/layout/alignment/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The alignment that enum numbers should have.

By default, this is set to `end + top`, which aligns enum numbers
towards end of the current text direction (in left-to-right script,
for example, this is the same as `right`) and at the top of the line.
The choice of `end` for horizontal alignment of enum numbers is
usually preferred over `start`, as numbers then grow away from the
text instead of towards it, avoiding certain visual issues. This option
lets you override this behaviour, however. (Also to note is that the
[unordered list](/docs/reference/model/list/) uses a different method for this, by giving the
`marker` content an alignment directly.).

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set enum(number-align: start + bottom)

Here are some powers of two:
1. One
2. Two
4. Four
8. Eight
16. Sixteen
32. Thirty two
```

![Preview](/assets/docs/s-zUl9r9z6yKdW4VnsLi_AAAAAAAAAAA.png)

Default: `end + top`

### `children` [content](/docs/reference/foundations/content/) or [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The numbered list's items.

When using the enum syntax, adjacent items are automatically collected
into enumerations, even through constructs like for loops.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#for phase in (
   "Launch",
   "Orbit",
   "Descent",
) [+ #phase]
```

![Preview](/assets/docs/9haSHPkr8gDAx-1cEtmf8QAAAAAAAAAA.png)

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `item`Element Question mark Element functions can be customized with `set` and `show` rules.

An enumeration item.

enum.item(

[auto](/docs/reference/foundations/auto/)[int](/docs/reference/foundations/int/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `number` [auto](/docs/reference/foundations/auto/) or [int](/docs/reference/foundations/int/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The item's number.

Default: `auto`

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The item's body.

[![←](/assets/icons/16-chevron-right.svg)

LinkPrevious page](/docs/reference/model/link/) [![→](/assets/icons/16-chevron-right.svg)

NumberingNext page](/docs/reference/model/numbering/)