# subElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/text/sub/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Text](/docs/reference/text/)
- ![](/assets/icons/16-chevron-right.svg)
- [Subscript](/docs/reference/text/sub/)

# `sub`Element Question mark Element functions can be customized with `set` and `show` rules.

Renders text in subscript.

The text is rendered smaller and its baseline is lowered.

## Example

```
Revenue#sub[yearly]
```

![Preview](/assets/docs/q6m3B3bVOLKPuJFIogqIMwAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

sub(

[typographic:](#parameters-typographic) [bool](/docs/reference/foundations/bool/),[baseline:](#parameters-baseline) [auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/),[size:](#parameters-size) [auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `typographic` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether to use subscript glyphs from the font if available.

Ideally, subscripts glyphs are provided by the font (using the `subs`
OpenType feature). Otherwise, Typst is able to synthesize subscripts by
lowering and scaling down regular glyphs.

When this is set to `false`, synthesized glyphs will be used
regardless of whether the font provides dedicated subscript glyphs. When
`true`, synthesized glyphs may still be used in case the font does not
provide the necessary subscript glyphs.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
N#sub(typographic: true)[1]
N#sub(typographic: false)[1]
```

![Preview](/assets/docs/eGuJ4coPHcIbozTvGKvULAAAAAAAAAAA.png)

Default: `true`

### `baseline` [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The downward baseline shift for synthesized subscripts.

This only applies to synthesized subscripts. In other words, this has no
effect if `typographic` is `true` and the font provides the necessary
subscript glyphs.

If set to `auto`, the baseline is shifted according to the metrics
provided by the font, with a fallback to `0.2em` in case the font does
not define the necessary metrics.

Default: `auto`

### `size` [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The font size for synthesized subscripts.

This only applies to synthesized subscripts. In other words, this has no
effect if `typographic` is `true` and the font provides the necessary
subscript glyphs.

If set to `auto`, the size is scaled according to the metrics provided
by the font, with a fallback to `0.6em` in case the font does not
define the necessary metrics.

Default: `auto`

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The text to display in subscript.

[![←](/assets/icons/16-chevron-right.svg)

StrikethroughPrevious page](/docs/reference/text/strike/) [![→](/assets/icons/16-chevron-right.svg)

SuperscriptNext page](/docs/reference/text/super/)