from chal6 import as_bytes
from chal10 import pad_EBC_encrypt
from chal11 import randomkey
from base64 import b64decode

KEY = randomkey()
STUFF = 'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'

def fancy_encryption_oracle(content):
    return pad_EBC_encrypt(content + b64decode(STUFF), KEY)

def byte(x):
    return bytes([x])

def extract_blocksize(cipher, max_size=100):
    text = b'A' * 3 * max_size
    out = cipher(text)
    for i in range(2, max_size):
        if out[i:2*i] == out[2*i:3*i]:
            return i

def find_secret(cipher):
    blocksize = extract_blocksize(cipher)
    def block1(text):
        return cipher(text)[:blocksize]

    # processing the bytes of first block in reverse order
        # determine value by caching every block with [filler] + x + known
        # extract value of encrypt(filler + x + known)
        # now we know
    known = b''
    for b in reversed(range(blocksize)):
        filler = b'A' * b
        blocks_to_bytes = { block1(filler + known + byte(i)): i for i in range(256) } 
        value = blocks_to_bytes[block1(filler)]
        known += byte(value)
    print(known)

    # for block n:
    #   filler = (known value of previous blocks) + (same as before)
    #   value is form blockn instead of block1


print(extract_blocksize(fancy_encryption_oracle))
find_secret(fancy_encryption_oracle)

