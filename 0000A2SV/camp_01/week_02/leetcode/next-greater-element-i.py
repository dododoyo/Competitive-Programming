class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [nums2[0]]
        greater_map = {}
        for i in range(1,len(nums2)):
            while stack and nums2[i] > stack[-1]:
                greater_map[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])

        solution = [-1]*len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in greater_map:
                solution[i] = greater_map[nums1[i]]
        return solution