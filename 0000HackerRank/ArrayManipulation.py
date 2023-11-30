#!/bin/python3

import math
import os
import random
import re
import sys
def arrayManipulation(n, queries):
    arr = [0]*(n+1);
    for l,r,val in queries:
        arr[l-1] += val 
        arr[r] += -1*val
    prefix_arr = [0]*(n+2)
    for i in range(1,n+1):
        prefix_arr[i] = arr[i-1] + prefix_arr[i-1]
    return max(prefix_arr)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
