class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack, invalids = [], 0
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")" and stack:
                stack.pop()
            else:
                invalids += 1
                
        return len(stack) + invalids