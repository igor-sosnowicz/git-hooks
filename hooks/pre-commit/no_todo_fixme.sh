#!/bin/bash

# Define the patterns to search for
PATTERNS='TODO\|FIXME\|HACK\|NOTE\|WIP'

# Check for the presence of any of the defined patterns in staged files
if git grep --cached -q -E "$PATTERNS"; then
    echo 'Your commit contains TODO, FIXME, HACK, NOTE, or WIP comments. Resolve them before committing.'
    exit 1
fi

exit 0
