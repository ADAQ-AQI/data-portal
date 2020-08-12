#!/bin/bash
set -eu

: ${PATH_INFO:=} ${CONTEXT_PREFIX:=} ${CONTEXT_DOCUMENT_ROOT:=}

# Use conda environment
PATH="/data/users/bsherrat/envs/dataportal/bin:$PATH"

if [[ -n $PATH_INFO ]]; then
  # Accessed a file

  # Map URL to a physical path
  if [[ -n $CONTEXT_PREFIX ]]; then
    fname=${PATH_INFO/$CONTEXT_PREFIX/$CONTEXT_DOCUMENT_ROOT}
  fi

  # HTTP headers
  echo "content-type: text/html"
  echo

  # Convert markdown to html
  pandoc $fname -t html -s --template templates/pandoc.html
else
  # Script (probably) accessed directly - show some debugging info
  echo "content-type: text/plain"
  echo
  env | sort
fi
