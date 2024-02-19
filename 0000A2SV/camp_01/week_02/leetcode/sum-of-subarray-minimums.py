class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """for each number we want to get how many
        subarray's minimum will this number be ?
        """
        MOD = 10**9 + 7
        prefix_arr = self.getMinCount(arr,True)
        suffix_arr = self.getMinCount(arr[::-1],False)
        suffix_arr = suffix_arr[::-1]
        solution = [prefix_arr[i]*suffix_arr[i]*arr[i] for i in range(len(arr))]

        return sum(solution)%MOD
    def getMinCount(self,arr,flag):
        mon_stack = []
        solution = [0]*len(arr)
        for i in range(len(arr)):
            while mon_stack and mon_stack[-1][1] + flag > arr[i]:
                mon_stack.pop()
            if mon_stack:
                max_till = i - mon_stack[-1][0]
            else:
                max_till = i+1
            solution[i] = max_till
            mon_stack.append([i,arr[i]])
        return solution
        