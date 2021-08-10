#!/bin/python3

import math
import os
import random
import re
import sys


#

def minimumLoss(price):
    sortedprice = sorted(price, reverse=True)
    minloss = sortedprice[0]
    for x in range(len(sortedprice) - 1):
        if (sortedprice[x] - sortedprice[x + 1]) < minloss:
            if price.index(sortedprice[x]) < price.index(sortedprice[x + 1]):
                minloss = (sortedprice[x] - sortedprice[x + 1])
    return minloss


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
