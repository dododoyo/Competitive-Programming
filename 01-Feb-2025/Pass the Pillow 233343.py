# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        zurr = time // (n-1)
        remaining = time % (n-1)

        if (zurr % 2):
            return n - remaining
        else:
            return remaining + 1