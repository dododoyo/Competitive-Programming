n = int(input())
str_list = input().split()
int_list = [0]*n
for i in range(n):
    int_list[i] = int(str_list[i])
range_size = [0]*1001
for i in int_list:
    range_size[i] += 1
found = False
for i in range(1,999):
    if range_size[i] > 0 and range_size[i+1] > 0 and range_size[i+2] > 0:
        found = True;break
if found:
    print('YES')
else:
    print('NO')