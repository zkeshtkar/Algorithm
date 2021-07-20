#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    index = n - 1
    value = arr[index]
    while value < arr[index - 1] and index > 0:
        arr[index] = arr[index - 1]
        for i in range(0, n):
            print(arr[i], end=' ')
        print()
        index -= 1
    arr[index] = value
    for i in range(0, n):
        print(arr[i], end=' ')
    print()


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
