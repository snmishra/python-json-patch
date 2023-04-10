#!/usr/bin/env python


import argparse
import json
import sys

import jsonpatch

parser = argparse.ArgumentParser(description="Diff two JSON files")
parser.add_argument("FILE1", type=argparse.FileType("r"))
parser.add_argument("FILE2", type=argparse.FileType("r"))
parser.add_argument(
    "--indent", type=int, default=None, help="Indent output by n spaces"
)
parser.add_argument(
    "-v", "--version", action="version", version="%(prog)s " + jsonpatch.__version__
)


def main():
    try:
        diff_files()
    except KeyboardInterrupt:
        sys.exit(1)


def diff_files():
    """Diffs two JSON files and prints a patch"""
    args = parser.parse_args()
    doc1 = json.load(args.FILE1)
    doc2 = json.load(args.FILE2)
    patch = jsonpatch.make_patch(doc1, doc2)
    if patch.patch:
        print(json.dumps(patch.patch, indent=args.indent))
        sys.exit(1)


if __name__ == "__main__":
    main()