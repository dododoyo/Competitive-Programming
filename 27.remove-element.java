import java.util.Arrays;
class Solution 
{
    public int removeElement(int[] nums, int val) 
    {
        int counter = 0;
        if ( nums.length == 0)
        {
            return 0;
        }
        else if ((nums.length == 1) && (val == nums[0]))
        {
            return 0;
        }
        else
        {
        int theMax = Arrays.stream(nums).max().getAsInt()+1;
        //System.out.println(theMax);
        //int counter = 0;
        for(int i = 0 ; i < nums.length ; i++)
        {
            if(nums[i] == val)
            {
                nums[i] = theMax;
                counter++;
            }
            
        }
        }
        
        Arrays.sort(nums);
        return nums.length - counter;
    } 
}