# Typed HTML

Source: https://typst.app/docs/reference/html/typed/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [HTML](/docs/reference/html/)
- ![](/assets/icons/16-chevron-right.svg)
- [Typed HTML](/docs/reference/html/typed/)

# Typed HTML

A typed layer over raw HTML elements.

The `html` module provides a typed layer over the raw [`html.elem`](/docs/reference/html/elem/ "`html.elem`") function
that allows you to conveniently create HTML elements. HTML attributes are
exposed as function parameters that accept Typst types and automatically
take care of converting those into the appropriate HTML.

Some parameters are common to all typed HTML functions. These are listed at
the bottom in the [Global Attributes](#global-attributes) section instead of
explicitly on each element for readability.

## Example

```typst
#html.video(
  controls: true,
  width: 1280,
  height: 720,
  src: "sunrise.mp4",
)[
  Your browser does not support the video tag.
]
```

## Functions

### `a`

Hyperlink.

html.a(

[download:](#functions-a-download) [str](/docs/reference/foundations/str/),[href:](#functions-a-href) [str](/docs/reference/foundations/str/),[hreflang:](#functions-a-hreflang) [str](/docs/reference/foundations/str/),[ping:](#functions-a-ping) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[referrerpolicy:](#functions-a-referrerpolicy) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/),[rel:](#functions-a-rel) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[target:](#functions-a-target) [str](/docs/reference/foundations/str/),[type:](#functions-a-type) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `download` [str](/docs/reference/foundations/str/)

Whether to download the resource instead of navigating to it, and its filename if so.

#### `href` [str](/docs/reference/foundations/str/)

Address of the hyperlink.

#### `hreflang` [str](/docs/reference/foundations/str/)

Language of the linked resource.

#### `ping` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

URLs to ping.

#### `referrerpolicy` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/)

Referrer policy for fetches initiated by the element.

| Variant | Details |
| --- | --- |
| `"no-referrer"` |  |
| `"no-referrer-when-downgrade"` |  |
| `"same-origin"` |  |
| `"origin"` |  |
| `"strict-origin"` |  |
| `"origin-when-cross-origin"` |  |
| `"strict-origin-when-cross-origin"` |  |
| `"unsafe-url"` |  |

#### `rel` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Relationship between the location in the document containing the hyperlink and the destination resource.

  ![](/assets/icons/16-chevron-right.svg) View options 

| Variant | Details |
| --- | --- |
| `"alternate"` |  |
| `"canonical"` |  |
| `"author"` |  |
| `"bookmark"` |  |
| `"dns-prefetch"` |  |
| `"expect"` |  |
| `"external"` |  |
| `"help"` |  |
| `"icon"` |  |
| `"manifest"` |  |
| `"modulepreload"` |  |
| `"license"` |  |
| `"next"` |  |
| `"nofollow"` |  |
| `"noopener"` |  |
| `"noreferrer"` |  |
| `"opener"` |  |
| `"pingback"` |  |
| `"preconnect"` |  |
| `"prefetch"` |  |
| `"preload"` |  |
| `"prev"` |  |
| `"privacy-policy"` |  |
| `"search"` |  |
| `"stylesheet"` |  |
| `"tag"` |  |
| `"terms-of-service"` |  |

#### `target` [str](/docs/reference/foundations/str/)

Navigable for hyperlink navigation.

| Variant | Details |
| --- | --- |
| `"_blank"` |  |
| `"_self"` |  |
| `"_parent"` |  |
| `"_top"` |  |

#### `type` [str](/docs/reference/foundations/str/)

Hint for the type of the referenced resource.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `abbr`

Abbreviation.

html.abbr(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `address`

Contact information for a page or article element.

html.address(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `area`

Hyperlink or dead area on an image map.

html.area(

[alt:](#functions-area-alt) [str](/docs/reference/foundations/str/),[coords:](#functions-area-coords) [array](/docs/reference/foundations/array/),[download:](#functions-area-download) [str](/docs/reference/foundations/str/),[href:](#functions-area-href) [str](/docs/reference/foundations/str/),[ping:](#functions-area-ping) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[referrerpolicy:](#functions-area-referrerpolicy) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/),[rel:](#functions-area-rel) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[shape:](#functions-area-shape) [str](/docs/reference/foundations/str/),[target:](#functions-area-target) [str](/docs/reference/foundations/str/),

) -> [content](/docs/reference/foundations/content/)

#### `alt` [str](/docs/reference/foundations/str/)

Replacement text for use when images are not available.

#### `coords` [array](/docs/reference/foundations/array/)

Coordinates for the shape to be created in an image map. Expects an array of floating point numbers.

#### `download` [str](/docs/reference/foundations/str/)

Whether to download the resource instead of navigating to it, and its filename if so.

#### `href` [str](/docs/reference/foundations/str/)

Address of the hyperlink.

#### `ping` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

URLs to ping.

#### `referrerpolicy` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/)

Referrer policy for fetches initiated by the element.

| Variant | Details |
| --- | --- |
| `"no-referrer"` |  |
| `"no-referrer-when-downgrade"` |  |
| `"same-origin"` |  |
| `"origin"` |  |
| `"strict-origin"` |  |
| `"origin-when-cross-origin"` |  |
| `"strict-origin-when-cross-origin"` |  |
| `"unsafe-url"` |  |

#### `rel` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Relationship between the location in the document containing the hyperlink and the destination resource.

  ![](/assets/icons/16-chevron-right.svg) View options 

| Variant | Details |
| --- | --- |
| `"alternate"` |  |
| `"canonical"` |  |
| `"author"` |  |
| `"bookmark"` |  |
| `"dns-prefetch"` |  |
| `"expect"` |  |
| `"external"` |  |
| `"help"` |  |
| `"icon"` |  |
| `"manifest"` |  |
| `"modulepreload"` |  |
| `"license"` |  |
| `"next"` |  |
| `"nofollow"` |  |
| `"noopener"` |  |
| `"noreferrer"` |  |
| `"opener"` |  |
| `"pingback"` |  |
| `"preconnect"` |  |
| `"prefetch"` |  |
| `"preload"` |  |
| `"prev"` |  |
| `"privacy-policy"` |  |
| `"search"` |  |
| `"stylesheet"` |  |
| `"tag"` |  |
| `"terms-of-service"` |  |

#### `shape` [str](/docs/reference/foundations/str/)

The kind of shape to be created in an image map.

| Variant | Details |
| --- | --- |
| `"circle"` |  |
| `"default"` |  |
| `"poly"` |  |
| `"rect"` |  |

#### `target` [str](/docs/reference/foundations/str/)

Navigable for hyperlink navigation.

| Variant | Details |
| --- | --- |
| `"_blank"` |  |
| `"_self"` |  |
| `"_parent"` |  |
| `"_top"` |  |

### `article`

Self-contained syndicatable or reusable composition.

html.article(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `aside`

Sidebar for tangentially related content.

html.aside(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `audio`

Audio player.

html.audio(

[autoplay:](#functions-audio-autoplay) [bool](/docs/reference/foundations/bool/),[controls:](#functions-audio-controls) [bool](/docs/reference/foundations/bool/),[crossorigin:](#functions-audio-crossorigin) [str](/docs/reference/foundations/str/),[loop:](#functions-audio-loop) [bool](/docs/reference/foundations/bool/),[muted:](#functions-audio-muted) [bool](/docs/reference/foundations/bool/),[preload:](#functions-audio-preload) [none](/docs/reference/foundations/none/)[auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/),[src:](#functions-audio-src) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `autoplay` [bool](/docs/reference/foundations/bool/)

Hint that the media resource can be started automatically when the page is loaded.

#### `controls` [bool](/docs/reference/foundations/bool/)

Show user agent controls.

#### `crossorigin` [str](/docs/reference/foundations/str/)

How the element handles crossorigin requests.

| Variant | Details |
| --- | --- |
| `"anonymous"` |  |
| `"use-credentials"` |  |

#### `loop` [bool](/docs/reference/foundations/bool/)

Whether to loop the media resource.

#### `muted` [bool](/docs/reference/foundations/bool/)

Whether to mute the media resource by default.

#### `preload` [none](/docs/reference/foundations/none/) or [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/)

Hints how much buffering the media resource will likely need.

| Variant | Details |
| --- | --- |
| `"metadata"` |  |

#### `src` [str](/docs/reference/foundations/str/)

Address of the resource.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `b`

Keywords.

html.b(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `base`

Base URL and default target navigable for hyperlinks and forms.

html.base(

[href:](#functions-base-href) [str](/docs/reference/foundations/str/),[target:](#functions-base-target) [str](/docs/reference/foundations/str/),

) -> [content](/docs/reference/foundations/content/)

#### `href` [str](/docs/reference/foundations/str/)

Document base URL.

#### `target` [str](/docs/reference/foundations/str/)

Default navigable for hyperlink navigation and form submission.

| Variant | Details |
| --- | --- |
| `"_blank"` |  |
| `"_self"` |  |
| `"_parent"` |  |
| `"_top"` |  |

### `bdi`

Text directionality isolation.

html.bdi(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `bdo`

Text directionality formatting.

html.bdo(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `blockquote`

A section quoted from another source.

html.blockquote(

[cite:](#functions-blockquote-cite) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `cite` [str](/docs/reference/foundations/str/)

Link to the source of the quotation or more information about the edit.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `body`

Document body.

html.body(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `br`

Line break, e.g. in poem or postal address.

html.br() -> [content](/docs/reference/foundations/content/)

### `button`

Button control.

html.button(

[command:](#functions-button-command) [str](/docs/reference/foundations/str/),[commandfor:](#functions-button-commandfor) [str](/docs/reference/foundations/str/),[disabled:](#functions-button-disabled) [bool](/docs/reference/foundations/bool/),[form:](#functions-button-form) [str](/docs/reference/foundations/str/),[formaction:](#functions-button-formaction) [str](/docs/reference/foundations/str/),[formenctype:](#functions-button-formenctype) [str](/docs/reference/foundations/str/),[formmethod:](#functions-button-formmethod) [str](/docs/reference/foundations/str/),[formnovalidate:](#functions-button-formnovalidate) [bool](/docs/reference/foundations/bool/),[formtarget:](#functions-button-formtarget) [str](/docs/reference/foundations/str/),[name:](#functions-button-name) [str](/docs/reference/foundations/str/),[popovertarget:](#functions-button-popovertarget) [str](/docs/reference/foundations/str/),[popovertargetaction:](#functions-button-popovertargetaction) [str](/docs/reference/foundations/str/),[type:](#functions-button-type) [str](/docs/reference/foundations/str/),[value:](#functions-button-value) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `command` [str](/docs/reference/foundations/str/)

Indicates to the targeted element which action to take.

| Variant | Details |
| --- | --- |
| `"toggle-popover"` |  |
| `"show-popover"` |  |
| `"hide-popover"` |  |
| `"close"` |  |
| `"request-close"` |  |
| `"show-modal"` |  |

#### `commandfor` [str](/docs/reference/foundations/str/)

Targets another element to be invoked.

#### `disabled` [bool](/docs/reference/foundations/bool/)

Whether the form control is disabled.

#### `form` [str](/docs/reference/foundations/str/)

Associates the element with a form element.

#### `formaction` [str](/docs/reference/foundations/str/)

URL to use for form submission.

#### `formenctype` [str](/docs/reference/foundations/str/)

Entry list encoding type to use for form submission.

| Variant | Details |
| --- | --- |
| `"application/x-www-form-urlencoded"` |  |
| `"multipart/form-data"` |  |
| `"text/plain"` |  |

#### `formmethod` [str](/docs/reference/foundations/str/)

Variant to use for form submission.

| Variant | Details |
| --- | --- |
| `"GET"` |  |
| `"POST"` |  |
| `"dialog"` |  |

#### `formnovalidate` [bool](/docs/reference/foundations/bool/)

Bypass form control validation for form submission.

#### `formtarget` [str](/docs/reference/foundations/str/)

Navigable for form submission.

| Variant | Details |
| --- | --- |
| `"_blank"` |  |
| `"_self"` |  |
| `"_parent"` |  |
| `"_top"` |  |

#### `name` [str](/docs/reference/foundations/str/)

Name of the element to use for form submission and in the form.elements API.

#### `popovertarget` [str](/docs/reference/foundations/str/)

Targets a popover element to toggle, show, or hide.

#### `popovertargetaction` [str](/docs/reference/foundations/str/)

Indicates whether a targeted popover element is to be toggled, shown, or hidden.

| Variant | Details |
| --- | --- |
| `"toggle"` |  |
| `"show"` |  |
| `"hide"` |  |

#### `type` [str](/docs/reference/foundations/str/)

Type of button.

| Variant | Details |
| --- | --- |
| `"submit"` |  |
| `"reset"` |  |
| `"button"` |  |

#### `value` [str](/docs/reference/foundations/str/)

Value to be used for form submission.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `canvas`

Scriptable bitmap canvas.

html.canvas(

[height:](#functions-canvas-height) [int](/docs/reference/foundations/int/),[width:](#functions-canvas-width) [int](/docs/reference/foundations/int/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `height` [int](/docs/reference/foundations/int/)

Vertical dimension.

#### `width` [int](/docs/reference/foundations/int/)

Horizontal dimension.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `caption`

Table caption.

html.caption(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `cite`

Title of a work.

html.cite(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `code`

Computer code.

html.code(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `col`

Table column.

html.col(

[span:](#functions-col-span) [int](/docs/reference/foundations/int/)

) -> [content](/docs/reference/foundations/content/)

#### `span` [int](/docs/reference/foundations/int/)

Number of columns spanned by the element.

### `colgroup`

Group of columns in a table.

html.colgroup(

[span:](#functions-colgroup-span) [int](/docs/reference/foundations/int/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `span` [int](/docs/reference/foundations/int/)

Number of columns spanned by the element.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `data`

Machine-readable equivalent.

html.data(

[value:](#functions-data-value) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `value` [str](/docs/reference/foundations/str/)

Machine-readable value.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `datalist`

Container for options for combo box control.

html.datalist(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `dd`

Content for corresponding dt element(s).

html.dd(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `del`

A removal from the document.

html.del(

[cite:](#functions-del-cite) [str](/docs/reference/foundations/str/),[datetime:](#functions-del-datetime) [datetime](/docs/reference/foundations/datetime/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `cite` [str](/docs/reference/foundations/str/)

Link to the source of the quotation or more information about the edit.

#### `datetime` [datetime](/docs/reference/foundations/datetime/)

Date and (optionally) time of the change.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `details`

Disclosure control for hiding details.

html.details(

[name:](#functions-details-name) [str](/docs/reference/foundations/str/),[open:](#functions-details-open) [bool](/docs/reference/foundations/bool/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `name` [str](/docs/reference/foundations/str/)

Name of group of mutually-exclusive details elements.

#### `open` [bool](/docs/reference/foundations/bool/)

Whether the details are visible.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `dfn`

Defining instance.

html.dfn(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `dialog`

Dialog box or window.

html.dialog(

[open:](#functions-dialog-open) [bool](/docs/reference/foundations/bool/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `open` [bool](/docs/reference/foundations/bool/)

Whether the dialog box is showing.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `div`

Generic flow container, or container for name-value groups in dl elements.

html.div(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `dl`

Association list consisting of zero or more name-value groups.

html.dl(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `dt`

Legend for corresponding dd element(s).

html.dt(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `em`

Stress emphasis.

html.em(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `embed`

Plugin.

html.embed(

[height:](#functions-embed-height) [int](/docs/reference/foundations/int/),[src:](#functions-embed-src) [str](/docs/reference/foundations/str/),[type:](#functions-embed-type) [str](/docs/reference/foundations/str/),[width:](#functions-embed-width) [int](/docs/reference/foundations/int/),

) -> [content](/docs/reference/foundations/content/)

#### `height` [int](/docs/reference/foundations/int/)

Vertical dimension.

#### `src` [str](/docs/reference/foundations/str/)

Address of the resource.

#### `type` [str](/docs/reference/foundations/str/)

Type of embedded resource.

#### `width` [int](/docs/reference/foundations/int/)

Horizontal dimension.

### `fieldset`

Group of form controls.

html.fieldset(

[disabled:](#functions-fieldset-disabled) [bool](/docs/reference/foundations/bool/),[form:](#functions-fieldset-form) [str](/docs/reference/foundations/str/),[name:](#functions-fieldset-name) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `disabled` [bool](/docs/reference/foundations/bool/)

Whether the descendant form controls, except any inside legend, are disabled.

#### `form` [str](/docs/reference/foundations/str/)

Associates the element with a form element.

#### `name` [str](/docs/reference/foundations/str/)

Name of the element to use for form submission and in the form.elements API.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `figcaption`

Caption for figure.

html.figcaption(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `figure`

Figure with optional caption.

html.figure(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `footer`

Footer for a page or section.

html.footer(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `form`

User-submittable form.

html.form(

[accept-charset:](#functions-form-accept-charset) [str](/docs/reference/foundations/str/),[action:](#functions-form-action) [str](/docs/reference/foundations/str/),[autocomplete:](#functions-form-autocomplete) [bool](/docs/reference/foundations/bool/),[enctype:](#functions-form-enctype) [str](/docs/reference/foundations/str/),[method:](#functions-form-method) [str](/docs/reference/foundations/str/),[name:](#functions-form-name) [str](/docs/reference/foundations/str/),[novalidate:](#functions-form-novalidate) [bool](/docs/reference/foundations/bool/),[rel:](#functions-form-rel) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[target:](#functions-form-target) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `accept-charset` [str](/docs/reference/foundations/str/)

Character encodings to use for form submission.

| Variant | Details |
| --- | --- |
| `"utf-8"` |  |

#### `action` [str](/docs/reference/foundations/str/)

URL to use for form submission.

#### `autocomplete` [bool](/docs/reference/foundations/bool/)

Default setting for autofill feature for controls in the form.

#### `enctype` [str](/docs/reference/foundations/str/)

Entry list encoding type to use for form submission.

| Variant | Details |
| --- | --- |
| `"application/x-www-form-urlencoded"` |  |
| `"multipart/form-data"` |  |
| `"text/plain"` |  |

#### `method` [str](/docs/reference/foundations/str/)

Variant to use for form submission.

| Variant | Details |
| --- | --- |
| `"GET"` |  |
| `"POST"` |  |
| `"dialog"` |  |

#### `name` [str](/docs/reference/foundations/str/)

Name of form to use in the document.forms API.

#### `novalidate` [bool](/docs/reference/foundations/bool/)

Bypass form control validation for form submission.

#### `rel` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Relationship between the document containing the form and its action destination

  ![](/assets/icons/16-chevron-right.svg) View options 

| Variant | Details |
| --- | --- |
| `"alternate"` |  |
| `"canonical"` |  |
| `"author"` |  |
| `"bookmark"` |  |
| `"dns-prefetch"` |  |
| `"expect"` |  |
| `"external"` |  |
| `"help"` |  |
| `"icon"` |  |
| `"manifest"` |  |
| `"modulepreload"` |  |
| `"license"` |  |
| `"next"` |  |
| `"nofollow"` |  |
| `"noopener"` |  |
| `"noreferrer"` |  |
| `"opener"` |  |
| `"pingback"` |  |
| `"preconnect"` |  |
| `"prefetch"` |  |
| `"preload"` |  |
| `"prev"` |  |
| `"privacy-policy"` |  |
| `"search"` |  |
| `"stylesheet"` |  |
| `"tag"` |  |
| `"terms-of-service"` |  |

#### `target` [str](/docs/reference/foundations/str/)

Navigable for form submission.

| Variant | Details |
| --- | --- |
| `"_blank"` |  |
| `"_self"` |  |
| `"_parent"` |  |
| `"_top"` |  |

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `h1`

Heading.

html.h1(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `h2`

Heading.

html.h2(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `h3`

Heading.

html.h3(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `h4`

Heading.

html.h4(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `h5`

Heading.

html.h5(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `h6`

Heading.

html.h6(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `head`

Container for document metadata.

html.head(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `header`

Introductory or navigational aids for a page or section.

html.header(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `hgroup`

Heading container.

html.hgroup(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `hr`

Thematic break.

html.hr() -> [content](/docs/reference/foundations/content/)

### `html`

Root element.

html.html(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `i`

Alternate voice.

html.i(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `iframe`

Child navigable.

html.iframe(

[allow:](#functions-iframe-allow) [str](/docs/reference/foundations/str/),[allowfullscreen:](#functions-iframe-allowfullscreen) [bool](/docs/reference/foundations/bool/),[height:](#functions-iframe-height) [int](/docs/reference/foundations/int/),[loading:](#functions-iframe-loading) [str](/docs/reference/foundations/str/),[name:](#functions-iframe-name) [str](/docs/reference/foundations/str/),[referrerpolicy:](#functions-iframe-referrerpolicy) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/),[sandbox:](#functions-iframe-sandbox) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[src:](#functions-iframe-src) [str](/docs/reference/foundations/str/),[srcdoc:](#functions-iframe-srcdoc) [str](/docs/reference/foundations/str/),[width:](#functions-iframe-width) [int](/docs/reference/foundations/int/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `allow` [str](/docs/reference/foundations/str/)

Permissions policy to be applied to the iframe's contents.

#### `allowfullscreen` [bool](/docs/reference/foundations/bool/)

Whether to allow the iframe's contents to use requestFullscreen().

#### `height` [int](/docs/reference/foundations/int/)

Vertical dimension.

#### `loading` [str](/docs/reference/foundations/str/)

Used when determining loading deferral.

| Variant | Details |
| --- | --- |
| `"lazy"` |  |
| `"eager"` |  |

#### `name` [str](/docs/reference/foundations/str/)

Name of content navigable.

| Variant | Details |
| --- | --- |
| `"_blank"` |  |
| `"_self"` |  |
| `"_parent"` |  |
| `"_top"` |  |

#### `referrerpolicy` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/)

Referrer policy for fetches initiated by the element.

| Variant | Details |
| --- | --- |
| `"no-referrer"` |  |
| `"no-referrer-when-downgrade"` |  |
| `"same-origin"` |  |
| `"origin"` |  |
| `"strict-origin"` |  |
| `"origin-when-cross-origin"` |  |
| `"strict-origin-when-cross-origin"` |  |
| `"unsafe-url"` |  |

#### `sandbox` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Security rules for nested content.

  ![](/assets/icons/16-chevron-right.svg) View options 

| Variant | Details |
| --- | --- |
| `"allow-downloads"` |  |
| `"allow-forms"` |  |
| `"allow-modals"` |  |
| `"allow-orientation-lock"` |  |
| `"allow-pointer-lock"` |  |
| `"allow-popups"` |  |
| `"allow-popups-to-escape-sandbox"` |  |
| `"allow-presentation"` |  |
| `"allow-same-origin"` |  |
| `"allow-scripts"` |  |
| `"allow-top-navigation"` |  |
| `"allow-top-navigation-by-user-activation"` |  |
| `"allow-top-navigation-to-custom-protocols"` |  |

#### `src` [str](/docs/reference/foundations/str/)

Address of the resource.

#### `srcdoc` [str](/docs/reference/foundations/str/)

A document to render in the iframe.

#### `width` [int](/docs/reference/foundations/int/)

Horizontal dimension.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `img`

Image.

html.img(

[alt:](#functions-img-alt) [str](/docs/reference/foundations/str/),[crossorigin:](#functions-img-crossorigin) [str](/docs/reference/foundations/str/),[decoding:](#functions-img-decoding) [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/),[fetchpriority:](#functions-img-fetchpriority) [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/),[height:](#functions-img-height) [int](/docs/reference/foundations/int/),[ismap:](#functions-img-ismap) [bool](/docs/reference/foundations/bool/),[loading:](#functions-img-loading) [str](/docs/reference/foundations/str/),[referrerpolicy:](#functions-img-referrerpolicy) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/),[sizes:](#functions-img-sizes) [array](/docs/reference/foundations/array/),[src:](#functions-img-src) [str](/docs/reference/foundations/str/),[srcset:](#functions-img-srcset) [array](/docs/reference/foundations/array/),[usemap:](#functions-img-usemap) [str](/docs/reference/foundations/str/),[width:](#functions-img-width) [int](/docs/reference/foundations/int/),

) -> [content](/docs/reference/foundations/content/)

#### `alt` [str](/docs/reference/foundations/str/)

Replacement text for use when images are not available.

#### `crossorigin` [str](/docs/reference/foundations/str/)

How the element handles crossorigin requests.

| Variant | Details |
| --- | --- |
| `"anonymous"` |  |
| `"use-credentials"` |  |

#### `decoding` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/)

Decoding hint to use when processing this image for presentation.

| Variant | Details |
| --- | --- |
| `"sync"` |  |
| `"async"` |  |

#### `fetchpriority` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/)

Sets the priority for fetches initiated by the element.

| Variant | Details |
| --- | --- |
| `"high"` |  |
| `"low"` |  |

#### `height` [int](/docs/reference/foundations/int/)

Vertical dimension.

#### `ismap` [bool](/docs/reference/foundations/bool/)

Whether the image is a server-side image map.

#### `loading` [str](/docs/reference/foundations/str/)

Used when determining loading deferral.

| Variant | Details |
| --- | --- |
| `"lazy"` |  |
| `"eager"` |  |

#### `referrerpolicy` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/)

Referrer policy for fetches initiated by the element.

| Variant | Details |
| --- | --- |
| `"no-referrer"` |  |
| `"no-referrer-when-downgrade"` |  |
| `"same-origin"` |  |
| `"origin"` |  |
| `"strict-origin"` |  |
| `"origin-when-cross-origin"` |  |
| `"strict-origin-when-cross-origin"` |  |
| `"unsafe-url"` |  |

#### `sizes` [array](/docs/reference/foundations/array/)

Image sizes for different page layouts. Expects an array of dictionaries with the keys `condition` (string) and `size` (length).

#### `src` [str](/docs/reference/foundations/str/)

Address of the resource.

#### `srcset` [array](/docs/reference/foundations/array/)

Images to use in different situations, e.g., high-resolution displays, small monitors, etc. Expects an array of dictionaries with the keys `src` (string) and `width` (integer) or `density` (float).

#### `usemap` [str](/docs/reference/foundations/str/)

Name of image map to use.

#### `width` [int](/docs/reference/foundations/int/)

Horizontal dimension.

### `input`

Form control.

html.input(

[accept:](#functions-input-accept) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[alpha:](#functions-input-alpha) [bool](/docs/reference/foundations/bool/),[alt:](#functions-input-alt) [str](/docs/reference/foundations/str/),[autocomplete:](#functions-input-autocomplete) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[checked:](#functions-input-checked) [bool](/docs/reference/foundations/bool/),[colorspace:](#functions-input-colorspace) [str](/docs/reference/foundations/str/),[dirname:](#functions-input-dirname) [str](/docs/reference/foundations/str/),[disabled:](#functions-input-disabled) [bool](/docs/reference/foundations/bool/),[form:](#functions-input-form) [str](/docs/reference/foundations/str/),[formaction:](#functions-input-formaction) [str](/docs/reference/foundations/str/),[formenctype:](#functions-input-formenctype) [str](/docs/reference/foundations/str/),[formmethod:](#functions-input-formmethod) [str](/docs/reference/foundations/str/),[formnovalidate:](#functions-input-formnovalidate) [bool](/docs/reference/foundations/bool/),[formtarget:](#functions-input-formtarget) [str](/docs/reference/foundations/str/),[height:](#functions-input-height) [int](/docs/reference/foundations/int/),[list:](#functions-input-list) [str](/docs/reference/foundations/str/),[max:](#functions-input-max) [float](/docs/reference/foundations/float/)[datetime](/docs/reference/foundations/datetime/)[str](/docs/reference/foundations/str/),[maxlength:](#functions-input-maxlength) [int](/docs/reference/foundations/int/),[min:](#functions-input-min) [float](/docs/reference/foundations/float/)[datetime](/docs/reference/foundations/datetime/)[str](/docs/reference/foundations/str/),[minlength:](#functions-input-minlength) [int](/docs/reference/foundations/int/),[multiple:](#functions-input-multiple) [bool](/docs/reference/foundations/bool/),[name:](#functions-input-name) [str](/docs/reference/foundations/str/),[pattern:](#functions-input-pattern) [str](/docs/reference/foundations/str/),[placeholder:](#functions-input-placeholder) [str](/docs/reference/foundations/str/),[popovertarget:](#functions-input-popovertarget) [str](/docs/reference/foundations/str/),[popovertargetaction:](#functions-input-popovertargetaction) [str](/docs/reference/foundations/str/),[readonly:](#functions-input-readonly) [bool](/docs/reference/foundations/bool/),[required:](#functions-input-required) [bool](/docs/reference/foundations/bool/),[size:](#functions-input-size) [int](/docs/reference/foundations/int/),[src:](#functions-input-src) [str](/docs/reference/foundations/str/),[step:](#functions-input-step) [float](/docs/reference/foundations/float/)[str](/docs/reference/foundations/str/),[type:](#functions-input-type) [str](/docs/reference/foundations/str/),[value:](#functions-input-value) [float](/docs/reference/foundations/float/)[color](/docs/reference/visualize/color/)[datetime](/docs/reference/foundations/datetime/)[str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[width:](#functions-input-width) [int](/docs/reference/foundations/int/),

) -> [content](/docs/reference/foundations/content/)

#### `accept` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Hint for expected file type in file upload controls.

#### `alpha` [bool](/docs/reference/foundations/bool/)

Allow the color's alpha component to be set.

#### `alt` [str](/docs/reference/foundations/str/)

Replacement text for use when images are not available.

#### `autocomplete` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Hint for form autofill feature.

  ![](/assets/icons/16-chevron-right.svg) View options 

| Variant | Details |
| --- | --- |
| `"shipping"` |  |
| `"billing"` |  |
| `"name"` |  |
| `"honorific-prefix"` |  |
| `"given-name"` |  |
| `"additional-name"` |  |
| `"family-name"` |  |
| `"honorific-suffix"` |  |
| `"nickname"` |  |
| `"username"` |  |
| `"new-password"` |  |
| `"current-password"` |  |
| `"one-time-code"` |  |
| `"organization-title"` |  |
| `"organization"` |  |
| `"street-address"` |  |
| `"address-line1"` |  |
| `"address-line2"` |  |
| `"address-line3"` |  |
| `"address-level4"` |  |
| `"address-level3"` |  |
| `"address-level2"` |  |
| `"address-level1"` |  |
| `"country"` |  |
| `"country-name"` |  |
| `"postal-code"` |  |
| `"cc-name"` |  |
| `"cc-given-name"` |  |
| `"cc-additional-name"` |  |
| `"cc-family-name"` |  |
| `"cc-number"` |  |
| `"cc-exp"` |  |
| `"cc-exp-month"` |  |
| `"cc-exp-year"` |  |
| `"cc-csc"` |  |
| `"cc-type"` |  |
| `"transaction-currency"` |  |
| `"transaction-amount"` |  |
| `"language"` |  |
| `"bday"` |  |
| `"bday-day"` |  |
| `"bday-month"` |  |
| `"bday-year"` |  |
| `"sex"` |  |
| `"url"` |  |
| `"photo"` |  |
| `"home"` |  |
| `"work"` |  |
| `"mobile"` |  |
| `"fax"` |  |
| `"pager"` |  |
| `"tel"` |  |
| `"tel-country-code"` |  |
| `"tel-national"` |  |
| `"tel-area-code"` |  |
| `"tel-local"` |  |
| `"tel-local-prefix"` |  |
| `"tel-local-suffix"` |  |
| `"tel-extension"` |  |
| `"email"` |  |
| `"impp"` |  |

#### `checked` [bool](/docs/reference/foundations/bool/)

Whether the control is checked.

#### `colorspace` [str](/docs/reference/foundations/str/)

The color space of the serialized color.

| Variant | Details |
| --- | --- |
| `"limited-srgb"` |  |
| `"display-p3"` |  |

#### `dirname` [str](/docs/reference/foundations/str/)

Name of form control to use for sending the element's directionality in form submission.

#### `disabled` [bool](/docs/reference/foundations/bool/)

Whether the form control is disabled.

#### `form` [str](/docs/reference/foundations/str/)

Associates the element with a form element.

#### `formaction` [str](/docs/reference/foundations/str/)

URL to use for form submission.

#### `formenctype` [str](/docs/reference/foundations/str/)

Entry list encoding type to use for form submission.

| Variant | Details |
| --- | --- |
| `"application/x-www-form-urlencoded"` |  |
| `"multipart/form-data"` |  |
| `"text/plain"` |  |

#### `formmethod` [str](/docs/reference/foundations/str/)

Variant to use for form submission.

| Variant | Details |
| --- | --- |
| `"GET"` |  |
| `"POST"` |  |
| `"dialog"` |  |

#### `formnovalidate` [bool](/docs/reference/foundations/bool/)

Bypass form control validation for form submission.

#### `formtarget` [str](/docs/reference/foundations/str/)

Navigable for form submission.

| Variant | Details |
| --- | --- |
| `"_blank"` |  |
| `"_self"` |  |
| `"_parent"` |  |
| `"_top"` |  |

#### `height` [int](/docs/reference/foundations/int/)

Vertical dimension.

#### `list` [str](/docs/reference/foundations/str/)

List of autocomplete options.

#### `max` [float](/docs/reference/foundations/float/) or [datetime](/docs/reference/foundations/datetime/) or [str](/docs/reference/foundations/str/)

Maximum value.

#### `maxlength` [int](/docs/reference/foundations/int/)

Maximum length of value.

#### `min` [float](/docs/reference/foundations/float/) or [datetime](/docs/reference/foundations/datetime/) or [str](/docs/reference/foundations/str/)

Minimum value.

#### `minlength` [int](/docs/reference/foundations/int/)

Minimum length of value.

#### `multiple` [bool](/docs/reference/foundations/bool/)

Whether to allow multiple values.

#### `name` [str](/docs/reference/foundations/str/)

Name of the element to use for form submission and in the form.elements API.

#### `pattern` [str](/docs/reference/foundations/str/)

Pattern to be matched by the form control's value.

#### `placeholder` [str](/docs/reference/foundations/str/)

User-visible label to be placed within the form control.

#### `popovertarget` [str](/docs/reference/foundations/str/)

Targets a popover element to toggle, show, or hide.

#### `popovertargetaction` [str](/docs/reference/foundations/str/)

Indicates whether a targeted popover element is to be toggled, shown, or hidden.

| Variant | Details |
| --- | --- |
| `"toggle"` |  |
| `"show"` |  |
| `"hide"` |  |

#### `readonly` [bool](/docs/reference/foundations/bool/)

Whether to allow the value to be edited by the user.

#### `required` [bool](/docs/reference/foundations/bool/)

Whether the control is required for form submission.

#### `size` [int](/docs/reference/foundations/int/)

Size of the control.

#### `src` [str](/docs/reference/foundations/str/)

Address of the resource.

#### `step` [float](/docs/reference/foundations/float/) or [str](/docs/reference/foundations/str/)

Granularity to be matched by the form control's value.

| Variant | Details |
| --- | --- |
| `"any"` |  |

#### `type` [str](/docs/reference/foundations/str/)

Type of form control.

  ![](/assets/icons/16-chevron-right.svg) View options 

| Variant | Details |
| --- | --- |
| `"hidden"` |  |
| `"text"` |  |
| `"search"` |  |
| `"tel"` |  |
| `"url"` |  |
| `"email"` |  |
| `"password"` |  |
| `"date"` |  |
| `"month"` |  |
| `"week"` |  |
| `"time"` |  |
| `"datetime-local"` |  |
| `"number"` |  |
| `"range"` |  |
| `"color"` |  |
| `"checkbox"` |  |
| `"radio"` |  |
| `"file"` |  |
| `"submit"` |  |
| `"image"` |  |
| `"reset"` |  |
| `"button"` |  |

#### `value` [float](/docs/reference/foundations/float/) or [color](/docs/reference/visualize/color/) or [datetime](/docs/reference/foundations/datetime/) or [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Value of the form control.

#### `width` [int](/docs/reference/foundations/int/)

Horizontal dimension.

### `ins`

An addition to the document.

html.ins(

[cite:](#functions-ins-cite) [str](/docs/reference/foundations/str/),[datetime:](#functions-ins-datetime) [datetime](/docs/reference/foundations/datetime/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `cite` [str](/docs/reference/foundations/str/)

Link to the source of the quotation or more information about the edit.

#### `datetime` [datetime](/docs/reference/foundations/datetime/)

Date and (optionally) time of the change.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `kbd`

User input.

html.kbd(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `label`

Caption for a form control.

html.label(

[for:](#functions-label-for) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `for` [str](/docs/reference/foundations/str/)

Associate the label with form control.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `legend`

Caption for fieldset.

html.legend(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `li`

List item.

html.li(

[value:](#functions-li-value) [int](/docs/reference/foundations/int/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `value` [int](/docs/reference/foundations/int/)

Ordinal value of the list item.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `link`

Link metadata.

html.link(

[as:](#functions-link-as) [str](/docs/reference/foundations/str/),[blocking:](#functions-link-blocking) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[color:](#functions-link-color) [color](/docs/reference/visualize/color/),[crossorigin:](#functions-link-crossorigin) [str](/docs/reference/foundations/str/),[disabled:](#functions-link-disabled) [bool](/docs/reference/foundations/bool/),[fetchpriority:](#functions-link-fetchpriority) [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/),[href:](#functions-link-href) [str](/docs/reference/foundations/str/),[hreflang:](#functions-link-hreflang) [str](/docs/reference/foundations/str/),[imagesizes:](#functions-link-imagesizes) [array](/docs/reference/foundations/array/),[imagesrcset:](#functions-link-imagesrcset) [array](/docs/reference/foundations/array/),[integrity:](#functions-link-integrity) [str](/docs/reference/foundations/str/),[media:](#functions-link-media) [str](/docs/reference/foundations/str/),[referrerpolicy:](#functions-link-referrerpolicy) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/),[rel:](#functions-link-rel) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[sizes:](#functions-link-sizes) [array](/docs/reference/foundations/array/),[type:](#functions-link-type) [str](/docs/reference/foundations/str/),

) -> [content](/docs/reference/foundations/content/)

#### `as` [str](/docs/reference/foundations/str/)

Potential destination for a preload request (for rel="preload" and rel="modulepreload").

  ![](/assets/icons/16-chevron-right.svg) View options 

| Variant | Details |
| --- | --- |
| `"audio"` |  |
| `"audioworklet"` |  |
| `"document"` |  |
| `"embed"` |  |
| `"font"` |  |
| `"frame"` |  |
| `"iframe"` |  |
| `"image"` |  |
| `"json"` |  |
| `"manifest"` |  |
| `"object"` |  |
| `"paintworklet"` |  |
| `"report"` |  |
| `"script"` |  |
| `"serviceworker"` |  |
| `"sharedworker"` |  |
| `"style"` |  |
| `"track"` |  |
| `"video"` |  |
| `"webidentity"` |  |
| `"worker"` |  |
| `"xslt"` |  |

#### `blocking` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Whether the element is potentially render-blocking.

| Variant | Details |
| --- | --- |
| `"blocking"` |  |

#### `color` [color](/docs/reference/visualize/color/)

Color to use when customizing a site's icon (for rel="mask-icon").

#### `crossorigin` [str](/docs/reference/foundations/str/)

How the element handles crossorigin requests.

| Variant | Details |
| --- | --- |
| `"anonymous"` |  |
| `"use-credentials"` |  |

#### `disabled` [bool](/docs/reference/foundations/bool/)

Whether the link is disabled.

#### `fetchpriority` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/)

Sets the priority for fetches initiated by the element.

| Variant | Details |
| --- | --- |
| `"high"` |  |
| `"low"` |  |

#### `href` [str](/docs/reference/foundations/str/)

Address of the hyperlink.

#### `hreflang` [str](/docs/reference/foundations/str/)

Language of the linked resource.

#### `imagesizes` [array](/docs/reference/foundations/array/)

Image sizes for different page layouts (for rel="preload"). Expects an array of dictionaries with the keys `condition` (string) and `size` (length).

#### `imagesrcset` [array](/docs/reference/foundations/array/)

Images to use in different situations, e.g., high-resolution displays, small monitors, etc. (for rel="preload"). Expects an array of dictionaries with the keys `src` (string) and `width` (integer) or `density` (float).

#### `integrity` [str](/docs/reference/foundations/str/)

Integrity metadata used in Subresource Integrity checks.

#### `media` [str](/docs/reference/foundations/str/)

Applicable media.

#### `referrerpolicy` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/)

Referrer policy for fetches initiated by the element.

| Variant | Details |
| --- | --- |
| `"no-referrer"` |  |
| `"no-referrer-when-downgrade"` |  |
| `"same-origin"` |  |
| `"origin"` |  |
| `"strict-origin"` |  |
| `"origin-when-cross-origin"` |  |
| `"strict-origin-when-cross-origin"` |  |
| `"unsafe-url"` |  |

#### `rel` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Relationship between the document containing the hyperlink and the destination resource.

  ![](/assets/icons/16-chevron-right.svg) View options 

| Variant | Details |
| --- | --- |
| `"alternate"` |  |
| `"canonical"` |  |
| `"author"` |  |
| `"bookmark"` |  |
| `"dns-prefetch"` |  |
| `"expect"` |  |
| `"external"` |  |
| `"help"` |  |
| `"icon"` |  |
| `"manifest"` |  |
| `"modulepreload"` |  |
| `"license"` |  |
| `"next"` |  |
| `"nofollow"` |  |
| `"noopener"` |  |
| `"noreferrer"` |  |
| `"opener"` |  |
| `"pingback"` |  |
| `"preconnect"` |  |
| `"prefetch"` |  |
| `"preload"` |  |
| `"prev"` |  |
| `"privacy-policy"` |  |
| `"search"` |  |
| `"stylesheet"` |  |
| `"tag"` |  |
| `"terms-of-service"` |  |

#### `sizes` [array](/docs/reference/foundations/array/)

Sizes of the icons (for rel="icon"). Expects an array of sizes. Each size is specified as an array of two integers (width and height).

#### `type` [str](/docs/reference/foundations/str/)

Hint for the type of the referenced resource.

### `main`

Container for the dominant contents of the document.

html.main(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `map`

Image map.

html.map(

[name:](#functions-map-name) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `name` [str](/docs/reference/foundations/str/)

Name of image map to reference from the usemap attribute.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `mark`

Highlight.

html.mark(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `menu`

Menu of commands.

html.menu(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `meta`

Text metadata.

html.meta(

[charset:](#functions-meta-charset) [str](/docs/reference/foundations/str/),[content:](#functions-meta-content) [str](/docs/reference/foundations/str/),[http-equiv:](#functions-meta-http-equiv) [str](/docs/reference/foundations/str/),[media:](#functions-meta-media) [str](/docs/reference/foundations/str/),[name:](#functions-meta-name) [str](/docs/reference/foundations/str/),

) -> [content](/docs/reference/foundations/content/)

#### `charset` [str](/docs/reference/foundations/str/)

Character encoding declaration.

| Variant | Details |
| --- | --- |
| `"utf-8"` |  |

#### `content` [str](/docs/reference/foundations/str/)

Value of the element.

#### `http-equiv` [str](/docs/reference/foundations/str/)

Pragma directive.

| Variant | Details |
| --- | --- |
| `"content-type"` |  |
| `"default-style"` |  |
| `"refresh"` |  |
| `"x-ua-compatible"` |  |
| `"content-security-policy"` |  |

#### `media` [str](/docs/reference/foundations/str/)

Applicable media.

#### `name` [str](/docs/reference/foundations/str/)

Metadata name.

### `meter`

Gauge.

html.meter(

[high:](#functions-meter-high) [float](/docs/reference/foundations/float/),[low:](#functions-meter-low) [float](/docs/reference/foundations/float/),[max:](#functions-meter-max) [float](/docs/reference/foundations/float/),[min:](#functions-meter-min) [float](/docs/reference/foundations/float/),[optimum:](#functions-meter-optimum) [float](/docs/reference/foundations/float/),[value:](#functions-meter-value) [float](/docs/reference/foundations/float/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `high` [float](/docs/reference/foundations/float/)

Low limit of high range.

#### `low` [float](/docs/reference/foundations/float/)

High limit of low range.

#### `max` [float](/docs/reference/foundations/float/)

Upper bound of range.

#### `min` [float](/docs/reference/foundations/float/)

Lower bound of range.

#### `optimum` [float](/docs/reference/foundations/float/)

Optimum value in gauge.

#### `value` [float](/docs/reference/foundations/float/)

Current value of the element.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `nav`

Section with navigational links.

html.nav(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `noscript`

Fallback content for script.

html.noscript(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `object`

Image, child navigable, or plugin.

html.object(

[data:](#functions-object-data) [str](/docs/reference/foundations/str/),[form:](#functions-object-form) [str](/docs/reference/foundations/str/),[height:](#functions-object-height) [int](/docs/reference/foundations/int/),[name:](#functions-object-name) [str](/docs/reference/foundations/str/),[type:](#functions-object-type) [str](/docs/reference/foundations/str/),[width:](#functions-object-width) [int](/docs/reference/foundations/int/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `data` [str](/docs/reference/foundations/str/)

Address of the resource.

#### `form` [str](/docs/reference/foundations/str/)

Associates the element with a form element.

#### `height` [int](/docs/reference/foundations/int/)

Vertical dimension.

#### `name` [str](/docs/reference/foundations/str/)

Name of content navigable.

| Variant | Details |
| --- | --- |
| `"_blank"` |  |
| `"_self"` |  |
| `"_parent"` |  |
| `"_top"` |  |

#### `type` [str](/docs/reference/foundations/str/)

Type of embedded resource.

#### `width` [int](/docs/reference/foundations/int/)

Horizontal dimension.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `ol`

Ordered list.

html.ol(

[reversed:](#functions-ol-reversed) [bool](/docs/reference/foundations/bool/),[start:](#functions-ol-start) [int](/docs/reference/foundations/int/),[type:](#functions-ol-type) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `reversed` [bool](/docs/reference/foundations/bool/)

Number the list backwards.

#### `start` [int](/docs/reference/foundations/int/)

Starting value of the list.

#### `type` [str](/docs/reference/foundations/str/)

Kind of list marker.

| Variant | Details |
| --- | --- |
| `"1"` |  |
| `"a"` |  |
| `"A"` |  |
| `"i"` |  |
| `"I"` |  |

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `optgroup`

Group of options in a list box.

html.optgroup(

[disabled:](#functions-optgroup-disabled) [bool](/docs/reference/foundations/bool/),[label:](#functions-optgroup-label) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `disabled` [bool](/docs/reference/foundations/bool/)

Whether the form control is disabled.

#### `label` [str](/docs/reference/foundations/str/)

User-visible label.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `option`

Option in a list box or combo box control.

html.option(

[disabled:](#functions-option-disabled) [bool](/docs/reference/foundations/bool/),[label:](#functions-option-label) [str](/docs/reference/foundations/str/),[selected:](#functions-option-selected) [bool](/docs/reference/foundations/bool/),[value:](#functions-option-value) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `disabled` [bool](/docs/reference/foundations/bool/)

Whether the form control is disabled.

#### `label` [str](/docs/reference/foundations/str/)

User-visible label.

#### `selected` [bool](/docs/reference/foundations/bool/)

Whether the option is selected by default.

#### `value` [str](/docs/reference/foundations/str/)

Value to be used for form submission.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `output`

Calculated output value.

html.output(

[for:](#functions-output-for) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[form:](#functions-output-form) [str](/docs/reference/foundations/str/),[name:](#functions-output-name) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `for` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Specifies controls from which the output was calculated.

#### `form` [str](/docs/reference/foundations/str/)

Associates the element with a form element.

#### `name` [str](/docs/reference/foundations/str/)

Name of the element to use for form submission and in the form.elements API.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `p`

Paragraph.

html.p(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `picture`

Image.

html.picture(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `pre`

Block of preformatted text.

html.pre(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `progress`

Progress bar.

html.progress(

[max:](#functions-progress-max) [float](/docs/reference/foundations/float/),[value:](#functions-progress-value) [float](/docs/reference/foundations/float/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `max` [float](/docs/reference/foundations/float/)

Upper bound of range.

#### `value` [float](/docs/reference/foundations/float/)

Current value of the element.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `q`

Quotation.

html.q(

[cite:](#functions-q-cite) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `cite` [str](/docs/reference/foundations/str/)

Link to the source of the quotation or more information about the edit.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `rp`

Parenthesis for ruby annotation text.

html.rp(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `rt`

Ruby annotation text.

html.rt(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `ruby`

Ruby annotation(s).

html.ruby(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `s`

Inaccurate text.

html.s(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `samp`

Computer output.

html.samp(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `script`

Embedded script.

html.script(

[async:](#functions-script-async) [bool](/docs/reference/foundations/bool/),[blocking:](#functions-script-blocking) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[crossorigin:](#functions-script-crossorigin) [str](/docs/reference/foundations/str/),[defer:](#functions-script-defer) [bool](/docs/reference/foundations/bool/),[fetchpriority:](#functions-script-fetchpriority) [auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/),[integrity:](#functions-script-integrity) [str](/docs/reference/foundations/str/),[nomodule:](#functions-script-nomodule) [bool](/docs/reference/foundations/bool/),[referrerpolicy:](#functions-script-referrerpolicy) [none](/docs/reference/foundations/none/)[str](/docs/reference/foundations/str/),[src:](#functions-script-src) [str](/docs/reference/foundations/str/),[type:](#functions-script-type) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `async` [bool](/docs/reference/foundations/bool/)

Execute script when available, without blocking while fetching.

#### `blocking` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Whether the element is potentially render-blocking.

| Variant | Details |
| --- | --- |
| `"blocking"` |  |

#### `crossorigin` [str](/docs/reference/foundations/str/)

How the element handles crossorigin requests.

| Variant | Details |
| --- | --- |
| `"anonymous"` |  |
| `"use-credentials"` |  |

#### `defer` [bool](/docs/reference/foundations/bool/)

Defer script execution.

#### `fetchpriority` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/)

Sets the priority for fetches initiated by the element.

| Variant | Details |
| --- | --- |
| `"high"` |  |
| `"low"` |  |

#### `integrity` [str](/docs/reference/foundations/str/)

Integrity metadata used in Subresource Integrity checks.

#### `nomodule` [bool](/docs/reference/foundations/bool/)

Prevents execution in user agents that support module scripts.

#### `referrerpolicy` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/)

Referrer policy for fetches initiated by the element.

| Variant | Details |
| --- | --- |
| `"no-referrer"` |  |
| `"no-referrer-when-downgrade"` |  |
| `"same-origin"` |  |
| `"origin"` |  |
| `"strict-origin"` |  |
| `"origin-when-cross-origin"` |  |
| `"strict-origin-when-cross-origin"` |  |
| `"unsafe-url"` |  |

#### `src` [str](/docs/reference/foundations/str/)

Address of the resource.

#### `type` [str](/docs/reference/foundations/str/)

Type of script.

| Variant | Details |
| --- | --- |
| `"module"` |  |

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `search`

Container for search controls.

html.search(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `section`

Generic document or application section.

html.section(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `select`

List box control.

html.select(

[autocomplete:](#functions-select-autocomplete) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[disabled:](#functions-select-disabled) [bool](/docs/reference/foundations/bool/),[form:](#functions-select-form) [str](/docs/reference/foundations/str/),[multiple:](#functions-select-multiple) [bool](/docs/reference/foundations/bool/),[name:](#functions-select-name) [str](/docs/reference/foundations/str/),[required:](#functions-select-required) [bool](/docs/reference/foundations/bool/),[size:](#functions-select-size) [int](/docs/reference/foundations/int/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `autocomplete` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Hint for form autofill feature.

  ![](/assets/icons/16-chevron-right.svg) View options 

| Variant | Details |
| --- | --- |
| `"shipping"` |  |
| `"billing"` |  |
| `"name"` |  |
| `"honorific-prefix"` |  |
| `"given-name"` |  |
| `"additional-name"` |  |
| `"family-name"` |  |
| `"honorific-suffix"` |  |
| `"nickname"` |  |
| `"username"` |  |
| `"new-password"` |  |
| `"current-password"` |  |
| `"one-time-code"` |  |
| `"organization-title"` |  |
| `"organization"` |  |
| `"street-address"` |  |
| `"address-line1"` |  |
| `"address-line2"` |  |
| `"address-line3"` |  |
| `"address-level4"` |  |
| `"address-level3"` |  |
| `"address-level2"` |  |
| `"address-level1"` |  |
| `"country"` |  |
| `"country-name"` |  |
| `"postal-code"` |  |
| `"cc-name"` |  |
| `"cc-given-name"` |  |
| `"cc-additional-name"` |  |
| `"cc-family-name"` |  |
| `"cc-number"` |  |
| `"cc-exp"` |  |
| `"cc-exp-month"` |  |
| `"cc-exp-year"` |  |
| `"cc-csc"` |  |
| `"cc-type"` |  |
| `"transaction-currency"` |  |
| `"transaction-amount"` |  |
| `"language"` |  |
| `"bday"` |  |
| `"bday-day"` |  |
| `"bday-month"` |  |
| `"bday-year"` |  |
| `"sex"` |  |
| `"url"` |  |
| `"photo"` |  |
| `"home"` |  |
| `"work"` |  |
| `"mobile"` |  |
| `"fax"` |  |
| `"pager"` |  |
| `"tel"` |  |
| `"tel-country-code"` |  |
| `"tel-national"` |  |
| `"tel-area-code"` |  |
| `"tel-local"` |  |
| `"tel-local-prefix"` |  |
| `"tel-local-suffix"` |  |
| `"tel-extension"` |  |
| `"email"` |  |
| `"impp"` |  |

#### `disabled` [bool](/docs/reference/foundations/bool/)

Whether the form control is disabled.

#### `form` [str](/docs/reference/foundations/str/)

Associates the element with a form element.

#### `multiple` [bool](/docs/reference/foundations/bool/)

Whether to allow multiple values.

#### `name` [str](/docs/reference/foundations/str/)

Name of the element to use for form submission and in the form.elements API.

#### `required` [bool](/docs/reference/foundations/bool/)

Whether the control is required for form submission.

#### `size` [int](/docs/reference/foundations/int/)

Size of the control.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `slot`

Shadow tree slot.

html.slot(

[name:](#functions-slot-name) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `name` [str](/docs/reference/foundations/str/)

Name of shadow tree slot.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `small`

Side comment.

html.small(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `source`

Image source for img or media source for video or audio.

html.source(

[height:](#functions-source-height) [int](/docs/reference/foundations/int/),[media:](#functions-source-media) [str](/docs/reference/foundations/str/),[sizes:](#functions-source-sizes) [array](/docs/reference/foundations/array/),[src:](#functions-source-src) [str](/docs/reference/foundations/str/),[srcset:](#functions-source-srcset) [array](/docs/reference/foundations/array/),[type:](#functions-source-type) [str](/docs/reference/foundations/str/),[width:](#functions-source-width) [int](/docs/reference/foundations/int/),

) -> [content](/docs/reference/foundations/content/)

#### `height` [int](/docs/reference/foundations/int/)

Vertical dimension.

#### `media` [str](/docs/reference/foundations/str/)

Applicable media.

#### `sizes` [array](/docs/reference/foundations/array/)

Image sizes for different page layouts. Expects an array of dictionaries with the keys `condition` (string) and `size` (length).

#### `src` [str](/docs/reference/foundations/str/)

Address of the resource.

#### `srcset` [array](/docs/reference/foundations/array/)

Images to use in different situations, e.g., high-resolution displays, small monitors, etc. Expects an array of dictionaries with the keys `src` (string) and `width` (integer) or `density` (float).

#### `type` [str](/docs/reference/foundations/str/)

Type of embedded resource.

#### `width` [int](/docs/reference/foundations/int/)

Horizontal dimension.

### `span`

Generic phrasing container.

html.span(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `strong`

Importance.

html.strong(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `style`

Embedded styling information.

html.style(

[blocking:](#functions-style-blocking) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[media:](#functions-style-media) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `blocking` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Whether the element is potentially render-blocking.

| Variant | Details |
| --- | --- |
| `"blocking"` |  |

#### `media` [str](/docs/reference/foundations/str/)

Applicable media.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `sub`

Subscript.

html.sub(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `summary`

Caption for details.

html.summary(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `sup`

Superscript.

html.sup(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `table`

Table.

html.table(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `tbody`

Group of rows in a table.

html.tbody(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `td`

Table cell.

html.td(

[colspan:](#functions-td-colspan) [int](/docs/reference/foundations/int/),[headers:](#functions-td-headers) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[rowspan:](#functions-td-rowspan) [int](/docs/reference/foundations/int/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `colspan` [int](/docs/reference/foundations/int/)

Number of columns that the cell is to span.

#### `headers` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

The header cells for this cell.

#### `rowspan` [int](/docs/reference/foundations/int/)

Number of rows that the cell is to span.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `template`

Template.

html.template(

[shadowrootclonable:](#functions-template-shadowrootclonable) [bool](/docs/reference/foundations/bool/),[shadowrootcustomelementregistry:](#functions-template-shadowrootcustomelementregistry) [bool](/docs/reference/foundations/bool/),[shadowrootdelegatesfocus:](#functions-template-shadowrootdelegatesfocus) [bool](/docs/reference/foundations/bool/),[shadowrootmode:](#functions-template-shadowrootmode) [str](/docs/reference/foundations/str/),[shadowrootserializable:](#functions-template-shadowrootserializable) [bool](/docs/reference/foundations/bool/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `shadowrootclonable` [bool](/docs/reference/foundations/bool/)

Sets clonable on a declarative shadow root.

#### `shadowrootcustomelementregistry` [bool](/docs/reference/foundations/bool/)

Enables declarative shadow roots to indicate they will use a custom element registry.

#### `shadowrootdelegatesfocus` [bool](/docs/reference/foundations/bool/)

Sets delegates focus on a declarative shadow root.

#### `shadowrootmode` [str](/docs/reference/foundations/str/)

Enables streaming declarative shadow roots.

| Variant | Details |
| --- | --- |
| `"open"` |  |
| `"closed"` |  |

#### `shadowrootserializable` [bool](/docs/reference/foundations/bool/)

Sets serializable on a declarative shadow root.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `textarea`

Multiline text controls.

html.textarea(

[autocomplete:](#functions-textarea-autocomplete) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[cols:](#functions-textarea-cols) [int](/docs/reference/foundations/int/),[dirname:](#functions-textarea-dirname) [str](/docs/reference/foundations/str/),[disabled:](#functions-textarea-disabled) [bool](/docs/reference/foundations/bool/),[form:](#functions-textarea-form) [str](/docs/reference/foundations/str/),[maxlength:](#functions-textarea-maxlength) [int](/docs/reference/foundations/int/),[minlength:](#functions-textarea-minlength) [int](/docs/reference/foundations/int/),[name:](#functions-textarea-name) [str](/docs/reference/foundations/str/),[placeholder:](#functions-textarea-placeholder) [str](/docs/reference/foundations/str/),[readonly:](#functions-textarea-readonly) [bool](/docs/reference/foundations/bool/),[required:](#functions-textarea-required) [bool](/docs/reference/foundations/bool/),[rows:](#functions-textarea-rows) [int](/docs/reference/foundations/int/),[wrap:](#functions-textarea-wrap) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `autocomplete` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Hint for form autofill feature.

  ![](/assets/icons/16-chevron-right.svg) View options 

| Variant | Details |
| --- | --- |
| `"shipping"` |  |
| `"billing"` |  |
| `"name"` |  |
| `"honorific-prefix"` |  |
| `"given-name"` |  |
| `"additional-name"` |  |
| `"family-name"` |  |
| `"honorific-suffix"` |  |
| `"nickname"` |  |
| `"username"` |  |
| `"new-password"` |  |
| `"current-password"` |  |
| `"one-time-code"` |  |
| `"organization-title"` |  |
| `"organization"` |  |
| `"street-address"` |  |
| `"address-line1"` |  |
| `"address-line2"` |  |
| `"address-line3"` |  |
| `"address-level4"` |  |
| `"address-level3"` |  |
| `"address-level2"` |  |
| `"address-level1"` |  |
| `"country"` |  |
| `"country-name"` |  |
| `"postal-code"` |  |
| `"cc-name"` |  |
| `"cc-given-name"` |  |
| `"cc-additional-name"` |  |
| `"cc-family-name"` |  |
| `"cc-number"` |  |
| `"cc-exp"` |  |
| `"cc-exp-month"` |  |
| `"cc-exp-year"` |  |
| `"cc-csc"` |  |
| `"cc-type"` |  |
| `"transaction-currency"` |  |
| `"transaction-amount"` |  |
| `"language"` |  |
| `"bday"` |  |
| `"bday-day"` |  |
| `"bday-month"` |  |
| `"bday-year"` |  |
| `"sex"` |  |
| `"url"` |  |
| `"photo"` |  |
| `"home"` |  |
| `"work"` |  |
| `"mobile"` |  |
| `"fax"` |  |
| `"pager"` |  |
| `"tel"` |  |
| `"tel-country-code"` |  |
| `"tel-national"` |  |
| `"tel-area-code"` |  |
| `"tel-local"` |  |
| `"tel-local-prefix"` |  |
| `"tel-local-suffix"` |  |
| `"tel-extension"` |  |
| `"email"` |  |
| `"impp"` |  |

#### `cols` [int](/docs/reference/foundations/int/)

Maximum number of characters per line.

#### `dirname` [str](/docs/reference/foundations/str/)

Name of form control to use for sending the element's directionality in form submission.

#### `disabled` [bool](/docs/reference/foundations/bool/)

Whether the form control is disabled.

#### `form` [str](/docs/reference/foundations/str/)

Associates the element with a form element.

#### `maxlength` [int](/docs/reference/foundations/int/)

Maximum length of value.

#### `minlength` [int](/docs/reference/foundations/int/)

Minimum length of value.

#### `name` [str](/docs/reference/foundations/str/)

Name of the element to use for form submission and in the form.elements API.

#### `placeholder` [str](/docs/reference/foundations/str/)

User-visible label to be placed within the form control.

#### `readonly` [bool](/docs/reference/foundations/bool/)

Whether to allow the value to be edited by the user.

#### `required` [bool](/docs/reference/foundations/bool/)

Whether the control is required for form submission.

#### `rows` [int](/docs/reference/foundations/int/)

Number of lines to show.

#### `wrap` [str](/docs/reference/foundations/str/)

How the value of the form control is to be wrapped for form submission.

| Variant | Details |
| --- | --- |
| `"soft"` |  |
| `"hard"` |  |

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `tfoot`

Group of footer rows in a table.

html.tfoot(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `th`

Table header cell.

html.th(

[abbr:](#functions-th-abbr) [str](/docs/reference/foundations/str/),[colspan:](#functions-th-colspan) [int](/docs/reference/foundations/int/),[headers:](#functions-th-headers) [str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/),[rowspan:](#functions-th-rowspan) [int](/docs/reference/foundations/int/),[scope:](#functions-th-scope) [str](/docs/reference/foundations/str/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `abbr` [str](/docs/reference/foundations/str/)

Alternative label to use for the header cell when referencing the cell in other contexts.

#### `colspan` [int](/docs/reference/foundations/int/)

Number of columns that the cell is to span.

#### `headers` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

The header cells for this cell.

#### `rowspan` [int](/docs/reference/foundations/int/)

Number of rows that the cell is to span.

#### `scope` [str](/docs/reference/foundations/str/)

Specifies which cells the header cell applies to.

| Variant | Details |
| --- | --- |
| `"row"` |  |
| `"col"` |  |
| `"rowgroup"` |  |
| `"colgroup"` |  |

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `thead`

Group of heading rows in a table.

html.thead(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `time`

Machine-readable equivalent of date- or time-related data.

html.time(

[datetime:](#functions-time-datetime) [datetime](/docs/reference/foundations/datetime/)[duration](/docs/reference/foundations/duration/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `datetime` [datetime](/docs/reference/foundations/datetime/) or [duration](/docs/reference/foundations/duration/)

Machine-readable value.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `title`

Document title.

html.title(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `tr`

Table row.

html.tr(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `track`

Timed text track.

html.track(

[default:](#functions-track-default) [bool](/docs/reference/foundations/bool/),[kind:](#functions-track-kind) [str](/docs/reference/foundations/str/),[label:](#functions-track-label) [str](/docs/reference/foundations/str/),[src:](#functions-track-src) [str](/docs/reference/foundations/str/),[srclang:](#functions-track-srclang) [str](/docs/reference/foundations/str/),

) -> [content](/docs/reference/foundations/content/)

#### `default` [bool](/docs/reference/foundations/bool/)

Enable the track if no other text track is more suitable.

#### `kind` [str](/docs/reference/foundations/str/)

The type of text track.

| Variant | Details |
| --- | --- |
| `"subtitles"` |  |
| `"captions"` |  |
| `"descriptions"` |  |
| `"chapters"` |  |
| `"metadata"` |  |

#### `label` [str](/docs/reference/foundations/str/)

User-visible label.

#### `src` [str](/docs/reference/foundations/str/)

Address of the resource.

#### `srclang` [str](/docs/reference/foundations/str/)

Language of the text track.

### `u`

Unarticulated annotation.

html.u(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `ul`

List.

html.ul(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `var`

Variable.

html.var(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `video`

Video player.

html.video(

[autoplay:](#functions-video-autoplay) [bool](/docs/reference/foundations/bool/),[controls:](#functions-video-controls) [bool](/docs/reference/foundations/bool/),[crossorigin:](#functions-video-crossorigin) [str](/docs/reference/foundations/str/),[height:](#functions-video-height) [int](/docs/reference/foundations/int/),[loop:](#functions-video-loop) [bool](/docs/reference/foundations/bool/),[muted:](#functions-video-muted) [bool](/docs/reference/foundations/bool/),[playsinline:](#functions-video-playsinline) [bool](/docs/reference/foundations/bool/),[poster:](#functions-video-poster) [str](/docs/reference/foundations/str/),[preload:](#functions-video-preload) [none](/docs/reference/foundations/none/)[auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/),[src:](#functions-video-src) [str](/docs/reference/foundations/str/),[width:](#functions-video-width) [int](/docs/reference/foundations/int/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `autoplay` [bool](/docs/reference/foundations/bool/)

Hint that the media resource can be started automatically when the page is loaded.

#### `controls` [bool](/docs/reference/foundations/bool/)

Show user agent controls.

#### `crossorigin` [str](/docs/reference/foundations/str/)

How the element handles crossorigin requests.

| Variant | Details |
| --- | --- |
| `"anonymous"` |  |
| `"use-credentials"` |  |

#### `height` [int](/docs/reference/foundations/int/)

Vertical dimension.

#### `loop` [bool](/docs/reference/foundations/bool/)

Whether to loop the media resource.

#### `muted` [bool](/docs/reference/foundations/bool/)

Whether to mute the media resource by default.

#### `playsinline` [bool](/docs/reference/foundations/bool/)

Encourage the user agent to display video content within the element's playback area.

#### `poster` [str](/docs/reference/foundations/str/)

Poster frame to show prior to video playback.

#### `preload` [none](/docs/reference/foundations/none/) or [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/)

Hints how much buffering the media resource will likely need.

| Variant | Details |
| --- | --- |
| `"metadata"` |  |

#### `src` [str](/docs/reference/foundations/str/)

Address of the resource.

#### `width` [int](/docs/reference/foundations/int/)

Horizontal dimension.

#### `body` [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names.

The contents of the HTML element.

### `wbr`

Line breaking opportunity.

html.wbr() -> [content](/docs/reference/foundations/content/)

## Global Attributes

These parameters are common to all typed HTML functions. They are listed
here once instead of explicitly on each element for readability.

### `accesskey` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Keyboard shortcut to activate or focus element. Expects a single-codepoint string or an array thereof.

### `aria-activedescendant` [str](/docs/reference/foundations/str/)

Identifies the currently active element when DOM focus is on a composite widget, textbox, group, or application.

### `aria-atomic` [bool](/docs/reference/foundations/bool/)

Indicates whether assistive technologies will present all, or only parts of, the changed region based on the change notifications defined by the aria-relevant attribute.

### `aria-autocomplete` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/)

Indicates whether inputting text could trigger display of one or more predictions of the user's intended value for an input and specifies how predictions would be presented if they are made.

| Variant | Details |
| --- | --- |
| `"inline"` | When a user is providing input, text suggesting one way to complete the provided input may be dynamically inserted after the caret. |
| `"list"` | When a user is providing input, an element containing a collection of values that could complete the provided input may be displayed. |
| `"both"` | When a user is providing input, an element containing a collection of values that could complete the provided input may be displayed. If displayed, one value in the collection is automatically selected, and the text needed to complete the automatically selected value appears after the caret in the input. |

### `aria-busy` [bool](/docs/reference/foundations/bool/)

Indicates an element is being modified and that assistive technologies MAY want to wait until the modifications are complete before exposing them to the user.

### `aria-checked` [bool](/docs/reference/foundations/bool/) or [str](/docs/reference/foundations/str/)

Indicates the current "checked" state of checkboxes, radio buttons, and other widgets. See related aria-pressed and aria-selected.

| Variant | Details |
| --- | --- |
| `"mixed"` | An intermediate value between true and false. |

### `aria-colcount` [int](/docs/reference/foundations/int/)

Defines the total number of columns in a table, grid, or treegrid. See related aria-colindex.

### `aria-colindex` [int](/docs/reference/foundations/int/)

Defines an element's column index or position with respect to the total number of columns within a table, grid, or treegrid. See related aria-colcount and aria-colspan.

### `aria-colspan` [int](/docs/reference/foundations/int/)

Defines the number of columns spanned by a cell or gridcell within a table, grid, or treegrid. See related aria-colindex and aria-rowspan.

### `aria-controls` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Identifies the element (or elements) whose contents or presence are controlled by the current element. See related aria-owns.

### `aria-current` [bool](/docs/reference/foundations/bool/) or [str](/docs/reference/foundations/str/)

Indicates the element that represents the current item within a container or set of related elements.

| Variant | Details |
| --- | --- |
| `"page"` | Represents the current page within a set of pages. |
| `"step"` | Represents the current step within a process. |
| `"location"` | Represents the current location within an environment or context. |
| `"date"` | Represents the current date within a collection of dates. |
| `"time"` | Represents the current time within a set of times. |

### `aria-describedby` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Identifies the element (or elements) that describes the object. See related aria-labelledby.

### `aria-details` [str](/docs/reference/foundations/str/)

Identifies the element that provides a detailed, extended description for the object. See related aria-describedby.

### `aria-disabled` [bool](/docs/reference/foundations/bool/)

Indicates that the element is perceivable but disabled, so it is not editable or otherwise operable. See related aria-hidden and aria-readonly.

### `aria-errormessage` [str](/docs/reference/foundations/str/)

Identifies the element that provides an error message for the object. See related aria-invalid and aria-describedby.

### `aria-expanded` [none](/docs/reference/foundations/none/) or [bool](/docs/reference/foundations/bool/)

Indicates whether the element, or another grouping element it controls, is currently expanded or collapsed.

### `aria-flowto` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Identifies the next element (or elements) in an alternate reading order of content which, at the user's discretion, allows assistive technology to override the general default of reading in document source order.

### `aria-haspopup` [bool](/docs/reference/foundations/bool/) or [str](/docs/reference/foundations/str/)

Indicates the availability and type of interactive popup element, such as menu or dialog, that can be triggered by an element.

| Variant | Details |
| --- | --- |
| `"menu"` | Indicates the popup is a menu. |
| `"listbox"` | Indicates the popup is a listbox. |
| `"tree"` | Indicates the popup is a tree. |
| `"grid"` | Indicates the popup is a grid. |
| `"dialog"` | Indicates the popup is a dialog. |

### `aria-hidden` [none](/docs/reference/foundations/none/) or [bool](/docs/reference/foundations/bool/)

Indicates whether the element is exposed to an accessibility API. See related aria-disabled.

### `aria-invalid` [bool](/docs/reference/foundations/bool/) or [str](/docs/reference/foundations/str/)

Indicates the entered value does not conform to the format expected by the application. See related aria-errormessage.

| Variant | Details |
| --- | --- |
| `"grammar"` | A grammatical error was detected. |
| `"spelling"` | A spelling error was detected. |

### `aria-keyshortcuts` [str](/docs/reference/foundations/str/)

Indicates keyboard shortcuts that an author has implemented to activate or give focus to an element.

### `aria-label` [str](/docs/reference/foundations/str/)

Defines a string value that labels the current element. See related aria-labelledby.

### `aria-labelledby` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Identifies the element (or elements) that labels the current element. See related aria-describedby.

### `aria-level` [int](/docs/reference/foundations/int/)

Defines the hierarchical level of an element within a structure.

### `aria-live` [str](/docs/reference/foundations/str/)

Indicates that an element will be updated, and describes the types of updates the user agents, assistive technologies, and user can expect from the live region.

| Variant | Details |
| --- | --- |
| `"assertive"` | Indicates that updates to the region have the highest priority and should be presented the user immediately. |
| `"off"` | Indicates that updates to the region should not be presented to the user unless the used is currently focused on that region. |
| `"polite"` | Indicates that updates to the region should be presented at the next graceful opportunity, such as at the end of speaking the current sentence or when the user pauses typing. |

### `aria-modal` [bool](/docs/reference/foundations/bool/)

Indicates whether an element is modal when displayed.

### `aria-multiline` [bool](/docs/reference/foundations/bool/)

Indicates whether a text box accepts multiple lines of input or only a single line.

### `aria-multiselectable` [bool](/docs/reference/foundations/bool/)

Indicates that the user may select more than one item from the current selectable descendants.

### `aria-orientation` [str](/docs/reference/foundations/str/)

Indicates whether the element's orientation is horizontal, vertical, or unknown/ambiguous.

| Variant | Details |
| --- | --- |
| `"horizontal"` | The element is oriented horizontally. |
| `"undefined"` | The element's orientation is unknown/ambiguous. |
| `"vertical"` | The element is oriented vertically. |

### `aria-owns` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Identifies an element (or elements) in order to define a visual, functional, or contextual parent/child relationship between DOM elements where the DOM hierarchy cannot be used to represent the relationship. See related aria-controls.

### `aria-placeholder` [str](/docs/reference/foundations/str/)

Defines a short hint (a word or short phrase) intended to aid the user with data entry when the control has no value. A hint could be a sample value or a brief description of the expected format.

### `aria-posinset` [int](/docs/reference/foundations/int/)

Defines an element's number or position in the current set of listitems or treeitems. Not required if all elements in the set are present in the DOM. See related aria-setsize.

### `aria-pressed` [bool](/docs/reference/foundations/bool/) or [str](/docs/reference/foundations/str/)

Indicates the current "pressed" state of toggle buttons. See related aria-checked and aria-selected.

| Variant | Details |
| --- | --- |
| `"mixed"` | An intermediate value between true and false. |

### `aria-readonly` [bool](/docs/reference/foundations/bool/)

Indicates that the element is not editable, but is otherwise operable. See related aria-disabled.

### `aria-relevant` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Indicates what notifications the user agent will trigger when the accessibility tree within a live region is modified. See related aria-atomic.

| Variant | Details |
| --- | --- |
| `"additions"` | Element nodes are added to the accessibility tree within the live region. |
| `"additions text"` | Equivalent to the combination of values, "additions text". |
| `"all"` | Equivalent to the combination of all values, "additions removals text". |
| `"removals"` | Text content, a text alternative, or an element node within the live region is removed from the accessibility tree. |
| `"text"` | Text content or a text alternative is added to any descendant in the accessibility tree of the live region. |

### `aria-required` [bool](/docs/reference/foundations/bool/)

Indicates that user input is required on the element before a form may be submitted.

### `aria-roledescription` [str](/docs/reference/foundations/str/)

Defines a human-readable, author-localized description for the role of an element.

### `aria-rowcount` [int](/docs/reference/foundations/int/)

Defines the total number of rows in a table, grid, or treegrid. See related aria-rowindex.

### `aria-rowindex` [int](/docs/reference/foundations/int/)

Defines an element's row index or position with respect to the total number of rows within a table, grid, or treegrid. See related aria-rowcount and aria-rowspan.

### `aria-rowspan` [int](/docs/reference/foundations/int/)

Defines the number of rows spanned by a cell or gridcell within a table, grid, or treegrid. See related aria-rowindex and aria-colspan.

### `aria-selected` [none](/docs/reference/foundations/none/) or [bool](/docs/reference/foundations/bool/)

Indicates the current "selected" state of various widgets. See related aria-checked and aria-pressed.

### `aria-setsize` [int](/docs/reference/foundations/int/)

Defines the number of items in the current set of listitems or treeitems. Not required if all elements in the set are present in the DOM. See related aria-posinset.

### `aria-sort` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/)

Indicates if items in a table or grid are sorted in ascending or descending order.

| Variant | Details |
| --- | --- |
| `"ascending"` | Items are sorted in ascending order by this column. |
| `"descending"` | Items are sorted in descending order by this column. |
| `"other"` | A sort algorithm other than ascending or descending has been applied. |

### `aria-valuemax` [float](/docs/reference/foundations/float/)

Defines the maximum allowed value for a range widget.

### `aria-valuemin` [float](/docs/reference/foundations/float/)

Defines the minimum allowed value for a range widget.

### `aria-valuenow` [float](/docs/reference/foundations/float/)

Defines the current value for a range widget. See related aria-valuetext.

### `aria-valuetext` [str](/docs/reference/foundations/str/)

Defines the human readable text alternative of aria-valuenow for a range widget.

### `autocapitalize` [none](/docs/reference/foundations/none/) or [bool](/docs/reference/foundations/bool/) or [str](/docs/reference/foundations/str/)

Recommended autocapitalization behavior (for supported input methods).

| Variant | Details |
| --- | --- |
| `"sentences"` |  |
| `"words"` |  |
| `"characters"` |  |

### `autocorrect` [bool](/docs/reference/foundations/bool/)

Recommended autocorrection behavior (for supported input methods).

### `autofocus` [bool](/docs/reference/foundations/bool/)

Automatically focus the element when the page is loaded.

### `class` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Classes to which the element belongs.

### `contenteditable` [bool](/docs/reference/foundations/bool/) or [str](/docs/reference/foundations/str/)

Whether the element is editable.

| Variant | Details |
| --- | --- |
| `"plaintext-only"` |  |

### `dir` [auto](/docs/reference/foundations/auto/) or [direction](/docs/reference/layout/direction/)

The text directionality of the element.

### `draggable` [bool](/docs/reference/foundations/bool/)

Whether the element is draggable.

### `enterkeyhint` [str](/docs/reference/foundations/str/)

Hint for selecting an enter key action.

| Variant | Details |
| --- | --- |
| `"enter"` |  |
| `"done"` |  |
| `"go"` |  |
| `"next"` |  |
| `"previous"` |  |
| `"search"` |  |
| `"send"` |  |

### `hidden` [bool](/docs/reference/foundations/bool/) or [str](/docs/reference/foundations/str/)

Whether the element is relevant.

| Variant | Details |
| --- | --- |
| `"until-found"` |  |

### `id` [str](/docs/reference/foundations/str/)

The element's ID.

### `inert` [bool](/docs/reference/foundations/bool/)

Whether the element is inert.

### `inputmode` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/)

Hint for selecting an input modality.

| Variant | Details |
| --- | --- |
| `"text"` |  |
| `"tel"` |  |
| `"email"` |  |
| `"url"` |  |
| `"numeric"` |  |
| `"decimal"` |  |
| `"search"` |  |

### `is` [str](/docs/reference/foundations/str/)

Creates a customized built-in element.

### `itemid` [str](/docs/reference/foundations/str/)

Global identifier for a microdata item.

### `itemprop` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Property names of a microdata item.

### `itemref` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Referenced elements.

### `itemscope` [bool](/docs/reference/foundations/bool/)

Introduces a microdata item.

### `itemtype` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/)

Item types of a microdata item.

### `lang` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/)

Language of the element.

### `nonce` [str](/docs/reference/foundations/str/)

Cryptographic nonce used in Content Security Policy checks.

### `popover` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/)

Makes the element a popover element.

| Variant | Details |
| --- | --- |
| `"manual"` |  |

### `role` [none](/docs/reference/foundations/none/) or [str](/docs/reference/foundations/str/)

An ARIA role.

  ![](/assets/icons/16-chevron-right.svg) View options 

| Variant | Details |
| --- | --- |
| `"alert"` | A type of live region with important, and usually time-sensitive, information. See related alertdialog and status. |
| `"alertdialog"` | A type of dialog that contains an alert message, where initial focus goes to an element within the dialog. See related alert and dialog. |
| `"application"` | A structure containing one or more focusable elements requiring user input, such as keyboard or gesture events, that do not follow a standard interaction pattern supported by a widget role. |
| `"article"` | A section of a page that consists of a composition that forms an independent part of a document, page, or site. |
| `"banner"` | A region that contains mostly site-oriented content, rather than page-specific content. |
| `"button"` | An input that allows for user-triggered actions when clicked or pressed. See related link. |
| `"cell"` | A cell in a tabular container. See related gridcell. |
| `"checkbox"` | A checkable input that has three possible values: true, false, or mixed. |
| `"columnheader"` | A cell containing header information for a column. |
| `"combobox"` | A composite widget containing a single-line textbox and another element, such as a listbox or grid, that can dynamically pop up to help the user set the value of the textbox. |
| `"command"` | A form of widget that performs an action but does not receive input data. |
| `"complementary"` | A supporting section of the document, designed to be complementary to the main content at a similar level in the DOM hierarchy, but remains meaningful when separated from the main content. |
| `"composite"` | A widget that may contain navigable descendants or owned children. |
| `"contentinfo"` | A large perceivable region that contains information about the parent document. |
| `"definition"` | A definition of a term or concept. See related term. |
| `"dialog"` | A dialog is a descendant window of the primary window of a web application. For HTML pages, the primary application window is the entire web document, i.e., the body element. |
| `"directory"` | A list of references to members of a group, such as a static table of contents. |
| `"document"` | An element containing content that assistive technology users may want to browse in a reading mode. |
| `"feed"` | A scrollable list of articles where scrolling may cause articles to be added to or removed from either end of the list. |
| `"figure"` | A perceivable section of content that typically contains a graphical document, images, code snippets, or example text. The parts of a figure MAY be user-navigable. |
| `"form"` | A landmark region that contains a collection of items and objects that, as a whole, combine to create a form. See related search. |
| `"grid"` | A composite widget containing a collection of one or more rows with one or more cells where some or all cells in the grid are focusable by using methods of two-dimensional navigation, such as directional arrow keys. |
| `"gridcell"` | A cell in a grid or treegrid. |
| `"group"` | A set of user interface objects which are not intended to be included in a page summary or table of contents by assistive technologies. |
| `"heading"` | A heading for a section of the page. |
| `"img"` | A container for a collection of elements that form an image. |
| `"input"` | A generic type of widget that allows user input. |
| `"landmark"` | A perceivable section containing content that is relevant to a specific, author-specified purpose and sufficiently important that users will likely want to be able to navigate to the section easily and to have it listed in a summary of the page. Such a page summary could be generated dynamically by a user agent or assistive technology. |
| `"link"` | An interactive reference to an internal or external resource that, when activated, causes the user agent to navigate to that resource. See related button. |
| `"list"` | A section containing listitem elements. See related listbox. |
| `"listbox"` | A widget that allows the user to select one or more items from a list of choices. See related combobox and list. |
| `"listitem"` | A single item in a list or directory. |
| `"log"` | A type of live region where new information is added in meaningful order and old information may disappear. See related marquee. |
| `"main"` | The main content of a document. |
| `"marquee"` | A type of live region where non-essential information changes frequently. See related log. |
| `"math"` | Content that represents a mathematical expression. |
| `"menu"` | A type of widget that offers a list of choices to the user. |
| `"menubar"` | A presentation of menu that usually remains visible and is usually presented horizontally. |
| `"menuitem"` | An option in a set of choices contained by a menu or menubar. |
| `"menuitemcheckbox"` | A menuitem with a checkable state whose possible values are true, false, or mixed. |
| `"menuitemradio"` | A checkable menuitem in a set of elements with the same role, only one of which can be checked at a time. |
| `"navigation"` | A collection of navigational elements (usually links) for navigating the document or related documents. |
| `"note"` | A section whose content is parenthetic or ancillary to the main content of the resource. |
| `"option"` | A selectable item in a select list. |
| `"presentation"` | An element whose implicit native role semantics will not be mapped to the accessibility API. See synonym none. |
| `"progressbar"` | An element that displays the progress status for tasks that take a long time. |
| `"radio"` | A checkable input in a group of elements with the same role, only one of which can be checked at a time. |
| `"radiogroup"` | A group of radio buttons. |
| `"range"` | An input representing a range of values that can be set by the user. |
| `"region"` | A perceivable section containing content that is relevant to a specific, author-specified purpose and sufficiently important that users will likely want to be able to navigate to the section easily and to have it listed in a summary of the page. Such a page summary could be generated dynamically by a user agent or assistive technology. |
| `"roletype"` | The base role from which all other roles in this taxonomy inherit. |
| `"row"` | A row of cells in a tabular container. |
| `"rowgroup"` | A structure containing one or more row elements in a tabular container. |
| `"rowheader"` | A cell containing header information for a row in a grid. |
| `"scrollbar"` | A graphical object that controls the scrolling of content within a viewing area, regardless of whether the content is fully displayed within the viewing area. |
| `"search"` | A landmark region that contains a collection of items and objects that, as a whole, combine to create a search facility. See related form and searchbox. |
| `"searchbox"` | A type of textbox intended for specifying search criteria. See related textbox and search. |
| `"section"` | A renderable structural containment unit in a document or application. |
| `"sectionhead"` | A structure that labels or summarizes the topic of its related section. |
| `"select"` | A form widget that allows the user to make selections from a set of choices. |
| `"separator"` | A divider that separates and distinguishes sections of content or groups of menuitems. |
| `"slider"` | A user input where the user selects a value from within a given range. |
| `"spinbutton"` | A form of range that expects the user to select from among discrete choices. |
| `"status"` | A type of live region whose content is advisory information for the user but is not important enough to justify an alert, often but not necessarily presented as a status bar. |
| `"structure"` | A document structural element. |
| `"switch"` | A type of checkbox that represents on/off values, as opposed to checked/unchecked values. See related checkbox. |
| `"tab"` | A grouping label providing a mechanism for selecting the tab content that is to be rendered to the user. |
| `"table"` | A section containing data arranged in rows and columns. See related grid. |
| `"tablist"` | A list of tab elements, which are references to tabpanel elements. |
| `"tabpanel"` | A container for the resources associated with a tab, where each tab is contained in a tablist. |
| `"term"` | A word or phrase with a corresponding definition. See related definition. |
| `"textbox"` | A type of input that allows free-form text as its value. |
| `"timer"` | A type of live region containing a numerical counter which indicates an amount of elapsed time from a start point, or the time remaining until an end point. |
| `"toolbar"` | A collection of commonly used function buttons or controls represented in compact visual form. |
| `"tooltip"` | A contextual popup that displays a description for an element. |
| `"tree"` | A type of list that may contain sub-level nested groups that can be collapsed and expanded. |
| `"treegrid"` | A grid whose rows can be expanded and collapsed in the same manner as for a tree. |
| `"treeitem"` | An option item of a tree. This is an element within a tree that may be expanded or collapsed if it contains a sub-level group of tree item elements. |
| `"widget"` | An interactive component of a graphical user interface (GUI). |
| `"window"` | A browser or application window. |

### `slot` [str](/docs/reference/foundations/str/)

The element's desired slot.

### `spellcheck` [bool](/docs/reference/foundations/bool/)

Whether the element is to have its spelling and grammar checked.

### `style` [str](/docs/reference/foundations/str/)

Presentational and formatting instructions.

### `tabindex` [int](/docs/reference/foundations/int/)

Whether the element is focusable and sequentially focusable, and the relative order of the element for the purposes of sequential focus navigation.

### `title` [str](/docs/reference/foundations/str/)

Advisory information for the element.

### `translate` [bool](/docs/reference/foundations/bool/)

Whether the element is to be translated when the page is localized.

### `writingsuggestions` [bool](/docs/reference/foundations/bool/)

Whether the element can offer writing suggestions or not.

[![←](/assets/icons/16-chevron-right.svg)

FramePrevious page](/docs/reference/html/frame/) [![→](/assets/icons/16-chevron-right.svg)

PNGNext page](/docs/reference/png/)