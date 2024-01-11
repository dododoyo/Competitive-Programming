class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len,left,char_set = 0,0,set()
        for right in range(len(s)):
            if s[right] in char_set:
                while s[left] != s[right]:
                    char_set.remove(s[left])
                    left += 1
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len,right-left+1)
        return max_len
                