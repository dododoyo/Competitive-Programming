class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_freq,solution   = [0]*101,[0]*len(nums)
        minn = min(nums)
        for number in nums:nums_freq[number] += 1
        for i in range(1,101):nums_freq[i] += nums_freq[i-1]
        for i in range(len(nums)):
            if nums[i] == minn:
                solution[i] = 0
            else:
                solution[i] = nums_freq[nums[i]-1]
        return solution