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

## Performance

On my (slow) test machine, it took ~8 seconds to work through 10 x 100 megabyte of files. Interestingly standard `sha256sum` was not faster (but actually a bit slower).
```console
$ time sha256sum /tmp/100m*
2fc7c6ee108f91ff17d58e6c6a0c187bcb0926fadf355181b3fee569dc915890  /tmp/100m0.txt
59a43d3cf365e0049611650f6f22d0080715d679a026f7ed241563c6c49d9438  /tmp/100m1.txt
d69895692be7bface731ec9b6c57ecd2fba796c89633fa3970e550e432dfe965  /tmp/100m2.txt
19fab7404fe02168a9b2c06f639393c7fba67879a7165563826b79c906989fd9  /tmp/100m3.txt
032b27339420a836f0bd4047707f382b0c7266c124c3bc68134594657b7c616b  /tmp/100m4.txt
eaf31e2c548d08dd03e0261baa5be5cd526301abe933bb8fc9de7a5a275cd77c  /tmp/100m5.txt
826d3adcbb65ca4142e42ce7e0798ea188c422b78d9057a4fac36e6481998c35  /tmp/100m6.txt
c6024294dfee6678d782983b719499403e8b052f2ac3c1232e9d0f5ec58a09c3  /tmp/100m7.txt
cb9600b6dfe8b1cec7f6b98312fdb841d9dfea49b8de257cbb1a8d7568d546dc  /tmp/100m8.txt
e2247336944139a4c7aed87a1caffa8a2c5514eb0dac2c03425e088cf0e71de4  /tmp/100m9.txt

real    0m10.229s
user    0m6.552s
sys     0m0.739s

$ time ./bill.py /tmp/100m*
2fc7c6ee108f91ff17d58e6c6a0c187bcb0926fadf355181b3fee569dc915890 /tmp/100m0.txt
59a43d3cf365e0049611650f6f22d0080715d679a026f7ed241563c6c49d9438 /tmp/100m1.txt
d69895692be7bface731ec9b6c57ecd2fba796c89633fa3970e550e432dfe965 /tmp/100m2.txt
19fab7404fe02168a9b2c06f639393c7fba67879a7165563826b79c906989fd9 /tmp/100m3.txt
032b27339420a836f0bd4047707f382b0c7266c124c3bc68134594657b7c616b /tmp/100m4.txt
eaf31e2c548d08dd03e0261baa5be5cd526301abe933bb8fc9de7a5a275cd77c /tmp/100m5.txt
826d3adcbb65ca4142e42ce7e0798ea188c422b78d9057a4fac36e6481998c35 /tmp/100m6.txt
c6024294dfee6678d782983b719499403e8b052f2ac3c1232e9d0f5ec58a09c3 /tmp/100m7.txt
cb9600b6dfe8b1cec7f6b98312fdb841d9dfea49b8de257cbb1a8d7568d546dc /tmp/100m8.txt
e2247336944139a4c7aed87a1caffa8a2c5514eb0dac2c03425e088cf0e71de4 /tmp/100m9.txt
c60550d1ce601d72a31ba55ae1fd5e8a806962140bcf2db30c669e1147f869bd

real    0m8.126s
user    0m3.212s
sys     0m2.013s
```
