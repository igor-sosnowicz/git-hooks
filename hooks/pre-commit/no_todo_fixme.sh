#!/bin/bash

# Search for TODO or FIXME in .py and .cpp files
if grep -r --include="*.py" --include="*.cpp" "TODO\|FIXME" .; then
    echo "You have TODO or FIXME in your code. Please fix them before committing."
    exit 1
fi

exit 0
