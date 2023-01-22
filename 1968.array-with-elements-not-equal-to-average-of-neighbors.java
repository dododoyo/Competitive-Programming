import java.util.*;
class Solution 
{
    public int[] rearrangeArray(int[] nums) 
    {
        Arrays.sort(nums);
        int[] newNums = new int[nums.length];

        // {1.2.3.4.5} --> {1.0.2.0.3}-->{1.4.2.5.3}

        if((nums.length)%2 != 0)
        {
            for(int i = 0; i <= nums.length/2 ; i++)
            {
                newNums[2*i] = nums[i];
            }
            for(int i = (nums.length/2)+1; i < nums.length ; i++)
            {
                newNums[2*(i-(nums.length/2))-1] = nums[i];
            }
        }
        else
        {
            // 1,2,3,4,6,8   1,0,2,0,3,0    1,4,2,6,3,8
            // 3 1
            // 4 3
            // 5 5
            for(int i = 0; i < nums.length/2 ; i++)
            {
                newNums[2*i] = nums[i];
            }
            for(int i = (nums.length/2); i < nums.length ; i++)
            {
                newNums[2*(i-nums.length/2)+1] = nums[i];
            }

        }
        
        return newNums;
    }
}