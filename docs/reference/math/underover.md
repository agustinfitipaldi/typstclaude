# Under/Over

Source: https://typst.app/docs/reference/math/underover/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Math](/docs/reference/math/)
- ![](/assets/icons/16-chevron-right.svg)
- [Under/Over](/docs/reference/math/underover/)

# Under/Over

Delimiters above or below parts of an equation.

The braces and brackets further allow you to add an optional annotation
below or above themselves.

## Functions

### `underline`Element Question mark Element functions can be customized with `set` and `show` rules.

A horizontal line under content.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ underline(1 + 2 + ... + 5) $
```

![Preview](/assets/docs/kPv2rkuOYqE5xrS9gynyqwAAAAAAAAAA.png)

math.underline(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content above the line.

### `overline`Element Question mark Element functions can be customized with `set` and `show` rules.

A horizontal line over content.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ overline(1 + 2 + ... + 5) $
```

![Preview](/assets/docs/brbtze6pYcbdDHZXqYtX4QAAAAAAAAAA.png)

math.overline(

[content](/docs/reference/foundations/content/)

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content below the line.

### `underbrace`Element Question mark Element functions can be customized with `set` and `show` rules.

A horizontal brace under content, with an optional annotation below.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ underbrace(0 + 1 + dots.c + n, n + 1 "numbers") $
```

![Preview](/assets/docs/zl1VYCw-onHF-Ug3V7hjSAAAAAAAAAAA.png)

math.underbrace(

[content](/docs/reference/foundations/content/),[none](/docs/reference/foundations/none/)[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content above the brace.

#### `annotation` [none](/docs/reference/foundations/none/) or [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The optional content below the brace.

Default: `none`

### `overbrace`Element Question mark Element functions can be customized with `set` and `show` rules.

A horizontal brace over content, with an optional annotation above.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ overbrace(0 + 1 + dots.c + n, n + 1 "numbers") $
```

![Preview](/assets/docs/QXOfUqCiAGNy7coUIoblWgAAAAAAAAAA.png)

math.overbrace(

[content](/docs/reference/foundations/content/),[none](/docs/reference/foundations/none/)[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content below the brace.

#### `annotation` [none](/docs/reference/foundations/none/) or [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The optional content above the brace.

Default: `none`

### `underbracket`Element Question mark Element functions can be customized with `set` and `show` rules.

A horizontal bracket under content, with an optional annotation below.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ underbracket(0 + 1 + dots.c + n, n + 1 "numbers") $
```

![Preview](/assets/docs/yEc16DvCdXuZmjrYcFaXOwAAAAAAAAAA.png)

math.underbracket(

[content](/docs/reference/foundations/content/),[none](/docs/reference/foundations/none/)[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content above the bracket.

#### `annotation` [none](/docs/reference/foundations/none/) or [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The optional content below the bracket.

Default: `none`

### `overbracket`Element Question mark Element functions can be customized with `set` and `show` rules.

A horizontal bracket over content, with an optional annotation above.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ overbracket(0 + 1 + dots.c + n, n + 1 "numbers") $
```

![Preview](/assets/docs/qVz-RyPwAWSA71NXMaWtJQAAAAAAAAAA.png)

math.overbracket(

[content](/docs/reference/foundations/content/),[none](/docs/reference/foundations/none/)[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content below the bracket.

#### `annotation` [none](/docs/reference/foundations/none/) or [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The optional content above the bracket.

Default: `none`

### `underparen`Element Question mark Element functions can be customized with `set` and `show` rules.

A horizontal parenthesis under content, with an optional annotation below.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ underparen(0 + 1 + dots.c + n, n + 1 "numbers") $
```

![Preview](/assets/docs/TxHXlDEDPngSMIqzkzKJEgAAAAAAAAAA.png)

math.underparen(

[content](/docs/reference/foundations/content/),[none](/docs/reference/foundations/none/)[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content above the parenthesis.

#### `annotation` [none](/docs/reference/foundations/none/) or [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The optional content below the parenthesis.

Default: `none`

### `overparen`Element Question mark Element functions can be customized with `set` and `show` rules.

A horizontal parenthesis over content, with an optional annotation above.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ overparen(0 + 1 + dots.c + n, n + 1 "numbers") $
```

![Preview](/assets/docs/n3BEuMIowb9ooJDrct-vagAAAAAAAAAA.png)

math.overparen(

[content](/docs/reference/foundations/content/),[none](/docs/reference/foundations/none/)[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content below the parenthesis.

#### `annotation` [none](/docs/reference/foundations/none/) or [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The optional content above the parenthesis.

Default: `none`

### `undershell`Element Question mark Element functions can be customized with `set` and `show` rules.

A horizontal tortoise shell bracket under content, with an optional
annotation below.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ undershell(0 + 1 + dots.c + n, n + 1 "numbers") $
```

![Preview](/assets/docs/9EADiqZIpP3kBbATjQxK9gAAAAAAAAAA.png)

math.undershell(

[content](/docs/reference/foundations/content/),[none](/docs/reference/foundations/none/)[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content above the tortoise shell bracket.

#### `annotation` [none](/docs/reference/foundations/none/) or [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The optional content below the tortoise shell bracket.

Default: `none`

### `overshell`Element Question mark Element functions can be customized with `set` and `show` rules.

A horizontal tortoise shell bracket over content, with an optional
annotation above.

  ![](/assets/icons/16-chevron-right.svg) View example 

```
$ overshell(0 + 1 + dots.c + n, n + 1 "numbers") $
```

![Preview](/assets/docs/E1XSg6qpufqXrpj7eKwGVwAAAAAAAAAA.png)

math.overshell(

[content](/docs/reference/foundations/content/),[none](/docs/reference/foundations/none/)[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

#### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content below the tortoise shell bracket.

#### `annotation` [none](/docs/reference/foundations/none/) or [content](/docs/reference/foundations/content/) Positional Question mark Positional parameters are specified in order, without names. Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The optional content above the tortoise shell bracket.

Default: `none`

[![←](/assets/icons/16-chevron-right.svg)

Text OperatorPrevious page](/docs/reference/math/op/) [![→](/assets/icons/16-chevron-right.svg)

VariantsNext page](/docs/reference/math/variants/)