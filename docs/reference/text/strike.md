# strikeElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/text/strike/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Text](/docs/reference/text/)
- ![](/assets/icons/16-chevron-right.svg)
- [Strikethrough](/docs/reference/text/strike/)

# `strike`Element Question mark Element functions can be customized with `set` and `show` rules.

Strikes through text.

## Example

```
This is #strike[not] relevant.
```

![Preview](/assets/docs/gYmGRzTLJUGSNzHzEZFB3gAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

strike(

[stroke:](#parameters-stroke) [auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[stroke](/docs/reference/visualize/stroke/)[tiling](/docs/reference/visualize/tiling/)[dictionary](/docs/reference/foundations/dictionary/),[offset:](#parameters-offset) [auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/),[extent:](#parameters-extent) [length](/docs/reference/layout/length/),[background:](#parameters-background) [bool](/docs/reference/foundations/bool/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `stroke` [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [stroke](/docs/reference/visualize/stroke/) or [tiling](/docs/reference/visualize/tiling/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How to [stroke](/docs/reference/visualize/stroke/ "stroke") the line.

If set to `auto`, takes on the text's color and a thickness defined in
the current font.

*Note:* Please don't use this for real redaction as you can still copy
paste the text.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
This is #strike(stroke: 1.5pt + red)[very stricken through]. \
This is #strike(stroke: 10pt)[redacted].
```

![Preview](/assets/docs/z5bibL2s5nJ9Rg5dVQco5QAAAAAAAAAA.png)

Default: `auto`

### `offset` [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The position of the line relative to the baseline. Read from the font
tables if `auto`.

This is useful if you are unhappy with the offset your font provides.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(font: "Inria Serif")
This is #strike(offset: auto)[low-ish]. \
This is #strike(offset: -3.5pt)[on-top].
```

![Preview](/assets/docs/1OEdd7_f0OE1q_8jKEVHmQAAAAAAAAAA.png)

Default: `auto`

### `extent` [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The amount by which to extend the line beyond (or within if negative)
the content.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
This #strike(extent: -2pt)[skips] parts of the word.
This #strike(extent: 2pt)[extends] beyond the word.
```

![Preview](/assets/docs/EqeD8OvCZeei8kbI8T5T0AAAAAAAAAAA.png)

Default: `0pt`

### `background` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether the line is placed behind the content.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set strike(stroke: red)
#strike(background: true)[This is behind.] \
#strike(background: false)[This is in front.]
```

![Preview](/assets/docs/5BzB-6LlvrhILN951-2KuQAAAAAAAAAA.png)

Default: `false`

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to strike through.

[![←](/assets/icons/16-chevron-right.svg)

SmartquotePrevious page](/docs/reference/text/smartquote/) [![→](/assets/icons/16-chevron-right.svg)

SubscriptNext page](/docs/reference/text/sub/)