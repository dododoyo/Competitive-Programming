class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        """
        we want to break it into pieces so that the
        smaller one is as large as possible but not
        larger than the previous one.

        Steps to split = (nums[i] - 1)/last

        New smallest element formed (last) = nums[i]/(steps+1).

        ans += step"""
        
        n = len(nums)
        last = nums[n - 1]  
        ans = 0  
        for i in range(n - 2, -1, -1):
            if nums[i] > last:  
                t = nums[i] // last
                if nums[i] % last:
                    t += 1  
                last = nums[i] // t 
                ans += t - 1 
            else:
                last = nums[i]
        return ans 