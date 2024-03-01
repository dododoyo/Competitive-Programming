for _ in range(int(input())):
    input()
    arr = list(map(int, input().split()))
    arr.sort()
    print(2*(arr[-1] - arr[0]) + 2*(arr[-2] - arr[1]))