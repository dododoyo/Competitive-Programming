class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = sum(nums[:3])
        nums.sort() # nlogn
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            current_sum = 0
            while left < right:
                current_sum = nums[left]+nums[right]+nums[i]
                if current_sum > target:
                    right -= 1
                elif current_sum < target:
                    left +=1
                else:
                    return target
                if self.absLT(closest-target) > self.absLT(current_sum-target):
                    closest = current_sum
        return closest
    def absLT(self,num):
        return (-1*num) if num < 0 else num;
                
        
        