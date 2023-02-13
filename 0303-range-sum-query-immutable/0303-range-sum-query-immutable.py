class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_summed = nums
        
        for i in range(1,len(nums)):
            self.prefix_summed[i] = self.prefix_summed[i] + self.prefix_summed[i-1]
           
    def sumRange(self, left: int, right: int) -> int:
       
        if(left > 0): 
            return self.prefix_summed[right] - self.prefix_summed[left-1]
        
        return self.prefix_summed[right]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)