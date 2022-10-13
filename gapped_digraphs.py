#!/usr/bin/python3

import sys

ciphers = sys.stdin.read().splitlines()

gaps = []
max_gap = 15

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def find_gapped_digraphs_starting_with(value, rest, exclude_offset):
    c = rest[0]
    offset = c.find(value)
    # ignore isomorphs
    while offset != -1:
        if offset == exclude_offset:
            offset = c.find(value, offset + 1)
            continue
        # look for gapped pattern
        for i in range(0, min(len(rest[0]), len(c) - offset - 1, max_gap)):
            if value == rest[0][i]:
                continue
            if rest[0][i] == c[offset + 1 + i]:
                gaps[-1].append((i, value, rest[0][i]))
        offset = c.find(value, offset + 1)

for i, c in enumerate(ciphers): # for each ciphertext
    gaps.append([])
    for j, v in enumerate(c): # for each value in the ciphertext
        rest = [c[j+1:]] + ciphers[i+1:] # take the rest of the messages
        # find_gapped_digraphs_starting_with(v, rest, j)
        find_gapped_digraphs_starting_with(v, rest, -1)



for j, c in enumerate(ciphers):
    result = []
    for i in range(max_gap):
        result.append([" "]*len(c))
    for g,v1,v2 in gaps[j]:
        for i in find_all(c, v1):
            if i+g+1 >= len(c):
                break
            if c[i] == v1 and c[i+g+1] == v2:
                result[g][i] = v1
                result[g][i+g+1] = v2
    for i, g in enumerate(result):
        print("gap {:2}: ".format(i) + "".join(g))
    print("msg {:2}: ".format(j+1) + c)
    print()
