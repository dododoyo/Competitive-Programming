from collections import defaultdict

from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]

t = ls()[0]
for i in range(t):
    n = ls()[0]

    arr = ls()
    each_freq = defaultdict(int)
    for i in arr:
      each_freq[i] += 1

    freq_list = sorted(list(each_freq.values()))
    solution = float('inf')
    distinct = len(freq_list)

    for i in range(distinct):
        freq = freq_list[i]
        solution = min(solution,n-(freq*(distinct-i)))

    print(solution)