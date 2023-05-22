n = int(input())
cities = list(map(int,input().split()))
min_distance = 1000000001
min_index = 0
double_exists = False
for i in range(n):
    if cities[i] < min_distance:
        min_distance = cities[i];double_exists = False;min_index = i
    elif cities[i] == min_distance:
        min_distance = cities[i];double_exists = True;min_index = i
print('Still Rozdil') if double_exists else print(min_index+1)