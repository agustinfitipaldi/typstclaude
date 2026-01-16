# gradient

Source: https://typst.app/docs/reference/visualize/gradient/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Visualize](/docs/reference/visualize/)
- ![](/assets/icons/16-chevron-right.svg)
- [Gradient](/docs/reference/visualize/gradient/)

# gradient

A color gradient.

Typst supports linear gradients through the
[`gradient.linear` function](/docs/reference/visualize/gradient/#definitions-linear), radial gradients through
the [`gradient.radial` function](/docs/reference/visualize/gradient/#definitions-radial), and conic gradients
through the [`gradient.conic` function](/docs/reference/visualize/gradient/#definitions-conic).

A gradient can be used for the following purposes:

- As a fill to paint the interior of a shape:
  `rect(fill: gradient.linear(..))`
- As a stroke to paint the outline of a shape:
  `rect(stroke: 1pt + gradient.linear(..))`
- As the fill of text:
  `set text(fill: gradient.linear(..))`
- As a color map you can [sample](/docs/reference/visualize/gradient/#definitions-sample) from:
  `gradient.linear(..).sample(50%)`

## Examples

```typst
#stack(
  dir: ltr,
  spacing: 1fr,
  square(fill: gradient.linear(..color.map.rainbow)),
  square(fill: gradient.radial(..color.map.rainbow)),
  square(fill: gradient.conic(..color.map.rainbow)),
)
```

![Preview](/assets/docs/_ynuy5GKkV7ADtX87C9EiAAAAAAAAAAA.png)

Gradients are also supported on text, but only when setting the
[relativeness](/docs/reference/visualize/gradient/#definitions-relative) to either `auto` (the default value) or
`"parent"`. To create word-by-word or glyph-by-glyph gradients, you can
wrap the words or characters of your text in [boxes](/docs/reference/layout/box/) manually or
through a [show rule](/docs/reference/styling/#show-rules).

```typst
#set text(fill: gradient.linear(red, blue))
#let rainbow(content) = {
  set text(fill: gradient.linear(..color.map.rainbow))
  box(content)
}

This is a gradient on text, but with a #rainbow[twist]!
```

![Preview](/assets/docs/ch0LALUCwuQoVDnxrE_UZwAAAAAAAAAA.png)

## Stops

A gradient is composed of a series of stops. Each of these stops has a color
and an offset. The offset is a [ratio](/docs/reference/layout/ratio/) between `0%` and `100%` or
an angle between `0deg` and `360deg`. The offset is a relative position
that determines how far along the gradient the stop is located. The stop's
color is the color of the gradient at that position. You can choose to omit
the offsets when defining a gradient. In this case, Typst will space all
stops evenly.

Typst predefines color maps that you can use as stops. See the
[`color`](/docs/reference/visualize/color/#predefined-color-maps) documentation for more details.

## Relativeness

The location of the `0%` and `100%` stops depends on the dimensions
of a container. This container can either be the shape that it is being
painted on, or the closest surrounding container. This is controlled by the
`relative` argument of a gradient constructor. By default, gradients are
relative to the shape they are being painted on, unless the gradient is
applied on text, in which case they are relative to the closest ancestor
container.

Typst determines the ancestor container as follows:

- For shapes that are placed at the root/top level of the document, the
  closest ancestor is the page itself.
- For other shapes, the ancestor is the innermost [`block`](/docs/reference/layout/block/ "`block`") or [`box`](/docs/reference/layout/box/ "`box`") that
  contains the shape. This includes the boxes and blocks that are implicitly
  created by show rules and elements. For example, a [`rotate`](/docs/reference/layout/rotate/ "`rotate`") will not
  affect the parent of a gradient, but a [`grid`](/docs/reference/layout/grid/ "`grid`") will.

## Color spaces and interpolation

Gradients can be interpolated in any color space. By default, gradients are
interpolated in the [Oklab](/docs/reference/visualize/color/#definitions-oklab) color space, which is a
[perceptually uniform](https://programmingdesignsystems.com/color/perceptually-uniform-color-spaces/index.html)
color space. This means that the gradient will be perceived as having a
smooth progression of colors. This is particularly useful for data
visualization.

However, you can choose to interpolate the gradient in any supported color
space you want, but beware that some color spaces are not suitable for
perceptually interpolating between colors. Consult the table below when
choosing an interpolation space.

| Color space | Perceptually uniform? |
| --- | --- |
| [Oklab](/docs/reference/visualize/color/#definitions-oklab) | *Yes* |
| [Oklch](/docs/reference/visualize/color/#definitions-oklch) | *Yes* |
| [sRGB](/docs/reference/visualize/color/#definitions-rgb) | *No* |
| [linear-RGB](/docs/reference/visualize/color/#definitions-linear-rgb) | *Yes* |
| [CMYK](/docs/reference/visualize/color/#definitions-cmyk) | *No* |
| [Grayscale](/docs/reference/visualize/color/#definitions-luma) | *Yes* |
| [HSL](/docs/reference/visualize/color/#definitions-hsl) | *No* |
| [HSV](/docs/reference/visualize/color/#definitions-hsv) | *No* |

![Preview](/assets/docs/vhi2AIjx3T8urqy_40DDsQAAAAAAAAAA.png)

## Direction

Some gradients are sensitive to direction. For example, a linear gradient
has an angle that determines its direction. Typst uses a clockwise angle,
with 0° being from left to right, 90° from top to bottom, 180° from right to
left, and 270° from bottom to top.

```typst
#stack(
  dir: ltr,
  spacing: 1fr,
  square(fill: gradient.linear(red, blue, angle: 0deg)),
  square(fill: gradient.linear(red, blue, angle: 90deg)),
  square(fill: gradient.linear(red, blue, angle: 180deg)),
  square(fill: gradient.linear(red, blue, angle: 270deg)),
)
```

![Preview](/assets/docs/cXgxeaTP2ci7NL16a3rB_gAAAAAAAAAA.png)

## Note on file sizes

Gradients can be quite large, especially if they have many stops. This is
because gradients are stored as a list of colors and offsets, which can
take up a lot of space. If you are concerned about file sizes, you should
consider the following:

- SVG gradients are currently inefficiently encoded. This will be improved
  in the future.
- PDF gradients in the [`color.oklab`](/docs/reference/visualize/color/#definitions-oklab "`color.oklab`"), [`color.hsv`](/docs/reference/visualize/color/#definitions-hsv "`color.hsv`"), [`color.hsl`](/docs/reference/visualize/color/#definitions-hsl "`color.hsl`"), and
  [`color.oklch`](/docs/reference/visualize/color/#definitions-oklch "`color.oklch`") color spaces are stored as a list of [`color.rgb`](/docs/reference/visualize/color/#definitions-rgb "`color.rgb`") colors
  with extra stops in between. This avoids needing to encode these color
  spaces in your PDF file, but it does add extra stops to your gradient,
  which can increase the file size.

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `linear`

Creates a new linear gradient, in which colors transition along a
straight line.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#rect(
  width: 100%,
  height: 20pt,
  fill: gradient.linear(
    ..color.map.viridis,
  ),
)
```

![Preview](/assets/docs/3vCVaADmPcUqYOLma4-wcgAAAAAAAAAA.png)

gradient.linear(

[..](#definitions-linear-stops)[color](/docs/reference/visualize/color/)[array](/docs/reference/foundations/array/),[space:](#definitions-linear-space) any,[relative:](#definitions-linear-relative) [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/),[direction](/docs/reference/layout/direction/),[angle](/docs/reference/layout/angle/),

) -> [gradient](/docs/reference/visualize/gradient/)

#### `stops` [color](/docs/reference/visualize/color/) or [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The color [stops](#stops) of the gradient.

#### `space` any

The color space in which to interpolate the gradient.

Defaults to a perceptually uniform color space called
[Oklab](/docs/reference/visualize/color/#definitions-oklab).

Default: `oklab`

#### `relative` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/)

The [relative placement](#relativeness) of the gradient.

For an element placed at the root/top level of the document, the
parent is the page itself. For other elements, the parent is the
innermost block, box, column, grid, or stack that contains the
element.

| Variant | Details |
| --- | --- |
| `"self"` | Relative to itself (its own bounding box). |
| `"parent"` | Relative to its parent (the parent's bounding box). |

Default: `auto`

#### `dir` [direction](/docs/reference/layout/direction/) Positional Question mark Positional parameters are specified in order, without names.

The direction of the gradient.

Default: `ltr`

#### `angle` [angle](/docs/reference/layout/angle/) Required Positional Question mark Positional parameters are specified in order, without names.

The angle of the gradient.

### `radial`

Creates a new radial gradient, in which colors radiate away from an
origin.

The gradient is defined by two circles: the focal circle and the end
circle. The focal circle is a circle with center `focal-center` and
radius `focal-radius`, that defines the points at which the gradient
starts and has the color of the first stop. The end circle is a circle
with center `center` and radius `radius`, that defines the points at
which the gradient ends and has the color of the last stop. The gradient
is then interpolated between these two circles.

Using these four values, also called the focal point for the starting
circle and the center and radius for the end circle, we can define a
gradient with more interesting properties than a basic radial gradient.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#stack(
  dir: ltr,
  spacing: 1fr,
  circle(fill: gradient.radial(
    ..color.map.viridis,
  )),
  circle(fill: gradient.radial(
    ..color.map.viridis,
    focal-center: (10%, 40%),
    focal-radius: 5%,
  )),
)
```

![Preview](/assets/docs/IfkE7bIcLhrH24l0nk0sIQAAAAAAAAAA.png)

gradient.radial(

[..](#definitions-radial-stops)[color](/docs/reference/visualize/color/)[array](/docs/reference/foundations/array/),[space:](#definitions-radial-space) any,[relative:](#definitions-radial-relative) [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/),[center:](#definitions-radial-center) [array](/docs/reference/foundations/array/),[radius:](#definitions-radial-radius) [ratio](/docs/reference/layout/ratio/),[focal-center:](#definitions-radial-focal-center) [auto](/docs/reference/foundations/auto/)[array](/docs/reference/foundations/array/),[focal-radius:](#definitions-radial-focal-radius) [ratio](/docs/reference/layout/ratio/),

) -> [gradient](/docs/reference/visualize/gradient/)

#### `stops` [color](/docs/reference/visualize/color/) or [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The color [stops](#stops) of the gradient.

#### `space` any

The color space in which to interpolate the gradient.

Defaults to a perceptually uniform color space called
[Oklab](/docs/reference/visualize/color/#definitions-oklab).

Default: `oklab`

#### `relative` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/)

The [relative placement](#relativeness) of the gradient.

For an element placed at the root/top level of the document, the parent
is the page itself. For other elements, the parent is the innermost block,
box, column, grid, or stack that contains the element.

| Variant | Details |
| --- | --- |
| `"self"` | Relative to itself (its own bounding box). |
| `"parent"` | Relative to its parent (the parent's bounding box). |

Default: `auto`

#### `center` [array](/docs/reference/foundations/array/)

The center of the end circle of the gradient.

A value of `(50%, 50%)` means that the end circle is
centered inside of its container.

Default: `(50%, 50%)`

#### `radius` [ratio](/docs/reference/layout/ratio/)

The radius of the end circle of the gradient.

By default, it is set to `50%`. The ending radius must be bigger
than the focal radius.

Default: `50%`

#### `focal-center` [auto](/docs/reference/foundations/auto/) or [array](/docs/reference/foundations/array/)

The center of the focal circle of the gradient.

The focal center must be inside of the end circle.

A value of `(50%, 50%)` means that the focal circle is
centered inside of its container.

By default it is set to the same as the center of the last circle.

Default: `auto`

#### `focal-radius` [ratio](/docs/reference/layout/ratio/)

The radius of the focal circle of the gradient.

The focal center must be inside of the end circle.

By default, it is set to `0%`. The focal radius must be smaller
than the ending radius`.

Default: `0%`

### `conic`

Creates a new conic gradient, in which colors change radially around a
center point.

You can control the center point of the gradient by using the `center`
argument. By default, the center point is the center of the shape.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#stack(
  dir: ltr,
  spacing: 1fr,
  circle(fill: gradient.conic(
    ..color.map.viridis,
  )),
  circle(fill: gradient.conic(
    ..color.map.viridis,
    center: (20%, 30%),
  )),
)
```

![Preview](/assets/docs/Mqmcewscuekk2Rsln7oKygAAAAAAAAAA.png)

gradient.conic(

[..](#definitions-conic-stops)[color](/docs/reference/visualize/color/)[array](/docs/reference/foundations/array/),[angle:](#definitions-conic-angle) [angle](/docs/reference/layout/angle/),[space:](#definitions-conic-space) any,[relative:](#definitions-conic-relative) [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/),[center:](#definitions-conic-center) [array](/docs/reference/foundations/array/),

) -> [gradient](/docs/reference/visualize/gradient/)

#### `stops` [color](/docs/reference/visualize/color/) or [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The color [stops](#stops) of the gradient.

#### `angle` [angle](/docs/reference/layout/angle/)

The angle of the gradient.

Default: `0deg`

#### `space` any

The color space in which to interpolate the gradient.

Defaults to a perceptually uniform color space called
[Oklab](/docs/reference/visualize/color/#definitions-oklab).

Default: `oklab`

#### `relative` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/)

The [relative placement](#relativeness) of the gradient.

For an element placed at the root/top level of the document, the parent
is the page itself. For other elements, the parent is the innermost block,
box, column, grid, or stack that contains the element.

| Variant | Details |
| --- | --- |
| `"self"` | Relative to itself (its own bounding box). |
| `"parent"` | Relative to its parent (the parent's bounding box). |

Default: `auto`

#### `center` [array](/docs/reference/foundations/array/)

The center of the circle of the gradient.

A value of `(50%, 50%)` means that the circle is centered inside
of its container.

Default: `(50%, 50%)`

### `sharp`

Creates a sharp version of this gradient.

Sharp gradients have discrete jumps between colors, instead of a
smooth transition. They are particularly useful for creating color
lists for a preset gradient.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set rect(width: 100%, height: 20pt)
#let grad = gradient.linear(..color.map.rainbow)
#rect(fill: grad)
#rect(fill: grad.sharp(5))
#rect(fill: grad.sharp(5, smoothness: 20%))
```

![Preview](/assets/docs/k1IrJvVHW9DTjXfwHdfh_QAAAAAAAAAA.png)

self.sharp(

[int](/docs/reference/foundations/int/),[smoothness:](#definitions-sharp-smoothness) [ratio](/docs/reference/layout/ratio/),

) -> [gradient](/docs/reference/visualize/gradient/)

#### `steps` [int](/docs/reference/foundations/int/) Required Positional Question mark Positional parameters are specified in order, without names.

The number of stops in the gradient.

#### `smoothness` [ratio](/docs/reference/layout/ratio/)

How much to smooth the gradient.

Default: `0%`

### `repeat`

Repeats this gradient a given number of times, optionally mirroring it
at every second repetition.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#circle(
  radius: 40pt,
  fill: gradient
    .radial(aqua, white)
    .repeat(4),
)
```

![Preview](/assets/docs/ydbGAMwgwvGMCJpfMs1wAAAAAAAAAAAA.png)

self.repeat(

[int](/docs/reference/foundations/int/),[mirror:](#definitions-repeat-mirror) [bool](/docs/reference/foundations/bool/),

) -> [gradient](/docs/reference/visualize/gradient/)

#### `repetitions` [int](/docs/reference/foundations/int/) Required Positional Question mark Positional parameters are specified in order, without names.

The number of times to repeat the gradient.

#### `mirror` [bool](/docs/reference/foundations/bool/)

Whether to mirror the gradient at every second repetition, i.e.,
the first instance (and all odd ones) stays unchanged.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#circle(
  radius: 40pt,
  fill: gradient
    .conic(green, black)
    .repeat(2, mirror: true)
)
```

![Preview](/assets/docs/Eutu8PgoFxJKvF2RZ_813AAAAAAAAAAA.png)

Default: `false`

### `kind`

Returns the kind of this gradient.

self.kind() -> [function](/docs/reference/foundations/function/)

### `stops`

Returns the stops of this gradient.

self.stops() -> [array](/docs/reference/foundations/array/)

### `space`

Returns the mixing space of this gradient.

self.space() -> any

### `relative`

Returns the relative placement of this gradient.

self.relative() -> [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/)

### `angle`

Returns the angle of this gradient.

Returns `none` if the gradient is neither linear nor conic.

self.angle() -> [none](/docs/reference/foundations/none/)[angle](/docs/reference/layout/angle/)

### `center`

Returns the center of this gradient.

Returns `none` if the gradient is neither radial nor conic.

self.center() -> [none](/docs/reference/foundations/none/)[array](/docs/reference/foundations/array/)

### `radius`

Returns the radius of this gradient.

Returns `none` if the gradient is not radial.

self.radius() -> [none](/docs/reference/foundations/none/)[ratio](/docs/reference/layout/ratio/)

### `focal-center`

Returns the focal-center of this gradient.

Returns `none` if the gradient is not radial.

self.focal-center() -> [none](/docs/reference/foundations/none/)[array](/docs/reference/foundations/array/)

### `focal-radius`

Returns the focal-radius of this gradient.

Returns `none` if the gradient is not radial.

self.focal-radius() -> [none](/docs/reference/foundations/none/)[ratio](/docs/reference/layout/ratio/)

### `sample`

Sample the gradient at a given position.

The position is either a position along the gradient (a [ratio](/docs/reference/layout/ratio/ "ratio") between
`0%` and `100%`) or an [angle](/docs/reference/layout/angle/ "angle"). Any value outside of this range will
be clamped.

self.sample(

[angle](/docs/reference/layout/angle/)[ratio](/docs/reference/layout/ratio/)

) -> [color](/docs/reference/visualize/color/)

#### `t` [angle](/docs/reference/layout/angle/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names.

The position at which to sample the gradient.

### `samples`

Samples the gradient at multiple positions at once and returns the
results as an array.

self.samples(

[..](#definitions-samples-ts)[angle](/docs/reference/layout/angle/)[ratio](/docs/reference/layout/ratio/)

) -> [array](/docs/reference/foundations/array/)

#### `ts` [angle](/docs/reference/layout/angle/) or [ratio](/docs/reference/layout/ratio/) Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The positions at which to sample the gradient.

[![←](/assets/icons/16-chevron-right.svg)

EllipsePrevious page](/docs/reference/visualize/ellipse/) [![→](/assets/icons/16-chevron-right.svg)

ImageNext page](/docs/reference/visualize/image/)