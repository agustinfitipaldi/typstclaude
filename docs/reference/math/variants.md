# Variants

Source: https://typst.app/docs/reference/math/variants/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Math](/docs/reference/math/)
- ![](/assets/icons/16-chevron-right.svg)
- [Variants](/docs/reference/math/variants/)

# Variants

Alternate typefaces within formulas.

These functions are distinct from the [`text`](/docs/reference/text/text/ "`text`") function because math fonts
contain multiple variants of each letter.

## Functions

### `serif`

Serif (roman) font style in math.

This is already the default.

math.serif(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to style.

### `sans`

Sans-serif font style in math.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ sans(A B C) $
```

![Preview](/assets/docs/QH7JeXflCs-wCjP8nkBWrQAAAAAAAAAA.png)

math.sans(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to style.

### `frak`

Fraktur font style in math.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ frak(P) $
```

![Preview](/assets/docs/e8XkJAdgWXZDqbWs94GeeQAAAAAAAAAA.png)

math.frak(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to style.

### `mono`

Monospace font style in math.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ mono(x + y = z) $
```

![Preview](/assets/docs/VdkE7dQPvzJTe7BxDZHcnwAAAAAAAAAA.png)

math.mono(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to style.

### `bb`

Blackboard bold (double-struck) font style in math.

For uppercase latin letters, blackboard bold is additionally available
through [symbols](/docs/reference/symbols/sym/) of the form `NN` and `RR`.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ bb(b) $
$ bb(N) = NN $
$ f: NN -> RR $
```

![Preview](/assets/docs/7qs4sC1Ha0vO_Ei_dnjHuQAAAAAAAAAA.png)

math.bb(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to style.

### `cal`

Calligraphic (chancery) font style in math.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
Let $cal(P)$ be the set of ...
```

![Preview](/assets/docs/kqxr3_NhGcBq3QZhkIfIjwAAAAAAAAAA.png)

This is the default calligraphic/script style for most math fonts. See
[`scr`](/docs/reference/math/variants/#functions-scr) for more on how to get the other style (roundhand).

math.cal(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to style.

### `scr`

Script (roundhand) font style in math.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$scr(L)$ is not the set of linear
maps $cal(L)$.
```

![Preview](/assets/docs/_wgGRiUY_HVPSfuugEOreQAAAAAAAAAA.png)

There are two ways that fonts can support differentiating `cal` and `scr`.
The first is using Unicode variation sequences. This works out of the box
in Typst, however only a few math fonts currently support this.

The other way is using [font features](/docs/reference/text/text/#parameters-features). For example, the
roundhand style might be available in a font through the
*[stylistic set](/docs/reference/text/text/#parameters-stylistic-set) 1* (`ss01`) feature. To use it in
Typst, you could then define your own version of `scr` like in the example
below.

  ![](/assets/icons/16-chevron-right.svg) View example: Recreation using stylistic set 1 

```typst
#let scr(it) = text(
  stylistic-set: 1,
  $cal(it)$,
)

We establish $cal(P) != scr(P)$.
```

![Preview](/assets/docs/7yK1cKVZZwIMi9iLmfaMFgAAAAAAAAAA.png)

math.scr(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to style.

[![←](/assets/icons/16-chevron-right.svg)

Under/OverPrevious page](/docs/reference/math/underover/) [![→](/assets/icons/16-chevron-right.svg)

VectorNext page](/docs/reference/math/vec/)