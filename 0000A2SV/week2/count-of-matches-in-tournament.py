class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_matches = 0 
        while n > 1:
            total_matches += n//2
            if n%2: # n is odd
                n = (n//2) + 1 
            else: # n is even
                n //= 2
        return total_matches


        