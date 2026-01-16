# textElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/text/text/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Text](/docs/reference/text/)
- ![](/assets/icons/16-chevron-right.svg)
- [Text](/docs/reference/text/text/)

# `text`Element Question mark Element functions can be customized with `set` and `show` rules.

Customizes the look and layout of text in a variety of ways.

This function is used frequently, both with set rules and directly. While
the set rule is often the simpler choice, calling the `text` function
directly can be useful when passing text as an argument to another function.

## Example

```typst
#set text(18pt)
With a set rule.

#emph(text(blue)[
  With a function call.
])
```

![Preview](/assets/docs/TE1TKvqGw3ajR6jn3phXugAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

text(

[font:](#parameters-font) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/)[dictionary](/docs/reference/foundations/dictionary/),[fallback:](#parameters-fallback) [bool](/docs/reference/foundations/bool/),[style:](#parameters-style) [str](/docs/reference/foundations/str/),[weight:](#parameters-weight) [int](/docs/reference/foundations/int/)[str](/docs/reference/foundations/str/),[stretch:](#parameters-stretch) [ratio](/docs/reference/layout/ratio/),[size:](#parameters-size) [length](/docs/reference/layout/length/),[fill:](#parameters-fill) [color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[tiling](/docs/reference/visualize/tiling/),[stroke:](#parameters-stroke) [none](/docs/reference/foundations/none/)[length](/docs/reference/layout/length/)[color](/docs/reference/visualize/color/)[gradient](/docs/reference/visualize/gradient/)[stroke](/docs/reference/visualize/stroke/)[tiling](/docs/reference/visualize/tiling/)[dictionary](/docs/reference/foundations/dictionary/),[tracking:](#parameters-tracking) [length](/docs/reference/layout/length/),[spacing:](#parameters-spacing) [relative](/docs/reference/layout/relative/),[cjk-latin-spacing:](#parameters-cjk-latin-spacing) [none](/docs/reference/foundations/none/)[auto](/docs/reference/foundations/auto/),[baseline:](#parameters-baseline) [length](/docs/reference/layout/length/),[overhang:](#parameters-overhang) [bool](/docs/reference/foundations/bool/),[top-edge:](#parameters-top-edge) [length](/docs/reference/layout/length/)[str](/docs/reference/foundations/str/),[bottom-edge:](#parameters-bottom-edge) [length](/docs/reference/layout/length/)[str](/docs/reference/foundations/str/),[lang:](#parameters-lang) [str](/docs/reference/foundations/str/),[region:](#parameters-region) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/),[script:](#parameters-script) [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/),[dir:](#parameters-dir) [auto](/docs/reference/foundations/auto/)[direction](/docs/reference/layout/direction/),[hyphenate:](#parameters-hyphenate) [auto](/docs/reference/foundations/auto/)[bool](/docs/reference/foundations/bool/),[costs:](#parameters-costs) [dictionary](/docs/reference/foundations/dictionary/),[kerning:](#parameters-kerning) [bool](/docs/reference/foundations/bool/),[alternates:](#parameters-alternates) [bool](/docs/reference/foundations/bool/),[stylistic-set:](#parameters-stylistic-set) [none](/docs/reference/foundations/none/)[int](/docs/reference/foundations/int/)[array](/docs/reference/foundations/array/),[ligatures:](#parameters-ligatures) [bool](/docs/reference/foundations/bool/),[discretionary-ligatures:](#parameters-discretionary-ligatures) [bool](/docs/reference/foundations/bool/),[historical-ligatures:](#parameters-historical-ligatures) [bool](/docs/reference/foundations/bool/),[number-type:](#parameters-number-type) [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/),[number-width:](#parameters-number-width) [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/),[slashed-zero:](#parameters-slashed-zero) [bool](/docs/reference/foundations/bool/),[fractions:](#parameters-fractions) [bool](/docs/reference/foundations/bool/),[features:](#parameters-features) [array](/docs/reference/foundations/array/)[dictionary](/docs/reference/foundations/dictionary/),[body:](#parameters-body) [content](/docs/reference/foundations/content/),[str](/docs/reference/foundations/str/),

) -> [content](/docs/reference/foundations/content/)

### `font` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

A font family descriptor or priority list of font family descriptors.

A font family descriptor can be a plain string representing the family
name or a dictionary with the following keys:

- `name` (required): The font family name.
- `covers` (optional): Defines the Unicode codepoints for which the
  family shall be used. This can be:
  - A predefined coverage set:
    - `"latin-in-cjk"` covers all codepoints except for those which
      exist in Latin fonts, but should preferably be taken from CJK
      fonts.
  - A [regular expression](/docs/reference/foundations/regex/) that defines exactly which codepoints
    shall be covered. Accepts only the subset of regular expressions
    which consist of exactly one dot, letter, or character class.

When processing text, Typst tries all specified font families in order
until it finds a font that has the necessary glyphs. In the example
below, the font `Inria Serif` is preferred, but since it does not
contain Arabic glyphs, the arabic text uses `Noto Sans Arabic` instead.

The collection of available fonts differs by platform:

- In the web app, you can see the list of available fonts by clicking on
  the "Ag" button. You can provide additional fonts by uploading `.ttf`
  or `.otf` files into your project. They will be discovered
  automatically. The priority is: project fonts > server fonts.
- Locally, Typst uses your installed system fonts or embedded fonts in
  the CLI, which are `Libertinus Serif`, `New Computer Modern`,
  `New Computer Modern Math`, and `DejaVu Sans Mono`. In addition, you
  can use the `--font-path` argument or `TYPST_FONT_PATHS` environment
  variable to add directories that should be scanned for fonts. The
  priority is: `--font-paths` > system fonts > embedded fonts. Run
  `typst fonts` to see the fonts that Typst has discovered on your
  system. Note that you can pass the `--ignore-system-fonts` parameter
  to the CLI to ensure Typst won't search for system fonts.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(font: "PT Sans")
This is sans-serif.

#set text(font: (
  "Inria Serif",
  "Noto Sans Arabic",
))

