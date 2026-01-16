# System

Source: https://typst.app/docs/reference/foundations/sys/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Foundations](/docs/reference/foundations/)
- ![](/assets/icons/16-chevron-right.svg)
- [System](/docs/reference/foundations/sys/)

# System

Module for system interactions.

This module defines the following items:

- The `sys.version` constant (of type [`version`](/docs/reference/foundations/version/ "`version`")) that specifies
  the currently active Typst compiler version.
- The `sys.inputs` [dictionary](/docs/reference/foundations/dictionary/ "dictionary"), which makes external inputs
  available to the project. An input specified in the command line as
  `--input key=value` becomes available under `sys.inputs.key` as
  `"value"`. To include spaces in the value, it may be enclosed with
  single or double quotes.

  The value is always of type [string](/docs/reference/foundations/str/). More complex data
  may be parsed manually using functions like [`json`](/docs/reference/data-loading/json/).

[![←](/assets/icons/16-chevron-right.svg)

SymbolPrevious page](/docs/reference/foundations/symbol/) [![→](/assets/icons/16-chevron-right.svg)

TargetNext page](/docs/reference/foundations/target/)