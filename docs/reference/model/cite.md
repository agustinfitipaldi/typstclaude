# citeElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/model/cite/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Model](/docs/reference/model/)
- ![](/assets/icons/16-chevron-right.svg)
- [Cite](/docs/reference/model/cite/)

# `cite`Element Question mark Element functions can be customized with `set` and `show` rules.

Cite a work from the bibliography.

Before you starting citing, you need to add a [bibliography](/docs/reference/model/bibliography/ "bibliography") somewhere in
your document.

## Example

```typst
This was already noted by
pirates long ago. @arrgh

Multiple sources say ...
@arrgh @netwok.

You can also call `cite`
explicitly. #cite(<arrgh>)

#bibliography("works.bib")
```

![Preview](/assets/docs/VelsLOKdUATbBc5AK51_FgAAAAAAAAAA.png)

If your source name contains certain characters such as slashes, which are
not recognized by the `<>` syntax, you can explicitly call `label` instead.

```typst
Computer Modern is an example of a modernist serif typeface.
#cite(label("DBLP:books/lib/Knuth86a")).
```

## Syntax

This function indirectly has dedicated syntax. [References](/docs/reference/model/ref/) can be
used to cite works from the bibliography. The label then corresponds to the
citation key.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

cite(

[label](/docs/reference/foundations/label/),[supplement:](#parameters-supplement) [none](/docs/reference/foundations/none/)[content](/docs/reference/foundations/content/),[form:](#parameters-form) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/),[style:](#parameters-style) [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/)[bytes](/docs/reference/foundations/bytes/),

) -> [content](/docs/reference/foundations/content/)

### `key` [label](/docs/reference/foundations/label/) Required Positional Question mark Positional parameters are specified in order, without names.

The citation key that identifies the entry in the bibliography that
shall be cited, as a label.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
// All the same
@netwok \
#cite(<netwok>) \
#cite(label("netwok"))
```

![Preview](/assets/docs/fyv1W7ZKnlPyBVM6_1DvjgAAAAAAAAAA.png)

### `supplement` [none](/docs/reference/foundations/none/) or [content](/docs/reference/foundations/content/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

A supplement for the citation such as page or chapter number.

In reference syntax, the supplement can be added in square brackets:

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
This has been proven. @distress[p.~7]

#bibliography("works.bib")
```

![Preview](/assets/docs/yJ9a0jIezaQUawq1k-YqqwAAAAAAAAAA.png)

Default: `none`

### `form` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The kind of citation to produce. Different forms are useful in different
scenarios: A normal citation is useful as a source at the end of a
sentence, while a "prose" citation is more suitable for inclusion in the
flow of text.

If set to `none`, the cited work is included in the bibliography, but
nothing will be displayed.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#cite(<netwok>, form: "prose")
show the outsized effects of
pirate life on the human psyche.
```

![Preview](/assets/docs/xCamzQ_SHz1kKaOAByx_rAAAAAAAAAAA.png)

| Variant | Details |
| --- | --- |
| `"normal"` | Display in the standard way for the active style. |
| `"prose"` | Produces a citation that is suitable for inclusion in a sentence. |
| `"full"` | Mimics a bibliography entry, with full information about the cited work. |
| `"author"` | Shows only the cited work's author(s). |
| `"year"` | Shows only the cited work's year. |

Default: `"normal"`

### `style` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/) or [bytes](/docs/reference/foundations/bytes/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The citation style.

This can be:

- `auto` to automatically use the
  [bibliography's style](/docs/reference/model/bibliography/#parameters-style) for citations.
- A string with the name of one of the built-in styles (see below). Some
  of the styles listed below appear twice, once with their full name and
  once with a short alias.
- A path string to a [CSL file](https://citationstyles.org/). For more
  details about paths, see the [Paths section](/docs/reference/syntax/#paths).
- Raw bytes from which a CSL style should be decoded.

  ![](/assets/icons/16-chevron-right.svg) View options 

| Variant | Details |
| --- | --- |
| `"alphanumeric"` | Alphanumeric |
| `"american-anthropological-association"` | American Anthropological Association |
| `"american-chemical-society"` | American Chemical Society |
| `"american-geophysical-union"` | American Geophysical Union |
| `"american-institute-of-aeronautics-and-astronautics"` | American Institute of Aeronautics and Astronautics |
| `"american-institute-of-physics"` | American Institute of Physics 4th edition |
| `"american-medical-association"` | American Medical Association 11th edition |
| `"american-meteorological-society"` | American Meteorological Society |
| `"american-physics-society"` | American Physical Society |
| `"american-physiological-society"` | American Physiological Society |
| `"american-political-science-association"` | American Political Science Association |
| `"american-psychological-association"` | American Psychological Association 7th edition |
| `"apa"` | A short alias of `american-psychological-association` |
| `"american-society-for-microbiology"` | American Society for Microbiology |
| `"american-society-of-civil-engineers"` | American Society of Civil Engineers |
| `"american-society-of-mechanical-engineers"` | American Society of Mechanical Engineers |
| `"american-sociological-association"` | American Sociological Association 6th/7th edition |
| `"angewandte-chemie"` | Angewandte Chemie International Edition |
| `"annual-reviews"` | Annual Reviews (sorted by order of appearance) |
| `"annual-reviews-author-date"` | Annual Reviews (author-date) |
| `"associacao-brasileira-de-normas-tecnicas"` | Associação Brasileira de Normas Técnicas (Português - Brasil) |
| `"association-for-computing-machinery"` | Association for Computing Machinery |
| `"biomed-central"` | BioMed Central |
| `"bristol-university-press"` | Bristol University Press |
| `"british-medical-journal"` | BMJ |
| `"bmj"` | A short alias of `british-medical-journal` |
| `"cell"` | Cell |
| `"chicago-author-date"` | Chicago Manual of Style 18th edition (author-date) |
| `"chicago-notes"` | Chicago Manual of Style 18th edition (notes and bibliography) |
| `"chicago-fullnotes"` | A short alias of `chicago-notes` |
| `"chicago-shortened-notes"` | Chicago Manual of Style 18th edition (shortened notes and bibliography) |
| `"copernicus"` | Copernicus Publications |
| `"council-of-science-editors"` | Council of Science Editors, Citation-Sequence (numeric, brackets) |
| `"council-of-science-editors-author-date"` | Council of Science Editors, Name-Year 9th edition (author-date) |
| `"current-opinion"` | Current Opinion journals |
| `"deutsche-gesellschaft-für-psychologie"` | Deutsche Gesellschaft für Psychologie 5. Auflage (Deutsch) |
| `"deutsche-sprache"` | Deutsche Sprache (Deutsch) |
| `"elsevier-harvard"` | Elsevier - Harvard (with titles) |
| `"elsevier-vancouver"` | Elsevier - Vancouver |
| `"elsevier-with-titles"` | Elsevier (numeric, with titles) |
| `"frontiers"` | Frontiers journals |
| `"future-medicine"` | Future Medicine journals |
| `"future-science"` | Future Science Group |
| `"gb-7714-2005-numeric"` | China National Standard GB/T 7714-2005 (numeric, 中文) |
| `"gb-7714-2015-author-date"` | China National Standard GB/T 7714-2015 (author-date, 中文) |
| `"gb-7714-2015-note"` | China National Standard GB/T 7714-2015 (note, 中文) |
| `"gb-7714-2015-numeric"` | China National Standard GB/T 7714-2015 (numeric, 中文) |
| `"gost-r-705-2008-numeric"` | Russian GOST R 7.0.5-2008 (numeric) |
| `"harvard-cite-them-right"` | Cite Them Right 12th edition - Harvard |
| `"institute-of-electrical-and-electronics-engineers"` | IEEE |
| `"ieee"` | A short alias of `institute-of-electrical-and-electronics-engineers` |
| `"institute-of-physics-numeric"` | Institute of Physics (numeric) |
| `"iso-690-author-date"` | ISO-690 (author-date, English) |
| `"iso-690-numeric"` | ISO-690 (numeric, English) |
| `"karger"` | Karger journals |
| `"mary-ann-liebert-vancouver"` | Mary Ann Liebert - Vancouver |
| `"modern-humanities-research-association-notes"` | Modern Humanities Research Association 4th edition (notes) |
| `"modern-humanities-research-association"` | A short alias of `modern-humanities-research-association-notes` |
| `"modern-language-association"` | Modern Language Association 9th edition (in-text citations) |
| `"mla"` | A short alias of `modern-language-association` |
| `"modern-language-association-8"` | Modern Language Association 8th edition |
| `"mla-8"` | A short alias of `modern-language-association-8` |
| `"multidisciplinary-digital-publishing-institute"` | Multidisciplinary Digital Publishing Institute |
| `"nature"` | Nature |
| `"pensoft"` | Pensoft Journals |
| `"public-library-of-science"` | Public Library of Science |
| `"plos"` | A short alias of `public-library-of-science` |
| `"royal-society-of-chemistry"` | Royal Society of Chemistry |
| `"sage-vancouver"` | SAGE - Vancouver |
| `"sist02"` | SIST02 (日本語) |
| `"spie"` | SPIE journals |
| `"springer-basic"` | Springer - Basic (numeric, brackets) |
| `"springer-basic-author-date"` | Springer - Basic (author-date) |
| `"springer-fachzeitschriften-medizin-psychologie"` | Springer - Fachzeitschriften Medizin Psychologie (Deutsch) |
| `"springer-humanities-author-date"` | Springer - Humanities (author-date) |
| `"springer-lecture-notes-in-computer-science"` | Springer - Lecture Notes in Computer Science |
| `"springer-mathphys"` | Springer - MathPhys (numeric, brackets) |
| `"springer-socpsych-author-date"` | Springer - SocPsych (author-date) |
| `"springer-vancouver"` | Springer - Vancouver (brackets) |
| `"taylor-and-francis-chicago-author-date"` | Taylor & Francis Journals Standard Reference Style Guide: Chicago author-date version 2.0 |
| `"taylor-and-francis-national-library-of-medicine"` | Taylor & Francis - National Library of Medicine |
| `"the-institution-of-engineering-and-technology"` | The Institution of Engineering and Technology |
| `"the-lancet"` | The Lancet |
| `"thieme"` | Thieme-German (Deutsch) |
| `"trends"` | Trends journals |
| `"turabian-author-date"` | Chicago Manual of Style 17th edition (author-date) |
| `"turabian-fullnote-8"` | Chicago Manual of Style 17th edition (notes and bibliography, subsequent author-title) |
| `"vancouver"` | Vancouver |
| `"vancouver-superscript"` | Vancouver (superscript) |

Default: `auto`

[![←](/assets/icons/16-chevron-right.svg)

Bullet ListPrevious page](/docs/reference/model/list/) [![→](/assets/icons/16-chevron-right.svg)

DocumentNext page](/docs/reference/model/document/)