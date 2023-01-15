import java.util.*;
class Solution {
    public void sortColors(int[] nums) 
    {
        // use counting sort
        
        int[] freqElement = {0,0,0};

        for(int val: nums)
        freqElement[val]++;

        for ( int i = 1; i < freqElement.length; i++)
        freqElement[i] = freqElement[i] + freqElement[i-1];

        int[] sortedArray = new int[nums.length];

        for ( int i = (nums.length-1); i > -1 ; i--)
        sortedArray[--freqElement[nums[i]]] = nums[i];

        for ( int i = 0 ; i < nums.length ; i++)
        nums[i] = sortedArray[i];
    }
}