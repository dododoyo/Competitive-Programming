class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        bob,me,alice = 0,len(piles)-2,len(piles)-1
        sol = 0
        while bob < me:
            sol += piles[me]
            me -= 2
            alice -= 2
            bob += 1
        return sol;
        