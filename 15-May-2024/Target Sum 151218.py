# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(lambda : -1)
        n = len(nums)

        def find_target(index,target):
            if (index == n):
                return target == 0

            next_index = index+1
            target_after_addition = target-nums[index]
            target_after_subtraction = target+nums[index]

            add_current = find_target(next_index,target_after_addition) if dp[(next_index,target_after_addition)] == -1 else dp[(next_index,target_after_addition)]
            subtract_current = find_target(next_index,target_after_subtraction) if dp[(next_index,target_after_subtraction)] == -1 else dp[(next_index,target_after_subtraction)]

            dp[(index,target)] = add_current + subtract_current 

            return dp[(index,target)]

        return find_target(0,target) 