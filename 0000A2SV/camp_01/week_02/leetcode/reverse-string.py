class Solution:
    def reverseString(self, s: List[str]) -> None:
        self.helper(s,0,len(s)-1)
    def helper(self,s,left,right):
        if right > left:
            s[left],s[right] = s[right],s[left]
            self.helper(s,left+1,right-1)