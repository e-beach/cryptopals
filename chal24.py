import cryptopals as c
import time

def MT_19377_encrypt(content, seed):
    twister = c.MersenneTwister(seed)
    return b''.join(
        c.strxor(twister.uint32(), chunk) for chunk in c.chunks(content, 4)
    )

def prefix(content):
    return c.rand_bytes(10, 100) + content

def encryption_oracle(content):
    seed = c.rand_int(0, 0xFFFF)
    return MT_19377_encrypt(prefix(content), seed)

def breakit(content, encrypted):
    padding = len(encrypted) - len(content)
    content = b'B' * padding + content
    for seed in range(0xFFFF):
        if MT_19377_encrypt(content, seed)[padding:] == encrypted[padding:]:
            return seed
    raise ValueError("Couldn't get seed")

def password_reset_token():
    return MT_19377_encrypt(c.RAND_KEY, time.time())

def is_token_for_current_time(token):
    return password_reset_token() == token




if __name__ == "__main__":
    content = b'A' * 14
    encrypted = encryption_oracle(content)
    seed = breakit(content, encrypted)
    print(MT_19377_encrypt(encrypted, seed))



