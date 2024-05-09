# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        new_arr = [(capital[i],profits[i]) for i in range(len(profits))]
        new_arr.sort()
        max_heap,i = [],0

        while k:
            while i < len(profits) and w >= new_arr[i][0]:
                heappush(max_heap,-new_arr[i][1])
                i += 1

            if not max_heap:
                # there are no qualified capitals.
                break
                    
            w -= heappop(max_heap)
            k -= 1

        return w
