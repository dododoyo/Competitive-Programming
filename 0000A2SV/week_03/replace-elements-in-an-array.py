from collections import defaultdict
class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        number_map = defaultdict(int)
        for index,number in enumerate(nums):
            number_map[number] = index
        solution = []
        for each_operation in operations:
            index = number_map.pop(each_operation[0])
            solution.append(each_operation[1])
            number_map[each_operation[1]] = index
        for each_key in number_map.keys():
            nums[number_map[each_key]] = each_key
        return nums
        