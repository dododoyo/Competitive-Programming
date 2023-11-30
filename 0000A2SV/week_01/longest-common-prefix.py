class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum_string_length = 2000
        for string in strs:
            minimum_string_length = min(minimum_string_length,len(string))
        i = 0
        while i < minimum_string_length:
            for each_string in strs:
                if each_string[i] != strs[0][i]:
                    return strs[0][:i] if i != 0 else ""
            i +=1 
        return strs[0][:i] 