from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]

for _ in range(ls()[0]):
    s = inp()
    has_pair = False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            has_pair = True
            break
        
    print(1 if has_pair else len(s))