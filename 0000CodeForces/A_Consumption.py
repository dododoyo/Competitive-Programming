from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]


n = ls()[0]
remaining = ls()
capacity = sorted(ls())


total_drink = sum(remaining)
largest_cans = capacity[-1] + capacity[-2]

print("YES" if largest_cans >= total_drink else "NO")