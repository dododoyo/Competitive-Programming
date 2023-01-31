class Solution 
{
    public void moveZeroes(int[] nums) 
    {
        if(nums.length == 0)
        {}
        else if(nums.length == 1)
        {}
        else if(nums.length >= 2)
        {
            int p1=0;
            int p2=(nums.length-1);
            
            while(p1<p2)
            {
                if(nums[p1] == 0)
                {
                    for(int j = p1 ; j < p2;j++)
                        nums[j] = nums[j+1];
                    
                    nums[p2] = 0;
                    p2--;
                }
                else
                    p1++;
            }
        }
         
       
    }
}