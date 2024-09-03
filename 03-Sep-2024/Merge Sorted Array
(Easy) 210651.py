# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # merge sort but from the end
        last_index = n + m - 1
        n,m = n-1,m-1

        while n > -1 and m > -1:
            if nums1[m] > nums2[n]:
                nums1[last_index] = nums1[m]
                m -= 1
            else:
                nums1[last_index] = nums2[n]
                n -= 1
            last_index -= 1

        while n > -1:
            nums1[last_index] = nums2[n]
            n -= 1
            last_index -= 1
        
        while m > -1:
            nums1[last_index] = nums1[m]
            m -= 1
            last_index -= 1
        
        