# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def backtrack(self,curr_sum,index):
        if index >= len(self.candidates):
            return 

        if curr_sum > self.target:
            return 

        if curr_sum == self.target:
            self.valid_combinations.append(self.track[:])
            return 

        # take
        self.track.append(self.candidates[index]) 
        self.backtrack(curr_sum+self.candidates[index],index)
        
        self.track.pop()
        # not take 
        self.backtrack(curr_sum,index+1)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.target = target

        self.valid_combinations = []
        self.track = []
        
        # find possible sums
        self.backtrack(curr_sum=0,index=0)

        return self.valid_combinations