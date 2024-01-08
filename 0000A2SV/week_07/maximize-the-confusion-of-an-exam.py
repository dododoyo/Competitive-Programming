class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max(self.getMax(answerKey,k,"T"),self.getMax(answerKey,k,"F"))
        
    def getMax(self, answerKey: str, k: int, char: str) -> int:
        # this function get the maximum number of continuous 
        # consequative elements with value 'char'
        left = 0
        for right in range(len(answerKey)):
            if answerKey[right] != char:k -= 1
            if k < 0:
                if answerKey[left] != char:
                    k += 1
                left += 1
        return right - left + 1
