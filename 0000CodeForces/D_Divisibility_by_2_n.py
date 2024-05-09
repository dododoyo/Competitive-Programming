def getPower(n):
    total_power = 0
    while n%2 == 0:
        n //= 2
        total_power += 1
    return total_power
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    total_power = 0
    for i in range(n):
        n_p = getPower(nums[i])
        # print(n_p)
        total_power += n_p
        # two_powers[i] = n_p
    # print(total_power)
    # get all even indeces 
    valids = []
    for i in range(2,n+1,2):
        valids.append(getPower(i))
    adds = 0
    # print(valids)
    for i in range(len(valids)-1,-1,-1):
        # print(valids[i])
        if total_power  >= n:
            break
        total_power += valids[i]
        adds += 1

    if total_power < n:
      print(-1)
    else:
      print(adds)
    # print()




