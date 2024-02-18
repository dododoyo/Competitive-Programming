class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_map ={")":"(","}":"{","]":"["}
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if stack and stack[-1] == valid_map[char]:
                    stack.pop()
                else:
                    return False
        return not stack
        