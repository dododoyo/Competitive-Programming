#########################################################################
from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd
import heapq

def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return [list(map(int, inp().split())) for _ in range(rows)]

# setrecursionlimit(10**6)
#########################################################################


solution = [0,1]
string = inp()
n = len(string)

# index of unmatched openning paranthesis
stack = [-1]

for i in range(n):
    c = string[i]
    
    if c == '(': 
        stack.append(i)
    else:
        if len(stack) > 1:
            stack.pop()
            
            #get distance between matching parenthesis
            curr_distance = i - stack[-1]

            if curr_distance > solution[0]:
                solution = [curr_distance,1]
            elif curr_distance == solution[0]:
                solution[1] += 1
        else:
          # closing parenthesis with no 
          # matching opening parenthesis
          
          stack[0] = i # update the sentinel value from "-1"
          # this will be the starting point 
          # for our next computations
print(*solution)
