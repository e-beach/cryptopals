from sys import argv
from chal1 import from_hex, to_hex

def _xor(h1, h2):
    assert len(h1) == len(h2)
    return [ a^b for a,b in zip(h1,h2)]

if __name__ == "__main__":
    # hex strings
    s1 = from_hex(argv[1])
    s2 = from_hex(argv[2])
    xord = _xor(s1,s2)
    print(to_hex(xord))

