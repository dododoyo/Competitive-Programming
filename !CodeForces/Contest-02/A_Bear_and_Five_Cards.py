nums = input().split()
all_nums = [0]*101
for i in range(len(nums)):
    nums[i] = int(nums[i])
    all_nums[nums[i]] += 1
total_sum = sum(nums)
min_sum = total_sum
for i in range(101):
    current_sum = min_sum
    if all_nums[i] == 2:
        current_sum = total_sum - i - i
    elif all_nums[i] > 2:
        current_sum = total_sum - (3*i)
    min_sum = min(current_sum,min_sum)
print(min_sum)
