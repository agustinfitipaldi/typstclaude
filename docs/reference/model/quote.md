# quoteElement  Question mark   
Element functions can be customized with set and show rules.

Source: https://typst.app/docs/reference/model/quote/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Model](/docs/reference/model/)
- ![](/assets/icons/16-chevron-right.svg)
- [Quote](/docs/reference/model/quote/)

# `quote`Element Question mark Element functions can be customized with `set` and `show` rules.

Displays a quote alongside an optional attribution.

## Example

```typst
Plato is often misquoted as the author of #quote[I know that I know
nothing], however, this is a derivation form his original quote:

#set quote(block: true)

#quote(attribution: [Plato])[
  ... ἔοικα γοῦν τούτου γε σμικρῷ τινι αὐτῷ τούτῳ σοφώτερος εἶναι, ὅτι
  ἃ μὴ οἶδα οὐδὲ οἴομαι εἰδέναι.
]
#quote(attribution: [from the Henry Cary literal translation of 1897])[
  ... I seem, then, in just this little thing to be wiser than this man at
  any rate, that what I do not know I do not think I know either.
]
```

![Preview](/assets/docs/SJpe1zkhE_liZRMF5cAy4gAAAAAAAAAA.png)

By default block quotes are padded left and right by `1em`, alignment and
padding can be controlled with show rules:

```typst
#set quote(block: true)
#show quote: set align(center)
#show quote: set pad(x: 5em)

#quote[
  You cannot pass... I am a servant of the Secret Fire, wielder of the
  flame of Anor. You cannot pass. The dark fire will not avail you,
  flame of Udûn. Go back to the Shadow! You cannot pass.
]
```

![Preview](/assets/docs/QLNv4Pfp0zBKSvwxIfby-wAAAAAAAAAA.png)

## Parameters Question mark Parameters are the inputs to a function. They are specified in parentheses after the function name.

quote(

[block:](#parameters-block) [bool](/docs/reference/foundations/bool/),[quotes:](#parameters-quotes) [auto](/docs/reference/foundations/auto/)[bool](/docs/reference/foundations/bool/),[attribution:](#parameters-attribution) [none](/docs/reference/foundations/none/)[label](/docs/reference/foundations/label/)[content](/docs/reference/foundations/content/),[content](/docs/reference/foundations/content/),

) -> [content](/docs/reference/foundations/content/)

### `block` [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether this is a block quote.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
An inline citation would look like
this: #quote(
  attribution: [René Descartes]
)[
  cogito, ergo sum
], and a block equation like this:
#quote(
  block: true,
  attribution: [JFK]
)[
  Ich bin ein Berliner.
]
```

![Preview](/assets/docs/bYLjzIuUOzRO9HYX7xT11wAAAAAAAAAA.png)

Default: `false`

### `quotes` [auto](/docs/reference/foundations/auto/) or [bool](/docs/reference/foundations/bool/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

Whether double quotes should be added around this quote.

The double quotes used are inferred from the `quotes` property on
[smartquote](/docs/reference/text/smartquote/ "smartquote"), which is affected by the `lang` property on [text](/docs/reference/text/text/ "text").

- `true`: Wrap this quote in double quotes.
- `false`: Do not wrap this quote in double quotes.
- `auto`: Infer whether to wrap this quote in double quotes based on
  the `block` property. If `block` is `false`, double quotes are
  automatically added.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#set text(lang: "de")

Ein deutsch-sprechender Author
zitiert unter umständen JFK:
#quote[Ich bin ein Berliner.]

#set text(lang: "en")

And an english speaking one may
translate the quote:
#quote[I am a Berliner.]
```

![Preview](/assets/docs/3Qsm4wm5qgO3MH7h3rFICAAAAAAAAAAA.png)

Default: `auto`

### `attribution` [none](/docs/reference/foundations/none/) or [label](/docs/reference/foundations/label/) or [content](/docs/reference/foundations/content/) Settable Question mark Settable parameters can be customized for all following uses of the function with a `set` rule.

The attribution of this quote, usually the author or source. Can be a
label pointing to a bibliography entry or any content. By default only
displayed for block quotes, but can be changed using a `show` rule.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#quote(attribution: [René Descartes])[
  cogito, ergo sum
]

#show quote.where(block: false): it => {
  ["] + h(0pt, weak: true) + it.body + h(0pt, weak: true) + ["]
  if it.attribution != none [ (#it.attribution)]
}

#quote(
  attribution: link("https://typst.app/home")[typst.app]
)[
  Compose papers faster
]

#set quote(block: true)

#quote(attribution: <tolkien54>)[
  You cannot pass... I am a servant
  of the Secret Fire, wielder of the
  flame of Anor. You cannot pass. The
  dark fire will not avail you, flame
  of Udûn. Go back to the Shadow! You
  cannot pass.
]

#bibliography("works.bib", style: "apa")
```

![Preview](/assets/docs/b7Rj4jn7nBz6a3iK73MpbQAAAAAAAAAA.png)

Default: `none`

### `body` [content](/docs/reference/foundations/content/) Required Positional Question mark Positional parameters are specified in order, without names.

The quote.

[![←](/assets/icons/16-chevron-right.svg)

Paragraph BreakPrevious page](/docs/reference/model/parbreak/) [![→](/assets/icons/16-chevron-right.svg)

ReferenceNext page](/docs/reference/model/ref/)