class NumArray:

    def __init__(self, nums: List[int]):
        self.the_number = nums
        

    def sumRange(self, left: int, right: int) -> int:
        self.sum = 0
        for i in range(left,right+1): # + 1 added to make it inclusive
            self.sum += self.the_number[i]
        
        return self.sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)