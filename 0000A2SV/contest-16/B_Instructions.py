import sys
import threading
def input(): return sys.stdin.readline().strip()


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = [int(num) for num in input().split()]
        max_sol = 0

        for i in range(n-1,-1,-1):
            can_reach =  arr[i] + i
            if can_reach < n:
                arr[i] += arr[can_reach]

            if arr[i] > max_sol:
                max_sol = arr[i]

        print(max_sol)


if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
