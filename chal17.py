import cryptopals as c
from copy import copy

text = """MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=
MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=
MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==
MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==
MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl
MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==
MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==
MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=
MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=
MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93"""

strings = [ c.b64decode(s) for s in text.split('\n') ]

def cookie(string):
    return (c.pad_CBC_encrypt(string, key=c.RAND_KEY), c.IV)

def decrypt(cookie):
    return c.CBC_decrypt(cookie, key=c.RAND_KEY)

def check(cookie):
    try:
        c.remove_padding(decrypt(cookie))
    except ValueError:
        return False
    return True

if __name__ == "__main__":

    s = strings[c.rand_int(0, 9)]
    print(s)

    token, IV = cookie(s)
    token = IV + token
    token = list(bytearray(token))

    result = []

    for i in range(len(token) // 16 - 1):

        decoded = []
        prepend = lambda x: decoded.insert(0, x)

        for i in range(1, 255):
            prev = token[-1 -16]
            token[-1 -16] ^= i
            if check(bytes(token)): # i ^ message[-1] = 1
                prepend(i ^ 1)
                token[-1 -16] = prev
                break
            token[-1 -16] = prev
        else:
            prepend(1)

        for b in range(2, 17):
            tok = copy(token)
            for k in range(1, b):
                tok[-k -16] ^= decoded[-k] ^ b
            for i in range(255):
                tok[-b -16] ^= i
                if check(bytes(tok)):
                    prepend(i ^ b)
                    break
                tok[-b -16] ^= i

        token = token[ : -16 ]
        result = decoded + result

    print(c.remove_padding(bytes(result)))
