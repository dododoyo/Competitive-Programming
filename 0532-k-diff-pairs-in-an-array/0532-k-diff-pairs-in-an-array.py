from collections import defaultdict
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        solution = 0
        if k == 0:
            freq_cntr = defaultdict(int)
            for number in nums:freq_cntr[number] += 1
            for number in freq_cntr:
                if freq_cntr[number] > 1:solution +=1
        else:
            nums_set = set(nums)
            for i in nums_set:
                if i+k in nums_set:
                    solution += 1
        return solution
            
                