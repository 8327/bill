# bill

Simple python script that prints the SHA256 hash for each file in the input list plus the SHA256 hash over all prior hashes.

## Example 
(Input list hardcoded in bill.py)

```console
070c82d3d87e8841088e07633ad58dabed49926a46ca481ec17453542397a939 /tmp/1m.txt
7d8c00354210828c6740782fe3bab21c4bb8408b754d8b2ad81690098590f1bf /tmp/2m.txt
686f8d3b87eee781e04a62a00c7ab2e3990ef608c0b8744240dd0dc17946f25e /tmp/3m.txt
de9b4a5b462603cb21d809dc26a8cc87ee0dbff49dae002f9bc773dbb8c16dd6 /tmp/4m.txt
270173bc31ac22a22a08feca1f20bf35b1b991ecbbd4e958e74d8c3ba1b6d9ab /tmp/5m.txt
e4ca6c1cf5be7a08eb9e5cc7b268f56f235bc58fafb1383fa4273d47422f0727 /tmp/6m.txt
38ab174789ddb553151e176cde4e6d65d8a31171dc6e2bb167ac12b066a62169
```

Changes in the files in the input list can then be 'detected' using diff:
```console
diff -u <(tail -n 1 bill-output-now.txt) <(tail -n 1 bill-output-then.txt)
```
## Todo:
- [ ] File list via command line flags (either file with file list or file list in flag)
- [ ] Why is this better then the standard sha256sum Linux command? (didn't knew a day ago that this existed;-)
- [ ] Installer
