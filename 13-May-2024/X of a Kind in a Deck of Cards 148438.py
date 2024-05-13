# Problem: X of a Kind in a Deck of Cards - https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = Counter(deck)
        count_values = list(counts.values())

        n = len(count_values)
        if 1 in count_values :
            return False

        for i in range(n-1) :
            for j in range(1+i, n) :
                if gcd(count_values[i], count_values[j]) == 1 :
                    return False
        return True