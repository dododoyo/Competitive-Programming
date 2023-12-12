def sol(lst):
    ans = 0
    first_min,second_min = lst[0][1], lst[0][1]
    for i in range(n):
        ans += lst[i][1]
        first_min = min(first_min, lst[i][0])
        second_min = min(second_min, lst[i][1])
    ans += first_min-second_min
    return ans;


t = int(input());

for _ in range(t):
    n = int(input())
    lst_of_arrays = [0]*n
    for i in range(n):
        unwantedValue = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        lst_of_arrays[i] = arr;
    
    print(sol(lst_of_arrays));