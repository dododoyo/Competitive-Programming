n = int(input())
guest_list,home_list = [0]*n,[0]*n
for i in range(n):
  uniform= input().split()
  home_list[i],guest_list[i] = uniform[0],uniform[1]

counter = 0
for home_uniform in home_list:
  for guest_uniform in guest_list:
    if home_uniform == guest_uniform:
      counter += 1
print(counter)