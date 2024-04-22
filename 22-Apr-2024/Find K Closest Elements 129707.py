# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        min_heap = []
        for number in arr:
            heapq.heappush(min_heap,[abs(number-x),number])
        return sorted([heapq.heappop(min_heap)[1] for _ in range(k)])