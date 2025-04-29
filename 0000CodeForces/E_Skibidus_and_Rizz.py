from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]


for _ in range(ls()[0]):
    x,y,k = ls()
    vals = ['0', '1']

    if x > y:
        vals = ['1','0']
    y, x = max(x, y), min(x,y)
    
    if y - x > k or y < k:
        print(-1)
        continue  

    solution = []
    while y > 0:
        x_ = min(x,k)
        y_ = min(y,k)

        y -= y_
        x -= x_

        if y_:
            solution.append(vals[1] * y_)
        if x_:
            solution.append(vals[0] * x_)

    print(''.join(solution))