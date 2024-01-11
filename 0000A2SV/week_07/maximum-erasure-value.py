class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # return the subarray with unique elements and maximum sum

        # get all of the subarrays with unique elements 
        # register each sum of a valid subarray
        # register the max_sum from all the sums of the subarrays
        window_set,curr_sum,max_sum,left = set(),0,0,0
        for right in range(len(nums)):
            if nums[right] in window_set:
                while nums[right] != nums[left]:
                    window_set.remove(nums[left])
                    curr_sum -= nums[left]
                    left += 1
                window_set.remove(nums[left])
                curr_sum -= nums[left]
                left += 1   
            window_set.add(nums[right])
            curr_sum += nums[right]
            max_sum = max(max_sum,curr_sum)
        return max_sum
