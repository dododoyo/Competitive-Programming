class Solution 
{
    public int[] productExceptSelf(int[] nums) 
    {
        // let's use prefix sum 
        int nums_length = nums.length;
            
        if(nums_length == 2)
        {
            int temp = nums[0];
            nums[0] = nums[1];
            nums[1] = temp;
            return nums;
        }
        int[] firstTraverse = new int[nums_length];
        int[] secondTraverse = new int[nums_length]; 
        
        firstTraverse[0] = nums[0];
        secondTraverse[nums_length-1] = nums[nums_length-1];
        
        for(int i = 1 ; i < nums_length;i++)
        {
            firstTraverse[i] = firstTraverse[i-1]*nums[i];
        }
        
       
        
        for(int i = nums_length-2 ; i > -1 ;i--)
        {
            secondTraverse[i] = nums[i]*secondTraverse[i+1];
             
        }
        
       
        
        int[] solution = new int[nums_length];
        
        solution[0] = secondTraverse[1];
        solution[nums_length-1] = firstTraverse[nums_length-2];
            
        for(int i = 1 ; i < nums_length-1 ; i++)
        {
            solution[i] = firstTraverse[i-1]*secondTraverse[i+1];
        }

        return solution;
        
        
    }
}