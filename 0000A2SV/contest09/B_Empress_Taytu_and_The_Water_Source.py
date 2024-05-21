import math

def isTimeValid(wagon, hours, demands, k, n):
    each_time = [math.ceil(demand/wagon) for demand in demands]
    total_time = sum([hours[i]*each_time[i] for i in range(n)])
    return total_time <= k

for _ in range(int(input())):
    n, k = map(int, input().split())
    demands = list(map(int, input().split()))
    hours = list(map(int, input().split()))
    min_wagon, max_wagon = float("inf"), -float("inf")
    for demand in demands:
        if demand < min_wagon:
            min_wagon = demand
        if demand > max_wagon:
            max_wagon = demand
    low, high = 1, max_wagon
    while low <= high:
        middle = low + (high-low)//2
        if isTimeValid(middle, hours, demands, k, n):
            high = middle - 1
        else:
            low = middle + 1
    print(-1 if low > max_wagon else low)
