class Solution {
    public int maxArea(int[] height) 
    {
        // let's use two pointer starting from the largest separation
        int p1 = 0, p2 = height.length -1 ;
        int maxArea = 0;

        while (p2 > p1)
        {
            if(height[p1] > height[p2])
            {
                maxArea = Math.max(maxArea,(p2-p1)*height[p2] );
                p2--;
            }
            else
            {
                maxArea = Math.max(maxArea,(p2-p1)*height[p1]);
                p1++;
            }
            
        }
        return maxArea;
        
    }
}