This is Latin. \
هذا عربي.

// Change font only for numbers.
#set text(font: (
  (name: "PT Sans", covers: regex("[0-9]")),
  "Libertinus Serif"
))

The number 123.

// Mix Latin and CJK fonts.
#set text(font: (
  (name: "Inria Serif", covers: "latin-in-cjk"),
  "Noto Serif CJK SC"
))
分别设置“中文”和English字体
```

![Preview](/assets/docs/sOblR8SVPqI-sT7CQgTVtwAAAAAAAAAA.png)

Default: `"libertinus serif"`

### `fallback` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether to allow last resort font fallback when the primary font list
contains no match. This lets Typst search through all available fonts
for the most similar one that has the necessary glyphs.

*Note:* Currently, there are no warnings when fallback is disabled and
no glyphs are found. Instead, your text shows up in the form of "tofus":
Small boxes that indicate the lack of an appropriate glyph. In the
future, you will be able to instruct Typst to issue warnings so you know
something is up.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(font: "Inria Serif")
هذا عربي

#set text(fallback: false)
هذا عربي
```

![Preview](/assets/docs/sa8VqsYbdClSlqi08qJyhAAAAAAAAAAA.png)

Default: `true`

### `style` [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The desired font style.

When an italic style is requested and only an oblique one is available,
it is used. Similarly, the other way around, an italic style can stand
in for an oblique one. When neither an italic nor an oblique style is
available, Typst selects the normal style. Since most fonts are only
available either in an italic or oblique style, the difference between
italic and oblique style is rarely observable.

