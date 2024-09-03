# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        solution = [intervals[0]]

        for right in range(1,len(intervals)):
            if intervals[right][0] <= solution[-1][1]:
                end = max(intervals[right][1],solution[-1][1])
                solution[-1][1] = end
            else:
                solution.append(intervals[right])

        return solution
        