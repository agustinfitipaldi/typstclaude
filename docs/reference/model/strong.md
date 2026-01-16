# strongElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/model/strong/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Model](/docs/reference/model/)
- ![](/assets/icons/16-chevron-right.svg)
- [Strong Emphasis](/docs/reference/model/strong/)

# `strong`Element Question mark Element functions can be customized with `set` and `show` rules.

Strongly emphasizes content by increasing the font weight.

Increases the current font weight by a given `delta`.

## Example

```typst
This is *strong.* \
This is #strong[too.] \

#show strong: set text(red)
And this is *evermore.*
```

![Preview](/assets/docs/8PFV4SUNXNbbYe9uHW1ITAAAAAAAAAAA.png)

## Syntax

This function also has dedicated syntax: To strongly emphasize content,
simply enclose it in stars/asterisks (`*`). Note that this only works at
word boundaries. To strongly emphasize part of a word, you have to use the
function.

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

strong(

[delta:](#parameters-delta) [int](/docs/reference/foundations/int/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `delta` [int](/docs/reference/foundations/int/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The delta to apply on the font weight.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set strong(delta: 0)
No *effect!*
```

![Preview](/assets/docs/SC7LmnRUxtrvxQL331fpfAAAAAAAAAAA.png)

Default: `300`

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The content to strongly emphasize.

[![←](/assets/icons/16-chevron-right.svg)

ReferencePrevious page](/docs/reference/model/ref/) [![→](/assets/icons/16-chevron-right.svg)

TableNext page](/docs/reference/model/table/)