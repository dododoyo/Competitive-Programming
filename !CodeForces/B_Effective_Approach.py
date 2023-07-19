def vasya_and_petya_approach(a,e):
    for i in range(len(a)):
        if a[i] == e:
            return i+1 , len(a)-i


def effective_approach():
    #counters for vasya and petya
    v,p = 0,0
    n = int(input()) #len of list
    a = [int(i) for i in input().split()]
    input()#no need to get the number of queries we can get it from the len of the queries list
    queries = [int(i) for i in input().split()]
    for i in queries:
        v += vasya_and_petya_approach(a,i)[0]
        p += vasya_and_petya_approach(a,i)[1]
    #return results
    print(v,p)

effective_approach()