def effective_approach():
    n = int(input()) #len of list
    a = [int(i) for i in input().split()]
    input()#no need to get the number of queries we can get it from the len of the queries list
    
    #arrays to register each elements index in each's perspective
    v_method = [0]*len(a)
    p_method = [0]*len(a)

    #initialize counters
    v,p=0,0
    queries = [int(i) for i in input().split()]

    #register the amount of moves needed for each element
    for j in range(len(a)):
        v_method[a[j]-1] = j+1
        p_method[a[j]-1] = len(a)-j

    for i in queries:
        v+=v_method[i-1]
        p+=p_method[i-1]
    #print results
    print(v,p)

effective_approach()