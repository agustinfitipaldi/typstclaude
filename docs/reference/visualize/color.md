# color

Source: https://typst.app/docs/reference/visualize/color/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Visualize](/docs/reference/visualize/)
- ![](/assets/icons/16-chevron-right.svg)
- [Color](/docs/reference/visualize/color/)

# color

A color in a specific color space.

Typst supports:

- sRGB through the [`rgb` function](/docs/reference/visualize/color/#definitions-rgb)
- Device CMYK through the [`cmyk` function](/docs/reference/visualize/color/#definitions-cmyk)
- D65 Gray through the [`luma` function](/docs/reference/visualize/color/#definitions-luma)
- Oklab through the [`oklab` function](/docs/reference/visualize/color/#definitions-oklab)
- Oklch through the [`oklch` function](/docs/reference/visualize/color/#definitions-oklch)
- Linear RGB through the [`color.linear-rgb` function](/docs/reference/visualize/color/#definitions-linear-rgb)
- HSL through the [`color.hsl` function](/docs/reference/visualize/color/#definitions-hsl)
- HSV through the [`color.hsv` function](/docs/reference/visualize/color/#definitions-hsv)

## Example

```typst
#rect(fill: aqua)
```

![Preview](/assets/docs/k-6wh2l9TTXmPhzZxpahjQAAAAAAAAAA.png)

## Predefined colors

Typst defines the following built-in colors:

| Color | Definition |
| --- | --- |
| `black` | `luma(0)` |
| `gray` | `luma(170)` |
| `silver` | `luma(221)` |
| `white` | `luma(255)` |
| `navy` | `rgb("#001f3f")` |
| `blue` | `rgb("#0074d9")` |
| `aqua` | `rgb("#7fdbff")` |
| `teal` | `rgb("#39cccc")` |
| `eastern` | `rgb("#239dad")` |
| `purple` | `rgb("#b10dc9")` |
| `fuchsia` | `rgb("#f012be")` |
| `maroon` | `rgb("#85144b")` |
| `red` | `rgb("#ff4136")` |
| `orange` | `rgb("#ff851b")` |
| `yellow` | `rgb("#ffdc00")` |
| `olive` | `rgb("#3d9970")` |
| `green` | `rgb("#2ecc40")` |
| `lime` | `rgb("#01ff70")` |

The predefined colors and the most important color constructors are
available globally and also in the color type's scope, so you can write
either `color.red` or just `red`.

![Preview](/assets/docs/IWvUAQq21Ue1zu9gwjch-gAAAAAAAAAA.png)

## Predefined color maps

Typst also includes a number of preset color maps that can be used for
[gradients](/docs/reference/visualize/gradient/#stops). These are simply arrays of colors defined in
the module `color.map`.

```typst
#circle(fill: gradient.linear(..color.map.crest))
```

![Preview](/assets/docs/uG6iVgmQwH_6_-1N42yKHwAAAAAAAAAA.png)

| Map | Details |
| --- | --- |
| `turbo` | A perceptually uniform rainbow-like color map. Read [this blog post](https://ai.googleblog.com/2019/08/turbo-improved-rainbow-colormap-for.html) for more details. |
| `cividis` | A blue to gray to yellow color map. See [this blog post](https://bids.github.io/colormap/) for more details. |
| `rainbow` | Cycles through the full color spectrum. This color map is best used by setting the interpolation color space to [HSL](/docs/reference/visualize/color/#definitions-hsl). The rainbow gradient is **not suitable** for data visualization because it is not perceptually uniform, so the differences between values become unclear to your readers. It should only be used for decorative purposes. |
| `spectral` | Red to yellow to blue color map. |
| `viridis` | A purple to teal to yellow color map. |
| `inferno` | A black to red to yellow color map. |
| `magma` | A black to purple to yellow color map. |
| `plasma` | A purple to pink to yellow color map. |
| `rocket` | A black to red to white color map. |
| `mako` | A black to teal to white color map. |
| `vlag` | A light blue to white to red color map. |
| `icefire` | A light teal to black to orange color map. |
| `flare` | A orange to purple color map that is perceptually uniform. |
| `crest` | A light green to blue color map. |

Some popular presets are not included because they are not available under a
free licence. Others, like
[Jet](https://jakevdp.github.io/blog/2014/10/16/how-bad-is-your-colormap/),
are not included because they are not color blind friendly. Feel free to use
or create a package with other presets that are useful to you!

![Preview](/assets/docs/S2ExoTDRK30Xf9wXJbWIZgAAAAAAAAAA.png)

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `luma`

Create a grayscale color.

A grayscale color is represented internally by a single `lightness`
component.

These components are also available using the
[`components`](/docs/reference/visualize/color/#definitions-components) method.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#for x in range(250, step: 50) {
  box(square(fill: luma(x)))
}
```

![Preview](/assets/docs/bCTOWkOtpDPjuD2iPgTajQAAAAAAAAAA.png)

color.luma(

[int](/docs/reference/foundations/int/)[ratio](/docs/reference/layout/ratio/),[ratio](/docs/reference/layout/ratio/),[color](/docs/reference/visualize/color/),

) -> [color](/docs/reference/visualize/color/)

#### `lightness` [int](/docs/reference/foundations/int/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The lightness component.

#### `alpha` [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The alpha component.

#### `color` [color](/docs/reference/visualize/color/) Required Positional Question mark Positional parameters are specified in order, without names.

Alternatively: The color to convert to grayscale.

If this is given, the `lightness` should not be given.

### `oklab`

Create an [Oklab](https://bottosson.github.io/posts/oklab/) color.

This color space is well suited for the following use cases:

- Color manipulation such as saturating while keeping perceived hue
- Creating grayscale images with uniform perceived lightness
- Creating smooth and uniform color transition and gradients

A linear Oklab color is represented internally by an array of four
components:

- lightness ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))
- a ([`float`](/docs/reference/foundations/float/ "`float`") or [`ratio`](/docs/reference/layout/ratio/ "`ratio`").
  Ratios are relative to `0.4`; meaning `50%` is equal to `0.2`)
- b ([`float`](/docs/reference/foundations/float/ "`float`") or [`ratio`](/docs/reference/layout/ratio/ "`ratio`").
  Ratios are relative to `0.4`; meaning `50%` is equal to `0.2`)
- alpha ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))

These components are also available using the
[`components`](/docs/reference/visualize/color/#definitions-components) method.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#square(
  fill: oklab(27%, 20%, -3%, 50%)
)
```

![Preview](/assets/docs/1dGzDbwdYzYb5NzJEzQzFAAAAAAAAAAA.png)

color.oklab(

[ratio](/docs/reference/layout/ratio/),[float](/docs/reference/foundations/float/)[ratio](/docs/reference/layout/ratio/),[float](/docs/reference/foundations/float/)[ratio](/docs/reference/layout/ratio/),[ratio](/docs/reference/layout/ratio/),[color](/docs/reference/visualize/color/),

) -> [color](/docs/reference/visualize/color/)

#### `lightness` [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The lightness component.

#### `a` [float](/docs/reference/foundations/float/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The a ("green/red") component.

#### `b` [float](/docs/reference/foundations/float/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The b ("blue/yellow") component.

#### `alpha` [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The alpha component.

#### `color` [color](/docs/reference/visualize/color/) Required Positional Question mark Positional parameters are specified in order, without names.

Alternatively: The color to convert to Oklab.

If this is given, the individual components should not be given.

### `oklch`

Create an [Oklch](https://bottosson.github.io/posts/oklab/) color.

This color space is well suited for the following use cases:

- Color manipulation involving lightness, chroma, and hue
- Creating grayscale images with uniform perceived lightness
- Creating smooth and uniform color transition and gradients

A linear Oklch color is represented internally by an array of four
components:

- lightness ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))
- chroma ([`float`](/docs/reference/foundations/float/ "`float`") or [`ratio`](/docs/reference/layout/ratio/ "`ratio`").
  Ratios are relative to `0.4`; meaning `50%` is equal to `0.2`)
- hue ([`angle`](/docs/reference/layout/angle/ "`angle`"))
- alpha ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))

These components are also available using the
[`components`](/docs/reference/visualize/color/#definitions-components) method.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#square(
  fill: oklch(40%, 0.2, 160deg, 50%)
)
```

![Preview](/assets/docs/gEJt1PBpGTajcUm46S-JNgAAAAAAAAAA.png)

color.oklch(

[ratio](/docs/reference/layout/ratio/),[float](/docs/reference/foundations/float/)[ratio](/docs/reference/layout/ratio/),[angle](/docs/reference/layout/angle/),[ratio](/docs/reference/layout/ratio/),[color](/docs/reference/visualize/color/),

) -> [color](/docs/reference/visualize/color/)

#### `lightness` [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The lightness component.

#### `chroma` [float](/docs/reference/foundations/float/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The chroma component.

#### `hue` [angle](/docs/reference/layout/angle/) Required Positional Question mark Positional parameters are specified in order, without names.

The hue component.

#### `alpha` [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The alpha component.

#### `color` [color](/docs/reference/visualize/color/) Required Positional Question mark Positional parameters are specified in order, without names.

Alternatively: The color to convert to Oklch.

If this is given, the individual components should not be given.

### `linear-rgb`

Create an RGB(A) color with linear luma.

This color space is similar to sRGB, but with the distinction that the
color component are not gamma corrected. This makes it easier to perform
color operations such as blending and interpolation. Although, you
should prefer to use the [`oklab` function](/docs/reference/visualize/color/#definitions-oklab) for these.

A linear RGB(A) color is represented internally by an array of four
components:

- red ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))
- green ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))
- blue ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))
- alpha ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))

These components are also available using the
[`components`](/docs/reference/visualize/color/#definitions-components) method.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#square(fill: color.linear-rgb(
  30%, 50%, 10%,
))
```

![Preview](/assets/docs/C39dYHKq1AmgEkOU8XX2kQAAAAAAAAAA.png)

color.linear-rgb(

[int](/docs/reference/foundations/int/)[ratio](/docs/reference/layout/ratio/),[int](/docs/reference/foundations/int/)[ratio](/docs/reference/layout/ratio/),[int](/docs/reference/foundations/int/)[ratio](/docs/reference/layout/ratio/),[int](/docs/reference/foundations/int/)[ratio](/docs/reference/layout/ratio/),[color](/docs/reference/visualize/color/),

) -> [color](/docs/reference/visualize/color/)

#### `red` [int](/docs/reference/foundations/int/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The red component.

#### `green` [int](/docs/reference/foundations/int/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The green component.

#### `blue` [int](/docs/reference/foundations/int/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The blue component.

#### `alpha` [int](/docs/reference/foundations/int/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The alpha component.

#### `color` [color](/docs/reference/visualize/color/) Required Positional Question mark Positional parameters are specified in order, without names.

Alternatively: The color to convert to linear RGB(A).

If this is given, the individual components should not be given.

### `rgb`

Create an RGB(A) color.

The color is specified in the sRGB color space.

An RGB(A) color is represented internally by an array of four components:

- red ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))
- green ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))
- blue ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))
- alpha ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))

These components are also available using the [`components`](/docs/reference/visualize/color/#definitions-components)
method.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#square(fill: rgb("#b1f2eb"))
#square(fill: rgb(87, 127, 230))
#square(fill: rgb(25%, 13%, 65%))
```

![Preview](/assets/docs/eWivZbkq7oFotM06OeK92AAAAAAAAAAA.png)

color.rgb(

[int](/docs/reference/foundations/int/)[ratio](/docs/reference/layout/ratio/),[int](/docs/reference/foundations/int/)[ratio](/docs/reference/layout/ratio/),[int](/docs/reference/foundations/int/)[ratio](/docs/reference/layout/ratio/),[int](/docs/reference/foundations/int/)[ratio](/docs/reference/layout/ratio/),[str](/docs/reference/foundations/str/),[color](/docs/reference/visualize/color/),

) -> [color](/docs/reference/visualize/color/)

#### `red` [int](/docs/reference/foundations/int/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The red component.

#### `green` [int](/docs/reference/foundations/int/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The green component.

#### `blue` [int](/docs/reference/foundations/int/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The blue component.

#### `alpha` [int](/docs/reference/foundations/int/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The alpha component.

#### `hex` [str](/docs/reference/foundations/str/) Required Positional Question mark Positional parameters are specified in order, without names.

Alternatively: The color in hexadecimal notation.

Accepts three, four, six or eight hexadecimal digits and optionally
a leading hash.

If this is given, the individual components should not be given.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#text(16pt, rgb("#239dad"))[
  *Typst*
]
```

![Preview](/assets/docs/rKfIt6nqSzoBRXt7k7BMOwAAAAAAAAAA.png)

#### `color` [color](/docs/reference/visualize/color/) Required Positional Question mark Positional parameters are specified in order, without names.

Alternatively: The color to convert to RGB(a).

If this is given, the individual components should not be given.

### `cmyk`

Create a CMYK color.

This is useful if you want to target a specific printer. The conversion
to RGB for display preview might differ from how your printer reproduces
the color.

A CMYK color is represented internally by an array of four components:

- cyan ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))
- magenta ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))
- yellow ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))
- key ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))

