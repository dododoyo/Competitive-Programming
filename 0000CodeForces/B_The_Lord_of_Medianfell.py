from sys import stdin
def input(): return stdin.readline().strip()

for _ in range([int(i) for i in input().split()][0]):
  length, summ = [int(i) for i in input().split()]
  print(summ // (length//2+1))