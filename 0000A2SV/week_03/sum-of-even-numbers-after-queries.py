class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        solution = [0]*len(queries)
        current_sum = sum([number for number in nums if number%2==0])
        
        for i in range(len(queries)):
            old_value = nums[queries[i][1]]
            new_value = old_value + queries[i][0]
    
            if old_value%2 and new_value%2==0:current_sum += new_value
            elif old_value%2==0 and new_value%2:current_sum -= old_value
            elif old_value%2==0 and new_value%2==0:current_sum += (new_value-old_value)
            # print(old_value,new_value)
            nums[queries[i][1]] = new_value
            solution[i] = current_sum
        return solution;
        