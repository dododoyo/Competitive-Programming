class Solution:
    def largestOddNumber(self, num: str) -> str:
        for number_index in range(len(num)-1,-1,-1):
            if int(num[number_index])%2:
                return num[:number_index+1]
        return ""