import java.util.*;
class Solution 
{
    public List<List<Integer>> threeSum(int[] nums) 
    {
        Arrays.sort(nums);

        int startPointer = 0 ;
        int endPointer = 0;
        
        List<List<Integer>> solution = new LinkedList<>();
       

        for( int i = 0 ; (i <nums.length-2)  ; i++)
        {
            // if the elements are duplicated no need to do current iteration
            if (i > 0 && nums[i] == nums[i-1])
            continue;
            else
            {

            
                startPointer = i +1;
                endPointer = nums.length-1;

                while ( startPointer < endPointer)
                {
                    if(nums[i]+nums[startPointer]+nums[endPointer] == 0)
                    {
                        solution.add(Arrays.asList(nums[startPointer],nums[i],nums[endPointer]));

                        // if solution elements are also duplicates no need to do current iteration
                        while ( startPointer < endPointer && (nums[startPointer+1] == nums[startPointer]))
                        {
                            startPointer++;
                        }
                        while ( startPointer < endPointer && (nums[endPointer-1] == nums[endPointer]))
                        {
                            endPointer--;
                        }

                        startPointer++;
                        endPointer--;
                        
                    }
                    else if (nums[i]+nums[startPointer]+nums[endPointer] > 0)
                    {
                        endPointer--;
                    }
                    else 
                    {
                        startPointer++;
                    }

                }
            }


        }

        return solution;
    }
}