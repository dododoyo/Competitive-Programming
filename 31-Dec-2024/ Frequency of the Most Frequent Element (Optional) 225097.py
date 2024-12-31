# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # sort nums and use sliding window
        # create a window which is valid 

        # a window is valid if it can be changed 
        # to all same elements using atmost k moves

        left,running_sum = 0,0
        max_window_length = 0
        nums.sort()

        for right in range(len(nums)):
            running_sum += nums[right]

            # create a valid window

            if nums[right]*(right-left+1) > running_sum +k:
                running_sum -= nums[left]
                left += 1

            max_window_length = max(max_window_length,right-left+1)

        return max_window_length
            