# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # ger remainders of the subarrays 
        remainder,running_sum = defaultdict(int),0
        for i in range(len(nums)):
            running_sum += nums[i]
            remainder[running_sum%k] += 1 

        # add the subarray which is exactly divisible by k
        # which means remainder is zero
        solution = remainder[0]

        # for any other indeces if the remainders are the same
        # this means what ever elements inside them are divisible by k
        # so we need to count those 
        for value in remainder.values():
            if value != 0:
                solution += (value*(value-1))//2
        return solution