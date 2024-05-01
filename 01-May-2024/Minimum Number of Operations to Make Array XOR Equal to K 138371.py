# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums_xor = 0
        for number in nums:
            nums_xor ^= number
        xored = nums_xor^k
        return bin(xored).count("1")
