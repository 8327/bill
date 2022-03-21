# bill

Simple python script that prints the SHA256 hash for each file in the input list plus the SHA256 hash over all prior hashes.

## Example 

```console
$ ./bill.py /tmp/1m.txt /tmp/2m.txt /tmp/3m.txt /tmp/4m.txt
070c82d3d87e8841088e07633ad58dabed49926a46ca481ec17453542397a939 /tmp/1m.txt
7d8c00354210828c6740782fe3bab21c4bb8408b754d8b2ad81690098590f1bf /tmp/2m.txt
686f8d3b87eee781e04a62a00c7ab2e3990ef608c0b8744240dd0dc17946f25e /tmp/3m.txt
de9b4a5b462603cb21d809dc26a8cc87ee0dbff49dae002f9bc773dbb8c16dd6 /tmp/4m.txt
7f0f8cba7716c74ebcb4e441436ba463fa18fa6ada83b94e26689daa83be5c20
```

Changes in the files in the input list can then be 'detected' using diff:
```console
diff -u <(tail -n 1 bill-output-now.txt) <(tail -n 1 bill-output-then.txt)
```
