# refElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/model/ref/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Model](/docs/reference/model/)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/model/ref/)

# `ref`Element Question mark Element functions can be customized with `set` and `show` rules.

A reference to a label or bibliography.

Takes a label and cross-references it. There are two kind of references,
determined by its [`form`](/docs/reference/model/ref/#parameters-form): `"normal"` and `"page"`.

The default, a `"normal"` reference, produces a textual reference to a
label. For example, a reference to a heading will yield an appropriate
string such as "Section 1" for a reference to the first heading. The word
"Section" depends on the [`lang`](/docs/reference/text/text/#parameters-lang) setting and is localized
accordingly. The references are also links to the respective element.
Reference syntax can also be used to [cite](/docs/reference/model/cite/ "cite") from a bibliography.

As the default form requires a supplement and numbering, the label must be
attached to a *referenceable element*. Referenceable elements include
[headings](/docs/reference/model/heading/), [figures](/docs/reference/model/figure/), [equations](/docs/reference/math/equation/), and
[footnotes](/docs/reference/model/footnote/). To create a custom referenceable element like a
theorem, you can create a figure of a custom [`kind`](/docs/reference/model/figure/#parameters-kind) and
write a show rule for it. In the future, there might be a more direct way
to define a custom referenceable element.

If you just want to link to a labelled element and not get an automatic
textual reference, consider using the [`link`](/docs/reference/model/link/ "`link`") function instead.

A `"page"` reference produces a page reference to a label, displaying the
page number at its location. You can use the
[page's supplement](/docs/reference/layout/page/#parameters-supplement) to modify the text before the page
number. Unlike a `"normal"` reference, the label can be attached to any
element.

## Example

```typst
#set page(numbering: "1")
#set heading(numbering: "1.")
#set math.equation(numbering: "(1)")

= Introduction <intro>
Recent developments in
typesetting software have
rekindled hope in previously
frustrated researchers. @distress
As shown in @results (see
#ref(<results>, form: "page")),
we ...

= Results <results>
We discuss our approach in
comparison with others.

== Performance <perf>
@slow demonstrates what slow
software looks like.
$ T(n) = O(2^n) $ <slow>

#bibliography("works.bib")
```

![Preview](/assets/docs/p5J0XM7JRakHYxONTkV2LwAAAAAAAAAA.png)

## Syntax

This function also has dedicated syntax: A `"normal"` reference to a
label can be created by typing an `@` followed by the name of the label
(e.g. `= Introduction <intro>` can be referenced by typing `@intro`).

To customize the supplement, add content in square brackets after the
reference: `@intro[Chapter]`.

## Customization

When you only ever need to reference pages of a figure/table/heading/etc. in
a document, the default `form` field value can be changed to `"page"` with
a set rule. If you prefer a short "p." supplement over "page", the
[`page.supplement`](/docs/reference/layout/page/#parameters-supplement "`page.supplement`") field can be used for changing this:

```typst
#set page(
  numbering: "1",
  supplement: "p.",
)
#set ref(form: "page")

#figure(
  stack(
    dir: ltr,
    spacing: 1em,
    circle(),
    square(),
  ),
  caption: [Shapes],
) <shapes>

#pagebreak()

See @shapes for examples
of different shapes.
```

![Preview](/assets/docs/gJ5d2PrJIq0UrYQDXT3piQAAAAAAAAAA.png)
![Preview](/assets/docs/gJ5d2PrJIq0UrYQDXT3piQAAAAAAAAAB.png)

If you write a show rule for references, you can access the referenced
element through the `element` field of the reference. The `element` may
be `none` even if it exists if Typst hasn't discovered it yet, so you
always need to handle that case in your code.

```typst
#set heading(numbering: "1.")
#set math.equation(numbering: "(1)")

#show ref: it => {
  let eq = math.equation
  let el = it.element
  // Skip all other references.
  if el == none or el.func() != eq { return it }
  // Override equation references.
  link(el.location(), numbering(
    el.numbering,
    ..counter(eq).at(el.location())
  ))
}

= Beginnings <beginning>
In @beginning we prove @pythagoras.
$ a^2 + b^2 = c^2 $ <pythagoras>
```

![Preview](/assets/docs/RrkCbtiAxLAjFha9UP4x1gAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

ref(

[label](/docs/reference/foundations/label/),[supplement:](#parameters-supplement) [none](/docs/reference/foundations/none/)[auto](/docs/reference/foundations/auto/)[content](/docs/reference/foundations/content/)[function](/docs/reference/foundations/function/),[form:](#parameters-form) [str](/docs/reference/foundations/str/),

) -> [content](/docs/reference/foundations/content/)

### `target` [label](/docs/reference/foundations/label/) Required Positional Question mark Positional parameters are specified in order, without names.

The target label that should be referenced.

Can be a label that is defined in the document or, if the
[`form`](/docs/reference/model/ref/#parameters-form) is set to `"normal"`, an entry from the
[`bibliography`](/docs/reference/model/bibliography/ "`bibliography`").

### `supplement` [none](/docs/reference/foundations/none/) or [auto](/docs/reference/foundations/auto/) or [content](/docs/reference/foundations/content/) or [function](/docs/reference/foundations/function/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

A supplement for the reference.

If the [`form`](/docs/reference/model/ref/#parameters-form) is set to `"normal"`:

- For references to headings or figures, this is added before the
  referenced number.
- For citations, this can be used to add a page number.

If the [`form`](/docs/reference/model/ref/#parameters-form) is set to `"page"`, then this is added
before the page number of the label referenced.

If a function is specified, it is passed the referenced element and
should return content.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set heading(numbering: "1.")
#show ref.where(
  form: "normal"
): set ref(supplement: it => {
  if it.func() == heading {
    "Chapter"
  } else {
    "Thing"
  }
})

= Introduction <intro>
In @intro, we see how to turn
Sections into Chapters. And
in @intro[Part], it is done
manually.
```

![Preview](/assets/docs/qob2D2Yy9u96k7gKWpfH0QAAAAAAAAAA.png)

Default: `auto`

### `form` [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The kind of reference to produce.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set page(numbering: "1")

Here <here> we are on
#ref(<here>, form: "page").
```

![Preview](/assets/docs/fAuN6uCXc9u1D17Yl1nCQAAAAAAAAAAA.png)

| Variant | Details |
| --- | --- |
| `"normal"` | Produces a textual reference to a label. |
| `"page"` | Produces a page reference to a label. |

Default: `"normal"`

[![←](/assets/icons/16-chevron-right.svg)

QuotePrevious page](/docs/reference/model/quote/) [![→](/assets/icons/16-chevron-right.svg)

Strong EmphasisNext page](/docs/reference/model/strong/)