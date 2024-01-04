class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max_distance,right  = points[1][0]-points[0][0],2
        while right < len(points):
            max_distance = max(max_distance,points[right][0]-points[right-1][0])
            right += 1
        return max_distance
        