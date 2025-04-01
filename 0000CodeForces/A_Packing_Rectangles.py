from sys import stdin
from math import ceil
def input(): return stdin.readline().strip()

w,h,n = [int(i) for i in input().split()]

def isValid(x):
  row_boxes = x//w
  column_boxes = x//h

  return row_boxes*column_boxes >= n


low,high = max(h,w),max(w,h)*n
solution = high

while low <= high:
  middle = low + (high-low)//2
  if isValid(middle):
    solution = middle
    high = middle - 1
  else:
    low = middle + 1


print(solution)

