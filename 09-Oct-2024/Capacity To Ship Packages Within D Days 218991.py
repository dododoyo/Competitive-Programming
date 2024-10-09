# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights, days):
        def isValidCapacity(capacity):
            shipping_days, total_weight = 1, 0

            for weight in weights:
                total_weight += weight

                if total_weight > capacity:
                    shipping_days += 1
                    total_weight = weight

            return shipping_days <= days

        low, high = max(weights), sum(weights)
        solution = high
        # the capacity of the ship is between the maximum weight and the sum of the weights
        while low <= high:
            middle = low + (high-low)//2
            # if it can be done we currnet capacity still find lower capacities
            if isValidCapacity(middle):
                solution = middle
                high = middle -1
            else:
                low = middle + 1
        return solution