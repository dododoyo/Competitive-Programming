a,c=[],0
for _ in range(int(input())):
    a.append([int(i) for i in input().split()])

for x in a:
    r,l,d,u=0,0,0,0
    for y in a:
        if x!=y:
            if x[0]==y[0]:
                if x[1]<y[1]:d+=1
                elif x[1]>y[1]:u+=1
            if x[1]==y[1]:
                if x[0]<y[0]:l+=1
                elif x[0]>y[0]:r+=1
    if r and d and l and u:c+=1
print(c)