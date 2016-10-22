#!/usr/bin/env python

import os
import json
import fnmatch
import subprocess


def strip_output_cell(fn):
    changed = False
    with open(fn, "r") as f:
        js = json.load(f)
        for cell in js["cells"]:
            if cell["cell_type"] == "code":
                if len(cell["outputs"]) != 0:
                    cell["outputs"] = []
                    changed = True

                if cell["execution_count"] is not None:
                    cell["execution_count"] = None
                    changed = True

    if changed:
        with open(fn, "w") as f:
            json.dump(js, f)

repo_root = os.popen("git rev-parse --show-toplevel").read().strip()
for dirpath, dirnames, files in os.walk(repo_root):
    if not "/." in dirpath:
        for f in fnmatch.filter(files, "*.ipynb"):
            fn = os.path.join(dirpath, f)
            strip_output_cell(fn)
            subprocess.call(["git", "add", fn])
