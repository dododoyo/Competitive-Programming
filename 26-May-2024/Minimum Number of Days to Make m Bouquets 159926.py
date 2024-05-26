# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def canMakeBouquets(day,n):
            can_take = [0]*n
            for i in range(n):
                if bloomDay[i] <= day:
                    can_take[i] = 1
            adjacent_k, adjacent_count = 0, 0

            for i in range(n):
                if can_take[i] == 1:adjacent_count += 1
                else:adjacent_count = 0

                if adjacent_count == k:
                    adjacent_k += 1
                    adjacent_count = 0

            # how many k adacent 1's are there in can_take
            return adjacent_k >= m

        n = len(bloomDay)
        min_day,max_day = float("inf"),-float("inf")
        for day in bloomDay:
            if day < min_day:min_day = day
            if day > max_day:max_day = day
            
        low,high = min_day,max_day
        while low <= high:
            middle = low + (high-low)//2
            if canMakeBouquets(middle,n):
                high = middle - 1
            else:
                low = middle + 1
        return -1 if low > max_day else low