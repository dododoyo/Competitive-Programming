spaceships, bases = map(int, input().split())
spaceships_power = list(map(int, input().split()))
base_list = [0]*bases

for i in range(bases):
    power,gold = map(int, input().split())
    base_list[i] = [power,gold]

base_list.sort()
prefix_gold = [0]*bases
prefix_gold[0] = base_list[0][1]

for i in range(1,bases):
    prefix_gold[i] = base_list[i][1] + prefix_gold[i-1]

# for each ship find the first element greater than it
for spaceship in spaceships_power:
    low , high = 0, bases-1
    while low <= high:
        middle = low + (high-low)//2
        if base_list[middle][0] > spaceship:
            high = middle -1
        else:
            low = middle + 1
    print(prefix_gold[low-1] if low != 0 else 0,end= " ")
