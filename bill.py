#!/usr/bin/env python3

# prints the sha256 hashes for a list of files (per file) plus the sha256 hash
# of all hashes

import os
import hashlib

files = ['/tmp/1m.txt', '/tmp/2m.txt', '/tmp/3m.txt', '/tmp/4m.txt',
         '/tmp/5m.txt', '/tmp/6m.txt']
hashes = ''

for file in files:
    size = os.path.getsize(file)
    f = open(file, "rb")
    bytes = f.read()
    hash = hashlib.sha256(bytes).hexdigest()
    hashes += hash
    print(hash, file)

hash_hash = hashlib.sha256(str(hashes).encode('utf-8')).hexdigest()
print(hash_hash)

