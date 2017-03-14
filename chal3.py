from chal1 import from_hex

alphabet = 'abcdefghijklmnopqrstuvwxyz'

frequencies = { 'a':8.167, 'b':1.492, 'c':2.782, 'd':4.253, 'e':12.70, 'f':2.228, 'g':2.015, 'h':6.094, 'i':6.966, 'j':0.153, 'k':0.772, 'l':4.025, 'm':2.406, 'n':6.749, 'o':7.507, 'p':1.929, 'q':0.095, 'r':5.987, 's':6.327, 't':9.056, 'u':2.758, 'v':0.978, 'w':2.360, 'x':0.150, 'y':1.974, 'z':0.074,
}


def from_hex_bytes(string):
    """ return array of bytes from hex """
    half_bytes = from_hex(string)
    assert len(half_bytes) % 2 == 0
    result = []
    for i in range(0,len(half_bytes),2):
        byte_ = half_bytes[i] << 4 | half_bytes[i+1]
        assert 0 < byte_ < 0xFF
        result.append(byte_)
    return result

def distance(l1, l2):
    """return distance lists of floats l1 and l2"""
    from math import hypot
    return sum( [hypot(a,b) for a,b in zip(l1,l2)] )

def fitness(string):
    # just count the number of letters in the alphabet in the string.
    return len( [c for c in string.lower() if c in alphabet] )

def decrypt(string):
    """ decrypt a hex-encoded string that has been xored with a single character.  """
    # convert hex string to character array
    bytes_ = from_hex_bytes(string)

    candidates = []
    for b in range(0xFF):
        candidate = [ x ^ b for x in bytes_ ]
        # invalid ascii characters
        if any([ x < 32 or x > 126 for x in candidate]):
            continue
        string = ''.join([chr(x) for x in candidate])
        candidates.append(string)

    return max(candidates, key=fitness)


if __name__ == "__main__":
    from sys import argv
    print(decrypt(argv[1]))
