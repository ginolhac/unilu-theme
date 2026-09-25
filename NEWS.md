## Unreleased

- Added a `.grid-row` utility class: each child of the div is one grid cell, for comparison tables (e.g. task | base R | tidyverse | comment) without nested `.column` divs. Column widths are set with the `--grid-cols` custom property, defaulting to equal-width columns.


## Version 2.0.0

- Redesigned title slide: navy background with a white header stripe and the uni.lu logo, and a circular badge holding each deck's own logo to the left of the title.
- Title slide logo position/size are now fixed by the theme itself (`$title-logo-x/y/size` in `lectures.scss`); only `data-background-image` needs to be set per document — `data-background-position`/`data-background-size` in a doc's `title-slide-attributes` are ignored.
- Section/chapter slides show a white version of the logo on the dark background.
- Added spacing utilities for `.columns`/`.column` divs and a `.corner-img` helper class.
- Fixed a `resources:` omission in `_extension.yml` so `uni-logo-white.png` is bundled with the extension.

## Version 1.1.2

- grey background for code output


## Version 1.1.1

- lighter syntax highlighting

## Version 1.1.0

- `logo_url` in header to set the URL when logo is clicked (see [#3082](https://github.com/quarto-dev/quarto-cli/discussions/3082))

