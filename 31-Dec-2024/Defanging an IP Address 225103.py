# Problem: Defanging an IP Address - https://leetcode.com/problems/defanging-an-ip-address/description/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        solution = []

        for c in address:   
            if c == '.':
                solution.append('[.]')
            else:
                solution.append(c)

        return ''.join(solution)      