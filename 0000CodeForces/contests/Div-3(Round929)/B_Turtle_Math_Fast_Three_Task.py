def min_moves(arr):
    total = sum(arr)
    remainder = total % 3
    if remainder == 0:
        return 0
    else:
        same_remainder = [x for x in arr if (x % 3 == remainder)]
        if same_remainder:
            return 1
        else:
            return 3 - remainder


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    # print(arr)
    print(min_moves(arr))
    # print()