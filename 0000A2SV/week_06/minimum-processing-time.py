class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        solution = -1
        for i in range(len(processorTime)):
            curr_max = -1
            for j in range(4*i,4*(i+1)):
                curr_max = max(curr_max,processorTime[i] + tasks[j])
            solution = max(curr_max,solution)
        return solution
        