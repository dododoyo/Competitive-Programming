from math import ceil, sqrt, log, log2, pow, floor, gcd, inf, isqrt, lcm
import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint


number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yn = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp
rand = randint(1, 10000)
xor = lambda x: x ^ rand
prefix_sum = lambda arr: list(itertools.accumulate(arr))



def solve():
    n, n2 = numbers()
    a = numbers()
    b = numbers()
    
    idx = defaultdict(int)
    for i, val in enumerate(b):
        idx[val] = i
    idxs = [idx[x] if x in idx else -1 for x in a]

    # print(idx)
    # print(ye_a)
    idxs += idxs    
    ans = 0
    mid = 0
    right = 0

    for left in range(2 * n):
        # if idxs[left] == -1:
        #     continue

            
        mid = max(mid, left)
        while mid + 1 < len(idxs) and idxs[mid] != -1 and idxs[mid + 1] > idxs[mid]:
            mid += 1

        right = max(mid, right)
        if right + 1 < len(idxs) and idxs[right] != -1 and idxs[right] < idxs[left]: 
            right += 1

        while right + 1 < len(idxs) and idxs[right] != -1 and idxs[right] < idxs[right + 1] < idxs[left]:
            right += 1

        ans = max(ans, right - left + 1)

    print(min(n,ans))


    # tililikoch = 0 
    
    # for r in range(len(ye_a)):
    #     if ye_a[r] != -1:
    #         tililikoch += (r > l and ye_a[r-1] > ye_a[r])
    #         while (r - l + 1 > n) or (tililikoch > 1) or (tililikoch == 1 and ye_a[r] > ye_a[l]):
    #             if l < r and ye_a[l] > ye_a[l+1]:
    #                 tililikoch -= 1
    #             l += 1
    #         ans = max(ans, r - l + 1)
    #     else:
    #         l = r + 1
    #         tililikoch = 0
    #         continue
        
    # print(ans)
    # return


for _ in range(test_cases(1)):
    solve()