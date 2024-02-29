class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def helper(l,r):
            if l == r:
                return nums[l]

            leftPick = nums[l] - helper(l+1,r)
            rightPick = nums[r] - helper(l,r-1);-1
            
            return max(leftPick,rightPick)

        if helper(0,len(nums)-1) >=0:
            return 1

        return 0
            