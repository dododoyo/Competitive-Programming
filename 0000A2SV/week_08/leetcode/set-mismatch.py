class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mp = {i: 1 for i in range(1, len(nums) + 1)}
        for a in nums:mp[a] -= 1
        duplicate, missing = 0, 0
        for key, value in mp.items():
            if value < 0:duplicate = key
            if value == 1:missing = key
        return [duplicate, missing]