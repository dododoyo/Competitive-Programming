class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.efficient_power(x,n)
    def efficient_power(self,a,b):
        if b == 0:
            return 1
        if b < 0:
            return 1/ self.efficient_power(a,-b)
        if b%2:
            return a*self.efficient_power(a*a,(b-1)//2)
        return self.efficient_power(a*a,b//2)
        