from collections import Counter


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    count=Counter(arr)
    
    for num in range(1 , 1000 + 1):
        next_num = num + 1
        if count[num] > 2:
            count[next_num] += count[num] - 2
            count[num] = 2

    flag = True

    for val in count.values():
        if val%2 == 1:
            flag = False
            break
        
    if flag:
        print("Yes")
    else:
        print("No")