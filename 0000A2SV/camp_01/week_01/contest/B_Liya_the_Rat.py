def helper(s):
  prefix_sum = [0]*(len(s)+1)
  for i in range(1,len(s)):
    prefix_sum[i+1] = prefix_sum[i] + (s[i-1] == s[i])
  return prefix_sum
s = input()
n = len(s)
m = int(input())
count_same = helper(s)
# print(count_same)
for i in range(m):
  left,right = map(int,input().split())
  hashes = count_same[right] - count_same[left] 
  print(hashes)