#206983079	May/23/2023 22:03	dododoyo	352A - Jeff and Digits	PyPy 3	Accepted	154 ms	0 KB
n = int(input())
nums = input().split()
five_counter = 0
zero_counter = 0
for i in nums:
    if i == '5':five_counter+=1
    else: zero_counter+=1


if (five_counter//9) > 0 and zero_counter > 0:
    print(("5"*(five_counter//9)*9)+("0"*(len(nums)-five_counter)))
elif zero_counter > 0:
    print("0")
else:
    print("-1")