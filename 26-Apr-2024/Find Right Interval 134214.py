# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n  = len(intervals)
        original_index = {interval[0]:index for index,interval in enumerate(intervals)}
        solution = [-1]*n
        intervals.sort() #nlogn

        for i in range(n): # (n-1)*log(n)
            current_start,current_end = intervals[i]
            left,right = 0,n-1
            j = -1
            while left <= right:
                middle = left + (right-left)//2
                if intervals[middle][0] >= current_end:
                    j = middle
                    right = middle - 1
                else:
                    left = middle + 1
            if j != -1:
                solution[original_index[current_start]] = original_index[intervals[j][0]]

        return solution