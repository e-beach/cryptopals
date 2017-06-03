import cryptopals as c
from functools import partial

PRACTICE_MESSAGE = b"I'm actually really horny right now."

def round_down(x):
    return x - x % 16

def round_up(x):
    if x % 16 == 0:
        return x
    else:
        return round_down(x) + 16

def edit(ciphertext, key, offset, newtext):
    copy = bytearray(ciphertext)
    final_offset = offset + len(newtext)
    begin = round_down(offset)
    end = round_up(final_offset)

    encrypt = partial(c.CTR_Encrypt, key=key, offset=begin)

    edited = bytearray(encrypt(ciphertext[begin:end]))
    edited[offset - begin : final_offset - begin] = newtext
    copy[begin:end] = encrypt(edited)
    return bytes(copy)

def test():
    decrypt = encrypt = partial(c.CTR_Encrypt, key=c.RAND_KEY)
    plaintext = PRACTICE_MESSAGE
    ciphertext = bytearray(encrypt(plaintext))
    edit(ciphertext, c.RAND_KEY, plaintext.index(b"horny"), b"high!")
    print(decrypt(ciphertext))


def breakit(edit, ciphertext):

    def get_char_at(idx):
        for char in c.all_chars():
            cp = edit(ciphertext, offset=idx, newtext=char)
            if cp == ciphertext:
                print(char)
                return char
        raise ValueError("Couldn't break it!")

    return b''.join(map(get_char_at, range(len(ciphertext))))


if __name__ == "__main__":
    edit = partial(edit, key=c.RAND_KEY)
    decrypt = encrypt = partial(c.CTR_Encrypt, key=c.RAND_KEY)
    text = c.ECB_decrypt(c.b64decode(open('data/25.txt').read()))
    print(text)
    ciphertext = encrypt(PRACTICE_MESSAGE)
    print(breakit(edit, ciphertext))

