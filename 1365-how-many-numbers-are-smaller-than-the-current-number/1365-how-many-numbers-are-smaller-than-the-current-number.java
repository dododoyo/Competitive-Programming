class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) 
    {
        //use counting sort with array value of int[101]
        int[] frequency = new int[101];
        
        //count frequency of each number
        for(int j : nums)
            frequency[j]++;
       
        //sum the previous to current one to get the number of elements before 
        //it in a sorted array 
        for(int i = 1 ; i < frequency.length ;i++)
            frequency[i] = frequency[i] + frequency[i-1];
        
        int[] solution = new int[nums.length];
        
        for(int j = 0 ; j < nums.length ; j++)
        {
            //cant use --nums[j] because it will be negative
            if(nums[j] == 0)
                solution[j] = 0;
            else
                solution[j] = frequency[nums[j]-1];
        }
        return solution;
    }
    
}