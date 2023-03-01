class Solution {
    public int maxArea(int[] height) 
    {
        // let's use two pointer starting from the maximum length
        int r = height.length-1;
        int l = 0;
        int maxWater = 0;
        
        while(l<r)
        {
            if(height[r] > height[l])
            {
                maxWater = Math.max(maxWater,(r-l)*height[l]);
                l++;
            }
            else
            {
                maxWater = Math.max(maxWater,(r-l)*height[r]);
                r--;
            }
        }
        return maxWater;
    }
}