These components are also available using the
[`components`](/docs/reference/visualize/color/#definitions-components) method.

Note that CMYK colors are not currently supported when PDF/A output is
enabled.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#square(
  fill: cmyk(27%, 0%, 3%, 5%)
)
```

![Preview](/assets/docs/1LHigtpFCZVjSNs83fP0eAAAAAAAAAAA.png)

color.cmyk(

[ratio](/docs/reference/layout/ratio/),[ratio](/docs/reference/layout/ratio/),[ratio](/docs/reference/layout/ratio/),[ratio](/docs/reference/layout/ratio/),[color](/docs/reference/visualize/color/),

) -> [color](/docs/reference/visualize/color/)

#### `cyan` [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The cyan component.

#### `magenta` [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The magenta component.

#### `yellow` [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The yellow component.

#### `key` [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The key component.

#### `color` [color](/docs/reference/visualize/color/) Required Positional Question mark Positional parameters are specified in order, without names.

Alternatively: The color to convert to CMYK.

If this is given, the individual components should not be given.

### `hsl`

Create an HSL color.

This color space is useful for specifying colors by hue, saturation and
lightness. It is also useful for color manipulation, such as saturating
while keeping perceived hue.

An HSL color is represented internally by an array of four components:

- hue ([`angle`](/docs/reference/layout/angle/ "`angle`"))
- saturation ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))
- lightness ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))
- alpha ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))

These components are also available using the
[`components`](/docs/reference/visualize/color/#definitions-components) method.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#square(
  fill: color.hsl(30deg, 50%, 60%)
)
```

