import cryptopals as c
from chal19 import solve, solve_keystream

text = open('data/20.txt').read()

if __name__ == "__main__":
    lines = [c.CTR_Encrypt(c.b64decode(s)) for s in text.split('\n')]
    solve(lines, solve_keystream(lines))



