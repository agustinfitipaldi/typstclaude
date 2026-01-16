# attachElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/pdf/attach/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [PDF](/docs/reference/pdf/)
- ![](/assets/icons/16-chevron-right.svg)
- [Attach](/docs/reference/pdf/attach/)

# `attach`Element Question mark Element functions can be customized with `set` and `show` rules.

A file that will be attached to the output PDF.

This can be used to distribute additional files associated with the PDF
within it. PDF readers will display the files in a file listing.

Some international standards use this mechanism to attach machine-readable
data (e.g., ZUGFeRD/Factur-X for invoices) that mirrors the visual content
of the PDF.

## Example

```typst
#pdf.attach(
  "experiment.csv",
  relationship: "supplement",
  mime-type: "text/csv",
  description: "Raw Oxygen readings from the Arctic experiment",
)
```

## Notes

- This element is ignored if exporting to a format other than PDF.
- File attachments are not currently supported for PDF/A-2, even if the
  attached file conforms to PDF/A-1 or PDF/A-2.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

pdf.attach(

[str](/docs/reference/foundations/str/),[bytes](/docs/reference/foundations/bytes/),[relationship:](#parameters-relationship) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/),[mime-type:](#parameters-mime-type) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/),[description:](#parameters-description) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/),

) -> [content](/docs/reference/foundations/content/)

### `path` [str](/docs/reference/foundations/str/) Required Positional Question mark Positional parameters are specified in order, without names.

The [path](/docs/reference/syntax/#paths) of the file to be attached.

Must always be specified, but is only read from if no data is provided
in the following argument.

### `data` [bytes](/docs/reference/foundations/bytes/) Required Positional Question mark Positional parameters are specified in order, without names.

Raw file data, optionally.

If omitted, the data is read from the specified path.

### `relationship` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The relationship of the attached file to the document.

Ignored if export doesn't target PDF/A-3.

| Variant | Details |
| --- | --- |
| `"source"` | The PDF document was created from the source file. |
| `"data"` | The file was used to derive a visual presentation in the PDF. |
| `"alternative"` | An alternative representation of the document. |
| `"supplement"` | Additional resources for the document. |

Default: `none`

### `mime-type` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The MIME type of the attached file.

Default: `none`

### `description` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

A description for the attached file.

Default: `none`

[![←](/assets/icons/16-chevron-right.svg)

ArtifactPrevious page](/docs/reference/pdf/artifact/) [![→](/assets/icons/16-chevron-right.svg)

Data CellNext page](/docs/reference/pdf/data-cell/)