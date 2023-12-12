class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_elements,negative_elements = [],[]
        for number in nums:
            if number < 0:negative_elements.append(number)
            if number > 0:positive_elements.append(number)
        solution_index = 0
        for i in range(len(positive_elements)):
            nums[solution_index] = positive_elements[i]
            nums[solution_index+1] = negative_elements[i]
            solution_index += 2
        return nums