s, n = map(int, input().split())
dragons = []
for i in range(n):
    x, y = map(int, input().split())
    dragons.append((x, y))
dragons.sort(key=lambda sublist: sublist[0])
for dragon in dragons:
    if s > dragon[0]:s += dragon[1]
    else:
        print("NO");exit()
print("YES")
