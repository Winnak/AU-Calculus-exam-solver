"""
    frequency.py

    Prints the frequency of 1 and 2 and 3 and 4 in the solution_best.db
"""
import sqlite3

def main():
    """ Finds the frequency of 1 and 2 and 3 and 4 in the solution """
    conn = sqlite3.connect('solutions_best.db')
    sql = "SELECT guess, question FROM answers WHERE (result = 12)"

    ones = 0
    twos = 0
    tres = 0
    fors = 0

    result = conn.execute(sql).fetchall()
    for guess, question in result:
        for char in str(guess):
            if char == '1':
                ones += 1
            elif char == '2':
                twos += 1
            elif char == '3':
                tres += 1
            elif char == '4':
                fors += 1
            else:
                print("Error at: {}, with guess: {}".format(question, guess))
    sumof = ones + twos + tres + fors
    print("1: {}\t{}".format((100 * ones) / sumof, ones))
    print("2: {}\t{}".format((100 * twos) / sumof, twos))
    print("3: {}\t{}".format((100 * tres) / sumof, tres))
    print("4: {}\t{}".format((100 * fors) / sumof, fors))

if __name__ == '__main__':
    main()
