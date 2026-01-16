# layout

Source: https://typst.app/docs/reference/layout/layout/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/layout/)

# `layout`

Provides access to the current outer container's (or page's, if none)
dimensions (width and height).

Accepts a function that receives a single parameter, which is a dictionary
with keys `width` and `height`, both of type [`length`](/docs/reference/layout/length/ "`length`"). The function is
provided [context](/docs/reference/context/ "context"), meaning you don't need to use it in combination with the
`context` keyword. This is why [`measure`](/docs/reference/layout/measure/ "`measure`") can be called in the example
below.

```typst
#let text = lorem(30)
#layout(size => [
  #let (height,) = measure(
    width: size.width,
    text,
  )
  This text is #height high with
  the current page width: \
  #text
])
```

![Preview](/assets/docs/zHvMpi5pf_sw3zQ4Vw2xqwAAAAAAAAAA.png)

Note that the `layout` function forces its contents into a [block](/docs/reference/layout/block/ "block")-level
container, so placement relative to the page or pagebreaks are not possible
within it.

If the `layout` call is placed inside a box with a width of `800pt` and a
height of `400pt`, then the specified function will be given the argument
`(width: 800pt, height: 400pt)`. If it is placed directly into the page, it
receives the page's dimensions minus its margins. This is mostly useful in
combination with [measurement](/docs/reference/layout/measure/).

To retrieve the *remaining* height of the page rather than its full size,
you can wrap your `layout` call in a `block(height: 1fr)`. This works
because the block automatically grows to fill the remaining space (see the
[fraction](/docs/reference/layout/fraction/ "fraction") documentation for more details).

```typst
#set page(height: 150pt)

#lorem(20)

#block(height: 1fr, layout(size => [
  Remaining height: #size.height
]))
```

![Preview](/assets/docs/KHhhuOMSnLMBt0r6kv96BwAAAAAAAAAA.png)

You can also use this function to resolve a [`ratio`](/docs/reference/layout/ratio/ "`ratio`") to a fixed length.
This might come in handy if you're building your own layout abstractions.

```typst
#layout(size => {
  let half = 50% * size.width
  [Half a page is #half wide.]
})
```

![Preview](/assets/docs/1AoOPrEARH2i9ZcdcamicAAAAAAAAAAA.png)

Note that the width or height provided by `layout` will be infinite if the
corresponding page dimension is set to `auto`.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

layout(

[function](/docs/reference/foundations/function/)

) -> [content](/docs/reference/foundations/content/)

### `func` [function](/docs/reference/foundations/function/) Required Positional Question mark Positional parameters are specified in order, without names.

A function to call with the outer container's size. Its return value is
displayed in the document.

The container's size is given as a [dictionary](/docs/reference/foundations/dictionary/ "dictionary") with the keys `width`
and `height`, both of type [`length`](/docs/reference/layout/length/ "`length`").

This function is called once for each time the content returned by
`layout` appears in the document. This makes it possible to generate
content that depends on the dimensions of its container.

[![←](/assets/icons/16-chevron-right.svg)

HidePrevious page](/docs/reference/layout/hide/) [![→](/assets/icons/16-chevron-right.svg)

LengthNext page](/docs/reference/layout/length/)