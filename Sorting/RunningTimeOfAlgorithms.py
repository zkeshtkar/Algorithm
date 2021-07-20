#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    res = 0
    for i in range(1, len(arr)):
        index = i
        while arr[index - 1] > arr[index] and index > 0:
            temp = arr[index - 1]
            arr[index - 1] = arr[index]
            arr[index] = temp
            index -= 1
            res += 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
