import binascii
from itertools import cycle

def repeating_key_xor(M, key="ICE"):
    # convert strings to bytearray
    M = M.encode('utf-8')
    key = key.encode('utf-8')
    cycle_ = cycle(key)
    return binascii.hexlify(bytearray([ c ^ next(cycle_) for c in M]))

if __name__ == "__main__":
    string="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    print(string)
    print(repeating_key_xor(string))
