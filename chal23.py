import cryptopals

_NONE = {}
def disp(m, x = _NONE):
    if x is _NONE:
        x = m
        val = hex(x).zfill(8)
    else:
        val = m + " " + "0x" + hex(x)[2:].zfill(8)
    print(val.rjust(20))

def twister_reverser(w, n, m, r, u, s, t, l, d, b, c, a, f):

    class Reverser:

        @staticmethod
        def undo_xor_with_self_right_shifted(y, shift, arg_mask = None):
            mask = (2 ** shift - 1) << (w - shift)
            known = bits = 0
            while mask:
                bits = (y ^ bits) & mask
                if arg_mask is not None:
                    bits &= arg_mask
                    bits |= y & ~arg_mask
                known |= bits
                mask >>= shift
                bits >>= shift
            return known

        @staticmethod
        def undo_xor_with_self_left_shifted(y, shift, arg_mask = None):
            mask = 2 ** shift - 1
            known = bits = 0
            while not mask >> (w + shift):
                bits = (y ^ bits) & mask
                if arg_mask is not None:
                    bits &= arg_mask
                    bits |= y & ~arg_mask
                known |= bits
                mask <<= shift
                bits <<= shift
            return known

        @staticmethod
        def reverse(y5):

            # Operation we are reversing:
            # y1 = MT[index]
            # y2 = y1 ^ ((y1 >> u) & d)
            # y3 = y2 ^ ((y2 << s) & b)
            # y4 = y3 ^ ((y3 << t) & c)
            # y5 =  y4 ^ (y4 >> l)

            y4 = Reverser.undo_xor_with_self_right_shifted(y5, l)
            y3 = Reverser.undo_xor_with_self_left_shifted(y4, t, c)
            y2 = Reverser.undo_xor_with_self_left_shifted(y3, s, b)
            y1 = Reverser.undo_xor_with_self_right_shifted(y2, u, d)
            return y1

    return Reverser

Reverser = twister_reverser(**cryptopals.MT_19937_params)
n = cryptopals.MT_19937_params["n"]

def copy_twister(twister):
    MT = [ Reverser.reverse(twister.extract_number()) for i in range(n) ]
    twister_clone = cryptopals.MersenneTwister(seed=0)
    twister_clone.MT = MT
    twister_clone._twist()
    return twister_clone

if __name__ == "__main__":
    twister1 = cryptopals.MersenneTwister(cryptopals.randint(0, 2 ** 30))
    twister2 = copy_twister(twister1)
    print(twister1.extract_number())
    print(twister2.extract_number())