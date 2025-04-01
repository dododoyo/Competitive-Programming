t = int(input())

for _ in range(t):
    N , k = map(int , input().split())
    arr = list(map(int , input().split()))
    group = []
    below = []
    for num in arr:
        if num < k:
            below.append(num)
        else:
            group.append(num)
    


    solution = 0
    below.sort(reverse = True)
    left = 0
    for i in range(len(below)):
        if (i - left + 1) * below[i] >= k:
            solution += 1
            left = i + 1
    print(len(group) + solution)