#!/bin/bash

# Build the site.
#
# In fact, all the actual compilation happens at request-time by CGI
# scripts, this merely copies everything to a given directory.
#
# TODO: consider how best to customise the conda location and URL base

set -eu

# Handle arguments
if [[ $# -eq 0 ]]; then
  echo "usage: $(basename $0) HTMLDIR" >&2
  exit 1
fi
htmldir="${1%/}"

# Get directory of the script
root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Ensure target directory exists and is empty
if [[ -e "$htmldir" ]]; then
  echo "deleting $htmldir"
  rm -rf "$htmldir"
fi
echo "creating $htmldir"
mkdir -p "$htmldir"

# Copy all relevant files
cp -r assets "$htmldir"
cp -r templates "$htmldir"
cp -r content/.htaccess "$htmldir"
cp -r content/* "$htmldir"
cp -r src/cgi* "$htmldir"
