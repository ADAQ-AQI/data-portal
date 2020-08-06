import sys
import os
import argparse

import jinja2


def convert(files, templates, outdir=None):
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(templates),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    for fname in files:
        # Read
        if fname == "-":
            content = sys.stdin.read()
        elif os.path.isfile(fname):
            with open(fname, "r") as file:
                content = file.read()
        else:
            print(f"file '{fname}' not found", file=sys.stderr)

        # Interpret as a jinja template
        template = env.from_string(content)

        # Write result
        if outdir is None or fname == "-":
            print(template.render())
        else:
            fname_out = os.path.join(outdir, os.path.basename(fname))
            with open(fname_out, "w") as file:
                print(template.render(), file=file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "files",
        nargs="*",
        default=["-"],
        metavar="file",
        help="files to process",
    )
    parser.add_argument(
        "-t", "--templates", default="templates", help="template directory"
    )
    parser.add_argument("-o", "--outdir", help="output directory")

    args = parser.parse_args()

    convert(**vars(args))
