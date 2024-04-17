# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        while k:
            current_max = -heapq.heappop(piles)
            new_element = current_max - current_max//2
            heapq.heappush(piles,-new_element)
            k -= 1

        return -sum(piles)