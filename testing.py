""" todo """

import sys
import sqlite3
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

TARGET = "http://merry2.math.au.dk/cgi-bin/prtestanswer1"

def main(target):
    """ Finds the correct guess for the target question """
    conn = sqlite3.connect('solutions_best.db')
    sql = "SELECT guess FROM answers WHERE (question = {})".format(int(target))
    result = conn.execute(sql).fetchone()[0]
    print(result)

def test_guess(target, guess):
    """ Sends the guess to the server to get the amount of correct answers """
    payload = {'svar': guess, 'kode': target}
    urlvalues = urllib.parse.urlencode(payload)
    urlvalues = urlvalues.encode('ascii')
    respons = urllib.request.urlopen(TARGET, urlvalues, 10000)
    result = respons.read()
    if result is None:
        raise Exception("Did not get any data back")
    soup = BeautifulSoup(result, "html.parser")
    if soup.h4 is None:
        print(soup.prettify())
        raise Exception("what the fuck")
    return int(soup.h4.get_text()[-2:])

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
