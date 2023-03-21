#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diagOne = 0
    diagTwo = 0
    arrLength = len(arr)
    for i in range(arrLength):
        for j in range(arrLength):
            if(i==j):
                diagOne += arr[i][j]
                
            if((j==0 and i==arrLength-1)or(i==0 and j==arrLength-1) or (i+j)==arrLength-1):
                diagTwo += arr[i][j]
    
    return abs(diagTwo-diagOne)
                
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
