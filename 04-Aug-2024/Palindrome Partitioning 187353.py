# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/



class Solution:
    def partition(self, s: str) -> List[List[str]]:
        solution = []
        def dp(i, current):
            if i >= len(s):
                solution.append(current.copy())
                return 

            for j in range(i, len(s)):
                if palindrome(i, j):
                    current.append(s[i:j+1])
                    dp(j+1, current)
                    current.pop()

            return solution

        def palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left=left+1 
                right=right-1
            return True
        
        return dp(0, [])
