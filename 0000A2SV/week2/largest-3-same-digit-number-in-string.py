class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_number = -1
        for i in range(2,len(num)):
            if num[i-1] == num[i-2] and num[i-1] == num[i]:
                max_number = max(max_number,int(num[i])) 
        return ""  if max_number == -1 else str(max_number)*3;