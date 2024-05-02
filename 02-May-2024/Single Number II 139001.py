# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    once = 0
    twice = 0

    for number in nums:
      once = once ^ (number & (~twice))
      twice = twice ^ (number & (~once))

    return once