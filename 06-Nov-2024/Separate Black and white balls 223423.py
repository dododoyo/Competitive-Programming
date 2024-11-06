# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        solution,ones_count = 0,0
        """
        When we see a one we count
        When we see a zero we add the number of ones counted before it 
        Because all of the ones before it has to be swapped"""
        
        for i in range(len(s)):
            if s[i] == "1":
                ones_count += 1
            else:
                solution += ones_count
        return solution
        