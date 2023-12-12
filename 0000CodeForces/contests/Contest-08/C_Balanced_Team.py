# was present on previous contests

n = int(input())
studs = input().split()
studs = [int(i) for i in studs]

studs.sort()
l,r,sol = 0,0,0

while(r < len(studs)):
    if studs[r] - studs[l] < 6:
        sol = max(sol,r-l+1)
        r+=1
    else:
        l+=1
print(sol)
