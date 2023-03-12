class Solution {
    public List<Integer> findDuplicates(int[] nums) 
    {
        ArrayList<Integer> solution = new ArrayList<Integer>();
        int arrayLen = nums.length;
        
        for(int i = 0;i<arrayLen;i++)
        {
            if(nums[Math.abs(nums[i])-1] < 0)
                solution.add(Math.abs(nums[i]));
            nums[Math.abs(nums[i])-1] *= -1;
        }
    
        return solution;
    }
}