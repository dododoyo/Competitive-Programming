from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]

# we can always place a city before first element
# we can always place a city after the last element
# cities can be initialized with 2

n,k = ls()
cities = ls()
new_hotels = 2

for i in range(1,n):
  # for each consequative city check how many 
  # hotels can be placed between them 

  left_bound = cities[i-1] + k
  right_bound = cities[i] - k
  # print(left_bound,right_bound,cities[i-1],cities[i])

  if right_bound > left_bound:
    new_hotels += 1

  if right_bound >= left_bound:
    new_hotels += 1

print(new_hotels)
