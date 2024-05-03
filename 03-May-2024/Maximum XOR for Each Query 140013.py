# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        solution = [(1 << maximumBit) - 1]

        for number in nums:
            solution.append(solution[-1] ^ number)

        return solution[len(solution)-1:0:-1]