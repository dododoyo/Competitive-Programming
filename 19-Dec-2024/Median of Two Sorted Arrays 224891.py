# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def takeFromNum1(self,x,nums1,nums2):
        n,m = len(nums1),len(nums2)
        take1 = x 
        median = (n+m+1)//2
        take2 = median-take1

        left1 = nums1[take1-1] if take1 > 0 else -float('inf')
        left2 = nums2[take2-1] if take2 > 0 else -float('inf')

        right1 = nums1[take1] if take1 < n else float('inf')
        right2 = nums2[take2] if take2 < m else float('inf')

        return left1,left2,right1,right2


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n,m = len(nums1),len(nums2)
        # iterate over the minimum length element always 
        if n > m:
            return self.findMedianSortedArrays(nums2,nums1)

        # we know if we take x elements from nums1 
        # we must take y elements from nums2 such that 
        # x+y == median

        # and there are only one x and y that will 
        # give as a sorted array of the full merge 

        # we can find that x using binary search 

        # the range of elements we can take form nums1 is 
        # from 0 -> n
        left, right = 0, n
        while left <= right:
            x = left + (right-left)//2
            left1,left2,right1,right2 = self.takeFromNum1(x,nums1,nums2)

            # the last element of nums1 is bigger
            # take less from nums1
            if left1 > right2:
                # invalid 
                right = x - 1

            # the last element of nums1 is small 
            # take more from nums1
            elif left2 > right1:
                # invalid 
                left = x + 1
            else:
                # valid split

                # from the left side it will end 
                # with the greatest from all 
                first_end = max(left1,left2)

                # from the right side it will start 
                # with the smallest from all
                second_start = min(right1,right2)

                if (n+m)%2:
                    return first_end
                else:
                    return (first_end+second_start)/2
