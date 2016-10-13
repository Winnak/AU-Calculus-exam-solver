"""
    testing.py <number> <question (optional)>

    Looks for the solution in the database (solution_best.db) for quick look ups.
    Can also just return the answer for a particular question.
"""

import sys
import sqlite3
import urllib.request
import urllib.parse

TARGET = "http://merry2.math.au.dk/cgi-bin/prtestanswer1"

def main(target, question=-1):
    """ Finds the correct guess for the target question """
    conn = sqlite3.connect('solutions_best.db')
    sql = "SELECT guess FROM answers WHERE (question = {})".format(int(target))
    result = conn.execute(sql).fetchone()[0]
    if int(question) > 0 and int(question) <= 12:
        print(str(result)[int(question) - 1])
    else:
        print(result)

def test_guess(target, guess):
    """ Sends the guess to the server to get the amount of correct answers """
    payload = {'svar': guess, 'kode': target}
    urlvalues = urllib.parse.urlencode(payload)
    urlvalues = urlvalues.encode('ascii')
    respons = urllib.request.urlopen(TARGET, urlvalues, 10000)
    result = str(respons.read())
    if result is None:
        raise Exception("Did not get any data back")
    start, end = result.find('<h4>') + 35, result.find('</h4>')
    assert len(result) > start
    assert len(result) > end
    if start == -1 or end == -1:
        raise Exception("Could not find parse result")
    return int(result[start:end])

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
