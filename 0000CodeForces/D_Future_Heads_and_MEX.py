from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]

for _ in range(ls()[0]):
    n = ls()[0]
    nums = ls()

    freq = dict()
    for number in nums: 
      if number in freq:
        freq[number] += 1
      else:
        freq[number] = 1

    memo = [float('inf') for i in range(n+1)]

    first_missing = 0
    while first_missing in freq: 
      first_missing += 1

    memo[first_missing] = 0

    for i in range(first_missing, 0, -1):
        for j in range(i):
            f = 0 if j not in freq else freq[j]

            memo[j] = min(memo[j], memo[i]+i*f)

    print(memo[0]-first_missing)