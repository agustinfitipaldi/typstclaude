# measureContextual  Question mark   
Contextual functions can only be used when the context is known

Source: https://typst.app/docs/reference/layout/measure/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Measure](/docs/reference/layout/measure/)

# `measure`Contextual Question mark Contextual functions can only be used when the context is known

Measures the layouted size of content.

The `measure` function lets you determine the layouted size of content.
By default an infinite space is assumed, so the measured dimensions may
not necessarily match the final dimensions of the content.
If you want to measure in the current layout dimensions, you can combine
`measure` and [`layout`](/docs/reference/layout/layout/ "`layout`").

## Example

The same content can have a different size depending on the [context](/docs/reference/context/ "context") that
it is placed into. In the example below, the `#content` is of course
bigger when we increase the font size.

```typst
#let content = [Hello!]
#content
#set text(14pt)
#content
```

![Preview](/assets/docs/AhP31noWwrcSQXbwnmO-hwAAAAAAAAAA.png)

For this reason, you can only measure when context is available.

```typst
#let thing(body) = context {
  let size = measure(body)
  [Width of "#body" is #size.width]
}

#thing[Hey] \
#thing[Welcome]
```

![Preview](/assets/docs/-y6AuN3J3rl7Gz1x_VRjjwAAAAAAAAAA.png)

The measure function returns a dictionary with the entries `width` and
`height`, both of type [`length`](/docs/reference/layout/length/ "`length`").

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

measure(

[width:](#parameters-width) [auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/),[height:](#parameters-height) [auto](/docs/reference/foundations/auto/)[length](/docs/reference/layout/length/),[content](/docs/reference/foundations/content/),

) -> [dictionary](/docs/reference/foundations/dictionary/)

### `width` [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/)

The width available to layout the content.

Setting this to `auto` indicates infinite available width.

Note that using the `width` and `height` parameters of this function is
different from measuring a sized [`block`](/docs/reference/layout/block/ "`block`") containing the content. In
the following example, the former will get the dimensions of the inner
content instead of the dimensions of the block.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#context measure(lorem(100), width: 400pt)

#context measure(block(lorem(100), width: 400pt))
```

![Preview](/assets/docs/kGPOcZfxzWEfqWzKQCJaFgAAAAAAAAAA.png)

Default: `auto`

### `height` [auto](/docs/reference/foundations/auto/) or [length](/docs/reference/layout/length/)

The height available to layout the content.

Setting this to `auto` indicates infinite available height.

Default: `auto`

### `content` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content whose size to measure.

[![←](/assets/icons/16-chevron-right.svg)

LengthPrevious page](/docs/reference/layout/length/) [![→](/assets/icons/16-chevron-right.svg)

MoveNext page](/docs/reference/layout/move/)