# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

from heapq import heappop, heappush

n = int(input())
solution,min_heap = [],[]

for i in range(n):
    log = input()
    operation = log.split()

    # three possibilities

    # insert / just insert the value
    if operation[0] == "insert":
        heappush(min_heap, int(operation[1]))

    # getMin
    elif operation[0] == "getMin":
        val = int(operation[1])
        while len(min_heap) > 0 and min_heap[0] < val:
            solution.append("removeMin") #
            heappop(min_heap)
        if not (len(min_heap) and  min_heap[0] <= val):
            solution.append("insert " + operation[1]) #
            heappush(min_heap, val)

    # removeMin
    else:
        if not min_heap:
            solution.append("insert 1") #
        else:
            heappop(min_heap)
    # print(min_heap)
    solution.append(log) # original log is always appended 

print(len(solution))
for i in range(len(solution)):
    print(solution[i])