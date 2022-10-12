# Noita Eyes Novel Cipher

## usage

plaintexts are in plaintexts.py.
I used the messages showed when you pickup a new orb since they can easily show the shared isomorphs.

Those plaintext are used by cipher.py, cipher.py itself uses scheduler.py to pick a scheduler.

You can then use isomorphs.py to quickly see if the scheduler exhibit shared isomorphs.

`./cipher.py | ./isomorphs.py`

See [Novel Cipher](https://docs.google.com/document/d/1lLrICsL__b9Asn1P4O0bRMaqWeLU7-hjxDZCxnGpTlg/edit#) for an explanation of the implementation.
