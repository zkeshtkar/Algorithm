#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1, n):
        index = i
        while arr[index - 1] > arr[index] and index > 0:
            temp = arr[index - 1]
            arr[index - 1] = arr[index]
            arr[index] = temp
            index -= 1
        for i in range(0, n):
            print(arr[i], end=" ")
        print()


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