![Preview](/assets/docs/MqR1NhT-m_ImBDX23hY7xgAAAAAAAAAA.png)

color.hsl(

[angle](/docs/reference/layout/angle/),[int](/docs/reference/foundations/int/)[ratio](/docs/reference/layout/ratio/),[int](/docs/reference/foundations/int/)[ratio](/docs/reference/layout/ratio/),[int](/docs/reference/foundations/int/)[ratio](/docs/reference/layout/ratio/),[color](/docs/reference/visualize/color/),

) -> [color](/docs/reference/visualize/color/)

#### `hue` [angle](/docs/reference/layout/angle/) Required Positional Question mark Positional parameters are specified in order, without names.

The hue angle.

#### `saturation` [int](/docs/reference/foundations/int/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The saturation component.

#### `lightness` [int](/docs/reference/foundations/int/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The lightness component.

#### `alpha` [int](/docs/reference/foundations/int/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The alpha component.

#### `color` [color](/docs/reference/visualize/color/) Required Positional Question mark Positional parameters are specified in order, without names.

Alternatively: The color to convert to HSL.

If this is given, the individual components should not be given.

### `hsv`

Create an HSV color.

This color space is useful for specifying colors by hue, saturation and
value. It is also useful for color manipulation, such as saturating
while keeping perceived hue.

