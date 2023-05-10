k = int(input());#punched
l = int(input());#tail
m = int(input());#paws
n = int(input());#mom
d = int(input())
sol = 0
for i in range(1,d+1):
    if i%k == 0 or i%l == 0 or i%m == 0 or i%n == 0:sol+=1;
print(sol)