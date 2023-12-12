def is_valley(n,arr):
    sub_arr="YES";
    up=down=0
    for i in range(1,n):
        if arr[i] > arr[i-1]:up+=1
        elif arr[i] < arr[i-1]:
            down+=1;
            if up > 0:sub_arr="NO";break
    return sub_arr




for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(is_valley(n,arr))