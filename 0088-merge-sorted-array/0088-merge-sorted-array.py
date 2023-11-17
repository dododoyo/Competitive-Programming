class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_index = n+m-1
        while n > 0 and m > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last_index] = nums1[m-1]
                m -= 1
            else:
                nums1[last_index] = nums2[n-1]
                n-= 1
            last_index -= 1
        while n > 0:
            nums1[last_index] = nums2[n-1]
            n,last_index = n-1,last_index-1
        while m > 0:
            nums1[last_index] = nums1[m-1]
            m,last_index = m-1,last_index-1