#!/usr/bin/env python3

'''
mpy_cross_all.py
Vendored from MicroPython to make compiling KMK more feasible on Windows.
https://raw.githubusercontent.com/micropython/micropython/master/tools/mpy_cross_all.py

-----------------------------------------------------------------------------
The MIT License (MIT)

Copyright (c) 2013-2022 Damien P. George

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

--------------------------------------------------------------------------------
'''

import argparse
import os
import os.path

argparser = argparse.ArgumentParser(
    description="Compile all .py files to .mpy recursively"
)
argparser.add_argument("-o", "--out", help="output directory (default: input dir)")
argparser.add_argument("--target", help="select MicroPython target config")
argparser.add_argument("dir", help="input directory")
args = argparser.parse_args()

TARGET_OPTS = {
    "unix": "",
    "baremetal": "",
}

args.dir = args.dir.rstrip("/")

if not args.out:
    args.out = args.dir

path_prefix_len = len(args.dir) + 1

for path, subdirs, files in os.walk(args.dir):
    for f in files:
        if f.endswith(".py"):
            fpath = path + "/" + f
            # print(fpath)
            out_fpath = args.out + "/" + fpath[path_prefix_len:-3] + ".mpy"
            out_dir = os.path.dirname(out_fpath)
            if not os.path.isdir(out_dir):
                os.makedirs(out_dir)
            cmd = "mpy-cross -v -v %s -s %s %s -o %s" % (
                TARGET_OPTS.get(args.target, ""),
                fpath[path_prefix_len:],
                fpath,
                out_fpath,
            )
            # print(cmd)
            res = os.system(cmd)
            assert res == 0
