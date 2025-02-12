# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):nums[(nums[i])%n] += n

        solution = []

        for i in range(n):
            if nums[i] // n > 1:
                solution.append(i)

        return solution