class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurance = [0]*26
        for i in range(len(s)):
            last_occurance[ord(s[i])-97]  = i
        left,inner= 0, 0
        right = last_occurance[ord(s[left])-97]
        solution = []
        while right < len(s):
            while inner < right:
                if last_occurance[ord(s[inner])-97] > right:
                    right = last_occurance[ord(s[inner])-97]
                inner +=1
            solution.append(right-left+1)
            if right != len(s)-1:
                left = right + 1
                right = last_occurance[ord(s[left])-97]
                inner = left
            else:
                break

            
        return solution
            
        
        