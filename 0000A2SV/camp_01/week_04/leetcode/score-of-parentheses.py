class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack,score = [],0
        for char in s:
            if char == "(":
                stack.append(score)
                score = 0
            else:
                # consequative popping must be registered 
                last = stack.pop()
                if score == 0:
                    score = last + 1
                else:
                    score = last + 2*score  
        return score