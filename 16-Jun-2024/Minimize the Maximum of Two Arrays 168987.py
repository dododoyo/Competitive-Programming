# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

from bisect import bisect_left

class Solution:

    def custom_gcd(self, num1, num2):
        if num1 == 0:
            return num2
        return self.custom_gcd(num2 % num1, num1)

    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCount1: int, uniqueCount2: int) -> int:

        uniqueCountDivisor1 = uniqueCount1
        uniqueCountDivisor2 = uniqueCount2
        divisor1 = divisor1
        divisor2 = divisor2

        def isValid(n):
            onlyDivisor1 = (n // divisor2) - (n // leastCommonMultiple)
            onlyDivisor2 = (n // divisor1) - (n // leastCommonMultiple)

            bothDivisors = n - (n // divisor1) - (n // divisor2) + (n // leastCommonMultiple)

            x =  max(0, uniqueCountDivisor1 - onlyDivisor1)
            y = max(0, uniqueCountDivisor2 - onlyDivisor2)
            return (x+y) <= bothDivisors
            
        greatestCommonDivisor = self.custom_gcd(divisor1, divisor2)
        
        leastCommonMultiple = divisor1 * divisor2 / greatestCommonDivisor

        return bisect_left(range(uniqueCountDivisor1 * divisor1 + divisor2 * uniqueCountDivisor2 + 1), True, lo=1, key=isValid)