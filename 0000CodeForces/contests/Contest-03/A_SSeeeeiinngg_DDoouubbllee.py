from collections import defaultdict
#take the number of test cases 
t = int(input())
for i in range(t):
    #take the string
    s = input()
    double_s = ['a']*2*len(s)
    (i,j) = (0,2*len(s)-1)
    for k in s:
        double_s[i] = k;double_s[j] = k
        i+=1;j-=1

    print("".join(double_s))