import os
import io
import random

from chal7 import EBC_encrypt
from chal8 import chunks, countit
from chal9 import pad16
from chal10 import CBC_encrypt

IS_EBC = False
TEST = False

def really_randint(a, b):
    random.seed() # calls os.urandom
    return random.randint(a, b)

def randomkey():
    return os.urandom(16)
RANDKEY = randomkey()

def rand_bool():
    random.seed()
    return random.randint(0, 1)

def rand_bytes(begin, end):
    count = really_randint(begin, end)
    return os.urandom(count)

def encryption_oracle(content):
    global IS_EBC
    global TEST
    TEST = True
    content = rand_bytes(5,10) + content.encode('utf-8') + rand_bytes(5, 10)
    if rand_bool():
        print('Executing EBC...')
        IS_EBC = True
        return EBC_encrypt(pad16(content), key= randomkey())
    else:
        print('Executing CBC...')
        IS_EBC = False
        return CBC_encrypt(pad16(content), iv=randomkey(), key= randomkey())

def detect_EBC_or_CBC(encrypted_content):
    # This is going to work for all nonrandom data.
    # From what I know, I know that this will do EBC or CBC
    # I can count the number of bytes
    LENGTH = 2 ** 16
    assert len(encrypted_content) >= LENGTH
    encrypted_content = encrypted_content[:LENGTH]
    blocks = chunks(encrypted_content, 16)
    if len(blocks) > len(set(blocks)):
        if TEST and not IS_EBC:
            return 'False positive'
        return "EBC"
    else:
        if TEST and IS_EBC:
            return 'False negative'
        return "CBC"

if __name__ == "__main__":
    content = open('data/plaintext.txt').read()
    print(detect_EBC_or_CBC(encryption_oracle(content)))







