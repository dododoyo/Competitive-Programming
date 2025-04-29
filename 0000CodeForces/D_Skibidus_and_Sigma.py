from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


for _ in range(ls()[0]):
    n,m = ls()
    arrays = []

    for __ in range(n):
        arr = ls()
        s = sum(arr)
        sc = 0
        csum = 0
        for x in arr:
            csum += x
            sc += csum
        arrays.append((s, sc))

    arrays.sort(reverse=True)
    total_score = sum(sc for _, sc in arrays)
    running_sum = 0

    for s, _ in arrays[:-1]:
        running_sum += s
        total_score += running_sum * m

    print(total_score)

