# Quarto reveal.js uni.lu template


![Build](https://github.com/rolandkrause/unilu-theme/actions/workflows/publish.yml/badge.svg)

A [Quarto](https://quarto.org) extension for authoring [r-training](https://gitlab.lcsb.uni.lu/r-training) Reveal.js presentations at [University of Luxembourg](https://wwwen.uni.lu/)

## Installation

- To start a new presentation in a new folder:

``` bash
quarto use template rolandkrause/unilu-theme
```

- To install the theme in an existing folder:

``` bash
quarto install extension rolandkrause/unilu-theme
```

## Title slide logo

Each deck's own logo sits in a circular badge to the left of the title. Set only `data-background-image` in `title-slide-attributes`:

``` yaml
title-slide-attributes:
  data-background-image: https://tidyverse.tidyverse.org/logo.png
```

Position and size are fixed by the theme itself (`$title-logo-x`/`$title-logo-y`/`$title-logo-size` in `lectures.scss`), so a per-document `data-background-position` or `data-background-size` has no effect.

## Linked logo

Following discussion on [quarto-cli](https://github.com/quarto-dev/quarto-cli/discussions/3082#discussioncomment-7058099), logo on each slide can point to the desired URL.

Set it in the YAML header with `logo_url: "https://fasterthanli.me"`

If not set, it points to https://quarto.org


## Output

![template preview](template.png)

Preview this [Quarto reveal.js theme](https://rolandkrause.github.io/unilu-theme) on `gh-pages`.

## Acknowledgements

-   [Romain Lesur](https://github.com/RLesur) for the [onyxia-quarto template](https://github.com/InseeFrLab/onyxia-quarto) 
-   [Mickaël Canouil](https://github.com/mcanouil/) for maintaining the [awesome Quarto](https://github.com/mcanouil/awesome-quarto)
-   [Emi Tanaka](https://github.com/emitanaka) for her [syntax-highlthing CSS](https://github.com/emitanaka/talks/blob/master/Ihaka2022/assets/syntax-highlight.css)

## License

MIT License
