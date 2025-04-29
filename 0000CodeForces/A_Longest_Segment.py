from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]
from collections import defaultdict


n,k = ls()
houses = ls()
max_length = 0 
right,left = 0,0


for right in range(n):
    if right > 0 and houses[right] == houses[right - 1]:
        left = right
    max_length = max(max_length, right - left + 1)
    right += 1

print(max_length)