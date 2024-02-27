class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [nums2[0]]
        greater_map = defaultdict(lambda : -1)

        # since nums2 is subset of nums1 we can do the operation 
        # on nums2 and use that value for nums1 using a monotonic 
        # decreasing stack

        for i in range(1,len(nums2)):
            while stack and nums2[i] > stack[-1]:
                # which ever removed the element at the 
                # top of the stack is greater than it
                greater_map[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])

        return [greater_map[i] for i in nums1]