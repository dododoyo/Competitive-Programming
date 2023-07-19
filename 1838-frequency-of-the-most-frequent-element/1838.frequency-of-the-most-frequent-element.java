import java.util.*;
class Solution {
    	public int maxFrequency(int[] nums, int k) 
        {
            Arrays.sort(nums);
            int r = 0, l = 0, sum = 0, max_val = 0;
            for (r=0;r<nums.length;r++)
            {
                sum += nums[r];
                while (nums[r] * (r - l + 1) - sum > k){ sum -= nums[l++];}
                max_val = Math.max(max_val,r-l+1);
            }
        return max_val;
    }
}