#a form of prefix sum
t = int(input())
for j in range(t):
    n,k = map(int,input().split())
    each_list = list(map(int,input().split()))
    each_list.sort()

    #removes the last maxes in the sum
    max_sum = new_sum = sum(each_list[:n-k])

    for i in range(k):
        new_sum += each_list[n-k+i] - each_list[2*i] - each_list[2*i+1]
        max_sum = max(max_sum,new_sum)
    print(max_sum)

