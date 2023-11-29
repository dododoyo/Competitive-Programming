# the maximum sum of the maximum by size (length) alternating subsequence of arr

def get_k(n,arr):
    max_=left=0
    for right in range(1,n):
        if same_sign(arr[right],arr[right-1]):
            left = right;
        max_ = max(max_,right-left+1);
    return max_

def get_max(n,k,arr):
    max_=left=0
    #expand the first window
    prefix_sum = [0]*(n+1)
    for i in range(k,n):
        max_ = max(max_,prefix_sum[i])
    
   
def same_sign(a,b):
    return True if ((a>0 and b>0)or(a<0 and b<0)) else False;
for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(get_k(n,arr))