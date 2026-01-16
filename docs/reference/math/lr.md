# Left/Right

Source: https://typst.app/docs/reference/math/lr/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Math](/docs/reference/math/)
- ![](/assets/icons/16-chevron-right.svg)
- [Left/Right](/docs/reference/math/lr/)

# Left/Right

Delimiter matching.

The `lr` function allows you to match two delimiters and scale them with the
content they contain. While this also happens automatically for delimiters
that match syntactically, `lr` allows you to match two arbitrary delimiters
and control their size exactly. Apart from the `lr` function, Typst provides
a few more functions that create delimiter pairings for absolute, ceiled,
and floored values as well as norms.

To prevent a delimiter from being matched by Typst, and thus auto-scaled,
escape it with a backslash. To instead disable auto-scaling completely, use
`set math.lr(size: 1em)`.

## Example

```typst
$ [a, b/2] $
$ lr(]sum_(x=1)^n], size: #50%) x $
$ abs((x + y) / 2) $
$ \{ (x / y) \} $
#set math.lr(size: 1em)
$ { (a / b), a, b in (0; 1/2] } $
```

![Preview](/assets/docs/YzMDJzGPE42UQFlEMJiLuwAAAAAAAAAA.png)

## Functions

### `lr`Element Question mark Element functions can be customized with `set` and `show` rules.

Scales delimiters.

While matched delimiters scale by default, this can be used to scale
unmatched delimiters and to control the delimiter scaling more precisely.

math.lr(

[size:](#functions-lr-size) [relative](/docs/reference/layout/relative/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `size` [relative](/docs/reference/layout/relative/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The size of the brackets, relative to the height of the wrapped content.

Default: `100% + 0pt`

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The delimited content, including the delimiters.

### `mid`Element Question mark Element functions can be customized with `set` and `show` rules.

Scales delimiters vertically to the nearest surrounding `lr()` group.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ { x mid(|) sum_(i=1)^n w_i|f_i (x)| < 1 } $
```

![Preview](/assets/docs/op-SkIh83R9BuQA_mC41YAAAAAAAAAAA.png)

math.mid(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to be scaled.

### `abs`

Takes the absolute value of an expression.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ abs(x/2) $
```

![Preview](/assets/docs/WJLuRK0YgTAAKX7q_RtueAAAAAAAAAAA.png)

math.abs(

[size:](#functions-abs-size) [relative](/docs/reference/layout/relative/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `size` [relative](/docs/reference/layout/relative/)

The size of the brackets, relative to the height of the wrapped content.

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The expression to take the absolute value of.

### `norm`

Takes the norm of an expression.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ norm(x/2) $
```

![Preview](/assets/docs/YC6RjZ5CBxOUd9-0Ud9TzQAAAAAAAAAA.png)

math.norm(

[size:](#functions-norm-size) [relative](/docs/reference/layout/relative/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `size` [relative](/docs/reference/layout/relative/)

The size of the brackets, relative to the height of the wrapped content.

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The expression to take the norm of.

### `floor`

Floors an expression.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ floor(x/2) $
```

![Preview](/assets/docs/PDEHlUdVGIVhIYs9pZubiAAAAAAAAAAA.png)

math.floor(

[size:](#functions-floor-size) [relative](/docs/reference/layout/relative/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `size` [relative](/docs/reference/layout/relative/)

The size of the brackets, relative to the height of the wrapped content.

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The expression to floor.

### `ceil`

Ceils an expression.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ ceil(x/2) $
```

![Preview](/assets/docs/8M0cDo0mVWiDmMeZvIBqOAAAAAAAAAAA.png)

math.ceil(

[size:](#functions-ceil-size) [relative](/docs/reference/layout/relative/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `size` [relative](/docs/reference/layout/relative/)

The size of the brackets, relative to the height of the wrapped content.

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The expression to ceil.

### `round`

Rounds an expression.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ round(x/2) $
```

![Preview](/assets/docs/tF8zASmAKWpzYdWTOE8zPAAAAAAAAAAA.png)

math.round(

[size:](#functions-round-size) [relative](/docs/reference/layout/relative/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `size` [relative](/docs/reference/layout/relative/)

The size of the brackets, relative to the height of the wrapped content.

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The expression to round.

[![←](/assets/icons/16-chevron-right.svg)

FractionPrevious page](/docs/reference/math/frac/) [![→](/assets/icons/16-chevron-right.svg)

MatrixNext page](/docs/reference/math/mat/)