#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'chiefHopper' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def chiefHopper(arr):
    a = 1
    c = 0
    for obj in arr:
        a *= 2
        c = c * 2 - obj
    if a < 0:
        a *= -1
    if c < 0:
        c *= -1

    if c % a != 0:
        return int(c // a) + 1
    return int(c / a)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
