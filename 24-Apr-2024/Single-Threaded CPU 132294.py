# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([t + [i] for i, t in enumerate(tasks)])
        execution_que,min_heap = [],[]
        current_index,time = 0,tasks[0][0]

        while len(execution_que) < len(tasks):
            while (current_index < len(tasks)) and (tasks[current_index][0] <= time):
                heappush(min_heap, (tasks[current_index][1], tasks[current_index][2]))
                current_index += 1
            if min_heap:
                t_diff, original_index = heappop(min_heap)
                time += t_diff
                execution_que.append(original_index)
            elif current_index < len(tasks):
                time = tasks[current_index][0]
        return execution_que