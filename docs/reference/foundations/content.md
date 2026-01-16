# content

Source: https://typst.app/docs/reference/foundations/content/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Foundations](/docs/reference/foundations/)
- ![](/assets/icons/16-chevron-right.svg)
- [Content](/docs/reference/foundations/content/)

# content

A piece of document content.

This type is at the heart of Typst. All markup you write and most
[functions](/docs/reference/foundations/function/) you call produce content values. You can create a
content value by enclosing markup in square brackets. This is also how you
pass content to functions.

## Example

```typst
Type of *Hello!* is
#type([*Hello!*])
```

![Preview](/assets/docs/X4qekl24YgH3SaXf1J0tagAAAAAAAAAA.png)

Content can be added with the `+` operator,
[joined together](/docs/reference/scripting/#blocks) and multiplied with integers. Wherever
content is expected, you can also pass a [string](/docs/reference/foundations/str/) or `none`.

## Representation

Content consists of elements with fields. When constructing an element with
its *element function,* you provide these fields as arguments and when you
have a content value, you can access its fields with [field access
syntax](/docs/reference/scripting/#field-access).

Some fields are required: These must be provided when constructing an
element and as a consequence, they are always available through field access
on content of that type. Required fields are marked as such in the
documentation.

Most fields are optional: Like required fields, they can be passed to the
element function to configure them for a single element. However, these can
also be configured with [set rules](/docs/reference/styling/#set-rules) to apply them to
all elements within a scope. Optional fields are only available with field
access syntax when they were explicitly passed to the element function, not
when they result from a set rule.

Each element has a default appearance. However, you can also completely
customize its appearance with a [show rule](/docs/reference/styling/#show-rules). The show
rule is passed the element. It can access the element's field and produce
arbitrary content from it.

In the web app, you can hover over a content variable to see exactly which
elements the content is composed of and what fields they have.
Alternatively, you can inspect the output of the [`repr`](/docs/reference/foundations/repr/ "`repr`") function.

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `func`

The content's element function. This function can be used to create the element
contained in this content. It can be used in set and show rules for the
element. Can be compared with global functions to check whether you have
a specific
kind of element.

self.func() -> [function](/docs/reference/foundations/function/)

### `has`

Whether the content has the specified field.

self.has(

[str](/docs/reference/foundations/str/)

) -> [bool](/docs/reference/foundations/bool/)

#### `field` [str](/docs/reference/foundations/str/) Required Positional Question mark Positional parameters are specified in order, without names.

The field to look for.

### `at`

Access the specified field on the content. Returns the default value if
the field does not exist or fails with an error if no default value was
specified.

self.at(

[str](/docs/reference/foundations/str/),[default:](#definitions-at-default) any,

) -> any

#### `field` [str](/docs/reference/foundations/str/) Required Positional Question mark Positional parameters are specified in order, without names.

The field to access.

#### `default` any

A default value to return if the field does not exist.

### `fields`

Returns the fields of this content.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#rect(
  width: 10cm,
  height: 10cm,
).fields()
```

![Preview](/assets/docs/zNlYUwJ_V8GS40gGav-GlwAAAAAAAAAA.png)

self.fields() -> [dictionary](/docs/reference/foundations/dictionary/)

### `location`

The location of the content. This is only available on content returned
by [query](/docs/reference/introspection/query/ "query") or provided by a [show rule](/docs/reference/styling/#show-rules),
for other content it will be `none`. The resulting location can be
used with [counters](/docs/reference/introspection/counter/), [state](/docs/reference/introspection/state/ "state") and [queries](/docs/reference/introspection/query/).

self.location() -> [none](/docs/reference/foundations/none/)[location](/docs/reference/introspection/location/)

[![←](/assets/icons/16-chevron-right.svg)

CalculationPrevious page](/docs/reference/foundations/calc/) [![→](/assets/icons/16-chevron-right.svg)

DatetimeNext page](/docs/reference/foundations/datetime/)