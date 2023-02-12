class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        firstPointer = 0
        
        for i in range(len(haystack) - len(needle)+1):
            if needle == haystack[firstPointer:firstPointer+len(needle)]:
                return i
            firstPointer += 1
        return -1
        