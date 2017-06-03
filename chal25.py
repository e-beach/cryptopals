import cryptopals as c
from functools import partial

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

def breakit(edit, ciphertext):

    def get_char_at(idx):
        for char in c.all_chars():
            if edit(ciphertext, offset=idx, newtext=char) == ciphertext:
                return char
        raise ValueError("Couldn't break it!")

    return b''.join(map(get_char_at, range(len(ciphertext))))


if __name__ == "__main__":
    edit = partial(edit, key=c.RAND_KEY)
    decrypt = encrypt = partial(c.CTR_Encrypt, key=c.RAND_KEY)
    text = c.ECB_decrypt(c.b64decode(open('data/25.txt').read()))
    print(text)
    ciphertext = encrypt(text)
    print(breakit(edit, ciphertext))

