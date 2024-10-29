# Problem: Next Permutation - https://leetcode.com/problems/next-permutation/description/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # starting from the back find the point where you need to change
        break_point = -1
        n = len(nums)

        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                break_point = i-1
                break
        if break_point == -1:
            nums.reverse()
            return nums

        # find next greater number
        for i in range(n-1,-1,-1):
            if nums[break_point] < nums[i]:
                    # and swap the two numbers 
                    nums[i],nums[break_point] = nums[break_point],nums[i]
                    break

        # reverse manually
        # because it was previously reverse sorted
        left,right  = break_point+1,n-1
        while left < right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
