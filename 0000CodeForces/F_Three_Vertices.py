from sys import stdin
def input(): return stdin.readline().strip()
def ls(): return [int(i) for i in input().split()]

def furthest_bfs(start_nodes,n):
    distance = [0]*n
    current_level = []

    for node in start_nodes:
        distance[node]=1
        current_level.append(node)

    last_node = -1
    while current_level:
        next_level = []
        for node in current_level:
          last_node = node
          for nghbr in tree[node]:
              if distance[nghbr] == 0:
                  parent[nghbr]=node
                  next_level.append(nghbr)

                  distance[nghbr]=distance[node]+1

        current_level = next_level[:]

    return last_node,distance[last_node]

############3333333333333333333333

vertices = ls()[0]
parent = [-1]*vertices
tree = [[] for _ in range(vertices)]

# build tree
for _ in range(vertices-1):
    x,y = ls()
    tree[x-1].append(y-1)
    tree[y-1].append(x-1)

furthest_node, d = furthest_bfs([0],vertices)
second_furthest, distance = furthest_bfs([furthest_node],vertices)

# make furthest the parent
parent[furthest_node] = -1
curr = second_furthest

# construct path between the two furthest
current_level = []
while curr != -1:
    current_level.append(curr)
    curr = parent[curr]

# perform bfs on path
third_furthest, max_width = furthest_bfs(current_level,vertices)

# linkedlist
if third_furthest == furthest_node or third_furthest == second_furthest:
    x=0
    while x in [furthest_node, second_furthest]:
        x+=1
    third_furthest = x

print(distance+max_width-2)
print(furthest_node+1, second_furthest+1, third_furthest+1)