#!/bin/env python3

####
# Machine Automata - Session 1 - Practical String Closure Project
####

import sys

W = ["a", "b", "c"] # \Sigma={a,b,c}

def my_product(iterable, repeat):
    pool = list(iterable)
    n = len(pool)

    # start with [0,0,0,...]
    indices = [0] * repeat

    while True:
        # build current tuple
        yield tuple(pool[i] for i in indices)

        # increment like an odometer
        for pos in reversed(range(repeat)):
            indices[pos] += 1
            if indices[pos] < n:
                break
            indices[pos] = 0
        else:
            # we overflowed all positions
            return

# Join Lambda (0, \infinity)
def power(number) :
    all_strings = [p for p in my_product(W, repeat=number)]

    return all_strings

# Join Non-Lambda (1, \infinity)
def plus(number) :
    if number == 0:
        return tuple(W)

    all_strings = [p for p in my_product(W, repeat=number)]

    return all_strings

arg = int(sys.argv[1])
result_power = power(arg)
result_plus = plus(arg)

print("Power:", result_power) # Result could be 0 (lambda) to infinity
print("------")
print("Plus:", result_plus) # Result could be 0 (lambda) to infinity

# === Tests

def test_power():
    indices = [0] * 3
    n = len(W)
    while True:
        for pos in reversed(range(3)):
            indices[pos] += 1
            if indices[pos] < n:
                print(indices)
                break
            indices[pos] = 0
            print(indices, "<-")
        else:
            return


Tests = []

# Tests.append(test_power)

for i in Tests:
    i()
