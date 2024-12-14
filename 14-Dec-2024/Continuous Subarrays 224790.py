# Problem: Continuous Subarrays - https://leetcode.com/problems/continuous-subarrays/

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        solution, left, n = 0, 0, len(nums)
        min_heap, max_heap = [], []

        for right in range(n):
            heappush(min_heap,[nums[right],right])
            heappush(max_heap,[-nums[right],right])

            # while the diff between max and min is 
            # greater than 2 minimize the window size 
            while (-max_heap[0][0] - min_heap[0][0]) > 2:
                left += 1
                # remove min and max elements 
                # that are outside of the window 
                while min_heap and min_heap[0][1] < left:
                    heappop(min_heap)

                while max_heap and max_heap[0][1] < left:
                    heappop(max_heap)

            # register current window size in solution 
            solution += right - left + 1

        return solution