class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_freq,num2_freq = [0]*1001,[0]*1001
        for i in nums1:num1_freq[i] += 1
        for i in nums2:num2_freq[i] += 1
        solution = []
        for i in range(1001):
            if num1_freq[i] > 0 and num2_freq[i] > 0:
                for j in range(min(num1_freq[i], num2_freq[i])):
                    solution.append(i)
        return solution


        