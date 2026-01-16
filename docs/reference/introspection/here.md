# hereContextual  Question mark   
Contextual functions can only be used when the context is known

Source: https://typst.app/docs/reference/introspection/here/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Introspection](/docs/reference/introspection/)
- ![](/assets/icons/16-chevron-right.svg)
- [Here](/docs/reference/introspection/here/)

# `here`Contextual Question mark Contextual functions can only be used when the context is known

Provides the current location in the document.

You can think of `here` as a low-level building block that directly extracts
the current location from the active [context](/docs/reference/context/ "context"). Some other functions use it
internally: For instance, `counter.get()` is equivalent to
`counter.at(here())`.

Within show rules on [locatable](/docs/reference/introspection/location/#locatable) elements, `here()`
will match the location of the shown element.

If you want to display the current page number, refer to the documentation
of the [`counter`](/docs/reference/introspection/counter/ "`counter`") type. While `here` can be used to determine the physical
page number, typically you want the logical page number that may, for
instance, have been reset after a preface.

## Examples

Determining the current position in the document in combination with the
[`position`](/docs/reference/introspection/location/#definitions-position) method:

```typst
#context [
  I am located at
  #here().position()
]
```

![Preview](/assets/docs/5PrDc8FIHOrLs_qUjTj6iwAAAAAAAAAA.png)

Running a [query](/docs/reference/introspection/query/ "query") for elements before the current position:

```typst
= Introduction
= Background

There are
#context query(
  selector(heading).before(here())
).len()
headings before me.

= Conclusion
```

![Preview](/assets/docs/5DWH6TcZBrEjuGuSwKqf8AAAAAAAAAAA.png)

Refer to the [`selector`](/docs/reference/foundations/selector/ "`selector`") type for more details on before/after selectors.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

here() -> [location](/docs/reference/introspection/location/)

[![←](/assets/icons/16-chevron-right.svg)

CounterPrevious page](/docs/reference/introspection/counter/) [![→](/assets/icons/16-chevron-right.svg)

LocateNext page](/docs/reference/introspection/locate/)