import cryptopals

def untemper_factory(w, n, m, r, u, s, t, l, d, b, c, a, f):

        def undo_xor_shift(y, shift_count, arg_mask=-1, left_shift=True):
            current_mask = 2 ** shift_count - 1
            shift = lambda x: x << shift_count
            if not left_shift:
                current_mask <<= (w - shift_count)
                shift = lambda x: x >> shift_count
            result = current_bits = 0
            for i in range(w):
                current_bits = ((y ^ current_bits) & arg_mask) | (y & ~arg_mask)
                result |= current_bits & current_mask
                current_mask = shift(current_mask)
                current_bits = shift(current_bits)
            return result

        def untemper(y5):
            y4 = undo_xor_shift(y5, l, left_shift=False)
            y3 = undo_xor_shift(y4, t, c, left_shift=True)
            y2 = undo_xor_shift(y3, s, b, left_shift=True)
            y1 = undo_xor_shift(y2, u, d, left_shift=False)
            return y1

        return untemper

untemper = untemper_factory(**cryptopals.MT_19937_params)
n = cryptopals.MT_19937_params["n"]

def copy_twister(twister):
    MT = [ untemper(twister.extract_number()) for i in range(n) ]
    twister_clone = cryptopals.MersenneTwister(seed=0)
    twister_clone.MT = MT
    return twister_clone

if __name__ == "__main__":
    twister1 = cryptopals.MersenneTwister(cryptopals.rand_int(0, 2 ** 30))
    twister2 = copy_twister(twister1)
    for i in range(1000):
        assert twister1.extract_number() == twister2.extract_number()