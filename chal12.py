from chal6 import as_bytes
from chal10 import pad_ECB_encrypt
from chal11 import randomkey, detect_EBC_or_CBC
from base64 import b64decode

KEY = randomkey()
SUFFIX = 'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'

def oracle(content):
    return pad_ECB_encrypt(content + b64decode(SUFFIX), KEY)

def byte(x):
    return bytes([x])

def extract_blocksize(cipher, max_size=100):
    text = b'A' * 3 * max_size
    out = cipher(text)
    for i in range(2, max_size):
        if out[i: 2*i] == out[2*i: 3*i]:
            return i
    raise ValueError("cipher is not using EBC encryption")

def find_secret(cipher):
    blocksize = extract_blocksize(cipher)
    num_blocks = len(cipher(b'')) // blocksize

    def block_n(text, n):
        return cipher(text)[blocksize * n : blocksize * (n + 1)]

    decoded = b''
    for blck in range(num_blocks):
        for b in reversed(range(blocksize)):
            filler = b'A' * b
            d = { block_n(filler + decoded + i, blck): i for i in map(byte, range(256)) }
            actual_byte = block_n(filler, blck)
            if actual_byte not in d:
                break
            decoded += d[actual_byte]
    return decoded
    
if __name__ == "__main__":
    print(find_secret(oracle).decode('utf-8'))

