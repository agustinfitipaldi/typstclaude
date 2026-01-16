# Data Loading

Source: https://typst.app/docs/reference/data-loading/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Data Loading](/docs/reference/data-loading/)

# Data Loading

Data loading from external files.

These functions help you with loading and embedding data, for example from the
results of an experiment.

## Encoding

Some of the functions are also capable of encoding, e.g. [`cbor.encode`](/docs/reference/data-loading/cbor/#definitions-encode "`cbor.encode`"). They
facilitate passing structured data to [plugins](/docs/reference/foundations/plugin/).

However, each data format has its own native types. Therefore, for an arbitrary
Typst value, the encode-to-decode roundtrip might be lossy. In general, numbers,
strings, and [arrays](/docs/reference/foundations/array/) or [dictionaries](/docs/reference/foundations/dictionary/) composed of them
can be reliably converted, while other types may fall back to strings via [`repr`](/docs/reference/foundations/repr/ "`repr`"),
which is [for debugging purposes only](/docs/reference/foundations/repr/#debugging-only). Please refer to
the page of each data format for details.

## Definitions

- [`cbor`](/docs/reference/data-loading/cbor/)  Reads structured data from a CBOR file.
- [`csv`](/docs/reference/data-loading/csv/)  Reads structured data from a CSV file.
- [`json`](/docs/reference/data-loading/json/)  Reads structured data from a JSON file.
- [`read`](/docs/reference/data-loading/read/)  Reads plain text or data from a file.
- [`toml`](/docs/reference/data-loading/toml/)  Reads structured data from a TOML file.
- [`xml`](/docs/reference/data-loading/xml/)  Reads structured data from an XML file.
- [`yaml`](/docs/reference/data-loading/yaml/)  Reads structured data from a YAML file.

[![←](/assets/icons/16-chevron-right.svg)

StatePrevious page](/docs/reference/introspection/state/) [![→](/assets/icons/16-chevron-right.svg)

CBORNext page](/docs/reference/data-loading/cbor/)