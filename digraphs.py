#!/usr/bin/python3

import sys

ciphers = sys.stdin.read().splitlines()

def window(l, size):
    for i in range(len(l)-size):
        yield l[i:i+size]

group_size = 2
for c in ciphers:
    repeat_index = []
    for i, v in enumerate(c[:-1]):
        if v == c[i+1]:
            repeat_index.append(i)
    result = ""
    i = 0
    while i < len(c):
        if i in repeat_index:
            result += c[i:i+group_size]
            i += group_size
        else:
            result += " "
            i += 1
    print(result)
    print(c)
