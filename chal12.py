from chal6 import as_bytes
from chal10 import pad_EBC_encrypt
from chal11 import randomkey, detect_EBC_or_CBC
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
        if out[i: 2*i] == out[2*i: 3*i]:
            return i
    raise ValueError("cipher is not using EBC encryption")

# due to repeated byte concatenation, performance is poor.
def find_secret(cipher):
    blocksize = extract_blocksize(cipher)
    num_blocks = len(cipher(b'')) // blocksize

    def block_n(text, n):
        return cipher(text)[blocksize * n : blocksize * (n + 1)]

    decoded = b''
    for blck in range(num_blocks):
        current_block = b''
        for b in reversed(range(blocksize)):
            filler = b'A' * b
            blocks_to_bytes = { block_n(filler + decoded + current_block + i, blck): i for i in map(byte,range(256))}
            actual_byte = block_n(filler, blck)
            try:
                current_block += blocks_to_bytes[actual_byte]
            except KeyError: # occurs from reaching AES padding
                decoded += current_block[:-1]  #  a \x01 character gets appended for odd reasons
                return decoded
        decoded += current_block
    return decoded
    

print(find_secret(fancy_encryption_oracle).decode('utf-8'))

