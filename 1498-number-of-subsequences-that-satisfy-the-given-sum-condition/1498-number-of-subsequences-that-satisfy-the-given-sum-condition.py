class Solution:
     def numSubseq(self, A, target):
        A.sort()
        l,res,r = 0,0,len(A)-1
        while l <= r:
            if A[l] + A[r] > target:r -= 1
            else:res += pow(2, r - l, (10**9 + 7));l += 1
        return res % (10**9 + 7)