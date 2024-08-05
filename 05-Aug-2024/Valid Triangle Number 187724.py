# Problem: Valid Triangle Number - https://leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        sol = 0
        for last in range(2,len(nums)):
            left,middle = 0,last-1
            # middle will always be the one before the last
            while left < middle:
                if nums[left] + nums[middle] > nums[last]:
                    # because whatever after left is greater 
                    # than it we don't need to iterate over 
                    # those we can just add our window size to the sol
                    sol += middle-left
                    middle -= 1
                else:
                    left += 1
        return sol