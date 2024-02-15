class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # we will always have a minimum array of 1 for the first interval
        points.sort()
        prev_end,arrows,n = points[-1][0],1,len(points)
        for i in range(1,n):
            current_point = points[n-i-1]
            if not (current_point[0] <= prev_end and current_point[1] >= prev_end):
                prev_end = current_point[0]
                arrows += 1
        return arrows