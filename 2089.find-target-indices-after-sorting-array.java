import java.util.*;

class Solution {
    public List<Integer> targetIndices(int[] nums, int target) 
    {
        boolean isPresent = false;
        int maxElement = Arrays.stream(nums).max().getAsInt();
        int[] newNums = new int[maxElement+1];

        for(int val: nums)
        {
            newNums[val]++;
            if(val == target)
            isPresent = true;
        }
        
        
        for( int i = 1 ; i < newNums.length ;i++)
        {
            newNums[i] = newNums[i] + newNums[i-1];
        }

        if(!isPresent)
        {
            return new ArrayList<Integer>();
        }
        else
        {
            int[] theFreq = new int[newNums[target]-newNums[target-1]];
        
        

        int j = theFreq.length -1;
        while((newNums[target]-newNums[target-1]) > 0)
        {
            theFreq[j] = --newNums[target];
            j--;
        }

        List<Integer> theList = new ArrayList<Integer>();

        for ( int val: theFreq)
        theList.add(val);
        
        return theList;

        }
        
    }
}


