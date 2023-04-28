from collections import defaultdict
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = defaultdict(int)
        solution = []
        for i in nums1: freq[i] += 1
        for j in nums2:
            if j in freq and freq[j] > 0:
                    solution.append(j);freq[j] = 0
        return solution
        