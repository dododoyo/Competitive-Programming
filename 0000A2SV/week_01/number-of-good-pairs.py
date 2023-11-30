class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        frequency_array = [0]*101
        for number in nums:
            frequency_array[number] += 1
        solution = 0
        for frequency in frequency_array:
            solution += (frequency*(frequency-1))//2
        return solution
        