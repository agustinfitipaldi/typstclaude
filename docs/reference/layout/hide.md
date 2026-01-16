# hideElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/layout/hide/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Hide](/docs/reference/layout/hide/)

# `hide`Element Question mark Element functions can be customized with `set` and `show` rules.

Hides content without affecting layout.

The `hide` function allows you to hide content while the layout still "sees"
it. This is useful for creating blank space that is exactly as large as some
content.

## Example

```typst
Hello Jane \
#hide[Hello] Joe
```

![Preview](/assets/docs/w0ioP6Ne87hOMXgpgPJirgAAAAAAAAAA.png)

## Redaction

This function may also be useful for redacting content as its arguments are
neither present visually nor accessible to Assistive Technology. That said,
there can be *some* traces of the hidden content (such as a bookmarked
heading in the PDF's Document Outline).

Note that, depending on the circumstances, it may be possible for content to
be reverse engineered based on its size in the layout. We thus do not
recommend using this function to hide highly sensitive information.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

hide(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to hide.

[![←](/assets/icons/16-chevron-right.svg)

GridPrevious page](/docs/reference/layout/grid/) [![→](/assets/icons/16-chevron-right.svg)

LayoutNext page](/docs/reference/layout/layout/)