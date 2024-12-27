# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def backtrack(self,current_sum,index):
        if index > len(self.candidates)-1:
            return 
        if current_sum > self.target:
            return 

        if current_sum == self.target:
            self.valid_combinations.append(self.track[:])
            return 
        
        next_sum = current_sum+self.candidates[index]

        self.track.append(self.candidates[index])
        take = self.backtrack(next_sum,index)
        self.track.pop()

        not_take = self.backtrack(current_sum,index+1)
        

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:         
        self.candidates, self.target = candidates ,target

        self.valid_combinations = []
        self.track = []

        self.backtrack(current_sum=0,index=0)

        return self.valid_combinations