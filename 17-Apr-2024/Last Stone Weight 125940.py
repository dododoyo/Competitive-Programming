# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # O(n) to change stones into a heap

        # O(logn) to find maxes each time 
        # If we play n times => overall complexity O(nlogn)

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            if s1 != s2:
                heapq.heappush(stones,s1-s2)
            # if they are equal don't  push them back
        
        return abs(stones[0]) if stones  else 0