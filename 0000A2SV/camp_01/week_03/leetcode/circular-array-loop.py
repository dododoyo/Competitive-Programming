class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            # use slow and fast pointers
            slow = fast = i
            backward = (nums[i] < 0)
            while True:
                slow = self.findDestination(nums,backward,slow)
                fast = self.findDestination(nums,backward,fast)
                if fast != -1:
                    fast = self.findDestination(nums,backward,fast)
                if slow == -1 or fast == slow:
                    break
            if slow != -1 and slow == fast:
                return True
        return False
    def findDestination(self,nums,backward,index):
        direction = nums[index] < 0 
        if direction != backward:
            return -1
        jump = nums[index]
        destination = (index+jump) % len(nums)
        if destination == index:
            return -1
        return destination