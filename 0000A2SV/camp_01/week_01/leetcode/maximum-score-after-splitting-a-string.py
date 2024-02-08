class Solution:
    def maxScore(self, s: str) -> int:
        zero_count = [int(s[0]=="0")]*len(s)
        one_count = [int(s[-1])]*len(s)
        for i in range(1,len(s)):
            zero_count[i] = (int(s[i]=="0")) + zero_count[i-1]
            one_count[len(s)-i-1] = int(s[len(s)-i-1]) + one_count[len(s)-i]

        # the first one is never counted in ones
        one_count[0] = one_count[1]
        # the last zero is never counted in zeros 
        zero_count[-1] = zero_count[-2]

        #handeling edge case when all the elements are one
        if len(s) == one_count[0]:return one_count[1]

        #handeliing the edge case when all the elements are zeros
        if len(s) == zero_count[-1]:return zero_count[-2]
        
        solution = one_count[0] + zero_count[0]
        for i in range(len(s)):
            solution = max(solution,one_count[i]+zero_count[i])
        return solution
        