#!/usr/bin/env python3

# prints the sha256 hashes for a list of files (per file) plus the sha256 hash
# of all hashes

import os
import hashlib

def do_hash(input: str) -> str:
    return hashlib.sha256(input).hexdigest()

files = ['/tmp/1m.txt', '/tmp/2m.txt', '/tmp/3m.txt', '/tmp/4m.txt',
         '/tmp/5m.txt', '/tmp/6m.txt']

hashes: str = ''

for file in files:
    fh = open(file, "rb")
    contents = fh.read()
    hash = do_hash(contents)
    hashes += hash
    print(hash, file)

print(do_hash(str(hashes).encode('utf-8')))

