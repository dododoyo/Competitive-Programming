# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        all_nums = set()
        for r in ranges:
            for x in range(r[0],r[1]+1):
                all_nums.add(x)

        required_range = set()
        for j in range(left,right+1):
            required_range.add(j)

        return required_range <= all_nums