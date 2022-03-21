#!/usr/bin/env python3

import argparse
import hashlib
import os

def do_hash(input: str) -> str:
    return hashlib.sha256(input).hexdigest()

parser = argparse.ArgumentParser(description="Prints the SHA256 hashes for a list of files plus the SHA256 hash of all hashes")
parser.add_argument(
    'files',
    type=str,
    nargs='*',
    help="list of input files")
parser.add_argument(
    '--listfile',
    '-l',
    type=str,
    required=False,
    help="file that holds a input filename list, one filename per line")
args = parser.parse_args()

files = []
if args.listfile:
    f = open(args.listfile, "r")
    lines = f.readlines()
    for line in lines:
        files.append(line.rstrip())
else:
    files = args.files

hashes: str = ''

for file in files:
    fh = open(file, "rb")
    contents = fh.read()
    hash = do_hash(contents)
    hashes += hash
    print(hash, file)

print(do_hash(str(hashes).encode('utf-8')))

