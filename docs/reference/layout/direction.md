# direction

Source: https://typst.app/docs/reference/layout/direction/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Layout](/docs/reference/layout/)
- ![](/assets/icons/16-chevron-right.svg)
- [Direction](/docs/reference/layout/direction/)

# direction

The four directions into which content can be laid out.

Possible values are:

- `ltr`: Left to right.
- `rtl`: Right to left.
- `ttb`: Top to bottom.
- `btt`: Bottom to top.

These values are available globally and
also in the direction type's scope, so you can write either of the following
two:

```typst
#stack(dir: rtl)[A][B][C]
#stack(dir: direction.rtl)[A][B][C]
```

![Preview](/assets/docs/43rZPR36KLZcf8RLRLjX0wAAAAAAAAAA.png)

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `from`

Returns a direction from a starting point.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#direction.from(left) \
#direction.from(right) \
#direction.from(top) \
#direction.from(bottom)
```

![Preview](/assets/docs/NFWxMzCXgtaXng-dvhxGQgAAAAAAAAAA.png)

direction.from(

[alignment](/docs/reference/layout/alignment/)

) -> [direction](/docs/reference/layout/direction/)

#### `side` [alignment](/docs/reference/layout/alignment/) Required Positional Question mark Positional parameters are specified in order, without names.

### `to`

Returns a direction from an end point.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#direction.to(left) \
#direction.to(right) \
#direction.to(top) \
#direction.to(bottom)
```

![Preview](/assets/docs/3M0AhMqQCfBN9USjsZC6ggAAAAAAAAAA.png)

direction.to(

[alignment](/docs/reference/layout/alignment/)

) -> [direction](/docs/reference/layout/direction/)

#### `side` [alignment](/docs/reference/layout/alignment/) Required Positional Question mark Positional parameters are specified in order, without names.

### `axis`

The axis this direction belongs to, either `"horizontal"` or
`"vertical"`.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#ltr.axis() \
#ttb.axis()
```

![Preview](/assets/docs/JrNsSPuIGz5d-HyvpKlmRAAAAAAAAAAA.png)

self.axis() -> [str](/docs/reference/foundations/str/)

### `sign`

The corresponding sign, for use in calculations.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#ltr.sign() \
#rtl.sign() \
#ttb.sign() \
#btt.sign()
```

![Preview](/assets/docs/-WlTxVRdpeQIufltqmV6qwAAAAAAAAAA.png)

self.sign() -> [int](/docs/reference/foundations/int/)

### `start`

The start point of this direction, as an alignment.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#ltr.start() \
#rtl.start() \
#ttb.start() \
#btt.start()
```

![Preview](/assets/docs/N9RQCkuykNN4FsJgRg06GgAAAAAAAAAA.png)

self.start() -> [alignment](/docs/reference/layout/alignment/)

### `end`

The end point of this direction, as an alignment.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#ltr.end() \
#rtl.end() \
#ttb.end() \
#btt.end()
```

![Preview](/assets/docs/NDjcpeKFmKqoCGermlx1dAAAAAAAAAAA.png)

self.end() -> [alignment](/docs/reference/layout/alignment/)

### `inv`

The inverse direction.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#ltr.inv() \
#rtl.inv() \
#ttb.inv() \
#btt.inv()
```

![Preview](/assets/docs/kBDvCk2AJ9dPd5ZUJjxcOgAAAAAAAAAA.png)

self.inv() -> [direction](/docs/reference/layout/direction/)

[![←](/assets/icons/16-chevron-right.svg)

ColumnsPrevious page](/docs/reference/layout/columns/) [![→](/assets/icons/16-chevron-right.svg)

FractionNext page](/docs/reference/layout/fraction/)