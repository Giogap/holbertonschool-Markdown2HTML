#!/usr/bin/python3
""" Script markdown2html.py """

import re
import hashlib
import sys
import os

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, 'r') as f:
        text = f.read()
except FileNotFoundError:
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)


sys.exit(0)
