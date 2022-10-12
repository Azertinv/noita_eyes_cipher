#!/usr/bin/python3

import sys

ciphers = sys.stdin.readlines()

for c in ciphers:
    isomorph_indexs = []
    for i, v in enumerate(c):
        second = c.find(v, i+1)
        if second != -1 and second - i < 9:
            isomorph_indexs.append(i)
            isomorph_indexs.append(second)
    for i, v in enumerate(c):
        if i in isomorph_indexs:
            print(v, end="")
        else:
            print(" ", end="")
    print()
    print(c)
