# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        if len(heaters) == 1:
            return max([abs(heaters[0] - house) for house in houses])
        n = len(heaters)

        # find the closest heater for the house 
        def closest_heater(house):
            left,right,solution = 0,n-1,0

            while left <= right:
                middle = left + (right-left)//2
                if heaters[middle] == house:return heaters[middle]
                elif heaters[middle] < house:left = middle + 1
                else:right = middle -1

            # if both indeces are out of bound return their complement
            if right < 0:return heaters[left]
            if left >= n:return heaters[right]
            
            # if both indeces are in range return the closest
            if abs(heaters[left]-house) < abs(heaters[right]-house):return heaters[left]
            else:return heaters[right]

        houses.sort()
        heaters.sort()
        solution = -float("inf")
        for house in houses:
            solution = max(solution,abs(house-closest_heater(house)))

        return solution