import os
import io
import random

from chal7 import EBC_encrypt
from chal8 import chunks, countit
from chal10 import CBC_encrypt

def really_randint(a, b):
    random.seed() # calls os.urandom
    return random.randint(a, b)

def randomkey():
    return os.urandom(16)

def rand_bool():
    random.seed()
    return random.randint(0, 1)

def encryption_oracle(content):
    count_before = really_randint(5, 10)
    count_after = really_randint(5, 10)
    content = os.urandom(count_before) + content.encode('utf-8') + os.urandom(count_after)
    if rand_bool():
        return EBC_encrypt(content, key=randomkey())
    else:
        return CBC_encrypt(content, iv=randomkey(), key=randomkey())

def detect_EBC_or_CBC(encrypted_content):
    # This is going to work for all nonrandom data.
    # From what I know, I know that this will do EBC or CBC
    # I can count the number of bytes
    assert len(encrypted_content) >= 2048
    encrypted_content = encrypted_content[:2048]
    blocks = chunks(encrypted_content, 16)
    if len(blocks) - len(set(blocks)) > 2:
        return "EBC"
    else:
        return "CBC"

if __name__ == "__main__":
    content = open('data/plaintext.txt').read()
    print(detect_EBC_or_CBC(encryption_oracle(content)))







