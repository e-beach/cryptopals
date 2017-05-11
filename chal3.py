
freqs = { 'a':8.167, 'b':1.492, 'c':2.782, 'd':4.253, 'e':12.70, 'f':2.228, 'g':2.015, 'h':6.094, 'i':6.966, 'j':0.153, 'k':0.772, 'l':4.025, 'm':2.406, 'n':6.749, 'o':7.507, 'p':1.929, 'q':0.095, 'r':5.987, 's':6.327, 't':9.056, 'u':2.758, 'v':0.978, 'w':2.360, 'x':0.150, 'y':1.974, 'z':0.074, ' ': 19.18 }


# def from_hex_bytes(string):
#     from chal1 import from_hex
#     """ return array of bytes from hex """
#     half_bytes = from_hex(string)
#     assert len(half_bytes) % 2 == 0
#     result = []
#     for i in range(0,len(half_bytes),2):
#         byte_ = half_bytes[i] << 4 | half_bytes[i+1]
#         assert 0 <= byte_ <= 0xFF
#         result.append(byte_)
#     return result

def fitness(string):
    return sum( freqs[c] for c in string.lower() if c in freqs)

def to_string(bytes_):
    return [ ''.join([chr(x) for x in bytes_])]

def decrypt(bytes_):
    """ decrypt a hex-encoded string that has been xored with a single character.  """
    candidates = [to_string([chr(x^b) for x in bytes_]) for b in range(256)]
    return max(candidates, key=fitness)


if __name__ == "__main__":
    from sys import argv
    print(decrypt(argv[1]))