An HSV color is represented internally by an array of four components:

- hue ([`angle`](/docs/reference/layout/angle/ "`angle`"))
- saturation ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))
- value ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))
- alpha ([`ratio`](/docs/reference/layout/ratio/ "`ratio`"))

These components are also available using the
[`components`](/docs/reference/visualize/color/#definitions-components) method.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#square(
  fill: color.hsv(30deg, 50%, 60%)
)
```

![Preview](/assets/docs/dEOjXMxlVX8xgAuMFF-gkQAAAAAAAAAA.png)

color.hsv(

[angle](/docs/reference/layout/angle/),[int](/docs/reference/foundations/int/)[ratio](/docs/reference/layout/ratio/),[int](/docs/reference/foundations/int/)[ratio](/docs/reference/layout/ratio/),[int](/docs/reference/foundations/int/)[ratio](/docs/reference/layout/ratio/),[color](/docs/reference/visualize/color/),

) -> [color](/docs/reference/visualize/color/)

#### `hue` [angle](/docs/reference/layout/angle/) Required Positional Question mark Positional parameters are specified in order, without names.

The hue angle.

#### `saturation` [int](/docs/reference/foundations/int/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The saturation component.

#### `value` [int](/docs/reference/foundations/int/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The value component.

#### `alpha` [int](/docs/reference/foundations/int/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The alpha component.

#### `color` [color](/docs/reference/visualize/color/) Required Positional Question mark Positional parameters are specified in order, without names.

Alternatively: The color to convert to HSL.

If this is given, the individual components should not be given.

### `components`

Extracts the components of this color.

The size and values of this array depends on the color space. You can
obtain the color space using [`space`](/docs/reference/visualize/color/#definitions-space). Below is a table
of the color spaces and their components:

| Color space | C1 | C2 | C3 | C4 |
| --- | --- | --- | --- | --- |
| [`luma`](/docs/reference/visualize/color/#definitions-luma) | Lightness |  |  |  |
| [`oklab`](/docs/reference/visualize/color/#definitions-oklab) | Lightness | `a` | `b` | Alpha |
| [`oklch`](/docs/reference/visualize/color/#definitions-oklch) | Lightness | Chroma | Hue | Alpha |
| [`linear-rgb`](/docs/reference/visualize/color/#definitions-linear-rgb) | Red | Green | Blue | Alpha |
| [`rgb`](/docs/reference/visualize/color/#definitions-rgb) | Red | Green | Blue | Alpha |
| [`cmyk`](/docs/reference/visualize/color/#definitions-cmyk) | Cyan | Magenta | Yellow | Key |
| [`hsl`](/docs/reference/visualize/color/#definitions-hsl) | Hue | Saturation | Lightness | Alpha |
| [`hsv`](/docs/reference/visualize/color/#definitions-hsv) | Hue | Saturation | Value | Alpha |

For the meaning and type of each individual value, see the documentation
of the corresponding color space. The alpha component is optional and
only included if the `alpha` argument is `true`. The length of the
returned array depends on the number of components and whether the alpha
component is included.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
// note that the alpha component is included by default
#rgb(40%, 60%, 80%).components()
```

