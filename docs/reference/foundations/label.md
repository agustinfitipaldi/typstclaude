# label

Source: https://typst.app/docs/reference/foundations/label/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Foundations](/docs/reference/foundations/)
- ![](/assets/icons/16-chevron-right.svg)
- [Label](/docs/reference/foundations/label/)

# label

A label for an element.

Inserting a label into content attaches it to the closest preceding element
that is not a space. The preceding element must be in the same scope as the
label, which means that `Hello #[<label>]`, for instance, wouldn't work.

A labelled element can be [referenced](/docs/reference/model/ref/), [queried](/docs/reference/introspection/query/) for, and
[styled](/docs/reference/styling/) through its label.

Once constructed, you can get the name of a label using
[`str`](/docs/reference/foundations/str/#constructor).

## Example

```typst
#show <a>: set text(blue)
#show label("b"): set text(red)

= Heading <a>
*Strong* #label("b")
```

![Preview](/assets/docs/l3ZXI9iv-ZpcNuL82oagnwAAAAAAAAAA.png)

## Syntax

This function also has dedicated syntax: You can create a label by enclosing
its name in angle brackets. This works both in markup and code. A label's
name can contain letters, numbers, `_`, `-`, `:`, and `.`. A label cannot
be empty.

Note that there is a syntactical difference when using the dedicated syntax
for this function. In the code below, the `<a>` terminates the heading and
thus attaches to the heading itself, whereas the `#label("b")` is part of
the heading and thus attaches to the heading's text.

```
// Equivalent to `#heading[Introduction] <a>`.
= Introduction <a>

// Equivalent to `#heading[Conclusion #label("b")]`.
= Conclusion #label("b")
```

Currently, labels can only be attached to elements in markup mode, not in
code mode. This might change in the future.

## Constructor Question mark If a type has a constructor, you can call it like a function to create a new value of the type.

Creates a label from a string.

label(

[str](/docs/reference/foundations/str/)

) -> [label](/docs/reference/foundations/label/)

#### `name` [str](/docs/reference/foundations/str/) Required Positional Question mark Positional parameters are specified in order, without names.

The name of the label.

Unlike the [dedicated syntax](#syntax), this constructor accepts
any non-empty string, including names with special characters.

[![←](/assets/icons/16-chevron-right.svg)

IntegerPrevious page](/docs/reference/foundations/int/) [![→](/assets/icons/16-chevron-right.svg)

ModuleNext page](/docs/reference/foundations/module/)