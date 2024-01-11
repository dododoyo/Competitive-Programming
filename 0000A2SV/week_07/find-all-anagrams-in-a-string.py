class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_map,window_map= [0]*26,[0]*26
        offset,solution = ord("a"),[]
        for right in range(len(s)):
            if right < len(p):
                p_map[ord(p[right]) - offset] += 1
                window_map[ord(s[right]) - offset] += 1
            else:
                window_map[ord(s[right]) - offset] += 1
                window_map[ord(s[right-len(p)]) - offset] -= 1
            # by using (right > len(p)-2)  we make sure we also check for the frist window
            if (right > len(p)-2) and p_map == window_map:
                solution.append(right-len(p)+1)
        return solution
        