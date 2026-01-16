# type

Source: https://typst.app/docs/reference/foundations/type/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Foundations](/docs/reference/foundations/)
- ![](/assets/icons/16-chevron-right.svg)
- [Type](/docs/reference/foundations/type/)

# type

Describes a kind of value.

To style your document, you need to work with values of different kinds:
Lengths specifying the size of your elements, colors for your text and
shapes, and more. Typst categorizes these into clearly defined *types* and
tells you where it expects which type of value.

Apart from basic types for numeric values and [typical](/docs/reference/foundations/int/)
[types](/docs/reference/foundations/float/) [known](/docs/reference/foundations/str/) [from](/docs/reference/foundations/array/) [programming](/docs/reference/foundations/dictionary/)
languages, Typst provides a special type for [*content.*](/docs/reference/foundations/content/) A value
of this type can hold anything that you can enter into your document: Text,
elements like headings and shapes, and style information.

## Example

```typst
#let x = 10
#if type(x) == int [
  #x is an integer!
] else [
  #x is another value...
]

An image is of type
#type(image("glacier.jpg")).
```

![Preview](/assets/docs/dTjHaEMO5150e0-XVg1OzwAAAAAAAAAA.png)

The type of `10` is `int`. Now, what is the type of `int` or even `type`?

```typst
#type(int) \
#type(type)
```

![Preview](/assets/docs/HqIgZy_wqBbnboRlZ-Iv4AAAAAAAAAAA.png)

Unlike other types like `int`, [none](/docs/reference/foundations/none/ "none") and [auto](/docs/reference/foundations/auto/ "auto") do not have a name
representing them. To test if a value is one of these, compare your value to
them directly, e.g:

```typst
#let val = none
#if val == none [
  Yep, it's none.
]
```

![Preview](/assets/docs/n-ZLDWMH52qhM-X09GjUlAAAAAAAAAAA.png)

Note that `type` will return [`content`](/docs/reference/foundations/content/ "`content`") for all document elements. To
programmatically determine which kind of content you are dealing with, see
[`content.func`](/docs/reference/foundations/content/#definitions-func "`content.func`").

## Constructor Question mark If a type has a constructor, you can call it like a function to create a new value of the type.

Determines a value's type.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#type(12) \
#type(14.7) \
#type("hello") \
#type(<glacier>) \
#type([Hi]) \
#type(x => x + 1) \
#type(type)
```

![Preview](/assets/docs/A7_wGHgPK0Jhrp3CDC6IegAAAAAAAAAA.png)

type(

any

) -> [type](/docs/reference/foundations/type/)

#### `value` any Required Positional Question mark Positional parameters are specified in order, without names.

The value whose type's to determine.

[![←](/assets/icons/16-chevron-right.svg)

TargetPrevious page](/docs/reference/foundations/target/) [![→](/assets/icons/16-chevron-right.svg)

VersionNext page](/docs/reference/foundations/version/)