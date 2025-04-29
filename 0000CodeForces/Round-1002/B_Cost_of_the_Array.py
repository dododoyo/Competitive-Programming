from sys import stdin
def i(): return stdin.readline().strip()
def ls(): return [int(i) for i in i().split()]
def mt(rows): return[list(map(int, i().split())) for _ in range(rows)]

