"""
    collector.py <number (optional)>

    Brute forces all questions and stores them in the database
        note: Will remove database.

    Can limit search if supplied with a number.
"""

import sys
import os
import sqlite3
import mastermind_best

DATABASE_FILENAME = "solutions_best.db"

def main(start):
    """ Main entry point of the program """
    try:
        os.remove(DATABASE_FILENAME)
    except OSError:
        pass

    conn = sqlite3.connect(DATABASE_FILENAME)

    conn.execute("CREATE TABLE answers (question int, guess int, result int, attempt int)")
    conn.commit()

    for question in range(int(start), 10001):
        guess, result, seed = mastermind_best.find_answer(question)
        conn.execute("INSERT INTO answers VALUES ({},{},{},{})"
                     .format(question, guess, result, seed))
        conn.commit()
        if question % 100 == 0:
            print("Trying {}/{}".format(question, 10000))
    conn.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    main(1)
