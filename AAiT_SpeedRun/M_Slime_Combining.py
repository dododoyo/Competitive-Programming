from sys import stdin
from math import log2
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]

n = ls()[0]

binary = bin(n)[2:][::-1]
solution = []
for i  in range(len(binary)):
  if binary[i] == "1":
    solution.append(int(i)+1)
  
print(*solution[::-1])

