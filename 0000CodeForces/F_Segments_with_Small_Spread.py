from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]

n,k = ls()
arr = ls()

solution = 0
left = 0

# use monotonic stacks 
min_stack = []  # monotonically increasing
max_stack = []  # monotonically decreasing

for right in range(n):
    # keep monotonocity of increasing stack
    while min_stack and arr[min_stack[-1]] > arr[right]:
        min_stack.pop()

    # keep monotonocity of decreasing stack
    while max_stack and arr[max_stack[-1]] < arr[right]:
        max_stack.pop()

    min_stack.append(right)
    max_stack.append(right)

    while arr[max_stack[0]] - arr[min_stack[0]] > k:
        left += 1
        while min_stack and min_stack[0] < left:
            min_stack.pop(0)  
        while max_stack and max_stack[0] < left:
            max_stack.pop(0)  
    
    solution += right - left + 1

print(solution)
