from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]


for _ in range(ls()[0]):
  s = input()
  if len(s)%2:
    print("NO")
  else:
    half = len(s)//2
    first_half = s[:half]
    second_half = s[half:]
    print("NO" if first_half != second_half else "YES")