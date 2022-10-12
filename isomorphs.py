#!/usr/bin/python3

import sys

ciphers = sys.stdin.readlines()

isomorph_count = {}

for c in ciphers:
    isomorph_indexs = []
    for i, v in enumerate(c):
        second = c.find(v, i+1)
        if second != -1 and second - i < 18:
            diff = second - i - 1
            if diff in isomorph_count:
                isomorph_count[diff] += 1
            else:
                isomorph_count[diff] = 1
            isomorph_indexs.append(i)
            isomorph_indexs.append(second)
    for i, v in enumerate(c):
        if i in isomorph_indexs:
            print(v, end="")
        else:
            print(" ", end="")
    print()
    print(c)

isomorph_count = {k: v for k, v in sorted(isomorph_count.items(), key=lambda item: item[0])}
print(isomorph_count)
for i in range(1, 18):
    if i in isomorph_count:
        print(isomorph_count[i])
    else:
        print(0)
