class Solution(object):
    def reverse(self, x):
        res = 0
        negative = (x < 0)

        if negative:
            x = -x

        while x:
            res = res*10
            res += (x%10)
            x = x//10

        if (res > 2147483648):
            return 0

        if negative:
            return -res

        return res