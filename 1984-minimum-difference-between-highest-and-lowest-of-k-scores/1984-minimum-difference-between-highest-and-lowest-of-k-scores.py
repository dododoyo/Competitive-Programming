class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        length = len(nums)
        if(length < 2):
            return 0
        nums.sort()
        
        lft_pntr = 0
        rht_pntr = k-1
        dif = 10**6
        
        while(rht_pntr < length):
            cur_dif = max(nums[lft_pntr:rht_pntr+1]) - min(nums[lft_pntr:rht_pntr+1])
            dif = min(cur_dif,dif)
            rht_pntr += 1
            lft_pntr += 1
            
        return dif
            
            
        