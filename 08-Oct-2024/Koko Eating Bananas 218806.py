# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isPossible(eating_speed):
            total_time = 0
            for pile in piles:
                total_time += ceil(pile/eating_speed)
            return total_time <= h
        # maximum speed koko can have is 
        # the maximum number of 
        # bananas from the pile

        # use binary search to find the minimum 
        # speed of eating that allows him to finish 


        low ,high = 1,max(piles)
        solution = high

        while low <= high:
            mid = low + (high-low)//2

            if isPossible(mid):
                # find lower speed still
                solution = mid
                high = mid - 1
            else:
                low = mid + 1
        return solution
                