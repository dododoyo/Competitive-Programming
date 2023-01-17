import java.util.*;
class Solution 
{
    public int[][] merge(int[][] intervals) 
    {
        Arrays.sort(intervals,(arr1,arr2) -> Integer.compare(arr1[0], arr2[0]));
        
        List<int[]> intSolution = new ArrayList<>();

        int[] prevInterval = intervals[0];
        intSolution.add(prevInterval);

        for ( int[] eachInterval : intervals)
        {
            
            int previousEnd = prevInterval[1];

            int eachBegin = eachInterval[0];
            int eachEnd = eachInterval[1];

            if ( previousEnd >= eachBegin)
            {
                prevInterval[1] = Math.max(eachEnd,previousEnd);

            }
            else 
            {
                intSolution.add(eachInterval);
                prevInterval = eachInterval;
            }
        }


        return intSolution.toArray(new int[intSolution.size()][]); 
    }
}