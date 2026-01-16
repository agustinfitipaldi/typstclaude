# version

Source: https://typst.app/docs/reference/foundations/version/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Foundations](/docs/reference/foundations/)
- ![](/assets/icons/16-chevron-right.svg)
- [Version](/docs/reference/foundations/version/)

# version

A version with an arbitrary number of components.

The first three components have names that can be used as fields: `major`,
`minor`, `patch`. All following components do not have names.

The list of components is semantically extended by an infinite list of
zeros. This means that, for example, `0.8` is the same as `0.8.0`. As a
special case, the empty version (that has no components at all) is the same
as `0`, `0.0`, `0.0.0`, and so on.

The current version of the Typst compiler is available as `sys.version`.

You can convert a version to an array of explicitly given components using
the [`array`](/docs/reference/foundations/array/ "`array`") constructor.

## Constructor Question mark If a type has a constructor, you can call it like a function to create a new value of the type.

Creates a new version.

It can have any number of components (even zero).

  ![](/assets/icons/16-chevron-right.svg) View example: Constructing versions 

```typst
#version() \
#version(1) \
#version(1, 2, 3, 4) \
#version((1, 2, 3, 4)) \
#version((1, 2), 3)
```

![Preview](/assets/docs/Fx1_6ds8kbJ35Werk0qIqQAAAAAAAAAA.png)

As a practical use case, this allows comparing the current version
([`sys.version`](/docs/reference/foundations/version/)) to a specific one.

  ![](/assets/icons/16-chevron-right.svg) View example: Comparing with the current version 

```typst
Current version: #sys.version \
#(sys.version >= version(0, 14, 0)) \
#(version(3, 2, 0) > version(4, 1, 0))
```

![Preview](/assets/docs/mr2u5taEIulcnVx2r9fNzwAAAAAAAAAA.png)

version(

[..](#constructor-components)[int](/docs/reference/foundations/int/)[array](/docs/reference/foundations/array/)

) -> [version](/docs/reference/foundations/version/)

#### `components` [int](/docs/reference/foundations/int/) or [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The components of the version (array arguments are flattened)

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `at`

Retrieves a component of a version.

The returned integer is always non-negative. Returns `0` if the version
isn't specified to the necessary length.

self.at(

[int](/docs/reference/foundations/int/)

) -> [int](/docs/reference/foundations/int/)

#### `index` [int](/docs/reference/foundations/int/) Required Positional Question mark Positional parameters are specified in order, without names.

The index at which to retrieve the component. If negative, indexes
from the back of the explicitly given components.

[![←](/assets/icons/16-chevron-right.svg)

TypePrevious page](/docs/reference/foundations/type/) [![→](/assets/icons/16-chevron-right.svg)

ModelNext page](/docs/reference/model/)