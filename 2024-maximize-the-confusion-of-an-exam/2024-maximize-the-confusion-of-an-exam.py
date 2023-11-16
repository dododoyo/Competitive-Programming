class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max(self.maxConsecutiveSame("T",answerKey,k),self.maxConsecutiveSame("F",answerKey,k))
    def maxConsecutiveSame(self,value,answerKey,k):
        left = 0
        for right in range(len(answerKey)):
            k -= answerKey[right] != value
            if k < 0: 
                k += answerKey[left] != value
                left +=1
        return right-left+1