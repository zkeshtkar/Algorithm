#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    res = 0
    length = len(arr)
    index = 0
    while index < length:
        if arr[index] != index + 1:
            temp =  arr[arr[index] - 1]
            arr[arr[index] - 1] = arr[index]
            arr[index] = temp
            res += 1
        else :
            index += 1
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
