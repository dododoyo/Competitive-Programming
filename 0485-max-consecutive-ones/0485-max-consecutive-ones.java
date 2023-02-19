class Solution {
    public int findMaxConsecutiveOnes(int[] nums)
{
    int l = 0, max = 0, r = 0;
    
    while(r < nums.length)
    {
        if(nums[r] == 1)
        {
            max = Math.max(max,r-l+1);
            r++;
        }
        else
        {
            l = r + 1;
            r = l;
            
        }
        
    }
    return max;
}
}