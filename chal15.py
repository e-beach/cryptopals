from chal12 import byte
def remove_padding(decrypted, check_padding=True):
    padcount = decrypted[-1]
    padding = decrypted[-1 * padcount :]
    if padding != byte(padcount) * padcount:
        if check_padding:
            raise ValueError("invalid padding")
        else:
            return decrypted
    return decrypted[0 : -1 * padcount]

