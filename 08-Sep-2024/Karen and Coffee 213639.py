# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k , q= map(int, input().split())

arr = [0] * (20**5+2)

for i in range(n):
    left, right = map(int, input().split())
    arr[left] += 1
    arr[right+1] -= 1
nums = [1 if arr[0] > k else 0]
for i in range(1, len(arr)):
    arr[i] += arr[i-1]
    if arr[i] >= k:
        nums.append(1+nums[-1])
    else:
        nums.append(nums[-1])
for i in range(q):
    l, r = map(int, input().split())
    print(nums[r]-nums[l-1])