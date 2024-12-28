# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:

    def backtrack(self,index,path):
        self.solution.append(path)

        for i in range(index,len(self.nums)):
            self.backtrack(i+1,path+[self.nums[i]])
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.solution = []

        self.backtrack(0,[])

        return self.solution
