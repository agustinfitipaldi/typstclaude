# Search

Source: https://typst.app/docs/web-app/search/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Web App](/docs/web-app/)
- ![](/assets/icons/16-chevron-right.svg)
- [Search](/docs/web-app/search/)

# Search

Typst gives you the tools to search through the files in your project and find
exactly what you're looking for. You can search through the currently open file,
all files, or a subset of files, configure case sensitivity and word boundaries,
and use regular expressions.

## Searching in the current file

To search in the current file, press Ctrl/Cmd+F or select "Edit > Search and
replace" from the menu bar. A search panel opens at the bottom of the editor. As
you enter text in the textbox labelled "Find", Typst continually searches
through the file and highlights matches with a yellow background. If you press
Ctrl/Cmd+F while you have text selected, the search box will be prepopulated
with that text.

Repeatedly press Enter or F3 to cycle through all matches in the file. If you
hold shift while pressing Enter or F3, you will instead cycle backwards. You can
also use the ![Arrow down](/assets/icons/16-arrow-down.svg) Down and ![Arrow up](/assets/icons/16-arrow-up.svg) Up buttons
to navigate through the matches. With the ![Select all](/assets/icons/16-align-justify.svg) button, you can select all
matches in the editor.

![The search box for the current file. Searches for the word 'glacier' and next to it are buttons to jump to the previous and next match, select all matches, match case-sensitively, match whole words, and search with regular expressions. Below, the replacement text 'vulcano' and buttons to replace one or all matches.](/assets/images/search-current.png)

Next to the "Find" input, you'll find three buttons to further narrow down your
search:

- The ![Capitalization](/assets/icons/16-capitalization.svg) "Case
  sensitive" button determines whether matches must have the exact same
  capitalization as the search term or not.
- With the ![Whole word](/assets/icons/16-whole.svg)
  "Whole word" button, you can filter your matches to only include those
  that are a full word in the source text rather than e.g. part of a word.
- Last but not least is the ![Regex](/assets/icons/16-regex.svg) "Regex" button,
  which will enable search with regular expressions. Regular expressions are a
  powerful tool to find text that matches a pattern of your design. The regular
  expressions that are accepted by the search panel match those of JavaScript.
  Visit the [MDN article on regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions) to learn more about
  their syntax.

Below the "Find" input, there is a "Replace" input. Enter text and then press
![Replace one](/assets/icons/16-replace.svg) "Replace
one" or ![Replace all](/assets/icons/16-replace-all.svg) "Replace all" to replace the
current or all matches with what you've entered. When searching with regular
expressions, you can also use dollar replacement syntax (e.g. `$1`) to reuse
text matched by capture groups.

You can close the search box by clicking the ![Close](/assets/icons/16-close.svg) Close button or
pressing Escape.

## Searching in all files

As your project grows larger, you'll start splitting it up into multiple files.
When you're searching for something in your project, but aren't sure in which
file it is, or when you know that there will be matches across multiple files,
the search side panel comes in handy.

You can open the search panel by clicking the magnifying glass button in the
sidebar. Like the search box, the search panel will display two text inputs, one
to search and one to replace. You can also use the "Case sensitive", "Whole
word", and "Regex" options you already know from search in the current file.

When the search input is focused, you can start navigating through the matches
by pressing the down and up arrow keys. To jump to a specific match, click on it
or press Enter after selecting it with the arrow keys.

![The search panel for all files. Searches for the word 'glacier' and next to it are buttons to match case-sensitively, match whole words, search regular expressions, and filter which files to include. Below, the replacement text 'vulcano' and a button to replace all instances. Even below, the matches for all files and buttons to replace per file and per match.](/assets/images/search-all.png)

### Replacing across files

When replacing across files, you have multiple options. You can press the ![Replace all](/assets/icons/16-replace.svg) "Replace
all" button next to the replacement input to perform the replacement
everywhere at once. Make sure everything is correct before clicking this button
as the action is not reversible across all files at once. (You can still press
Ctrl/Cmd+Z in each file individually.)

Alternatively, you can replace all matches in a particular file (by clicking the
replacement button next to the file name) or just a single match (by clicking
the replacement button next to that match).

### File filtering

Sometimes, you may want to search in just part of your project. Typst's search
has built-in support for file filtering. Click the ![Folder](/assets/icons/16-folder.svg) Folder button to
reveal a third input field. You can use this input to filter in which files and
folders you want to search. The input accepts a *glob pattern.* A file path must
match this pattern for the file to be considered during search. Most letters in
a glob pattern are considered as-is and must match exactly. That said, there are
a few special characters:

- `?` matches an arbitrary character
- `*` matches an arbitrary part of a file or folder name, but only within one
  path segment, i.e. not across a `/`
- `**` matches an arbitrary subpath, i.e. a sequence of file and folder names
- `,` combines multiple globs
- `!` negates the following glob

Here are some examples of valid glob patterns:

- Search in one specific file: `path/to/my/file.typ`
- Search in any Typst file: `**/*.typ`
- Search in any file in a specific folder: `myfolder/**`
- Search in any CSV or JSON file in a data directory: `data/*.csv,data/*.json`
- Search in everything but SVGs: `**,!**/*.svg`. This is the default filter and
  will be applied if the file filtering input is hidden.

### Line numbers

By default, Typst will show a line number below each match. You can disable this
by navigating to the settings side panel and unchecking "Show line numbers in
search results".

[![←](/assets/icons/16-chevron-right.svg)

Invite by EmailPrevious page](/docs/web-app/invite-by-email/) [![→](/assets/icons/16-chevron-right.svg)

RoadmapNext page](/docs/roadmap/)