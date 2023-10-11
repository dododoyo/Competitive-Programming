class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        bob,me,alc = 0,len(piles)-2,len(piles)-1
        sol = 0
        while bob < me:
            sol += piles[me]
            bob,me,alc = bob+1,me-2,alc-2
        return sol
        