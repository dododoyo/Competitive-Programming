n_t = input().split()
n = int(n_t[0])
t = int(n_t[1])
s = list(input())
i = 0
for k in range(t):
    while(i < len(s)-1):
        if(s[i]=='B' and s[i+1]=='G'):
            s[i],s[i+1] = s[i+1],s[i]
            i+=2
        else:
            i+=1
    i = 0
print("".join(s))  

