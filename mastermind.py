"""
    mastermind.py <number>

    Finds the solution by randomly shuffling a string of 1, 2, 3 and 4

    Worst case: (length^(frequency))/frequency
    This worst case: (12*4)/4 = 5184
        note: frequency is around 3, but could technically be 4
"""

import sys
from random import Random
import testing

GUESS_LENGTH = 12
GUESS_ATTEMPTS = 20000
CORRECT = 7

def find_answer(target):
    """ Finds the answer to the specific assignment """
    if int(target) > 10000 or int(target) <= 0:
        print("0 < NUMBER <= 10000")
        return


    ones = testing.test_guess(target, "111111111111")
    twos = testing.test_guess(target, "222222222222")
    tres = testing.test_guess(target, "333333333333")

    rand_seed = Random()
    offset = rand_seed.randint(0, 10000)

    unique_guess = dict()
    for seed in range(GUESS_ATTEMPTS):
        guess = generate_guess(seed + offset, ones, twos, tres)
        if unique_guess.get(guess) is not None:
            continue
        unique_guess[guess] = seed + offset
        result = testing.test_guess(target, guess)
        if result >= CORRECT:
            print(guess, end=", with ")
            print(result, end=" correct, with ")
            print(seed + 4, end=" guesses\n")
            return guess, result, seed + 4
    print("did not find the answer using {} guesses".format(GUESS_ATTEMPTS))

def generate_guess(seed, one, two, three):
    """ Generates a guess string based on the amount of '1' '2' '3' and '4' """
    onestring = "1" * one
    twostring = "2" * two
    trestring = "3" * three
    forstring = "4" * (GUESS_LENGTH - one - two - three)

    result = onestring + twostring + trestring + forstring
    assert len(result) == GUESS_LENGTH

    rand = Random(seed)
    return ''.join(rand.sample(result, GUESS_LENGTH))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        find_answer(sys.argv[1])
