# Introspection

Source: https://typst.app/docs/reference/introspection/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Introspection](/docs/reference/introspection/)

# Introspection

Interactions between document parts.

This category is home to Typst's introspection capabilities: With the `counter`
function, you can access and manipulate page, section, figure, and equation
counters or create custom ones. Meanwhile, the `query` function lets you search
for elements in the document to construct things like a list of figures or
headers which show the current chapter title.

Most of the functions are *contextual.* It is recommended to read the chapter on
[context](/docs/reference/context/ "context") before continuing here.

## Definitions

- [`counter`](/docs/reference/introspection/counter/)  Counts through pages, elements, and more.
- [`here`](/docs/reference/introspection/here/)  Provides the current location in the document.
- [`locate`](/docs/reference/introspection/locate/)  Determines the location of an element in the document.
- [`location`](/docs/reference/introspection/location/)  Identifies an element in the document.
- [`metadata`](/docs/reference/introspection/metadata/)  Exposes a value to the query system without producing visible content.
- [`query`](/docs/reference/introspection/query/)  Finds elements in the document.
- [`state`](/docs/reference/introspection/state/)  Manages stateful parts of your document.

[![←](/assets/icons/16-chevron-right.svg)

TilingPrevious page](/docs/reference/visualize/tiling/) [![→](/assets/icons/16-chevron-right.svg)

CounterNext page](/docs/reference/introspection/counter/)