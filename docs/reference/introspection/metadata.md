# metadataElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/introspection/metadata/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Introspection](/docs/reference/introspection/)
- ![](/assets/icons/16-chevron-right.svg)
- [Metadata](/docs/reference/introspection/metadata/)

# `metadata`Element Question mark Element functions can be customized with `set` and `show` rules.

Exposes a value to the query system without producing visible content.

This element can be retrieved with the [`query`](/docs/reference/introspection/query/ "`query`") function and from the
command line with
[`typst query`](/docs/reference/introspection/query/#command-line-queries). Its
purpose is to expose an arbitrary value to the introspection system. To
identify a metadata value among others, you can attach a [`label`](/docs/reference/foundations/label/ "`label`") to it and
query for that label.

The `metadata` element is especially useful for command line queries because
it allows you to expose arbitrary values to the outside world.

```typst
// Put metadata somewhere.
#metadata("This is a note") <note>

// And find it from anywhere else.
#context {
  query(<note>).first().value
}
```

![Preview](/assets/docs/sbF_Ac863-gI1m3qoL9avwAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

metadata(

any

) -> [content](/docs/reference/foundations/content/)

### `value` any Required Positional Question mark Positional parameters are specified in order, without names.

The value to embed into the document.

[![←](/assets/icons/16-chevron-right.svg)

LocationPrevious page](/docs/reference/introspection/location/) [![→](/assets/icons/16-chevron-right.svg)

QueryNext page](/docs/reference/introspection/query/)