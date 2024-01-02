for _ in range(int(input())):
  # n     ,    m
  villagers,chairs = map(int,input().split())
  pref = [int(i) for i in input().split()]
  if villagers > chairs:
    print("NO")
  else:
    pref.sort()
    max_chairs = pref[-1]
    for i in range(1, villagers):
        max_chairs = max(max_chairs,pref[i]+i)
    if max_chairs > chairs:
        print('NO')
    else:
        print('YES')
    # print(chairs)