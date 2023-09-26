class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = set(range(n))      
        for i, j in edges:
            if j in res:
                res.remove(j)
                
        return list(res)