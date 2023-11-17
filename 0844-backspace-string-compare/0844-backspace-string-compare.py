class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stk = []
        for char in s:
            if char == "#":
                if s_stk:s_stk.pop()
            else:s_stk.append(char)
        t_stk = []
        for char in t:
            if char == "#":
                if t_stk:t_stk.pop()
            else:t_stk.append(char)
        return t_stk == s_stk