class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i,j = 0,1;
        while i < num:i+=j;j+=2;
        return i == num;