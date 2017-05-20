import cryptopals as c

def block(encrypted, n, blocksize=16):
    return encrypted[blocksize*n: blocksize*(n+1)]

def blocks(encrypted, n, m, blocksize=16):
    return [ block(encrypted, i, blocksize=blocksize) for i in range(n, m)]


strings = [ c.b64decode(s) for s in """MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=
MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=
MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==
MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==
MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl
MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==
MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==
MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=
MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=
MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93""".split('\n') ]

def cookie(string):
    return ( c.CBC_encrypt(string, key=c.RANDKEY),  c.IV )


def check(cookie):
    try:
        c.remove_padding(c.CBC_decrypt(cookie))
    except ValueError:
        return False
    return True


s = strings[c.randint(0,9)]
cooki, IV = cookie(s)
cooki = list(bytearray(cooki))

decoded = []
for i in reversed(range(len(cooki) - 16, len(cooki))):
    target = len(cooki) - i
    cooki[i + 1 :] = c.strxor(reversed(decoded), [ target ] * len(decoded) )
    for char in range(1, 255):
        cooki[i] ^= char
        if check(bytes(cooki)):
            cooki[i] ^= char
            decoded.append(char ^ target)
            break
        cooki[i] ^= char
    else:
        raise ValueError("Can Never Happen")
decoded = c.strxor(reversed(decoded), block(cooki, -2))
print(bytes(decoded).decode('utf-8'))

# for each block
    # decode the block using xor magic
    # now we know what the block looks like after it was xored with the previous encrypted block
    # xor newly decrypted block with previous encrypted block to get real real value





