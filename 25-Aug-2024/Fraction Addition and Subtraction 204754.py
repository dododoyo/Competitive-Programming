# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = list(map(int, re.findall(r'[+-]?\d+', expression)))
        numrater = 0
        denominator = 1
        
        for i in range(0, len(nums), 2):
            num, den = nums[i], nums[i + 1]
            numrater = numrater * den + num * denominator
            denominator *= den
        
        common_divisor = gcd(numrater, denominator)
        return f"{numrater // common_divisor}/{denominator // common_divisor}"