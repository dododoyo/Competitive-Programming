class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min,second_min = float("inf"),float("inf")
        for number in nums:
            if number <= first_min:first_min = number
            elif number <= second_min:second_min = number
            else:return True
        return False