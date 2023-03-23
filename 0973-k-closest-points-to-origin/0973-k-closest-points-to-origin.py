class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda i : i[0]**2 + i[1]**2)
        return points[:k]