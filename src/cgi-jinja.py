#!/data/users/bsherrat/envs/dataportal/bin/python

import sys
import os
import cgi

import jinja2

DEBUG = True

if os.environ.get("HTTP_HOST"):
    # Running as part of a CGI script, so we need an HTTP header
    print("content-type: text/html\n")

    if DEBUG:
        sys.stderr = sys.stdout

fname = os.environ.get("PATH_INFO", "")

if not fname.startswith(os.environ.get("CONTEXT_PREFIX", "")):
    # Should only happen when the CGI script is accessed directly
    cgi.print_environ()
    sys.exit()

# Translate into a proper filesystem path
fname = fname.replace(
    os.environ.get("CONTEXT_PREFIX"), os.environ.get("CONTEXT_DOCUMENT_ROOT"), 1
)

if not os.path.isfile(fname):
    print(fname, "not found")
    sys.exit()

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader("templates"), trim_blocks=True, lstrip_blocks=True,
)

with open(fname, "r") as file:
    template = env.from_string(file.read())

print(template.render())
