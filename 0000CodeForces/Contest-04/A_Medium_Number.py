#given three numbers a, b, c. Print the second smallest number among them.
n = int(input())
for j in range(n):
    nums = input().split()
    nums = [int(i) for i in nums]
    nums.sort()
    print(nums[1])