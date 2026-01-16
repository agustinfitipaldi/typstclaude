# Roots

Source: https://typst.app/docs/reference/math/roots/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Math](/docs/reference/math/)
- ![](/assets/icons/16-chevron-right.svg)
- [Roots](/docs/reference/math/roots/)

# Roots

Square and non-square roots.

## Example

```
$ sqrt(3 - 2 sqrt(2)) = sqrt(2) - 1 $
$ root(3, x) $
```

![Preview](/assets/docs/YJMQ-3S5QEsCnosYijnvKwAAAAAAAAAA.png)

## Functions

### `root`Element Question mark Element functions can be customized with `set` and `show` rules.

A general root.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ root(3, x) $
```

![Preview](/assets/docs/5dcBKGUow3rGrUB1Eg_gjwAAAAAAAAAA.png)

math.root(

[none](/docs/reference/foundations/none/)[content](/docs/reference/foundations/content/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `index` [none](/docs/reference/foundations/none/) or [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Which root of the radicand to take.

Default: `none`

#### `radicand` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The expression to take the root of.

### `sqrt`

A square root.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ sqrt(3 - 2 sqrt(2)) = sqrt(2) - 1 $
```

![Preview](/assets/docs/5thyKdLM1Lrfm53ILJWqaQAAAAAAAAAA.png)

math.sqrt(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `radicand` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The expression to take the square root of.

[![←](/assets/icons/16-chevron-right.svg)

PrimesPrevious page](/docs/reference/math/primes/) [![→](/assets/icons/16-chevron-right.svg)

SizesNext page](/docs/reference/math/sizes/)