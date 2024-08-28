# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum,solution,sum_map = 0,0,defaultdict(int)
        # initializaiton for the sum_map[0]=1 is used to 
        # handle condition where the sum is exactly k 

        # and we must count that as the frist occurance so 
        # it's initialized with 1

        sum_map[0] = 1

        for number in nums:
            running_sum += number

            if running_sum-k in sum_map:
                solution += sum_map[running_sum-k]
            sum_map[running_sum] += 1
        return solution
        