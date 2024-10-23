# Problem: Two Sum - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_map = defaultdict(int)

        for i in range(len(nums)):
            if target-nums[i] in number_map:
                return number_map[target-nums[i]],i
            else:number_map[nums[i]] = i
