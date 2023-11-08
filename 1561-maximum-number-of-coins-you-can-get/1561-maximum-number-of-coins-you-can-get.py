class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        remaining_chances = len(piles)//3
        my_position = -2
        while remaining_chances:
            total += piles[my_position]
            my_position -= 2
            remaining_chances -= 1
        return total
            
            