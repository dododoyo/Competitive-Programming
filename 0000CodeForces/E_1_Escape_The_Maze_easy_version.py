for _ in range(int(input())):
  input()
  rooms,k = map(int,input().split())
  graph = [[] for _ in range(rooms)]
  frens = [int(num)-1 for num in input().split()]
  for _ in range(rooms-1):
    n1,n2 = map(int,input().split())
    graph[n1-1].append(n2-1)
    graph[n2-1].append(n1-1)

  frens_time = [0]*rooms
  # print(graph)
  # print(frens)

  current_level = frens
  visited = set()
  level = 0
  while current_level:
    next_level = []
    for node in current_level:
      if node not in visited:
        visited.add(node)
        frens_time[node] = level
        for nghbr in graph[node]:
          if nghbr not in visited:
            next_level.append(nghbr)
    current_level = next_level
    level += 1

  current_level = [0]
  visited = set()
  vlad_time = [0]*rooms
  level = 0

  while current_level:
    next_level = []
    for node in current_level:
      if node not in visited:
        visited.add(node)
        vlad_time[node] = level
        for nghbr in graph[node]:
          if nghbr not in visited:
            next_level.append(nghbr)
    current_level = next_level
    level += 1

  can_reach = False
  for i in range(rooms):
    if i!= 0 and len(graph[i]) == 1 and vlad_time[i] < frens_time[i]:
      can_reach = True
      break
  print("YES" if can_reach else "NO")