class Solution:
    def maximumGap(self, nums: List[int]) -> int:  # Time: O(nlogn)
        if len(nums) < 2:return 0
        nums.sort()                           # O(nlogn)
        sol = nums[1]-nums[0]                 # O(1)
        for r in range(2,len(nums)):          #
            sol = max(sol,nums[r]-nums[r-1])  # O(n)
        return sol                            # O(1)