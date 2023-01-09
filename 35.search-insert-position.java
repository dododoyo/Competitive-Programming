class Solution {
    public int searchInsert(int[] nums, int target) 
    {
        int found=0;
        for(int index = 0 ; index < nums.length ; index++)
        {
            if(nums[index] == target)
            found = index;

           
            else 
            {
                if(nums[index]<target)
                {
                    if (index == nums.length -1)
                        found = nums.length;
                    else if(nums[index+1]>target)
                        found = index+1;
                    else 
                    continue;
                
                }
                
            }
        
        }
        return found;
        
    }
}


