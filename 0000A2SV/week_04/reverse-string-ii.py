class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]
        list_s = [*s]
        start = 0
        while start < len(s) -k+1:
            list_s = self.helper(list_s,start,start+k)
            start += 2*k
        if len(s) > 2*k:list_s = self.helper(list_s,start,len(s))
        return "".join(list_s)
    def helper(self,list_s,start,end):
        while start < end:
            list_s[start],list_s[end-1] = list_s[end-1],list_s[start]
            start += 1
            end -= 1
        return list_s

        