If you want to emphasize your text, you should do so using the [emph](/docs/reference/model/emph/ "emph")
function instead. This makes it easy to adapt the style later if you
change your mind about how to signify the emphasis.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#text(font: "Libertinus Serif", style: "italic")[Italic]
#text(font: "DejaVu Sans", style: "oblique")[Oblique]
```

![Preview](/assets/docs/S5xaZcVoGLtnT_0XwbPSUQAAAAAAAAAA.png)

| Variant | Details |
| --- | --- |
| `"normal"` | The default, typically upright style. |
| `"italic"` | A cursive style with custom letterform. |
| `"oblique"` | Just a slanted version of the normal style. |

Default: `"normal"`

### `weight` [int](/docs/reference/foundations/int/) or [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The desired thickness of the font's glyphs. Accepts an integer between
`100` and `900` or one of the predefined weight names. When the
desired weight is not available, Typst selects the font from the family
that is closest in weight.

If you want to strongly emphasize your text, you should do so using the
[strong](/docs/reference/model/strong/ "strong") function instead. This makes it easy to adapt the style later
if you change your mind about how to signify the strong emphasis.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(font: "IBM Plex Sans")

#text(weight: "light")[Light] \
#text(weight: "regular")[Regular] \
#text(weight: "medium")[Medium] \
#text(weight: 500)[Medium] \
#text(weight: "bold")[Bold]
```

![Preview](/assets/docs/HLYJEJyYVhBAwk1NcGJZjQAAAAAAAAAA.png)

| Variant | Details |
| --- | --- |
| `"thin"` | Thin weight (100). |
| `"extralight"` | Extra light weight (200). |
| `"light"` | Light weight (300). |
| `"regular"` | Regular weight (400). |
| `"medium"` | Medium weight (500). |
| `"semibold"` | Semibold weight (600). |
| `"bold"` | Bold weight (700). |
| `"extrabold"` | Extrabold weight (800). |
| `"black"` | Black weight (900). |

Default: `"regular"`

### `stretch` [ratio](/docs/reference/layout/ratio/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The desired width of the glyphs. Accepts a ratio between `50%` and
`200%`. When the desired width is not available, Typst selects the
font from the family that is closest in stretch. This will only stretch
the text if a condensed or expanded version of the font is available.

