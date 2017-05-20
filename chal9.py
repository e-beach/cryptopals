import struct

def get_bytes(string):
    return string.encode('ascii')

def pad(string, length):
    count = length - len(string)
    assert 0 <= count <= 0xFF
    if isinstance(string, bytes):
        return string + bytes([count] * count)
    else:
        return string + chr(count) * count

def pad16(string):
    offset = 16 - (len(string) % 16)
    return pad(string, len(string) + offset)


if __name__ == "__main__":
    padded = pad('YELLOW SUBMARINE', 20)
    print(get_bytes(padded))
