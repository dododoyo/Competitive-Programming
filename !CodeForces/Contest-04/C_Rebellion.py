# given a binary array find number of minimum operation to make non-decreasing
t = int(input())
for _ in range(t):
    n = int(input())
    a = input().split()
    a = [int(i) for i in a] 
    
    sol= 0
    i,j = 0,len(a)-1
    while(i < j):
        #look for first 1 from left and first 0 from right
        while( i < j and a[i] == 0 ):i+=1
        while( i < j and a[j] == 1):j-=1
        #if 1 is on left and 0 is on right then swap them
        #and count the swap as an operation
        if a[i] == 1 and a[j] == 0:
            sol+=1;i+=1;j-=1
    print(sol)