If you want to adjust the amount of space between characters instead of
stretching the glyphs itself, use the [`tracking`](/docs/reference/text/text/#parameters-tracking)
property instead.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#text(stretch: 75%)[Condensed] \
#text(stretch: 100%)[Normal]
```

![Preview](/assets/docs/QhcCPECtjtdl-HaT2kdIoQAAAAAAAAAA.png)

Default: `100%`

### `size` [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The size of the glyphs. This value forms the basis of the `em` unit:
`1em` is equivalent to the font size.

You can also give the font size itself in `em` units. Then, it is
relative to the previous font size.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(size: 20pt)
very #text(1.5em)[big] text
```

![Preview](/assets/docs/blheA65DgOU1lkslOoHidgAAAAAAAAAA.png)

Default: `11pt`

### `fill` [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [tiling](/docs/reference/visualize/tiling/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The glyph fill paint.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(fill: red)
This text is red.
```

![Preview](/assets/docs/hjdTrz3B1HnAtRXCRTTtGAAAAAAAAAAA.png)

Default: `luma(0%)`

### `stroke` [none](/docs/reference/foundations/none/) or [length](/docs/reference/layout/length/) or [color](/docs/reference/visualize/color/) or [gradient](/docs/reference/visualize/gradient/) or [stroke](/docs/reference/visualize/stroke/) or [tiling](/docs/reference/visualize/tiling/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How to stroke the text.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#text(stroke: 0.5pt + red)[Stroked]
```

![Preview](/assets/docs/9XI8EQ1M6rOusSDRRIbaPQAAAAAAAAAA.png)

Default: `none`

### `tracking` [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The amount of space that should be added between characters.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(tracking: 1.5pt)
Distant text.
```

![Preview](/assets/docs/_W5ZMMvgiXlv5B8vI6sbcQAAAAAAAAAA.png)

Default: `0pt`

### `spacing` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The amount of space between words.

Can be given as an absolute length, but also relative to the width of
the space character in the font.

If you want to adjust the amount of space between characters rather than
words, use the [`tracking`](/docs/reference/text/text/#parameters-tracking) property instead.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(spacing: 200%)
Text with distant words.
```

![Preview](/assets/docs/NLatl7xe_PftXpK8eI1WSgAAAAAAAAAA.png)

Default: `100% + 0pt`

### `cjk-latin-spacing` [none](/docs/reference/foundations/none/) or [auto](/docs/reference/foundations/auto/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether to automatically insert spacing between CJK and Latin characters.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(cjk-latin-spacing: auto)
第4章介绍了基本的API。

#set text(cjk-latin-spacing: none)
第4章介绍了基本的API。
```

![Preview](/assets/docs/VxUeM1bvsLzygleocZmQUAAAAAAAAAAA.png)

Default: `auto`

### `baseline` [length](/docs/reference/layout/length/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

An amount to shift the text baseline by.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
A #text(baseline: 3pt)[lowered]
word.
```

![Preview](/assets/docs/Kc1E9Ts9m1i30dvtf5ymQgAAAAAAAAAA.png)

Default: `0pt`

### `overhang` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether certain glyphs can hang over into the margin in justified text.
This can make justification visually more pleasing.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set page(width: 220pt)

#set par(justify: true)
This justified text has a hyphen in
the paragraph's second line. Hanging
the hyphen slightly into the margin
results in a clearer paragraph edge.

#set text(overhang: false)
This justified text has a hyphen in
the paragraph's second line. Hanging
the hyphen slightly into the margin
results in a clearer paragraph edge.
```

![Preview](/assets/docs/foWEGoIXOSioaRXxZBKt7gAAAAAAAAAA.png)

Default: `true`

### `top-edge` [length](/docs/reference/layout/length/) or [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The top end of the conceptual frame around the text used for layout and
positioning. This affects the size of containers that hold text.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set rect(inset: 0pt)
#set text(size: 20pt)

#set text(top-edge: "ascender")
#rect(fill: aqua)[Typst]

#set text(top-edge: "cap-height")
#rect(fill: aqua)[Typst]
```

![Preview](/assets/docs/LDeMc2Iiqb_9L3aj1lNrpgAAAAAAAAAA.png)

| Variant | Details |
| --- | --- |
| `"ascender"` | The font's ascender, which typically exceeds the height of all glyphs. |
| `"cap-height"` | The approximate height of uppercase letters. |
| `"x-height"` | The approximate height of non-ascending lowercase letters. |
| `"baseline"` | The baseline on which the letters rest. |
| `"bounds"` | The top edge of the glyph's bounding box. |

Default: `"cap-height"`

### `bottom-edge` [length](/docs/reference/layout/length/) or [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The bottom end of the conceptual frame around the text used for layout
and positioning. This affects the size of containers that hold text.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set rect(inset: 0pt)
#set text(size: 20pt)

#set text(bottom-edge: "baseline")
#rect(fill: aqua)[Typst]

#set text(bottom-edge: "descender")
#rect(fill: aqua)[Typst]
```

![Preview](/assets/docs/l4WLB64gFfplM-bDPX7pEQAAAAAAAAAA.png)

| Variant | Details |
| --- | --- |
| `"baseline"` | The baseline on which the letters rest. |
| `"descender"` | The font's descender, which typically exceeds the depth of all glyphs. |
| `"bounds"` | The bottom edge of the glyph's bounding box. |

Default: `"baseline"`

### `lang` [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

An [ISO 639-1/2/3 language code.](https://en.wikipedia.org/wiki/ISO_639)

Setting the correct language affects various parts of Typst:

- The text processing pipeline can make more informed choices.
- Hyphenation will use the correct patterns for the language.
- [Smart quotes](/docs/reference/text/smartquote/) turns into the correct quotes for the
  language.
- And all other things which are language-aware.

Choosing the correct language is important for accessibility. For
example, screen readers will use it to choose a voice that matches the
language of the text. If your document is in another language than
English (the default), you should set the text language at the start of
your document, before any other content. You can, for example, put it
right after the `#set document(/* ... */)` rule that [sets your
document's title](/docs/reference/model/document/#parameters-title).

If your document contains passages in a different language than the main
language, you should locally change the text language just for those parts,
either with a set rule [scoped to a block](/docs/reference/scripting/#blocks) or using
a direct text function call such as `#text(lang: "de")[...]`.

If multiple codes are available for your language, you should prefer the
two-letter code (ISO 639-1) over the three-letter codes (ISO 639-2/3).
When you have to use a three-letter code and your language differs
between ISO 639-2 and ISO 639-3, use ISO 639-2 for PDF 1.7 (Typst's
default for PDF export) and below and ISO 639-3 for PDF 2.0 and HTML
export.

The language code is case-insensitive, and will be lowercased when
accessed through [context](/docs/reference/context/).

  ![](/assets/icons/16-chevron-right.svg) View example: Setting the text language to German 

```typst
#set text(lang: "de")
#outline()

= Einleitung
In diesem Dokument, ...
```

![Preview](/assets/docs/pV_uneCLTlX_ftfk4ZJI1QAAAAAAAAAA.png)

Default: `"en"`

### `region` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

An [ISO 3166-1 alpha-2 region code.](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

This lets the text processing pipeline make more informed choices.

The region code is case-insensitive, and will be uppercased when
accessed through [context](/docs/reference/context/).

Default: `none`

### `script` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The OpenType writing script.

The combination of `lang` and `script` determine how font features,
such as glyph substitution, are implemented. Frequently the value is a
modified (all-lowercase) ISO 15924 script identifier, and the `math`
writing script is used for features appropriate for mathematical
symbols.

When set to `auto`, the default and recommended setting, an
appropriate script is chosen for each block of characters sharing a
common Unicode script property.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(
  font: "Libertinus Serif",
  size: 20pt,
)

#let scedilla = [Ş]
#scedilla // S with a cedilla

#set text(lang: "ro", script: "latn")
#scedilla // S with a subscript comma

#set text(lang: "ro", script: "grek")
#scedilla // S with a cedilla
```

![Preview](/assets/docs/IJovpbe1c5rRr9DM_KRhvgAAAAAAAAAA.png)

Default: `auto`

### `dir` [auto](/docs/reference/foundations/auto/) or [direction](/docs/reference/layout/direction/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The dominant direction for text and inline objects. Possible values are:

- `auto`: Automatically infer the direction from the `lang` property.
- `ltr`: Layout text from left to right.
- `rtl`: Layout text from right to left.

When writing in right-to-left scripts like Arabic or Hebrew, you should
set the [text language](/docs/reference/text/text/#parameters-lang) or direction. While individual runs
of text are automatically layouted in the correct direction, setting the
dominant direction gives the bidirectional reordering algorithm the
necessary information to correctly place punctuation and inline objects.
Furthermore, setting the direction affects the alignment values `start`
and `end`, which are equivalent to `left` and `right` in `ltr` text and
the other way around in `rtl` text.

If you set this to `rtl` and experience bugs or in some way bad looking
output, please get in touch with us through the
[Forum](https://forum.typst.app/),
[Discord server](https://discord.gg/2uDybryKPe),
or our [contact form](https://typst.app/contact).

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(dir: rtl)
هذا عربي.
```

![Preview](/assets/docs/KrWAMeKAPNsts-l34CremAAAAAAAAAAA.png)

Default: `auto`

### `hyphenate` [auto](/docs/reference/foundations/auto/) or [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether to hyphenate text to improve line breaking. When `auto`, text
will be hyphenated if and only if justification is enabled.

Setting the [text language](/docs/reference/text/text/#parameters-lang) ensures that the correct
hyphenation patterns are used.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set page(width: 200pt)

#set par(justify: true)
This text illustrates how
enabling hyphenation can
improve justification.

#set text(hyphenate: false)
This text illustrates how
enabling hyphenation can
improve justification.
```

![Preview](/assets/docs/4Pafis8Dv1GSWE8dIkAx2wAAAAAAAAAA.png)

Default: `auto`

### `costs` [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The "cost" of various choices when laying out text. A higher cost means
the layout engine will make the choice less often. Costs are specified
as a ratio of the default cost, so `50%` will make text layout twice
as eager to make a given choice, while `200%` will make it half as
eager.

Currently, the following costs can be customized:

- `hyphenation`: splitting a word across multiple lines
- `runt`: ending a paragraph with a line with a single word
- `widow`: leaving a single line of paragraph on the next page
- `orphan`: leaving single line of paragraph on the previous page

Hyphenation is generally avoided by placing the whole word on the next
line, so a higher hyphenation cost can result in awkward justification
spacing. Note: Hyphenation costs will only be applied when the
[`linebreaks`](/docs/reference/model/par/#parameters-linebreaks) are set to "optimized". (For example
by default implied by [`justify`](/docs/reference/model/par/#parameters-justify).)

Runts are avoided by placing more or fewer words on previous lines, so a
higher runt cost can result in more awkward in justification spacing.

Text layout prevents widows and orphans by default because they are
generally discouraged by style guides. However, in some contexts they
are allowed because the prevention method, which moves a line to the
next page, can result in an uneven number of lines between pages. The
`widow` and `orphan` costs allow disabling these modifications.
(Currently, `0%` allows widows/orphans; anything else, including the
default of `100%`, prevents them. More nuanced cost specification for
these modifications is planned for the future.)

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(hyphenate: true, size: 11.4pt)
#set par(justify: true)

#lorem(10)

// Set hyphenation to ten times the normal cost.
#set text(costs: (hyphenation: 1000%))

#lorem(10)
```

![Preview](/assets/docs/k9JLw8qIVUINakYrnv50nAAAAAAAAAAA.png)

Default: `(
hyphenation: 100%,
runt: 100%,
widow: 100%,
orphan: 100%,
)`

### `kerning` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether to apply kerning.

When enabled, specific letter pairings move closer together or further
apart for a more visually pleasing result. The example below
demonstrates how decreasing the gap between the "T" and "o" results in a
more natural look. Setting this to `false` disables kerning by turning
off the OpenType `kern` font feature.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(size: 25pt)
Totally

#set text(kerning: false)
Totally
```

![Preview](/assets/docs/7Gj4TjnwP0QfSOeJi7dKdAAAAAAAAAAA.png)

Default: `true`

### `alternates` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether to apply stylistic alternates.

Sometimes fonts contain alternative glyphs for the same codepoint.
Setting this to `true` switches to these by enabling the OpenType
`salt` font feature.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(
  font: "IBM Plex Sans",
  size: 20pt,
)

0, a, g, ß

#set text(alternates: true)
0, a, g, ß
```

![Preview](/assets/docs/I0B88ggX_x3jq5W1mvWVIgAAAAAAAAAA.png)

Default: `false`

### `stylistic-set` [none](/docs/reference/foundations/none/) or [int](/docs/reference/foundations/int/) or [array](/docs/reference/foundations/array/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Which stylistic sets to apply. Font designers can categorize alternative
glyphs forms into stylistic sets. As this value is highly font-specific,
you need to consult your font to know which sets are available.

This can be set to an integer or an array of integers, all
of which must be between `1` and `20`, enabling the
corresponding OpenType feature(s) from `ss01` to `ss20`.
Setting this to `none` will disable all stylistic sets.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(font: "IBM Plex Serif")
ß vs #text(stylistic-set: 5)[ß] \
10 years ago vs #text(stylistic-set: (1, 2, 3))[10 years ago]
```

![Preview](/assets/docs/W4bB6oEym3iwH_NdeQRsEAAAAAAAAAAA.png)

Default: `()`

### `ligatures` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether standard ligatures are active.

Certain letter combinations like "fi" are often displayed as a single
merged glyph called a *ligature.* Setting this to `false` disables
these ligatures by turning off the OpenType `liga` and `clig` font
features.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(size: 20pt)
A fine ligature.

#set text(ligatures: false)
A fine ligature.
```

![Preview](/assets/docs/IQnLFKoKsoxRyhR3pSbfiwAAAAAAAAAA.png)

Note that some programming fonts use other OpenType font features to
implement "ligatures," including the contextual alternates (`calt`)
feature, which is also enabled by default. Use the general
[`features`](/docs/reference/text/text/#parameters-features) parameter to control such features.

Default: `true`

### `discretionary-ligatures` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether ligatures that should be used sparingly are active. Setting this
to `true` enables the OpenType `dlig` font feature.

Default: `false`

### `historical-ligatures` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether historical ligatures are active. Setting this to `true`
enables the OpenType `hlig` font feature.

Default: `false`

### `number-type` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Which kind of numbers / figures to select. When set to `auto`, the
default numbers for the font are used.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(font: "Noto Sans", 20pt)
#set text(number-type: "lining")
Number 9.

#set text(number-type: "old-style")
Number 9.
```

![Preview](/assets/docs/Jl5yPI_4pX3UbcVjqxI5_QAAAAAAAAAA.png)

| Variant | Details |
| --- | --- |
| `"lining"` | Numbers that fit well with capital text (the OpenType `lnum` font feature). |
| `"old-style"` | Numbers that fit well into a flow of upper- and lowercase text (the OpenType `onum` font feature). |

Default: `auto`

### `number-width` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The width of numbers / figures. When set to `auto`, the default
numbers for the font are used.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(font: "Noto Sans", 20pt)
#set text(number-width: "proportional")
A 12 B 34. \
A 56 B 78.

#set text(number-width: "tabular")
A 12 B 34. \
A 56 B 78.
```

![Preview](/assets/docs/6iCMWj0AW9bSFKBJ48tdiwAAAAAAAAAA.png)

| Variant | Details |
| --- | --- |
| `"proportional"` | Numbers with glyph-specific widths (the OpenType `pnum` font feature). |
| `"tabular"` | Numbers of equal width (the OpenType `tnum` font feature). |

Default: `auto`

### `slashed-zero` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether to have a slash through the zero glyph. Setting this to `true`
enables the OpenType `zero` font feature.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
0, #text(slashed-zero: true)[0]
```

![Preview](/assets/docs/NqkvE1KDtvrmSgKJnmfRWwAAAAAAAAAA.png)

Default: `false`

### `fractions` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether to turn numbers into fractions. Setting this to `true`
enables the OpenType `frac` font feature.

It is not advisable to enable this property globally as it will mess
with all appearances of numbers after a slash (e.g., in URLs). Instead,
enable it locally when you want a fraction.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
1/2 \
#text(fractions: true)[1/2]
```

![Preview](/assets/docs/ReL3WGljBzDnfTHeymCXGQAAAAAAAAAA.png)

Default: `false`

### `features` [array](/docs/reference/foundations/array/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Raw OpenType features to apply.

- If given an array of strings, sets the features identified by the
  strings to `1`.
- If given a dictionary mapping to numbers, sets the features
  identified by the keys to the values.

  ![](/assets/icons/16-chevron-right.svg) View example: Give an array of strings 

```typst
// Enable the `frac` feature manually.
#set text(features: ("frac",))
1/2
```

![Preview](/assets/docs/YY_AfHqvOwZWtTBzfgDvMwAAAAAAAAAA.png)

   ![](/assets/icons/16-chevron-right.svg) View example: Give a dictionary mapping to numbers 

```typst
#set text(font: "Cascadia Code")
=>
// Disable the contextual alternates (`calt`) feature.
#set text(features: (calt: 0))
=>
```

![Preview](/assets/docs/g0H81UZgT_6ubn0WiwGDigAAAAAAAAAA.png)

Default: `(:)`

### `body` [content](/docs/reference/foundations/content/)

Content in which all text is styled according to the other arguments.

Default: `[]`

### `text` [str](/docs/reference/foundations/str/) Required Positional Question mark Positional parameters are specified in order, without names.

The text.

[![←](/assets/icons/16-chevron-right.svg)

SuperscriptPrevious page](/docs/reference/text/super/) [![→](/assets/icons/16-chevron-right.svg)

UnderlineNext page](/docs/reference/text/underline/)