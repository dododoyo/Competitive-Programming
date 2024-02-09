class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # the sum of the subarray we will be looking for
        # must be the multiple of the mode left when we 
        # divide the sum with the target 
        MOD = sum(nums) % p

        # if the nums sum is divisible we return zero 
        # because we need to remove nothing
        if MOD == 0:return 0

        # dictionary to map current remainders and their indeces
        # initialized at zero = -1 to handle the edge case when
        # the first divisible is found

        remainder_map = {0: -1}
        running_remainder = 0

        # set solution length to be the maximum it can be
        solution  = len(nums)

        for i in range(len(nums)):
            # get the remainder encountered till now
            running_remainder = (running_remainder + nums[i])%p
            # map it's index with the remainder  value
            remainder_map[running_remainder] = i

            '''if needed remainder is in the remainder_map
            means that we found a previous subarray with the same
            remainder whose sum's remainder when divided by p is MOD'''
            needed_remainder = (running_remainder - MOD) % p

            if needed_remainder in remainder_map:
                solution = min(solution, i - remainder_map[needed_remainder])
        return solution if solution < len(nums) else -1