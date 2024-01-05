class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        right,solution = 0,set()
        nums.sort()
        for right in range(len(nums)-2):
            target = -1 * nums[right]
            found_pair = self.searchPair(target,nums,right+1)
            if found_pair:
                for pair in found_pair:
                    solution.add((nums[right],pair[0],pair[1]))
        return list(solution)
        
    def searchPair(self,target,nums,start):
        left,right = start,len(nums)-1
        solution = []
        while left < right:
            if nums[right] + nums[left] > target:right -= 1
            elif nums[right] + nums[left] < target:left += 1
            else:
                solution.append((nums[left],nums[right]))
                left,right = left+1,right-1
        return solution
