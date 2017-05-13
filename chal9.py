import struct

def get_bytes(string):
    return bytes(string.encode('ascii'))

def pad(string, length):
    assert length < 0xFF
    count = length - len(string)
    return string + chr(count) * count

padded = pad('YELLOW SUBMARINE', 20)
print(get_bytes(padded))
