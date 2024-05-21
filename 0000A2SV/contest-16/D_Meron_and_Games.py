import sys
import threading
from collections import defaultdict


def input(): return sys.stdin.readline().strip()


def main():
    dp = defaultdict(lambda:-1)
    n = int(input())
    arr = [int(num) for num in input().split()]
    freq = defaultdict(int)
    for e in arr:
        freq[e] += 1

    def find_max(n):
        if dp[n] != -1:
            return dp[n]
        
        if n < 2:
            return freq[n]
        
        dp[n] = max(find_max(n - 1), find_max(n - 2) + freq[n]*n)

        return dp[n]
    
    print(find_max(max(freq.keys())))


if __name__ == '__main__':

    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
