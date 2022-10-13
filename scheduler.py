#!/usr/bin/python3

import random
from random import sample, shuffle

def init_scheduler():
    random.seed(42)

def rotate(l, x):
    x = x % len(l)
    return l[-x:] + l[:-x]

# !!!!!!!!!! exhibits isomorphs
def ring(field, k, index, _):
    return rotate(field, index)[:k]

# !!!!!!!!!! exhibits isomorphs
# some multiple show a lot less isomorphs than others
# 41 show shared section at different index which doesn't happen in the eyes
# 41 also exhibit repeated groups of 3 char
# may have something to do with the fact that 41*2 is 82, the max value in the cipher field
def multi_ring(field, k, index, variation):
    return rotate(field, index*variation)[:k]

# TODO
def primitive_root(field, k, index, variation):
    return rotate(field, (variation**index) % 83)[:k]

# doesn't exhibit shared isomorphs
def random_shuffled(field, k, index, _):
    field = sample(field, k)
    shuffle(field)
    return bytes(field)

# doesn't exhibit shared isomorphs
def random_sorted(field, k, index, _):
    return bytes(sample(field, k))
