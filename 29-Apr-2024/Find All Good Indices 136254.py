# Problem: Find All Good Indices - https://leetcode.com/problems/find-all-good-indices/

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        if k == 1: 
            return list(range(1,len(nums)-1))

        t_dict,solution = {},[]
        current_decreasing_index, current_increasing_index = 0,k+1
        
        for i in range(1, len(nums) - k - 1):
            if nums[i] > nums[i-1]:
                current_decreasing_index = i
            if i - current_decreasing_index + 1== k:
                t_dict[current_decreasing_index+k+1] = current_decreasing_index
                current_decreasing_index += 1

        for i in range(k+2,len(nums)):
            if nums[i] < nums[i-1]:
                current_increasing_index = i
            if i - current_increasing_index + 1 == k:
                if current_increasing_index in t_dict:
                    solution.append(current_increasing_index - 1)
                current_increasing_index += 1

        return solution