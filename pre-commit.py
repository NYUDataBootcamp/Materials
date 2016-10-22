#!/usr/bin/env python

import os
import json
import fnmatch


def strip_output_cell(fn):
    with open(fn, "r") as f:
        js = json.load(f)
        for cell in js["cells"]:
            if cell["cell_type"] == "code":
                cell["outputs"] = []
                cell["execution_count"] = None

    with open(fn, "w") as f:
        json.dump(js, f)

for dirpath, dirnames, files in os.walk("../../"):
    if not "/." in dirpath:
        for f in fnmatch.filter(files, "*.ipynb"):
            strip_output_cell(os.path.join(dirpath, f))
