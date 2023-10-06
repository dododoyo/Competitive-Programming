class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = [0]*3
        for i in nums:freq[i] += 1;
        
        for i in range(freq[0]):nums[i] = 0
        for i in range(freq[1]):nums[i+freq[0]] = 1
        for i in range(freq[2]):nums[i+freq[0]+freq[1]] = 2
            
            
        return nums