class Solution {
    public int[] twoSum(int[] nums, int target) 
    {
        int[] solutions = {0,0};
        
        for (int i = 0; i < nums.length;i++)
        {
            for (int j = i+1; j < nums.length;j++)
            {
                if (nums[i]+nums[j] == target)
                {
                    solutions[0] = i;
                    solutions[1] = j;
                    
                }
            }
        }
        return solutions;
    }
}