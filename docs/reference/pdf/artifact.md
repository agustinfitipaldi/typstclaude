# artifactElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/pdf/artifact/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [PDF](/docs/reference/pdf/)
- ![](/assets/icons/16-chevron-right.svg)
- [Artifact](/docs/reference/pdf/artifact/)

# `artifact`Element Question mark Element functions can be customized with `set` and `show` rules.

Marks content as a PDF artifact.

Artifacts are parts of the document that are not meant to be read by
Assistive Technology (AT), such as screen readers. Typical examples include
purely decorative images that do not contribute to the meaning of the
document, watermarks, or repeated content such as page numbers.

Typst will automatically mark certain content, such as page headers,
footers, backgrounds, and foregrounds, as artifacts. Likewise, paths and
shapes are automatically marked as artifacts, but their content is not.
Repetitions of table headers and footers are also marked as artifacts.

Once something is marked as an artifact, you cannot make any of its
contents accessible again. If you need to mark only part of something as an
artifact, you may need to use this function multiple times.

If you are unsure what constitutes an artifact, check the [Accessibility
Guide](/docs/guides/accessibility/#artifacts).

In the future, this function may be moved out of the `pdf` module, making it
possible to hide content in HTML export from AT.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

pdf.artifact(

[kind:](#parameters-kind) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `kind` [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The artifact kind.

This will govern how the PDF reader treats the artifact during reflow
and content extraction (e.g. copy and paste).

| Variant | Details |
| --- | --- |
| `"header"` | Repeats on the top of each page. |
| `"footer"` | Repeats at the bottom of each page. |
| `"page"` | Not part of the document, but rather the page it is printed on. An example would be cut marks or color bars. |
| `"other"` | Other artifacts, including purely cosmetic content, backgrounds, watermarks, and repeated content. |

Default: `"other"`

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content that is an artifact.

[![←](/assets/icons/16-chevron-right.svg)

PDFPrevious page](/docs/reference/pdf/) [![→](/assets/icons/16-chevron-right.svg)

AttachNext page](/docs/reference/pdf/attach/)