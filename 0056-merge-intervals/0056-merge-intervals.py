class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        intervals.sort(key = lambda i : i[0])
        solution = [intervals[0]]
        for i in range(1,len(intervals)):
            if(solution[-1][1] < intervals[i][0]):solution.append(intervals[i])
            else:solution[-1][1]  = max(intervals[i][1],solution[-1][1])
        return solution