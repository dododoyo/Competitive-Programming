# from sys import stdin
# def inp(): return stdin.readline().strip()
# def ls(): return [int(i) for i in inp().split()]
# def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]

# n = ls()[0]
# stone_costs = ls()
# sorted_costs = sorted(stone_costs)

# normal_prefixs = [0]*(n+1)
# sorted_prefixs = [0]*(n+1)

# for i in range(n):
#   normal_prefixs[i+1] = normal_prefixs[i] + stone_costs[i]
#   sorted_prefixs[i+1] = sorted_prefixs[i] + sorted_costs[i]

# queries = ls()[0]

# for _ in range(queries):
#   typ,left,right = ls()
#   if typ == 1:
#     print(normal_prefixs[right] - normal_prefixs[left-1])
#   else:
#     print(sorted_prefixs[right] - sorted_prefixs[left-1])



from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    # print(a,b)
    is_reversed = False
    count = Counter(a)
    for i in range(n - 1, -1, -1):
        if (a[i] == b[i] and not is_reversed) or (is_reversed and a[i] != b[i]):
            if is_reversed:
                if a[i] =='0':
                    count['1'] -= 1
                else:
                    count['0'] -=1

            else:
                count[a[i]] -= 1
        else:
            if count['0'] == count['1']:
                is_reversed = not is_reversed
                if (a[i] == b[i] and not is_reversed) or (is_reversed and a[i] !=b[i]):
                    if is_reversed:
                        count[a[i]] += 1
                    else:
                        count[a[i]] -= 1
            else:
                print('NO')
                break
    else:
        print('YES')