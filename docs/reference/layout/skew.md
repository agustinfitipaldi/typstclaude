# skewElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/layout/skew/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Skew](/docs/reference/layout/skew/)

# `skew`Element Question mark Element functions can be customized with `set` and `show` rules.

Skews content.

Skews an element in horizontal and/or vertical direction. The layout will
act as if the element was not skewed unless you specify `reflow: true`.

## Example

```typst
#skew(ax: -12deg)[
  This is some fake italic text.
]
```

![Preview](/assets/docs/FUtSyVs-Ma5rvUP8B0w5fQAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

skew(

[ax:](#parameters-ax) [angle](/docs/reference/layout/angle/),[ay:](#parameters-ay) [angle](/docs/reference/layout/angle/),[origin:](#parameters-origin) [alignment](/docs/reference/layout/alignment/),[reflow:](#parameters-reflow) [bool](/docs/reference/foundations/bool/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `ax` [angle](/docs/reference/layout/angle/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The horizontal skewing angle.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#skew(ax: 30deg)[Skewed]
```

![Preview](/assets/docs/H9k2hlR_HYwp5MND40z3rgAAAAAAAAAA.png)

Default: `0deg`

### `ay` [angle](/docs/reference/layout/angle/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The vertical skewing angle.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#skew(ay: 30deg)[Skewed]
```

![Preview](/assets/docs/DIs5kgGdkepXxpgHWt0vxAAAAAAAAAAA.png)

Default: `0deg`

### `origin` [alignment](/docs/reference/layout/alignment/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The origin of the skew transformation.

The origin will stay fixed during the operation.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
X #box(skew(ax: -30deg, origin: center + horizon)[X]) X \
X #box(skew(ax: -30deg, origin: bottom + left)[X]) X \
X #box(skew(ax: -30deg, origin: top + right)[X]) X
```

![Preview](/assets/docs/2Hq4GFYS1tSqCnluz3jbcQAAAAAAAAAA.png)

Default: `center + horizon`

### `reflow` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether the skew transformation impacts the layout.

If set to `false`, the skewed content will retain the bounding box of
the original content. If set to `true`, the bounding box will take the
transformation of the content into account and adjust the layout accordingly.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
Hello #skew(ay: 30deg, reflow: true, "World")!
```

![Preview](/assets/docs/-k-PUuRezD-q6j7vk-xQWAAAAAAAAAAA.png)

Default: `false`

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to skew.

[![←](/assets/icons/16-chevron-right.svg)

ScalePrevious page](/docs/reference/layout/scale/) [![→](/assets/icons/16-chevron-right.svg)

Spacing (H)Next page](/docs/reference/layout/h/)