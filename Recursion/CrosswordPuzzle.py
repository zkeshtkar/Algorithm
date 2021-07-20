#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'crosswordPuzzle' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY crossword
#  2. STRING words
#

def crosswordPuzzle(crossword, words):
    if len(words) == 0:
        return crossword
    rows = len(crossword)
    columns = len(crossword[0])

    for word in words:
        for i in range(0, rows):
            counter = 0
            for j in range(0, columns):
                while crossword[i][j] == '-':
                    counter += 1
                if counter == len(word):
                    count = 0
                    while crossword[i][j] == '-':
                        crossword[i][j] = word[count]
                        count += 1
                    crosswordPuzzle()


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
