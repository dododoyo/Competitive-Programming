# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < k*m:
            return -1
        # function to check if we can find 
        # k adjacent flowers "m" times 
        # with the given day

        def canMakeBouquets(date):
            valid_count,adjacent_flowers = 0,0
            for day in bloomDay:
                # id the day of bloom is greater than
                # the date given we can't add to bouquet
                if day > date:
                    adjacent_flowers = 0
                else:
                    adjacent_flowers += 1
                
                if adjacent_flowers >= k:
                    valid_count += 1
                    adjacent_flowers = 0
            return valid_count >= m


        low,high = min(bloomDay),max(bloomDay)
        solution = float('inf')
        while low <= high:
            middle = low + (high-low)//2
            if canMakeBouquets(middle):
                solution = middle
                # still find a lower day
                high = middle - 1
            else:
                low = middle + 1

        return solution