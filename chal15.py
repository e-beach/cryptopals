from chal12 import byte
def remove_padding(decrypted):
    padcount = decrypted[-1]
    if padcount < 16:
        padding = decrypted[-1 * padcount :]
        if padding != byte(padcount) * padcount:
            raise ValueError("invalid padding")
        decrypted = decrypted[0 : -1 * padcount]
    return decrypted

