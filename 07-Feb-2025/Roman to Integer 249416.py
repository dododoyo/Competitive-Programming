# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        value_map = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}\

        # start from the back 
        index = len(s)-1
        solution = 0

        while index > -1:
            if index > 0 and value_map[s[index]] > value_map[s[index-1]]:
                solution += value_map[s[index]] - value_map[s[index-1]]
                index -= 2
            else:
                solution += value_map[s[index]]
                index -= 1
        
        return solution


        