# datetime

Source: https://typst.app/docs/reference/foundations/datetime/

---

- [![Docs](/assets/icons/16-docs-dark.svg)](/docs)
- ![](/assets/icons/16-chevron-right.svg)
- [Reference](/docs/reference/)
- ![](/assets/icons/16-chevron-right.svg)
- [Foundations](/docs/reference/foundations/)
- ![](/assets/icons/16-chevron-right.svg)
- [Datetime](/docs/reference/foundations/datetime/)

# datetime

Represents a date, a time, or a combination of both.

Can be created by either specifying a custom datetime using this type's
constructor function or getting the current date with [`datetime.today`](/docs/reference/foundations/datetime/#definitions-today "`datetime.today`").

## Example

```typst
#let date = datetime(
  year: 2020,
  month: 10,
  day: 4,
)

#date.display() \
#date.display(
  "y:[year repr:last_two]"
)

#let time = datetime(
  hour: 18,
  minute: 2,
  second: 23,
)

#time.display() \
#time.display(
  "h:[hour repr:12][period]"
)
```

![Preview](/assets/docs/aJRkqg11vpsxBq0NzqAo0gAAAAAAAAAA.png)

## Datetime and Duration

You can get a [duration](/docs/reference/foundations/duration/ "duration") by subtracting two datetime:

```typst
#let first-of-march = datetime(day: 1, month: 3, year: 2024)
#let first-of-jan = datetime(day: 1, month: 1, year: 2024)
#let distance = first-of-march - first-of-jan
#distance.hours()
```

![Preview](/assets/docs/xJIPnvV5Iiw8osdkiAUb_AAAAAAAAAAA.png)

You can also add/subtract a datetime and a duration to retrieve a new,
offset datetime:

```typst
#let date = datetime(day: 1, month: 3, year: 2024)
#let two-days = duration(days: 2)
#let two-days-earlier = date - two-days
#let two-days-later = date + two-days

#date.display() \
#two-days-earlier.display() \
#two-days-later.display()
```

![Preview](/assets/docs/R-BPj6xQMFasAxM1n3h_iwAAAAAAAAAA.png)

## Format

You can specify a customized formatting using the
[`display`](/docs/reference/foundations/datetime/#definitions-display) method. The format of a datetime is
specified by providing *components* with a specified number of *modifiers*.
A component represents a certain part of the datetime that you want to
display, and with the help of modifiers you can define how you want to
display that component. In order to display a component, you wrap the name
of the component in square brackets (e.g. `[year]` will display the year).
In order to add modifiers, you add a space after the component name followed
by the name of the modifier, a colon and the value of the modifier (e.g.
`[month repr:short]` will display the short representation of the month).

The possible combination of components and their respective modifiers is as
follows:

- `year`: Displays the year of the datetime.
  - `padding`: Can be either `zero`, `space` or `none`. Specifies how the
    year is padded.
  - `repr` Can be either `full` in which case the full year is displayed or
    `last_two` in which case only the last two digits are displayed.
  - `sign`: Can be either `automatic` or `mandatory`. Specifies when the
    sign should be displayed.
- `month`: Displays the month of the datetime.
  - `padding`: Can be either `zero`, `space` or `none`. Specifies how the
    month is padded.
  - `repr`: Can be either `numerical`, `long` or `short`. Specifies if the
    month should be displayed as a number or a word. Unfortunately, when
    choosing the word representation, it can currently only display the
    English version. In the future, it is planned to support localization.
- `day`: Displays the day of the datetime.
  - `padding`: Can be either `zero`, `space` or `none`. Specifies how the
    day is padded.
- `week_number`: Displays the week number of the datetime.
  - `padding`: Can be either `zero`, `space` or `none`. Specifies how the
    week number is padded.
  - `repr`: Can be either `ISO`, `sunday` or `monday`. In the case of `ISO`,
    week numbers are between 1 and 53, while the other ones are between 0
    and 53.
- `weekday`: Displays the weekday of the date.
  - `repr` Can be either `long`, `short`, `sunday` or `monday`. In the case
    of `long` and `short`, the corresponding English name will be displayed
    (same as for the month, other languages are currently not supported). In
    the case of `sunday` and `monday`, the numerical value will be displayed
    (assuming Sunday and Monday as the first day of the week, respectively).
  - `one_indexed`: Can be either `true` or `false`. Defines whether the
    numerical representation of the week starts with 0 or 1.
- `hour`: Displays the hour of the date.
  - `padding`: Can be either `zero`, `space` or `none`. Specifies how the
    hour is padded.
  - `repr`: Can be either `24` or `12`. Changes whether the hour is
    displayed in the 24-hour or 12-hour format.
- `period`: The AM/PM part of the hour
  - `case`: Can be `lower` to display it in lower case and `upper` to
    display it in upper case.
- `minute`: Displays the minute of the date.
  - `padding`: Can be either `zero`, `space` or `none`. Specifies how the
    minute is padded.
- `second`: Displays the second of the date.
  - `padding`: Can be either `zero`, `space` or `none`. Specifies how the
    second is padded.

Keep in mind that not always all components can be used. For example, if you
create a new datetime with `datetime(year: 2023, month: 10, day: 13)`, it
will be stored as a plain date internally, meaning that you cannot use
components such as `hour` or `minute`, which would only work on datetimes
that have a specified time.

## Constructor Question mark If a type has a constructor, you can call it like a function to create a new value of the type.

Creates a new datetime.

You can specify the [datetime](/docs/reference/foundations/datetime/ "datetime") using a year, month, day, hour, minute,
and second.

*Note*: Depending on which components of the datetime you specify, Typst
will store it in one of the following three ways:

- If you specify year, month and day, Typst will store just a date.
- If you specify hour, minute and second, Typst will store just a time.
- If you specify all of year, month, day, hour, minute and second, Typst
  will store a full datetime.

Depending on how it is stored, the [`display`](/docs/reference/foundations/datetime/#definitions-display) method
will choose a different formatting by default.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
#datetime(
  year: 2012,
  month: 8,
  day: 3,
).display()
```

![Preview](/assets/docs/6mpnNRypNysjXvXstSouiwAAAAAAAAAA.png)

datetime(

[year:](#constructor-year) [int](/docs/reference/foundations/int/),[month:](#constructor-month) [int](/docs/reference/foundations/int/),[day:](#constructor-day) [int](/docs/reference/foundations/int/),[hour:](#constructor-hour) [int](/docs/reference/foundations/int/),[minute:](#constructor-minute) [int](/docs/reference/foundations/int/),[second:](#constructor-second) [int](/docs/reference/foundations/int/),

) -> [datetime](/docs/reference/foundations/datetime/)

#### `year` [int](/docs/reference/foundations/int/)

The year of the datetime.

#### `month` [int](/docs/reference/foundations/int/)

The month of the datetime.

#### `day` [int](/docs/reference/foundations/int/)

The day of the datetime.

#### `hour` [int](/docs/reference/foundations/int/)

The hour of the datetime.

#### `minute` [int](/docs/reference/foundations/int/)

The minute of the datetime.

#### `second` [int](/docs/reference/foundations/int/)

The second of the datetime.

## Definitions Question mark Functions and types can have associated definitions. These are accessed by specifying the function or type, followed by a period, and then the definition's name.

### `today`

Returns the current date.

In the CLI, this can be overridden with the `--creation-timestamp`
argument or by setting the
[`SOURCE_DATE_EPOCH`](https://reproducible-builds.org/specs/source-date-epoch/)
environment variable. In both cases, the value should be given as a UNIX
timestamp.

  ![](/assets/icons/16-chevron-right.svg) View example 

```typst
Today's date is
#datetime.today().display().
```

![Preview](/assets/docs/SOSDKByfy_YbHbk7NejgOQAAAAAAAAAA.png)

datetime.today(

[offset:](#definitions-today-offset) [auto](/docs/reference/foundations/auto/)[int](/docs/reference/foundations/int/)

) -> [datetime](/docs/reference/foundations/datetime/)

#### `offset` [auto](/docs/reference/foundations/auto/) or [int](/docs/reference/foundations/int/)

An offset to apply to the current UTC date. If set to `auto`, the
offset will be the local offset.

Default: `auto`

### `display`

Displays the datetime in a specified format.

Depending on whether you have defined just a date, a time or both, the
default format will be different. If you specified a date, it will be
`[year]-[month]-[day]`. If you specified a time, it will be
`[hour]:[minute]:[second]`. In the case of a datetime, it will be
`[year]-[month]-[day] [hour]:[minute]:[second]`.

See the [format syntax](/docs/reference/foundations/datetime/#format) for more information.

self.display(

[auto](/docs/reference/foundations/auto/)[str](/docs/reference/foundations/str/)

) -> [str](/docs/reference/foundations/str/)

#### `pattern` [auto](/docs/reference/foundations/auto/) or [str](/docs/reference/foundations/str/) Positional Question mark Positional parameters are specified in order, without names.

The format used to display the datetime.

Default: `auto`

### `year`

The year if it was specified, or `none` for times without a date.

self.year() -> [none](/docs/reference/foundations/none/)[int](/docs/reference/foundations/int/)

### `month`

The month if it was specified, or `none` for times without a date.

self.month() -> [none](/docs/reference/foundations/none/)[int](/docs/reference/foundations/int/)

### `weekday`

The weekday (counting Monday as 1) or `none` for times without a date.

self.weekday() -> [none](/docs/reference/foundations/none/)[int](/docs/reference/foundations/int/)

### `day`

The day if it was specified, or `none` for times without a date.

self.day() -> [none](/docs/reference/foundations/none/)[int](/docs/reference/foundations/int/)

### `hour`

The hour if it was specified, or `none` for dates without a time.

self.hour() -> [none](/docs/reference/foundations/none/)[int](/docs/reference/foundations/int/)

### `minute`

The minute if it was specified, or `none` for dates without a time.

self.minute() -> [none](/docs/reference/foundations/none/)[int](/docs/reference/foundations/int/)

### `second`

The second if it was specified, or `none` for dates without a time.

self.second() -> [none](/docs/reference/foundations/none/)[int](/docs/reference/foundations/int/)

### `ordinal`

The ordinal (day of the year), or `none` for times without a date.

self.ordinal() -> [none](/docs/reference/foundations/none/)[int](/docs/reference/foundations/int/)

[![←](/assets/icons/16-chevron-right.svg)

ContentPrevious page](/docs/reference/foundations/content/) [![→](/assets/icons/16-chevron-right.svg)

DecimalNext page](/docs/reference/foundations/decimal/)