#!/bin/bash
set -eu

function notfound {
  echo "content-type: text/plain"
  echo
  echo "not found"
  exit
}

if [[ -z "${PATH_INFO:-}" ]]; then
  # No file accessed
  notfound
fi

# Use conda environment
PATH="/data/users/bsherrat/envs/dataportal/bin:$PATH"

# Step up from bin directory to html root
cd ..

# Map URL to a physical path
: ${CONTEXT_PREFIX:=} ${CONTEXT_DOCUMENT_ROOT:=$PWD}
if [[ -n "$CONTEXT_PREFIX" ]]; then
  fname=${PATH_INFO/$CONTEXT_PREFIX/$CONTEXT_DOCUMENT_ROOT}
fi

[[ ! -f $fname ]] && notfound

# HTTP headers
echo "content-type: text/html"
echo

if [[ $fname = *.md ]]; then
  # Convert markdown to html via jinja template
  pandoc $fname -t html -s --template templates/pandoc.html | python bin/render_template.py
elif [[ $fname = *.ipynb ]]; then
  # Convert notebooks
  jupyter nbconvert --to html $fname --stdout --no-prompt
else
  # Convert jinja template to html
  python bin/render_template.py $fname
fi
