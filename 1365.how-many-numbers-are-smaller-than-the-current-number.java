import java.util.*;
class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) 
    {
        // let's use counting sort to store the frequency of each element 
        int maxValue = Arrays.stream(nums).max().getAsInt();

        int[] frequency = new int[maxValue+1];

        for(int val: nums)
        {
            frequency[val]++;
        }

        // add consequetive elements to get ones below it
        for ( int i =1 ; i < frequency.length ; i++)
        frequency[i] = frequency[i] + frequency[i-1];

        int[] greaterArray = new int[nums.length];

        for(int i = 0 ; i < nums.length ; i++)
        {
            if (nums[i] == 0)
            greaterArray[i] = 0;
            else
            greaterArray[i] = frequency[--nums[i]];
        }

        return greaterArray;
    }
}


