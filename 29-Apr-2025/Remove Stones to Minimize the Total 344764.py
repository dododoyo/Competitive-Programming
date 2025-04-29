# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

from heapq import heapify,heappop,heappush

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapify(piles) #O(n)
    
        for j in range(k):
            current_max = -heappop(piles)
            new_element = current_max - current_max//2
            
            heappush(piles,-new_element)
                    
        return -sum(piles)
            
        