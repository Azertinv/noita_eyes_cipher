#!/usr/bin/python3

import sys

ciphers = sys.stdin.read().splitlines()

ciphertext_field_size = 83
plaintext_field_size = 41

values = []
for i in range(max([len(x) for x in ciphers])):
    values.append([])
for c in ciphers:
    for i, v in enumerate(c):
        values[i].append(ord(v) - 32)

holes = []
for index in values:
    index.sort()
    index_holes = []
    for i in range(len(index) - 1):
        index_holes.append((index[i+1] - index[i]) % ciphertext_field_size)
    holes.append(index_holes)

bounded = True
for i, index in enumerate(holes):
    if len(index) == 0:
        break
    index.remove(max(index))
    if sum(index) > plaintext_field_size:
        # print("unbounded:", i)
        bounded = False

if bounded:
    print("bounded, outer ring isn't scrambled")
else:
    print("unbounded, outer ring is scrambled")
