class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        pointer_1,pointer_2 = 0,0
        while pointer_1 < len(nums1) and pointer_2 < len(nums2):
            if nums1[pointer_1] > nums2[pointer_2]:
                pointer_2 += 1
            elif  nums1[pointer_1] < nums2[pointer_2]:
                pointer_1 += 1
            else:
                return nums1[pointer_1]
        return -1
        