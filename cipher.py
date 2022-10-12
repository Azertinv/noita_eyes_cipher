#!/usr/bin/python3

from random import sample, shuffle
from IPython import embed

import scheduler

# cipher field
# FIXME it is currently sorted, maybe it's not ?
cipher_field = bytes(range(83))

def autokeyer(field, value):
    field = list(field)
    field.remove(value)
    return bytes(field)

# takes an array of plaintexts and return the field that's shared between all of them
def get_plaintext_field(plaintexts):
    return bytes(set(b"".join(plaintexts)))

def normalize_plaintext(plaintext, plaintext_field):
    return bytes([plaintext_field.index(v) for v in plaintext])

def cipher_multiple(plaintexts, scheduler_fn):
    # convert to bytes for ease of use
    plaintexts = [bytes(p, "ascii") for p in plaintexts]
    # generate the field shared betweenall the plaintexts
    plaintext_field = get_plaintext_field(plaintexts)
    # normalize all the plaintexts
    plaintexts = [normalize_plaintext(p, plaintext_field) for p in plaintexts]
    # encrypt each message
    return [cipher(p, plaintext_field, scheduler_fn) for p in plaintexts]

# plaintext is normalized to plaintext_field
def cipher(plaintext, plaintext_field, scheduler_fn):
    # default previous value of 0
    # FIXME maybe it's 42 maybes it's 1337 who cares at this point TrollDespair
    previous_value = 0

    result = []
    # always init the schedulers to get the same cipher
    scheduler.init_scheduler()
    for i, v in enumerate(plaintext):
        field = autokeyer(cipher_field, previous_value)
        field = scheduler_fn(field, len(plaintext_field), i)
        previous_value = field[v]
        result.append(previous_value)

    # get a human readable output
    result = bytes([x + 32 for x in result])
    return result

from plaintexts import plaintexts, plaintexts_lower, plaintexts_no_space

ciphertexts = cipher_multiple(plaintexts, scheduler.ring)
ciphertexts_lower = cipher_multiple(plaintexts_lower, scheduler.ring)
ciphertexts_no_space = cipher_multiple(plaintexts_no_space, scheduler.ring)

for i, c in enumerate(ciphertexts):
    print(c.decode())
# for i, c in enumerate(ciphertexts_lower):
#     print(c.decode())
# for i, c in enumerate(ciphertexts_no_space):
#     print(c.decode())
