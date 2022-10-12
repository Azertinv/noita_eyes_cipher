#!/usr/bin/python3

import random
from random import sample, shuffle

def init_scheduler():
    random.seed(42)

def rotate(l, x):
    return l[-x:] + l[:-x]

# !!!!!!!!!! exhibits isomorphs
def ring(field, k, index):
    return rotate(field, index)[:k]

# doesn't exhibit shared isomorphs
def primitive_root(field, k, index):
    return rotate(field, (2**index) % 83)[:k]

# doesn't exhibit shared isomorphs
def random_shuffled(field, k, index):
    field = sample(field, k)
    shuffle(field)
    return bytes(field)

# doesn't exhibit shared isomorphs
def random_sorted(field, k, index):
    field = sample(field, k)
    return bytes(field)
