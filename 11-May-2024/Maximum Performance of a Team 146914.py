# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD,heap = 10**9 + 7,[]
        temp = sorted(zip(efficiency, speed), reverse=True)
        sum_,solution = 0,0
        
        for indx in range(n):
            e, v = temp[indx]
            sum_ += v
            solution = max(solution, sum_*e)
            
            if indx < k - 1:
                heappush(heap, v)
            elif heap and heap[0] < v:
                sum_ -= heappop(heap)
                heappush(heap, v)
            else:
                sum_ -= v
            
        return solution%MOD
