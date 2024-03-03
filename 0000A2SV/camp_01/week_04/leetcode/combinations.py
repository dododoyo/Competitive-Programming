class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums, solution = list(range(1,n+1)),[]
        def backtrack(index,elements):
            if len(elements) == k:
                solution.append(elements[:])
                return 
            if index > n-1:
                return
            # insert
            elements.append(nums[index])
            backtrack(index+1,elements)
            elements.pop()
            # not insert
            backtrack(index+1,elements)
            return
        backtrack(0,[])
        return solution