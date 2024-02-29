class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        for 2n people -> "n" people must go to A
        and other "n" must go to B

        return the minimum cost to fly every person
        ---------------------------------
        
        we make sure the first n elments gives as 
        the most profit from the other"""
        costs.sort(key= lambda cost: cost[0] - cost[1])
        solution,n = 0,len(costs)//2
        for i in range(n):
            solution += costs[i][0] + costs[i+n][1]
        return solution

        