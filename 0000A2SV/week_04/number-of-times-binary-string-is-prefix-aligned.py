class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        summ,solution = 0,0
        for i in range(len(flips)):
            summ += flips[i]
            if ((i+1)*(i+2))//2 == summ:
                solution +=1
        return solution
