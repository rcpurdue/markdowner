#!/usr/bin/python
"""Remove blank lines & headers from .md files."""

import os
import sys

for fname in os.listdir(sys.argv[1]):

    if fname.endswith('.md'):
        fpath = os.path.join(sys.argv[1], fname)

        with open(fpath, 'r', encoding='utf-8') as fobj:

            for line in fobj:
                tokens = line.strip().split()

                # Filter leading whitespace, blank lines, & header lines
                if tokens and not tokens[0][0] == '#':
                    print(' '.join(tokens))
