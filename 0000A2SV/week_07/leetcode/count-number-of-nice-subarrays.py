class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # returns the number of subarrays with k odd numbers inside them
        count,odd_count,solution = 0,0,0
        left = 0
        for right in range(len(nums)):
            if nums[right]%2 != 0:
                odd_count += 1
                count = 0
            
            if odd_count == k:
                while(nums[left]%2 == 0):
                    count,left = count+1,left+1
                count,left = count+1,left+1
                odd_count -= 1

            solution += count
        return solution