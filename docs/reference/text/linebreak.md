# linebreakElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/text/linebreak/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Text](/docs/reference/text/)
- ![](/assets/icons/16-chevron-right.svg)
- [Line Break](/docs/reference/text/linebreak/)

# `linebreak`Element Question mark Element functions can be customized with `set` and `show` rules.

Inserts a line break.

Advances the paragraph to the next line. A single trailing line break at the
end of a paragraph is ignored, but more than one creates additional empty
lines.

## Example

```
*Date:* 26.12.2022 \
*Topic:* Infrastructure Test \
*Severity:* High \
```

![Preview](/assets/docs/OEyyibskK4bIsTh7Qcp7OAAAAAAAAAAA.png)

## Syntax

This function also has dedicated syntax: To insert a line break, simply write
a backslash followed by whitespace. This always creates an unjustified
break.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

linebreak(

[justify:](#parameters-justify) [bool](/docs/reference/foundations/bool/)

) -> [content](/docs/reference/foundations/content/)

### `justify` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether to justify the line before the break.

This is useful if you found a better line break opportunity in your
justified text than Typst did.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set par(justify: true)
#let jb = linebreak(justify: true)

I have manually tuned the #jb
line breaks in this paragraph #jb
for an _interesting_ result. #jb
```

![Preview](/assets/docs/RlJnAEDPiPVRCZ7poOHTOwAAAAAAAAAA.png)

Default: `false`

[![←](/assets/icons/16-chevron-right.svg)

HighlightPrevious page](/docs/reference/text/highlight/) [![→](/assets/icons/16-chevron-right.svg)

LoremNext page](/docs/reference/text/lorem/)