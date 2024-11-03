# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_elements,greater_elements,equal_counter  = [],[],0

        for number in nums:
            if number < pivot:less_elements.append(number)
            elif number > pivot:greater_elements.append(number)
            else:equal_counter +=1
            
        return less_elements + [pivot]*equal_counter + greater_elements