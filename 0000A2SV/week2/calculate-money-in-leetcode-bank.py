class Solution:
    def totalMoney(self, n: int) -> int:
        full_week_money = 0
        for i in range(1,n//7+1):
            full_week_money = full_week_money + i + 3
        all_the_money = full_week_money*7 + sum([i for i in range((n//7)+1,(n//7)+1+(n%7))])
        return all_the_money
        