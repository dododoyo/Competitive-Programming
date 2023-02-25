class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        length_ = len(colors)
        p1 = length_ - 1
        max_len = 0
        
        for i in range(length_):
            
            if(colors[p1] != colors[i]):
                max_len = max(max_len,p1-i)
                break
            
        p1 = 0
        for j in range((length_-1),-1,-1):
            if(colors[j] != colors[p1]):
                max_len = max(max_len,j-p1)
                break
            
        return max_len
        