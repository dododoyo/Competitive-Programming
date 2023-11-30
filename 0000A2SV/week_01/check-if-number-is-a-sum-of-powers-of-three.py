class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 1:return True;
        if(n%3 > 1 or n == 0):return False;
        return self.checkPowersOfThree(n//3);