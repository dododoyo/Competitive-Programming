# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        solution = [intervals[0]]
        for right in range(1,len(intervals)):
            if solution[-1][1] >= intervals[right][0]:
                last = max(solution[-1][1],intervals[right][1]);
                solution[-1][1] = last
            else:
                solution.append(intervals[right]);
        return solution