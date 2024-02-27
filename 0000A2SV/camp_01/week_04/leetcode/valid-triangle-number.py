class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        solution = 0
        for last in range(2,len(nums)):
            left,middle = 0,last-1
            while left < middle:
                if nums[left] + nums[middle] > nums[last]:
                    # because whatever after left is greater 
                    # than it we don't need to iterate over 
                    # those we can just add our window size to the solution
                    solution += middle-left
                    middle -= 1
                else:
                    left += 1
        return solution