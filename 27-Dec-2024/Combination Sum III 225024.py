# Problem: Combination Sum III - https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def backtrack(self,running_sum,elements,start):

        # edge-cases
        if elements == self.k:
            if running_sum == self.n:
                self.valid_combinations.append(self.tracking_array[:])
            return 

        # continue finding 
        for i in range(start,10):
            self.tracking_array.append(i)
            self.backtrack(running_sum+i,elements+1,i+1)
            self.tracking_array.pop()


    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.k = k
        self.n = n
        self.valid_combinations = []
        self.tracking_array = []

        # find valid combinations
        self.backtrack(0,0,1)

        return self.valid_combinations