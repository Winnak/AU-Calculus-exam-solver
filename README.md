# AU Calculus exam solver

AU Calculus is a set of tools to solve the training set of the calculus exam, by simply asking for the solution (a lot of times). Please note that this was made as a joke, but turned into a academic curiosity, for instance, if I were to pick just one number through the entire exam, what would be the most likely number that would make me pass? (The answer turned out to be is 2)

Please check the license before using the tool.

## Usage
* `mastermind.py <number>`
Finds the solution by randomly shuffling a string of 1, 2, 3 and 4 (worst case: length^(frequency)/frequency (12\*4/frequency = 5184, note: frequency is around 3, but could technically be 4))

* `mastermind_best.py <number>` Brute forces the solution by 100000000 -> 2000000000 -> .. 312124121 (worst case: length\*(domain-1) (12\*3 = 36))

* `testing.py <number> <question (optional)>` Looks for the solution in the database (`solution_best.db`) for quick look ups. Can also just return the answer for a particular question.

* `collector.py <number (optional)>` Brute forces all questions and stores them in the database (note: will remove database). Will limit search if supplied with a number.

* `frequency.py` Prints the frequency of the answers in the `solution_best.db`

## License
The MIT License (MIT)
Copyright (c) 2016 Erik Hoyjor

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
