from collections import defaultdict
n = int(input())
numbers = list(map(int,input().split()))
if n == 1:
  print("YES")
else:
  nums_freq = defaultdict(int)
  for num in numbers:nums_freq[num] += 1
  # if any number repeats itself more than 
  # half of the numbers
  valid = n//2 + 1 if n%2 else n//2 
  freqs = nums_freq.values()
  for freq in freqs:
    if freq > valid:
      print("NO")
      exit(0)
  print("YES")
