
n = int(input())
position = list(map(int, input().split()))
speed = list(map(int, input().split()))

precision = 10**-6
left, right = min(position), max(position)

def max_time(target):
    maximum_time = 0
    for idx, pos in enumerate(position):
        time_ = abs(pos - target) / speed[idx]
        maximum_time = max(maximum_time, time_)
    
    return maximum_time

solution = max_time(left)

while left <= right:
    middle = left + (right - left ) / 2

    left_time = max_time(middle - precision)
    middle_time = max_time(middle)
    
    solution = middle_time
    
    if middle_time < left_time:
        left = middle + precision
    else:
        right = middle - precision
        
print(solution)