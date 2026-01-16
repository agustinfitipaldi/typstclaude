# arguments

Source: https://typst.app/docs/reference/foundations/arguments/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Foundations](/docs/reference/foundations/)
- ![](/assets/icons/16-chevron-right.svg)
- [Arguments](/docs/reference/foundations/arguments/)

# arguments

Captured arguments to a function.

## Argument Sinks

Like built-in functions, custom functions can also take a variable number of
arguments. You can specify an *argument sink* which collects all excess
arguments as `..sink`. The resulting `sink` value is of the `arguments`
type. It exposes methods to access the positional and named arguments.

```typst
#let format(title, ..authors) = {
  let by = authors
    .pos()
    .join(", ", last: " and ")

  [*#title* \ _Written by #by;_]
}

#format("ArtosFlow", "Jane", "Joe")
```

![Preview](/assets/docs/DWzn69gGuCd1q_LVZvjEEgAAAAAAAAAA.png)

## Spreading

Inversely to an argument sink, you can *spread* arguments, arrays and
dictionaries into a function call with the `..spread` operator:

```typst
#let array = (2, 3, 5)
#calc.min(..array)
#let dict = (fill: blue)
#text(..dict)[Hello]
```

![Preview](/assets/docs/kcmqtH9qxq6Bg8ZwwKnMCQAAAAAAAAAA.png)

## Constructor Question mark If a type has a constructor, you can call it like a function to create a new value of the type.

Construct spreadable arguments in place.

This function behaves like `let args(..sink) = sink`.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#let args = arguments(stroke: red, inset: 1em, [Body])
#box(..args)
```

![Preview](/assets/docs/JbzK099-rqq0pkW-oHCQsgAAAAAAAAAA.png)

arguments(

[..](#constructor-arguments)any

) -> [arguments](/docs/reference/foundations/arguments/)

#### `arguments` any Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The arguments to construct.

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `at`

Returns the positional argument at the specified index, or the named
argument with the specified name.

If the key is an [integer](/docs/reference/foundations/int/), this is equivalent to first calling
[`pos`](/docs/reference/foundations/arguments/#definitions-pos) and then [`array.at`](/docs/reference/foundations/array/#definitions-at "`array.at`"). If it is a [string](/docs/reference/foundations/str/),
this is equivalent to first calling [`named`](/docs/reference/foundations/arguments/#definitions-named) and then
[`dictionary.at`](/docs/reference/foundations/dictionary/#definitions-at "`dictionary.at`").

self.at(

[int](/docs/reference/foundations/int/)[str](/docs/reference/foundations/str/),[default:](#definitions-at-default) any,

) -> any

#### `key` [int](/docs/reference/foundations/int/) or [str](/docs/reference/foundations/str/) Required Positional Question mark Positional parameters are specified in order, without names.

The index or name of the argument to get.

#### `default` any

A default value to return if the key is invalid.

### `pos`

Returns the captured positional arguments as an array.

self.pos() -> [array](/docs/reference/foundations/array/)

### `named`

Returns the captured named arguments as a dictionary.

self.named() -> [dictionary](/docs/reference/foundations/dictionary/)

[![←](/assets/icons/16-chevron-right.svg)

FoundationsPrevious page](/docs/reference/foundations/) [![→](/assets/icons/16-chevron-right.svg)

ArrayNext page](/docs/reference/foundations/array/)