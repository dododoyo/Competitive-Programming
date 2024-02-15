class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        extras,num_map = 0,defaultdict(int)
        current_number = maximum_solution = len(arr)

        # count the elements occurance
        for number in arr:
            if number > maximum_solution:extras += 1
            else:num_map[number] += 1

        # get the maximum number you can get
        while current_number:
            if  current_number in num_map:
                extras += num_map[current_number] - 1
            else:
                if extras > 0:extras -= 1
                else:maximum_solution -= 1 
            current_number -= 1
            
        return maximum_solution