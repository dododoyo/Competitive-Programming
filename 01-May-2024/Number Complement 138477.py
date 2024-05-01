# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        # xor with largest 111...11 bit
        bit_len = num.bit_length()
        return num ^ ((1<<bit_len) -1)
        