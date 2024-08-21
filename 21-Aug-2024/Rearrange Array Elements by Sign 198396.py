# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        solution = [0]*n
        positive_pointer,negative_pointer = 0,1
        
        for number in nums:
            if number < 0:
                solution[negative_pointer] = number
                negative_pointer += 2
            else:
                solution[positive_pointer] = number
                positive_pointer += 2

        return solution