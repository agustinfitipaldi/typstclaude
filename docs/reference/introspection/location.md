# location

Source: https://typst.app/docs/reference/introspection/location/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Introspection](/docs/reference/introspection/)
- ![](/assets/icons/16-chevron-right.svg)
- [Location](/docs/reference/introspection/location/)

# location

Identifies an element in the document.

A location uniquely identifies an element in the document and lets you
access its absolute position on the pages. You can retrieve the current
location with the [`here`](/docs/reference/introspection/here/ "`here`") function and the location of a queried or shown
element with the [`location()`](/docs/reference/foundations/content/#definitions-location) method on content.

## Locatable elements

Elements that are automatically assigned a location are called *locatable.*
For efficiency reasons, not all elements are locatable.

- In the [Model category](/docs/reference/model/), most elements are locatable.
  This is because semantic elements like [headings](/docs/reference/model/heading/) and
  [figures](/docs/reference/model/figure/) are often used with introspection.
- In the [Text category](/docs/reference/text/), the [`raw`](/docs/reference/text/raw/ "`raw`") element, and the
  decoration elements [`underline`](/docs/reference/text/underline/ "`underline`"), [`overline`](/docs/reference/text/overline/ "`overline`"), [`strike`](/docs/reference/text/strike/ "`strike`"), and
  [`highlight`](/docs/reference/text/highlight/ "`highlight`") are locatable as these are also quite semantic in nature.
- In the [Introspection category](/docs/reference/introspection/), the [`metadata`](/docs/reference/introspection/metadata/ "`metadata`")
  element is locatable as being queried for is its primary purpose.
- In the other categories, most elements are not locatable. Exceptions are
  [`math.equation`](/docs/reference/math/equation/ "`math.equation`") and [`image`](/docs/reference/visualize/image/ "`image`").

To find out whether a specific element is locatable, you can try to
[`query`](/docs/reference/introspection/query/ "`query`") for it.

Note that you can still observe elements that are not locatable in queries
through other means, for instance, when they have a label attached to them.

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `page`

Returns the page number for this location.

Note that this does not return the value of the [page counter](/docs/reference/introspection/counter/)
at this location, but the true page number (starting from one).

If you want to know the value of the page counter, use
`counter(page).at(loc)` instead.

Can be used with [`here`](/docs/reference/introspection/here/ "`here`") to retrieve the physical page position
of the current context:

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#context [
  I am located on
  page #here().page()
]
```

![Preview](/assets/docs/0ToVSLLUesTLkEw_YsnJkwAAAAAAAAAA.png)

self.page() -> [int](/docs/reference/foundations/int/)

### `position`

Returns a dictionary with the page number and the x, y position for this
location. The page number starts at one and the coordinates are measured
from the top-left of the page.

If you only need the page number, use `page()` instead as it allows
Typst to skip unnecessary work.

self.position() -> [dictionary](/docs/reference/foundations/dictionary/)

### `page-numbering`

Returns the page numbering pattern of the page at this location. This
can be used when displaying the page counter in order to obtain the
local numbering. This is useful if you are building custom indices or
outlines.

If the page numbering is set to `none` at that location, this function
returns `none`.

self.page-numbering() -> [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/)[function](/docs/reference/foundations/function/)

[![←](/assets/icons/16-chevron-right.svg)

LocatePrevious page](/docs/reference/introspection/locate/) [![→](/assets/icons/16-chevron-right.svg)

MetadataNext page](/docs/reference/introspection/metadata/)