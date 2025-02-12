# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i in range(len(nums)):
            num1 = nums[i]
            # target = num1 + num2 => num2 = target - num1
            num2 = target-num1

            if num2 in index_map:
                return [i,index_map[num2]]

            index_map[num1] = i