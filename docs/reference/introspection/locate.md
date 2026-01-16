# locateContextual  Question mark   
Contextual functions can only be used when the context is known

Source: https://typst.app/docs/reference/introspection/locate/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Introspection](/docs/reference/introspection/)
- ![](/assets/icons/16-chevron-right.svg)
- [Locate](/docs/reference/introspection/locate/)

# `locate`Contextual Question mark Contextual functions can only be used when the context is known

Determines the location of an element in the document.

Takes a selector that must match exactly one element and returns that
element's [`location`](/docs/reference/introspection/location/ "`location`"). This location can, in particular, be used to
retrieve the physical [`page`](/docs/reference/introspection/location/#definitions-page) number and
[`position`](/docs/reference/introspection/location/#definitions-position) (page, x, y) for that element.

## Examples

Locating a specific element:

```typst
#context [
  Introduction is at: \
  #locate(<intro>).position()
]

= Introduction <intro>
```

![Preview](/assets/docs/fizxN7L7L7E8uWpTd8_mMgAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

locate(

[label](/docs/reference/foundations/label/)[selector](/docs/reference/foundations/selector/)[location](/docs/reference/introspection/location/)[function](/docs/reference/foundations/function/)

) -> [location](/docs/reference/introspection/location/)

### `selector` [label](/docs/reference/foundations/label/) or [selector](/docs/reference/foundations/selector/) or [location](/docs/reference/introspection/location/) or [function](/docs/reference/foundations/function/) Required Positional Question mark Positional parameters are specified in order, without names.

A selector that should match exactly one element. This element will be
located.

Especially useful in combination with

- [`here`](/docs/reference/introspection/here/ "`here`") to locate the current context,
- a [`location`](/docs/reference/introspection/location/ "`location`") retrieved from some queried element via the
  [`location()`](/docs/reference/foundations/content/#definitions-location) method on content.

[![←](/assets/icons/16-chevron-right.svg)

HerePrevious page](/docs/reference/introspection/here/) [![→](/assets/icons/16-chevron-right.svg)

LocationNext page](/docs/reference/introspection/location/)