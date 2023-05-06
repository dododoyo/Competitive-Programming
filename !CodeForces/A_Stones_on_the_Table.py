n = int(input())
s = list(input())
sol = 0
for i in range(1,n):
    if s[i-1] == s[i]:
        sol += 1
print(sol)
