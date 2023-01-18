class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) 
    {
        //if nums2 is empty no work is done
        if(n == 0)
        return;

        //check if nums1 is empty
        boolean isEmpty = true;
        for(int val: nums1)
        {
            if(val != 0)
            {
                isEmpty = false;
                break;
            }
        }

        // if nums1 is empty just copy nums2 into it
        if(isEmpty)
        {
            for (int index1 = 0 ; index1 < n ; index1++)
            {
                nums1[index1] = nums2[index1];
            }

        }
        
        // if not let's use two pointers each pointing at the end of each array
        else
        {
                
            int p1 = m-1, p2 = n-1;

            int index = m + n -1;

            while(p2 > -1)
            {
                if (p1 > -1 && nums1[p1] > nums2[p2])
                {
                    nums1[index] = nums1[p1];
                    p1--;
                    index--;
                }
                else
                {
                    nums1[index] = nums2[p2];
                    p2--;
                    index--;
                }
                
            }
        }
    }
}
