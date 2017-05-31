import struct


def mersenne_twister( w, n, m, r, u,s,t,l,d,b,c, a, f): 
    lowest_w = (1 << w) - 1
    lower_mask =  ( 1 << r ) - 1
    upper_mask =  lowest_w & ~lower_mask

    class Twister:
        def __init__(self, seed):
            self.index = n
            self.seed_mt(seed)

        def seed_mt(self, seed):
            MT = self.MT = [ seed ]
            for i in range(1, n):
                MT.append( lowest_w & (f * (MT[-1] ^ (MT[-1] >> (w-2))) + i) )

        def extract_number(self):
            if self.index == n:
                self._twist()
            assert self.index < n, "Generator was never seeded"
            y = self.MT[self.index]
            y ^= (y >> u) & d
            y ^= (y << s) & b
            y ^= (y << t) & c
            y ^= y >> l
            self.index += 1
            return lowest_w & y

        def _twist(self):
            MT = self.MT
            for i in range(n):
                x = MT[i] & upper_mask + MT[(i+1) % n] & lower_mask
                xA = x >> 1
                if x % 2 == 1:
                    xA ^= a
                MT[i] = MT[(i+m) % n] ^ xA
            self.index = 0

    return Twister

def twister(seed):
    wordsize = struct.calcsize('l') * 8
    return mersenne_twister(
        w= wordsize,
        n = 1000,
        m = 201,
        r = 4,
            u = 3,
            s = 4,
            t = 5,
            l = 2,
            d = 15,
            b = 16,
            c = 2048,
        a = -1,
        f = 6364136223846793005 if wordsize == 64 else 1812433253
        )(seed)

def call_with_MT19937_params(func):
    return func(
            w=32,
            n=624,
            m=397,
            r=31,
            a=0x9908b0df,
            u=11,
            d=0xffffffff,
            s=7,
            b=0x9d2c5680,
            t=15,
            c=0xefc60000,
            l=18,
            f=1812433253,
    )

def MT19937(seed):
    return call_with_MT19937_params(mersenne_twister)(seed)

if __name__ == "__main__":
    twist = twister(100)
    for i in range(100):
        print(twist.extract_number())