![Preview](/assets/docs/dzB_dzQf4SM_Ou0eAcFH9AAAAAAAAAAA.png)

self.components(

[alpha:](#definitions-components-alpha) [bool](/docs/reference/foundations/bool/)

) -> [array](/docs/reference/foundations/array/)

#### `alpha` [bool](/docs/reference/foundations/bool/)

Whether to include the alpha component.

Default: `true`

### `space`

Returns the constructor function for this color's space.

Returns one of:

- [`luma`](/docs/reference/visualize/color/#definitions-luma)
- [`oklab`](/docs/reference/visualize/color/#definitions-oklab)
- [`oklch`](/docs/reference/visualize/color/#definitions-oklch)
- [`linear-rgb`](/docs/reference/visualize/color/#definitions-linear-rgb)
- [`rgb`](/docs/reference/visualize/color/#definitions-rgb)
- [`cmyk`](/docs/reference/visualize/color/#definitions-cmyk)
- [`hsl`](/docs/reference/visualize/color/#definitions-hsl)
- [`hsv`](/docs/reference/visualize/color/#definitions-hsv)

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#let color = cmyk(1%, 2%, 3%, 4%)
#(color.space() == cmyk)
```

![Preview](/assets/docs/tfic_6Fu9JDbk4Tz2rYgKAAAAAAAAAAA.png)

self.space() -> any

### `to-hex`

Returns the color's RGB(A) hex representation (such as `#ffaa32` or
`#020304fe`). The alpha component (last two digits in `#020304fe`) is
omitted if it is equal to `ff` (255 / 100%).

self.to-hex() -> [str](/docs/reference/foundations/str/)

### `lighten`

Lightens a color by a given factor.

self.lighten(

[ratio](/docs/reference/layout/ratio/)

) -> [color](/docs/reference/visualize/color/)

#### `factor` [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The factor to lighten the color by.

### `darken`

Darkens a color by a given factor.

self.darken(

[ratio](/docs/reference/layout/ratio/)

) -> [color](/docs/reference/visualize/color/)

#### `factor` [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The factor to darken the color by.

### `saturate`

Increases the saturation of a color by a given factor.

self.saturate(

[ratio](/docs/reference/layout/ratio/)

) -> [color](/docs/reference/visualize/color/)

#### `factor` [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The factor to saturate the color by.

### `desaturate`

Decreases the saturation of a color by a given factor.

self.desaturate(

[ratio](/docs/reference/layout/ratio/)

) -> [color](/docs/reference/visualize/color/)

#### `factor` [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The factor to desaturate the color by.

### `negate`

Produces the complementary color using a provided color space.
You can think of it as the opposite side on a color wheel.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#square(fill: yellow)
#square(fill: yellow.negate())
#square(fill: yellow.negate(space: rgb))
```

![Preview](/assets/docs/oBWZW_i_eZ8A9K_46wXLaQAAAAAAAAAA.png)

self.negate(

[space:](#definitions-negate-space) any

) -> [color](/docs/reference/visualize/color/)

#### `space` any

The color space used for the transformation. By default, a perceptual color space is used.

Default: `oklab`

### `rotate`

Rotates the hue of the color by a given angle.

self.rotate(

[angle](/docs/reference/layout/angle/),[space:](#definitions-rotate-space) any,

) -> [color](/docs/reference/visualize/color/)

#### `angle` [angle](/docs/reference/layout/angle/) Required Positional Question mark Positional parameters are specified in order, without names.

The angle to rotate the hue by.

#### `space` any

The color space used to rotate. By default, this happens in a perceptual
color space ([`oklch`](/docs/reference/visualize/color/#definitions-oklch)).

Default: `oklch`

### `mix`

Create a color by mixing two or more colors.

In color spaces with a hue component (hsl, hsv, oklch), only two colors
can be mixed at once. Mixing more than two colors in such a space will
result in an error!

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set block(height: 20pt, width: 100%)
#block(fill: red.mix(blue))
#block(fill: red.mix(blue, space: rgb))
#block(fill: color.mix(red, blue, white))
#block(fill: color.mix((red, 70%), (blue, 30%)))
```

![Preview](/assets/docs/0jAT6gZPo0X02CVXUm7YpAAAAAAAAAAA.png)

color.mix(

[..](#definitions-mix-colors)[color](/docs/reference/visualize/color/)[array](/docs/reference/foundations/array/),[space:](#definitions-mix-space) any,

) -> [color](/docs/reference/visualize/color/)

#### `colors` [color](/docs/reference/visualize/color/) or [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The colors, optionally with weights, specified as a pair (array of
length two) of color and weight (float or ratio).

The weights do not need to add to `100%`, they are relative to the
sum of all weights.

#### `space` any

The color space to mix in. By default, this happens in a perceptual
color space ([`oklab`](/docs/reference/visualize/color/#definitions-oklab)).

Default: `oklab`

### `transparentize`

Makes a color more transparent by a given factor.

This method is relative to the existing alpha value.
If the scale is positive, calculates `alpha - alpha * scale`.
Negative scales behave like `color.opacify(-scale)`.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#block(fill: red)[opaque]
#block(fill: red.transparentize(50%))[half red]
#block(fill: red.transparentize(75%))[quarter red]
```

![Preview](/assets/docs/bnNXhQKfjc4AYVaZ1T3e3wAAAAAAAAAA.png)

self.transparentize(

[ratio](/docs/reference/layout/ratio/)

) -> [color](/docs/reference/visualize/color/)

#### `scale` [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The factor to change the alpha value by.

### `opacify`

Makes a color more opaque by a given scale.

This method is relative to the existing alpha value.
If the scale is positive, calculates `alpha + scale - alpha * scale`.
Negative scales behave like `color.transparentize(-scale)`.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#let half-red = red.transparentize(50%)
#block(fill: half-red.opacify(100%))[opaque]
#block(fill: half-red.opacify(50%))[three quarters red]
#block(fill: half-red.opacify(-50%))[one quarter red]
```

![Preview](/assets/docs/1fq--2OrISH1g8_dvUBroAAAAAAAAAAA.png)

self.opacify(

[ratio](/docs/reference/layout/ratio/)

) -> [color](/docs/reference/visualize/color/)

#### `scale` [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The scale to change the alpha value by.

[![←](/assets/icons/16-chevron-right.svg)

CirclePrevious page](/docs/reference/visualize/circle/) [![→](/assets/icons/16-chevron-right.svg)

CurveNext page](/docs/reference/visualize/curve/)