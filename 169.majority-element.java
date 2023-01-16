import java.util.*;
class Solution {
    public int majorityElement(int[] nums) 
    {
        Arrays.sort(nums);
        ArrayList<Integer> frequency = new ArrayList<>();
        ArrayList<Integer> nums2 = new ArrayList<>();


        for(int i = 0 ; i < nums.length ; i++)
        {
            if( i==0)
            {
                nums2.add(nums[i]);
                frequency.add(1);
                
            }
            else
            {
                if (nums[i-1] == nums[i])
                {
                    frequency.set(nums2.indexOf(nums[i]),(frequency.get(nums2.indexOf(nums[i]))+1));
                }
                else
                {
                    nums2.add(nums[i]);
                    frequency.add(1);
                }
                
            }

        }

        int mostFrequent = Collections.max(frequency);
        int freqNum = frequency.indexOf(mostFrequent);

        //if(maxIndex >= nums.length/2)
        return nums2.get(freqNum);

        
    }
}