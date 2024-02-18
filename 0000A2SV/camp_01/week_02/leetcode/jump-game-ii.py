class Solution:
    def jump(self, nums: List[int]) -> int:
        max_jump,jumps,last_index = 0,0,0
        n = len(nums)
        if n == 1: return 0
        for i in range(n):
            # when ever we can we go beyond our current maximum jump
            if nums[i] + i > max_jump:
                max_jump = nums[i] + i
            if i == last_index:
                jumps += 1
                last_index = max_jump
                if max_jump >= n-1:
                    return jumps
        