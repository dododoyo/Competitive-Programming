# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n,m = len(nums1),len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2,nums1)

        def splitArrays(mid1):
            mid2 = median - mid1
            
            right1 = nums1[mid1] if mid1 < n else float('inf')
            right2 = nums2[mid2] if mid2 < m else float('inf')

            left1 = nums1[mid1-1] if mid1 > 0 else -float('inf')
            left2 = nums2[mid2-1] if mid2 > 0 else - float('inf') 

            return left1,right1,left2,right2

        median = (n+m+1)//2
        low,high = 0,n

        while low <= high:
            mid1 = low + (high-low)//2   
            left1,right1,left2,right2 = splitArrays(mid1)    

            if left1 > right2:
                high = mid1 -1 
            elif left2 > right1:
                low = mid1 + 1
            else:
                # found solution
                if (n+m)%2:
                    return max(left1,left2)
                else:
                    return (max(left1,left2) + min(right1,right2))/2