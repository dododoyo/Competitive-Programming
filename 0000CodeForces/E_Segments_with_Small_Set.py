from sys import stdin
from collections import defaultdict

def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]



n,k = ls()
arr = ls()

numbers = defaultdict(int)
left = 0
solution = 0


for right in range(n):
  numbers[arr[right]] += 1

  while len(numbers) > k:
    numbers[arr[left]] -= 1

    if numbers[arr[left]] == 0:
      del numbers[arr[left]]

    left += 1

  solution += right - left + 1

print(solution)