# pagebreakElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/layout/pagebreak/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Page Break](/docs/reference/layout/pagebreak/)

# `pagebreak`Element Question mark Element functions can be customized with `set` and `show` rules.

A manual page break.

Must not be used inside any containers.

## Example

```typst
The next page contains
more details on compound theory.
#pagebreak()

== Compound Theory
In 1984, the first ...
```

![Preview](/assets/docs/MJju6am_GVBgtJWStEY3AwAAAAAAAAAA.png)
![Preview](/assets/docs/MJju6am_GVBgtJWStEY3AwAAAAAAAAAB.png)

Even without manual page breaks, content will be automatically paginated
based on the configured page size. You can set [the page height](/docs/reference/layout/page/#parameters-height)
to `auto` to let the page grow dynamically until a manual page break
occurs.

Pagination tries to avoid single lines of text at the top or bottom of a
page (these are called *widows* and *orphans*). You can adjust the
[`text.costs`](/docs/reference/text/text/#parameters-costs "`text.costs`") parameter to disable this behavior.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

pagebreak(

[weak:](#parameters-weak) [bool](/docs/reference/foundations/bool/),[to:](#parameters-to) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/),

) -> [content](/docs/reference/foundations/content/)

### `weak` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

If `true`, the page break is skipped if the current page is already
empty.

Default: `false`

### `to` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

If given, ensures that the next page will be an even/odd page, with an
empty page in between if necessary.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set page(height: 30pt)

First.
#pagebreak(to: "odd")
Third.
```

![Preview](/assets/docs/_4CDe0eaU4eyZtVUd1ArigAAAAAAAAAA.png)
![Preview](/assets/docs/_4CDe0eaU4eyZtVUd1ArigAAAAAAAAAB.png)
![Preview](/assets/docs/_4CDe0eaU4eyZtVUd1ArigAAAAAAAAAC.png)

| Variant | Details |
| --- | --- |
| `"even"` | Next page will be an even page. |
| `"odd"` | Next page will be an odd page. |

Default: `none`

[![←](/assets/icons/16-chevron-right.svg)

PagePrevious page](/docs/reference/layout/page/) [![→](/assets/icons/16-chevron-right.svg)

PlaceNext page](/docs/reference/layout/place/)