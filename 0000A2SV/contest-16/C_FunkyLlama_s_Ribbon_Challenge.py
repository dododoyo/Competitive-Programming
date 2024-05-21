import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n,a,b,c = map(int,input().split())
    # n must be a factor of a,b and c
    factors = [0]*3
    factors[0] = n//a
    factors[1] = n//b
    factors[2] = n//c
    print(factors)



if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()