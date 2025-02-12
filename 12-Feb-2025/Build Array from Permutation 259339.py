# Problem: Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        solution = [0]*n

        for i in range(n):
            solution[i] = nums[nums[i]]

        return solution
        