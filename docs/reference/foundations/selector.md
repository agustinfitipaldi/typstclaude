# selector

Source: https://typst.app/docs/reference/foundations/selector/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Foundations](/docs/reference/foundations/)
- ![](/assets/icons/16-chevron-right.svg)
- [Selector](/docs/reference/foundations/selector/)

# selector

A filter for selecting elements within the document.

To construct a selector you can:

- use an [element function](/docs/reference/foundations/function/#element-functions)
- filter for an element function with [specific fields](/docs/reference/foundations/function/#definitions-where)
- use a [string](/docs/reference/foundations/str/) or [regular expression](/docs/reference/foundations/regex/)
- use a [`<label>`](/docs/reference/foundations/label/)
- use a [`location`](/docs/reference/introspection/location/ "`location`")
- call the [`selector`](/docs/reference/foundations/selector/ "`selector`") constructor to convert any of the above types into a
  selector value and use the methods below to refine it

Selectors are used to [apply styling rules](/docs/reference/styling/#show-rules) to
elements. You can also use selectors to [query](/docs/reference/introspection/query/ "query") the document for certain
types of elements.

Furthermore, you can pass a selector to several of Typst's built-in
functions to configure their behaviour. One such example is the [outline](/docs/reference/model/outline/ "outline")
where it can be used to change which elements are listed within the outline.

Multiple selectors can be combined using the methods shown below. However,
not all kinds of selectors are supported in all places, at the moment.

## Example

```typst
#context query(
  heading.where(level: 1)
    .or(heading.where(level: 2))
)

= This will be found
== So will this
=== But this will not.
```

![Preview](/assets/docs/SW-2iLP1LIGQ0ITsB7LGEQAAAAAAAAAA.png)

## Constructor Question mark If a type has a constructor, you can call it like a function to create a new value of the type.

Turns a value into a selector. The following values are accepted:

- An element function like a `heading` or `figure`.
- A [string](/docs/reference/foundations/str/) or [regular expression](/docs/reference/foundations/regex/).
- A `<label>`.
- A [`location`](/docs/reference/introspection/location/ "`location`").
- A more complex selector like `heading.where(level: 1)`.

selector(

[str](/docs/reference/foundations/str/)[regex](/docs/reference/foundations/regex/)[label](/docs/reference/foundations/label/)[selector](/docs/reference/foundations/selector/)[location](/docs/reference/introspection/location/)[function](/docs/reference/foundations/function/)

) -> [selector](/docs/reference/foundations/selector/)

#### `target` [str](/docs/reference/foundations/str/) or [regex](/docs/reference/foundations/regex/) or [label](/docs/reference/foundations/label/) or [selector](/docs/reference/foundations/selector/) or [location](/docs/reference/introspection/location/) or [function](/docs/reference/foundations/function/) Required Positional Question mark Positional parameters are specified in order, without names.

Can be an element function like a `heading` or `figure`, a `<label>`
or a more complex selector like `heading.where(level: 1)`.

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `or`

Selects all elements that match this or any of the other selectors.

self.or(

[..](#definitions-or-others)[str](/docs/reference/foundations/str/)[regex](/docs/reference/foundations/regex/)[label](/docs/reference/foundations/label/)[selector](/docs/reference/foundations/selector/)[location](/docs/reference/introspection/location/)[function](/docs/reference/foundations/function/)

) -> [selector](/docs/reference/foundations/selector/)

#### `others` [str](/docs/reference/foundations/str/) or [regex](/docs/reference/foundations/regex/) or [label](/docs/reference/foundations/label/) or [selector](/docs/reference/foundations/selector/) or [location](/docs/reference/introspection/location/) or [function](/docs/reference/foundations/function/) Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The other selectors to match on.

### `and`

Selects all elements that match this and all of the other selectors.

self.and(

[..](#definitions-and-others)[str](/docs/reference/foundations/str/)[regex](/docs/reference/foundations/regex/)[label](/docs/reference/foundations/label/)[selector](/docs/reference/foundations/selector/)[location](/docs/reference/introspection/location/)[function](/docs/reference/foundations/function/)

) -> [selector](/docs/reference/foundations/selector/)

#### `others` [str](/docs/reference/foundations/str/) or [regex](/docs/reference/foundations/regex/) or [label](/docs/reference/foundations/label/) or [selector](/docs/reference/foundations/selector/) or [location](/docs/reference/introspection/location/) or [function](/docs/reference/foundations/function/) Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The other selectors to match on.

### `before`

Returns a modified selector that will only match elements that occur
before the first match of `end`.

self.before(

[label](/docs/reference/foundations/label/)[selector](/docs/reference/foundations/selector/)[location](/docs/reference/introspection/location/)[function](/docs/reference/foundations/function/),[inclusive:](#definitions-before-inclusive) [bool](/docs/reference/foundations/bool/),

) -> [selector](/docs/reference/foundations/selector/)

#### `end` [label](/docs/reference/foundations/label/) or [selector](/docs/reference/foundations/selector/) or [location](/docs/reference/introspection/location/) or [function](/docs/reference/foundations/function/) Required Positional Question mark Positional parameters are specified in order, without names.

The original selection will end at the first match of `end`.

#### `inclusive` [bool](/docs/reference/foundations/bool/)

Whether `end` itself should match or not. This is only relevant if
both selectors match the same type of element. Defaults to `true`.

Default: `true`

### `after`

Returns a modified selector that will only match elements that occur
after the first match of `start`.

self.after(

[label](/docs/reference/foundations/label/)[selector](/docs/reference/foundations/selector/)[location](/docs/reference/introspection/location/)[function](/docs/reference/foundations/function/),[inclusive:](#definitions-after-inclusive) [bool](/docs/reference/foundations/bool/),

) -> [selector](/docs/reference/foundations/selector/)

#### `start` [label](/docs/reference/foundations/label/) or [selector](/docs/reference/foundations/selector/) or [location](/docs/reference/introspection/location/) or [function](/docs/reference/foundations/function/) Required Positional Question mark Positional parameters are specified in order, without names.

The original selection will start at the first match of `start`.

#### `inclusive` [bool](/docs/reference/foundations/bool/)

Whether `start` itself should match or not. This is only relevant
if both selectors match the same type of element. Defaults to
`true`.

Default: `true`

[![←](/assets/icons/16-chevron-right.svg)

RepresentationPrevious page](/docs/reference/foundations/repr/) [![→](/assets/icons/16-chevron-right.svg)

Standard LibraryNext page](/docs/reference/foundations/std/)