class Solution:
    def square(self, n):
        result = 0
        while n>0:
            last = n%10
            result += last * last
            n = n//10
        return result
    def isHappy(self, n: int) -> bool:
        slow = self.square(n)
        fast = self.square(self.square(n))

        while slow!=fast and fast!=1:
            slow = self.square(slow)
            fast = self.square(self.square(fast))

        return fast == 1

        