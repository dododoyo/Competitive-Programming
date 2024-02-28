class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """for each number we want to get how many
        subarray's minimum number will this number be ?
        """
        MOD = 10**9 + 7

        # get the span of each element
        elmnt_span = self.getMinCount(arr)

        # the total solution will be the total sum of minimum elements
        solution = [elmnt_span[i]*arr[i] for i in range(len(arr))]

        return sum(solution)%MOD

    def getMinCount(self,arr):
        mon_stack,n = [],len(arr)

        # each element will span atleast itself
        solution = [1]*n
        for i in range(n):
            while mon_stack and mon_stack[-1][1] >= arr[i]:
                popped = mon_stack.pop()
                solution[popped[0]] *= i-popped[0]
            if mon_stack:
                max_till = i - mon_stack[-1][0]
            else:
                max_till = i+1

            solution[i] *= max_till
            mon_stack.append([i,arr[i]])

        while mon_stack:
            popped = mon_stack.pop()
            solution[popped[0]] *= n-popped[0]
        return solution
        