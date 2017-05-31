import cryptopals as c
import time

class Clock:
    """ Simulate time without actually sleeping. """
    def __init__(self):
        self.time = int(time.time())

    def sleep(self, seconds):
        self.time += seconds

clock = Clock()

def run():
    clock.sleep(c.randint(40, 1000))
    rng = c.MersenneTwister(clock.time)
    clock.sleep(c.randint(40, 1000))
    return rng.extract_number()

def crackit():
    start_time = clock.time
    val = run()
    end_time = clock.time
    for t in range(start_time, end_time):
        if val == c.MersenneTwister(t).extract_number():
            return t
    raise ValueError("Couldn't crack it!")

if __name__ == "__main__":
    print("seed:", crackit())
