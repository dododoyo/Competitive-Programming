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


stack = []
for _ in range(ls()[0]):
  s = inp().split(" ")

  #pwd 
  if len(s) == 1:
    print("/" + "".join(stack))

  #cd
  else:
    command,directory = s
    
    #absolute-path clear everything in directory
    if directory[0] == "/":
      stack = []

    directory = directory.split("/")
    for dir in directory:
      if dir == "..":
        stack.pop()
      else:
        if dir:
          stack.append(dir+"/")