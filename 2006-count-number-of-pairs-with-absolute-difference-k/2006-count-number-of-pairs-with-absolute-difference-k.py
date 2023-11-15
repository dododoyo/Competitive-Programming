from collections import defaultdict
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        num_freq = [0]*101
        solution = 0
        for number in nums:
            num_freq[number] +=1
         
        for right in range(k+1,101):
            if num_freq[right] and num_freq[right-k]:
                solution += num_freq[right]*num_freq[right-k]
        return solution
                