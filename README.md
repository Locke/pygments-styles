# pygments\_styles\_locke

## About

This repository contains Styles for [Pygments](https://github.com/pygments/pygments).

The `default-locke` Style is based on the `default` Style and changes:

- Number to blue
- Operator to black
- Name.Function.Magic bold

## Requirements

- Python setuptools
  - on Debian: `sudo apt-get install python3-setuptools`

- pygments
  - on Debian: `sudo apt-get install python3-pygments`
  - alternative: `sudo easy_install Pygments`


## Setup

One-Shot installation via: `sudo python3 setup.py install` (copies the files).

Development installation via: `sudo python3 setup.py develop` (links to the files). Uninstall with `sudo python3 setup.py develop --uninstall`.


## Usage with minted

- install the minted package in your latex distribution
  - on Debian: `sudo apt-get install texlive-latex-extra`

Example usage:

```LaTeX
\usepackage{minted}

\usemintedstyle{default-locke}
```

shell escape must be enabled (unless you use the draft mode), e.g. via `pdflatex -shell-escape`.
