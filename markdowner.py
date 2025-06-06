#!/usr/bin/python
"""Remove header lines & minimize whitespace from markdown files."""

from pathlib import Path

EXT = '*.md'
DIR = '.'
HDR = '#'

for path in Path(DIR).rglob(EXT):

    with open(path) as file:  # pylint: disable=unspecified-encoding

        for line in file:  # NOTE Could be dir!
            tokens = line.strip().split()

            if tokens and not tokens[0][0] == HDR:
                print(' '.join(tokens))
