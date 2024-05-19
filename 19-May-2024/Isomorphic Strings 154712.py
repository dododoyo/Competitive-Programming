# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        last_s = defaultdict(lambda : -1)
        last_t = defaultdict(lambda : -1)
        n = len(s)

        if n != len(t):return False

        for i in range(n):
            if last_s[s[i]] != last_t[t[i]]:
                return False

            last_s[s[i]] = i
            last_t[t[i]] = i
        return True