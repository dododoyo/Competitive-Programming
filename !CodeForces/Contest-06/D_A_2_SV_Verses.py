#failed on test 3
def count_subarrays(n, a, b, problems):
    l=eligible_count = 0 
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + problems[i - 1]
    for r in range(n+1):
        while prefix_sum[r]-prefix_sum[l]>b:l+=1
        if a<= prefix_sum[r]-prefix_sum[l] <= b:eligible_count+=1;l=r
    return eligible_count

n,a,b = map(int,input().split())
students = list(map(int,input().split()))
print(count_subarrays(n,a,b,students))
