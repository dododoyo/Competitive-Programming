# math, string, implementation, brute-force
def count(move):
  ups = 0
  for i in move:ups += i == "U"
  return ups,len(move)-ups
def solve(n,digits,moves):
  for i in range(n):
    up,down = count(moves[i])
    digits[i] += (down-up)
    digits[i] %= 10
  return digits
for _ in range(int(input())):
  n = int(input())
  digits = list(map(int,input().split()))
  moves = [input().split()[1] for _ in range(n)]
  print(*solve(n,digits,moves))
  