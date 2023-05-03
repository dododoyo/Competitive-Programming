class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i in ["(","{","["]:
                stk.append(i)
            elif len(stk) != 0 and stk[-1] == '{' and i == '}':
                stk.pop()
            elif len(stk) != 0 and stk[-1] == '[' and i == ']':
                stk.pop()
            elif len(stk) != 0 and stk[-1] == '(' and i == ')':
                stk.pop()
            else:
                return False
        return len(stk) == 0