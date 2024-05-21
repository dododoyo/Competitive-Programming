from math import gcd
n = int(input())
arr = [int(num) for num in input().split()]

for i in range(1,n):
  print(gcd(arr[i],arr[i-1]))