from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #brute_force approach
        freq_dictionary = defaultdict(int)
        for each_number in nums:
            freq_dictionary[each_number] += 1
        solution = []
        for each_number in freq_dictionary.keys():
            if freq_dictionary[each_number] > len(nums)//3:
                solution.append(each_number)
        return solution