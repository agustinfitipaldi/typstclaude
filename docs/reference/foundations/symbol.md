# symbol

Source: https://typst.app/docs/reference/foundations/symbol/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Foundations](/docs/reference/foundations/)
- ![](/assets/icons/16-chevron-right.svg)
- [Symbol](/docs/reference/foundations/symbol/)

# symbol

A Unicode symbol.

Typst defines common symbols so that they can easily be written with
standard keyboards. The symbols are defined in modules, from which they can
be accessed using [field access notation](/docs/reference/scripting/#fields):

- General symbols are defined in the [`sym` module](/docs/reference/symbols/sym/)
  and are accessible without the `sym.` prefix in math mode.
- Emoji are defined in the [`emoji` module](/docs/reference/symbols/emoji/)

Moreover, you can define custom symbols with this type's constructor
function.

```typst
#sym.arrow.r \
#sym.gt.eq.not \
$gt.eq.not$ \
#emoji.face.halo
```

![Preview](/assets/docs/VU7JCTNOvXZ0YxOKfFCHhgAAAAAAAAAA.png)

Many symbols have different variants, which can be selected by appending the
modifiers with dot notation. The order of the modifiers is not relevant.
Visit the documentation pages of the symbol modules and click on a symbol to
see its available variants.

```
$arrow.l$ \
$arrow.r$ \
$arrow.t.quad$
```

![Preview](/assets/docs/6bpO4zHphIuAdD1km_qbDAAAAAAAAAAA.png)

## Constructor Question mark If a type has a constructor, you can call it like a function to create a new value of the type.

Create a custom symbol with modifiers.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#let envelope = symbol(
  "🖂",
  ("stamped", "🖃"),
  ("stamped.pen", "🖆"),
  ("lightning", "🖄"),
  ("fly", "🖅"),
)

#envelope
#envelope.stamped
#envelope.stamped.pen
#envelope.lightning
#envelope.fly
```

![Preview](/assets/docs/KbY7ot9pSdzC8G6YXvE_VAAAAAAAAAAA.png)

symbol(

[..](#constructor-variants)[str](/docs/reference/foundations/str/)[array](/docs/reference/foundations/array/)

) -> [symbol](/docs/reference/foundations/symbol/)

#### `variants` [str](/docs/reference/foundations/str/) or [array](/docs/reference/foundations/array/) Required Positional Question mark Positional parameters are specified in order, without names. Variadic Question mark Variadic parameters can be specified multiple times.

The variants of the symbol.

Can be a just a string consisting of a single character for the
modifierless variant or an array with two strings specifying the modifiers
and the symbol. Individual modifiers should be separated by dots. When
displaying a symbol, Typst selects the first from the variants that have
all attached modifiers and the minimum number of other modifiers.

[![←](/assets/icons/16-chevron-right.svg)

StringPrevious page](/docs/reference/foundations/str/) [![→](/assets/icons/16-chevron-right.svg)

SystemNext page](/docs/reference/foundations/sys/)