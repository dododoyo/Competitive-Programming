from heapq import heappush, heappop

n, k, q = map(int, input().split())
friends = list(map(int, input().split()))
online, online_now = [],0

for _ in range(q):
    
    type, id = map(int, input().split())

    if type == 1:
        heappush(online, (friends[id - 1], id))
        # print(online)
        if online_now < k:
            online_now += 1
        else:
            heappop(online)
    
    elif type == 2:
        # print(friends,id)
        if (friends[id -1], id) in online:
            print('YES')
        else:
            print('NO')
