# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights, days):
        def isValidCapacity(capacity):
            capacity_days, total_weight = 1, 0
            for weight in weights:
                total_weight += weight
                if total_weight > capacity:
                    capacity_days += 1
                    # start from current weight for the next iteration
                    total_weight = weight
                    if capacity_days > days:
                        return False
            return True

        low, high = max(weights), sum(weights)
        # the capacity of the ship is between the maximum weight and the sum of the weights
        while low <= high:
            middle = low + (high-low)//2
            # if it can be done we currnet capacity find lower capacities
            if isValidCapacity(middle):
                high = middle -1
            else:
                low = middle + 1
        return low