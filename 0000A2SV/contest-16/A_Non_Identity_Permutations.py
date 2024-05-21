import sys
import threading
def input(): return sys.stdin.readline().strip()


def main():
    for _ in range(int(input())):
        n = int(input())
        solution = [i for i in range(n, 0, -1)]
        if n%2:
            solution[0], solution[n//2] = solution[n//2], solution[0]
        print(*solution)


if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
