#!/usr/bin/python3

import random
from IPython import embed

import scheduler

# scrambled cipher field
cipher_field = list(range(83))
random.seed(42)
random.shuffle(cipher_field)
cipher_field = bytes(cipher_field)

def autokeyer(field, value):
    field = list(field)
    field.remove(value)
    return bytes(field)


# takes an array of plaintexts and return the field that's shared between all of them
def get_plaintext_field(plaintexts):
    field = list(set(b"".join(plaintexts)))
    # is the plaintext field scrambled ?
    # random.seed(11111)
    # random.shuffle(field)
    # or sorted ?
    field.sort()
    return bytes(field)

def normalize_plaintext(plaintext, plaintext_field):
    return bytes([plaintext_field.index(v) for v in plaintext])

def cipher_multiple(plaintexts, scheduler_fn, variation=1):
    # convert to bytes for ease of use
    plaintexts = [bytes(p, "ascii") for p in plaintexts]
    # generate the field shared betweenall the plaintexts
    plaintext_field = get_plaintext_field(plaintexts)
    # normalize all the plaintexts
    plaintexts = [normalize_plaintext(p, plaintext_field) for p in plaintexts]
    # encrypt each message
    return [cipher(p, plaintext_field, scheduler_fn, variation) for p in plaintexts]

# plaintext is normalized to plaintext_field
def cipher(plaintext, plaintext_field, scheduler_fn, variation):
    # default previous value of 0
    # FIXME maybe it's 42 maybes it's 1337 who cares at this point TrollDespair
    previous_value = 0

    result = []
    # always init the schedulers to get the same cipher
    scheduler.init_scheduler()
    for i, v in enumerate(plaintext):
        field = autokeyer(cipher_field, previous_value)
        field = scheduler_fn(field, len(plaintext_field), i, variation)
        previous_value = field[v]
        result.append(previous_value)

    # get a human readable output
    result = bytes([x + 32 for x in result])
    return result

from plaintexts import plaintexts, plaintexts_lower, plaintexts_no_space

ciphertexts = cipher_multiple(plaintexts, scheduler.multi_ring, 42)
for i, c in enumerate(ciphertexts):
    print(c.decode())

# ciphertexts_lower = cipher_multiple(plaintexts_lower, scheduler.multi_ring)
# for i, c in enumerate(ciphertexts_lower):
#     print(c.decode())

# ciphertexts_no_space = cipher_multiple(plaintexts_no_space, scheduler.multi_ring)
# for i, c in enumerate(ciphertexts_no_space):
#     print(c.decode())
