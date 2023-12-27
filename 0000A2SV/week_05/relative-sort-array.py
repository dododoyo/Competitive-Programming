from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq_counter  = Counter(arr1)
        arr2_set,not_in, solution = set(arr2), [], []
        for i in arr1:
            if i not in arr2_set:not_in.append(i)
        not_in.sort()
        for num in arr2:
            while freq_counter[num] > 0:
                solution.append(num)
                freq_counter[num] -= 1
        return solution + not_in
