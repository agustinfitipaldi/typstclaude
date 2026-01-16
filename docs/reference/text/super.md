# superElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/text/super/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Text](/docs/reference/text/)
- ![](/assets/icons/16-chevron-right.svg)
- [Superscript](/docs/reference/text/super/)

# `super`Element Question mark Element functions can be customized with `set` and `show` rules.

Renders text in superscript.

The text is rendered smaller and its baseline is raised.

## Example

```
1#super[st] try!
```

![Preview](/assets/docs/052zwKrkvVHtZVzW65WFdQAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

super(

[typographic:](#parameters-typographic) [bool](/docs/reference/foundations/bool/),[baseline:](#parameters-baseline) [auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/),[size:](#parameters-size) [auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `typographic` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether to use superscript glyphs from the font if available.

Ideally, superscripts glyphs are provided by the font (using the `sups`
OpenType feature). Otherwise, Typst is able to synthesize superscripts
by raising and scaling down regular glyphs.

When this is set to `false`, synthesized glyphs will be used
regardless of whether the font provides dedicated superscript glyphs.
When `true`, synthesized glyphs may still be used in case the font
does not provide the necessary superscript glyphs.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
N#super(typographic: true)[1]
N#super(typographic: false)[1]
```

![Preview](/assets/docs/1_zKQkbZObDWVLT4k-2LKQAAAAAAAAAA.png)

Default: `true`

### `baseline` [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The downward baseline shift for synthesized superscripts.

This only applies to synthesized superscripts. In other words, this has
no effect if `typographic` is `true` and the font provides the
necessary superscript glyphs.

If set to `auto`, the baseline is shifted according to the metrics
provided by the font, with a fallback to `-0.5em` in case the font
does not define the necessary metrics.

Note that, since the baseline shift is applied downward, you will need
to provide a negative value for the content to appear as raised above
the normal baseline.

Default: `auto`

### `size` [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The font size for synthesized superscripts.

This only applies to synthesized superscripts. In other words, this has
no effect if `typographic` is `true` and the font provides the
necessary superscript glyphs.

If set to `auto`, the size is scaled according to the metrics provided
by the font, with a fallback to `0.6em` in case the font does not
define the necessary metrics.

Default: `auto`

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The text to display in superscript.

[![←](/assets/icons/16-chevron-right.svg)

SubscriptPrevious page](/docs/reference/text/sub/) [![→](/assets/icons/16-chevron-right.svg)

TextNext page](/docs/reference/text/text/)