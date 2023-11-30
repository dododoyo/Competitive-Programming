#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    i = 1
    j = len(arr) - 1
    while i < j:
        while arr[i] <= arr[0]:
            i += 1
        while arr[j] > arr[0]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j],arr[i]
    arr[0],arr[j] = arr[j],arr[0]
    return arr
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
