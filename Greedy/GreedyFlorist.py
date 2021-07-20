#!/bin/python3

import math
import os
import random
import re
import sys


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr


# Complete the getMinimumCost function below.
def getMinimumCost(k, c, n):
    arr = mergeSort(c)
    sum = 0
    count = 0
    mult = 1
    for i in range(n - 1, -1, -1):
        if count == k:
            count = 0
            mult += 1
        sum += arr[i] * mult
        count += 1
    return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c, n)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
