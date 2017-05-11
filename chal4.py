from chal3 import decrypt, from_hex_bytes, fitness

f = open('data.txt').read()
candidates = [ decrypt(from_hex_bytes(line)) for line in f.split('\n') ]
print(max(candidates, key=fitness))
