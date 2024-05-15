# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ%2:
            return False

        dp = [[-1 for _ in range((summ//2)+1)]for _ in range(len(nums))]
        n = len(nums)
        def find_target(index,target):
            if nums[index] == target:
                return True
            if (index == n -1 and nums[index] != target) or (target < 0):
                return False

            next_target = target-nums[index]
            next_index = index+1

            take = find_target(next_index,next_target) if dp[next_index][next_target] == -1 else  dp[next_index][next_target]
            not_take = find_target(next_index,target) if dp[next_index][target] == -1 else dp[next_index][target]

            dp[index][target] = take or not_take
            return dp[index][target]

        return find_target(0, summ//2)
            