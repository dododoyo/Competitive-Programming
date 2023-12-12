t = int(input())
for _ in range(t):
    n = int(input())
    arr = input().split()
    arr = [0]+[int(x) for x in arr]+[0]
    count,h,l = 0,1,1
    while h <= n:
        while arr[h] == arr[h+1]:h+=1
        if (l == 1 or arr[l-1] > arr[l]) and (h == n or arr[h+1] > arr[h] ):
            count +=1
        l=h+1;h+=1
    print('NO') if count > 1 else print('YES')
