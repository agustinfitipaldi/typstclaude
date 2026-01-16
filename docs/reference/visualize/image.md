# imageElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/visualize/image/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Visualize](/docs/reference/visualize/)
- ![](/assets/icons/16-chevron-right.svg)
- [Image](/docs/reference/visualize/image/)

# `image`Element Question mark Element functions can be customized with `set` and `show` rules.

A raster or vector graphic.

You can wrap the image in a [`figure`](/docs/reference/model/figure/ "`figure`") to give it a number and caption.

Like most elements, images are *block-level* by default and thus do not
integrate themselves into adjacent paragraphs. To force an image to become
inline, put it into a [`box`](/docs/reference/layout/box/ "`box`").

## Example

```typst
#figure(
  image("molecular.jpg", width: 80%),
  caption: [
    A step in the molecular testing
    pipeline of our lab.
  ],
)
```

![Preview](/assets/docs/znWnPh4HT5GrpkEcbnfOxAAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

image(

[str](/docs/reference/foundations/str/)[bytes](/docs/reference/foundations/bytes/),[format:](#parameters-format) [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/)[dictionary](/docs/reference/foundations/dictionary/),[width:](#parameters-width) [auto](/docs/reference/foundations/auto/)[relative](/docs/reference/layout/relative/),[height:](#parameters-height) [auto](/docs/reference/foundations/auto/)[relative](/docs/reference/layout/relative/)[fraction](/docs/reference/layout/fraction/),[alt:](#parameters-alt) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/),[page:](#parameters-page) [int](/docs/reference/foundations/int/),[fit:](#parameters-fit) [str](/docs/reference/foundations/str/),[scaling:](#parameters-scaling) [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/),[icc:](#parameters-icc) [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/)[bytes](/docs/reference/foundations/bytes/),

) -> [content](/docs/reference/foundations/content/)

### `source` [str](/docs/reference/foundations/str/) or [bytes](/docs/reference/foundations/bytes/) Required Positional Question mark Positional parameters are specified in order, without names.

A [path](/docs/reference/syntax/#paths) to an image file or raw bytes making up an
image in one of the supported [formats](/docs/reference/visualize/image/#parameters-format).

Bytes can be used to specify raw pixel data in a row-major,
left-to-right, top-to-bottom format.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#let original = read("diagram.svg")
#let changed = original.replace(
  "#2B80FF", // blue
  green.to-hex(),
)

#image(bytes(original))
#image(bytes(changed))
```

![Preview](/assets/docs/jEkAIh8knrr3qHE3YaDfUQAAAAAAAAAA.png)

### `format` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/) or [dictionary](/docs/reference/foundations/dictionary/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The image's format.

By default, the format is detected automatically. Typically, you thus
only need to specify this when providing raw bytes as the
[`source`](/docs/reference/visualize/image/#parameters-source) (even then, Typst will try to figure out the
format automatically, but that's not always possible).

Supported formats are `"png"`, `"jpg"`, `"gif"`, `"svg"`,
`"pdf"`, `"webp"` as well as raw pixel data.

Note that several restrictions apply when using PDF files as images:

- When exporting to PDF, any PDF image file used must have a version
  equal to or lower than the [export target PDF
  version](/docs/reference/pdf/#pdf-versions).
- PDF files as images are currently not supported when exporting with a
  specific PDF standard, like PDF/A-3 or PDF/UA-1. In these cases, you
  can instead use SVGs to embed vector images.
- The image file must not be password-protected.
- Tags in your PDF image will not be preserved. Instead, you must
  provide an [alternative description](/docs/reference/visualize/image/#parameters-alt) to make the image
  accessible.

When providing raw pixel data as the `source`, you must specify a
dictionary with the following keys as the `format`:

- `encoding` ([str](/docs/reference/foundations/str/ "str")): The encoding of the pixel data. One of:
  - `"rgb8"` (three 8-bit channels: red, green, blue)
  - `"rgba8"` (four 8-bit channels: red, green, blue, alpha)
  - `"luma8"` (one 8-bit channel)
  - `"lumaa8"` (two 8-bit channels: luma and alpha)
- `width` ([int](/docs/reference/foundations/int/ "int")): The pixel width of the image.
- `height` ([int](/docs/reference/foundations/int/ "int")): The pixel height of the image.

The pixel width multiplied by the height multiplied by the channel count
for the specified encoding must then match the `source` data.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#image(
  read(
    "tetrahedron.svg",
    encoding: none,
  ),
  format: "svg",
  width: 2cm,
)

#image(
  bytes(range(16).map(x => x * 16)),
  format: (
    encoding: "luma8",
    width: 4,
    height: 4,
  ),
  width: 2cm,
)
```

![Preview](/assets/docs/EP-W_DoQ_ePaY37BK1ZjegAAAAAAAAAA.png)

| Variant | Details |
| --- | --- |
| `"png"` | Raster format for illustrations and transparent graphics. |
| `"jpg"` | Lossy raster format suitable for photos. |
| `"gif"` | Raster format that is typically used for short animated clips. Typst can load GIFs, but they will become static. |
| `"webp"` | Raster format that supports both lossy and lossless compression. |
| `"svg"` | The vector graphics format of the web. |
| `"pdf"` | High-fidelity document and graphics format, with focus on exact reproduction in print. |

Default: `auto`

### `width` [auto](/docs/reference/foundations/auto/) or [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The width of the image.

Default: `auto`

### `height` [auto](/docs/reference/foundations/auto/) or [relative](/docs/reference/layout/relative/) or [fraction](/docs/reference/layout/fraction/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The height of the image.

Default: `auto`

### `alt` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

An alternative description of the image.

This text is used by Assistive Technology (AT) like screen readers to
describe the image to users with visual impairments.

When the image is wrapped in a [`figure`](/docs/reference/model/figure/), use this parameter
rather than the [figure's `alt` parameter](/docs/reference/model/figure/#parameters-alt) to describe the
image. The only exception to this rule is when the image and the other
contents in the figure form a single semantic unit. In this case, use
the figure's `alt` parameter to describe the entire composition and do
not use this parameter.

You can learn how to write good alternative descriptions in the
[Accessibility Guide](/docs/guides/accessibility/#textual-representations).

Default: `none`

### `page` [int](/docs/reference/foundations/int/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The page number that should be embedded as an image. This attribute only
has an effect for PDF files.

Default: `1`

### `fit` [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

How the image should adjust itself to a given area (the area is defined
by the `width` and `height` fields). Note that `fit` doesn't visually
change anything if the area's aspect ratio is the same as the image's
one.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set page(width: 300pt, height: 50pt, margin: 10pt)
#image("tiger.jpg", width: 100%, fit: "cover")
#image("tiger.jpg", width: 100%, fit: "contain")
#image("tiger.jpg", width: 100%, fit: "stretch")
```

![Preview](/assets/docs/oZRwamqZZ0p_tV8oioYxxgAAAAAAAAAA.png)
![Preview](/assets/docs/oZRwamqZZ0p_tV8oioYxxgAAAAAAAAAB.png)
![Preview](/assets/docs/oZRwamqZZ0p_tV8oioYxxgAAAAAAAAAC.png)

| Variant | Details |
| --- | --- |
| `"cover"` | The image should completely cover the area (preserves aspect ratio by cropping the image only horizontally or vertically). This is the default. |
| `"contain"` | The image should be fully contained in the area (preserves aspect ratio; doesn't crop the image; one dimension can be narrower than specified). |
| `"stretch"` | The image should be stretched so that it exactly fills the area, even if this means that the image will be distorted (doesn't preserve aspect ratio and doesn't crop the image). |

Default: `"cover"`

### `scaling` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

A hint to viewers how they should scale the image.

When set to `auto`, the default is left up to the viewer. For PNG
export, Typst will default to smooth scaling, like most PDF and SVG
viewers.

*Note:* The exact look may differ across PDF viewers.

| Variant | Details |
| --- | --- |
| `"smooth"` | Scale with a smoothing algorithm such as bilinear interpolation. |
| `"pixelated"` | Scale with nearest neighbor or a similar algorithm to preserve the pixelated look of the image. |

Default: `auto`

### `icc` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/) or [bytes](/docs/reference/foundations/bytes/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

An ICC profile for the image.

ICC profiles define how to interpret the colors in an image. When set
to `auto`, Typst will try to extract an ICC profile from the image.

Default: `auto`

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `decode` Warning `image.decode` is deprecated, directly pass bytes to `image` instead; it will be removed in Typst 0.15.0

Decode a raster or vector graphic from bytes or a string.

image.decode(

[str](/docs/reference/foundations/str/)[bytes](/docs/reference/foundations/bytes/),[format:](#definitions-decode-format) [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/)[dictionary](/docs/reference/foundations/dictionary/),[width:](#definitions-decode-width) [auto](/docs/reference/foundations/auto/)[relative](/docs/reference/layout/relative/),[height:](#definitions-decode-height) [auto](/docs/reference/foundations/auto/)[relative](/docs/reference/layout/relative/)[fraction](/docs/reference/layout/fraction/),[alt:](#definitions-decode-alt) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/),[fit:](#definitions-decode-fit) [str](/docs/reference/foundations/str/),[scaling:](#definitions-decode-scaling) [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/),

) -> [content](/docs/reference/foundations/content/)

#### `data` [str](/docs/reference/foundations/str/) or [bytes](/docs/reference/foundations/bytes/) Required Positional Question mark Positional parameters are specified in order, without names.

The data to decode as an image. Can be a string for SVGs.

#### `format` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/) or [dictionary](/docs/reference/foundations/dictionary/)

The image's format. Detected automatically by default.

| Variant | Details |
| --- | --- |
| `"png"` | Raster format for illustrations and transparent graphics. |
| `"jpg"` | Lossy raster format suitable for photos. |
| `"gif"` | Raster format that is typically used for short animated clips. Typst can load GIFs, but they will become static. |
| `"webp"` | Raster format that supports both lossy and lossless compression. |
| `"svg"` | The vector graphics format of the web. |
| `"pdf"` | High-fidelity document and graphics format, with focus on exact reproduction in print. |

#### `width` [auto](/docs/reference/foundations/auto/) or [relative](/docs/reference/layout/relative/)

The width of the image.

#### `height` [auto](/docs/reference/foundations/auto/) or [relative](/docs/reference/layout/relative/) or [fraction](/docs/reference/layout/fraction/)

The height of the image.

#### `alt` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/)

A text describing the image.

#### `fit` [str](/docs/reference/foundations/str/)

How the image should adjust itself to a given area.

| Variant | Details |
| --- | --- |
| `"cover"` | The image should completely cover the area (preserves aspect ratio by cropping the image only horizontally or vertically). This is the default. |
| `"contain"` | The image should be fully contained in the area (preserves aspect ratio; doesn't crop the image; one dimension can be narrower than specified). |
| `"stretch"` | The image should be stretched so that it exactly fills the area, even if this means that the image will be distorted (doesn't preserve aspect ratio and doesn't crop the image). |

#### `scaling` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/)

A hint to viewers how they should scale the image.

| Variant | Details |
| --- | --- |
| `"smooth"` | Scale with a smoothing algorithm such as bilinear interpolation. |
| `"pixelated"` | Scale with nearest neighbor or a similar algorithm to preserve the pixelated look of the image. |

[![←](/assets/icons/16-chevron-right.svg)

GradientPrevious page](/docs/reference/visualize/gradient/) [![→](/assets/icons/16-chevron-right.svg)

LineNext page](/docs/reference/visualize/line/)