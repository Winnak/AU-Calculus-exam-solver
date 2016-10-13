"""
    Bruteforces the solution of the calculus examn of Aarhus University

    1 dependencies:
        * BeautifulSoup (pip install BeautifulSoup4)
"""

import sys
import testing

GUESS_LENGTH = 12
CORRECT = 12

def find_answer(target):
    """ Finds the answer to the specific assignment """
    if int(target) > 10000 or int(target) <= 0:
        print("0 < NUMBER <= 10000")
        return

    tries = 0
    result = list("000000000000")
    current_result = 0
    while current_result < CORRECT:
        while True:
            tries += 1
            result[current_result] = '1'
            if testing.test_guess(target, "".join(result)) > current_result:
                current_result += 1
                break
            tries += 1
            result[current_result] = '2'
            if testing.test_guess(target, "".join(result)) > current_result:
                current_result += 1
                break
            tries += 1
            result[current_result] = '3'
            if testing.test_guess(target, "".join(result)) > current_result:
                current_result += 1
                break
            result[current_result] = '4'
            current_result += 1
            break
    print("".join(result))
    return "".join(result), CORRECT, tries

if __name__ == '__main__':
    if len(sys.argv) == 2:
        find_answer(sys.argv[1])
