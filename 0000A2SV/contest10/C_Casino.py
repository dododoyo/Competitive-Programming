from math import gcd
def is_valid(i):
    while i % 2 == 0:
        i //= 2
    while i % 3 == 0:
        i //= 3
    return i == 1
        
n = int(input())
nums = list(map(int, input().split()))
common_gcd = gcd(nums[0], nums[1])

for i in range(2, n):
    common_gcd = gcd(common_gcd, nums[i])

left_overs = [0]*n

for i in range(n):
    left_overs[i] = nums[i]//common_gcd

win_jackpot = True
for i in range(n):
    if not is_valid(left_overs[i]):
        win_jackpot = False
        break

print("Yes" if win_jackpot else "No")
