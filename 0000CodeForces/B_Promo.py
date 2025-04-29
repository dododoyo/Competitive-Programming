from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]

items,queries = ls()
items_price = ls()
items_price.sort(reverse=True)
prefix_sum = [0]*(items+1)

for index in range(items):
  prefix_sum[index+1] = prefix_sum[index] + items_price[index]

for _ in range(queries):
  purchase,free = ls()
  print(prefix_sum[purchase] - prefix_sum[purchase-free])
