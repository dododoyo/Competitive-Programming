class Solution {
    public String largestNumber(int[] nums) 
    {
        int temp;
        String maxNum="";
        boolean allZero = true;
        
        for(int p1 = 0 ; p1 < nums.length ; p1++)
        {
            for(int p2 = p1+1 ; p2 < nums.length ;p2++)
            {
                
                if(Long.parseLong(Long.toString(nums[p1]).concat(Long.toString(nums[p2]))) > Long.parseLong(Long.toString(nums[p2]).concat(Long.toString(nums[p1]))))
                continue;
                else 
                {
                    temp = nums[p1];
                    nums[p1] = nums[p2];
                    nums[p2] = temp;
                }
            }
        }

        for(int val: nums)
        {
            maxNum += Long.toString(val);
            if(val!=0)
            allZero = false;
        }

        if(allZero)
        return "0";
        else
        return maxNum;
        
    }
}