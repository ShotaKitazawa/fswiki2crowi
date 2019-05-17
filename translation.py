#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import glob

from src import utils

if __name__ == '__main__':
    if (len(sys.argv) <= 2):
        print("invalid argument:", sys.argv[0], "(input path)", "(output path)")
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    if not (os.path.exists(input_path)):
        print(input_path + ": folder dont exists.")
        sys.exit(1)
    if (os.path.exists(output_path)):
        check = input(output_path + ": folder already exists. overwrite? [y/n]: ")
        if (check.lower() != "y"):
            sys.exit(1)
    else:
        os.mkdir(output_path)

    input_files = glob.glob("./" + input_path + "/*")
    for input_file in input_files:
        rfile_array = utils.euc2utf8_file(input_file)
        output_file = utils.euc2utf8(output_path + "/" + os.path.basename(input_file)).rsplit(".wiki", 1)[0] + ".md"
        with open(output_file, "w", encoding="utf-8") as wfile:
            for line in rfile_array:
                wfile.write(utils.fs2md(line))
                # wfile.write(line)
