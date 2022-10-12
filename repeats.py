#!/usr/bin/python3

import sys

ciphers = sys.stdin.readlines()

def window(l, size):
    for i in range(len(l)-size):
        yield l[i:i+size]

group_size = 2
total_repeats = 0
for c in ciphers:
    repeat_index = []
    for i, w in enumerate(window(c, group_size)):
        index = c.find(w, i + group_size)
        if index >= 0:
            repeat_index.append(i)
            repeat_index.append(index)
    result = ""
    i = 0
    while i < len(c):
        if i in repeat_index:
            result += c[i:i+group_size]
            i += group_size
        else:
            result += " "
            i += 1
    if len(repeat_index) > 0:
        print(result)
        print(c)
        total_repeats += len(repeat_index) // 2
print(total_repeats)
