#!/bin/python3

import math
import os


def mergeSort(arr, arr2):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]
        L2 = arr2[:mid]
        # into 2 halves
        R = arr[mid:]
        R2 = arr2[mid:]
        # Sorting the first half
        mergeSort(L, arr2)

        # Sorting the second half
        mergeSort(R, arr2)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] >= R[j]:
                arr[k] = L[i]
                arr2[k] = L2[i]
                i += 1
            else:
                arr[k] = R[j]
                arr2[k] = R2[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            arr2[k] = L2[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            arr2[k] = R2[j]
            j += 1
            k += 1


# Code to print the list
#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

def maximumPeople(p, x, y, r):
    mergeSort(p, x)
    res = 0
    for people, x_ in zip(p, x):
        try:
            for cloud, r_ in zip(y, r):
                if cloud - r_ < x_ < cloud + r_:
                    res = people
                    raise StopIteration
        except StopIteration:
            break
    return res
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))
    x = list(map(int, input().rstrip().split()))
    m = int(input().strip())
    y = list(map(int, input().rstrip().split()))
    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
