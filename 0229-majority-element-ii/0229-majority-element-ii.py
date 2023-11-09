from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        number_frequency = defaultdict(int)
        for number in nums:number_frequency[number] += 1
        solution = []
        for number in number_frequency:
            if number_frequency[number] > len(nums)//3:solution.append(number)
        return solution
        