# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)

        if summ % 2:
            return False

        half = summ//2

        target = half
        n = len(nums)
        memo = [[False for i in range(target+1)] for _ in range(n)]
        # index, target 

        # for any index if the target is zero 
        # we have found a subsequence 
        for i in range(n):
            memo[i][0] = True

        # if the target is equal to the element 
        # this is a solution as well 
        if target >= nums[0]:
            memo[0][nums[0]] = True
        

        for index in range(1,n):
            for tg in range(1,target+1):
                take = False
                not_take = memo[index-1][tg]

                if nums[index] <= tg:
                    take = memo[index-1][tg-nums[index]]

                memo[index][tg] = take or not_take

        return memo[n-1][target]