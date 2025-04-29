from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]


def countSouvenirs(costs,m,n):
    souvenirs_bought = [0]*n

    for i in range(n):
        souvenirs_bought[i]=costs[i]+(i+1)*m

    total_cost = 0
    souvenirs_bought.sort()

    # buy the top m elements with less price
    for i in range(m):
        total_cost += souvenirs_bought[i]

    return total_cost

n,S = ls()
costs = ls()
low,high = 0,n

max_souvenirs,min_cost = -float('inf'),float('inf')

while low <= high:
    mid = low+(high-low)//2
    souvenirs_cost = countSouvenirs(costs,mid,n)

    if souvenirs_cost <= S:
        min_cost = souvenirs_cost
        max_souvenirs = mid
        
        low = mid + 1
    else:
        high = mid - 1

print(max_souvenirs,min_cost)
