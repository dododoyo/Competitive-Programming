class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # initialize variables
        solution = sum(nums[:3])
        # sort the array
        nums.sort()
        # use three pointers one for each element other for two 
        for number in range(len(nums)-2):
            left = number+1
            right = len(nums)-1
            current_sum = 0
            while left < right:
                current_sum =  nums[left]+nums[right]+nums[number]
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum
                if (abs(current_sum-target) < abs(solution-target)):
                    solution = current_sum
        return solution
    