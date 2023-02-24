from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #lets use a dictionary 
        solution = [0,0]
        eachElement = defaultdict(int)
        for i in range(len(nums)):
            if((target - nums[i]) in eachElement):
                solution[0] = eachElement[target - nums[i]]
                solution[1] = i
                break
            else:
                eachElement[nums[i]] = i
        return solution
                
        