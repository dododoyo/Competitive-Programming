class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        pointer,summ = 0,0
        while pointer < len(costs) and summ < coins:
            summ += costs[pointer]
            if coins >= summ:
                pointer +=1
        return pointer