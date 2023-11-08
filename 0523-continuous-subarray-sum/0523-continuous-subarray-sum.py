class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0:-1}
        current_sum = 0
        for index,number in enumerate(nums):
            current_sum += number
            current_remainder = current_sum % k
            if current_remainder not in remainder_map:
                remainder_map[current_remainder] = index
            elif index - remainder_map[current_remainder] > 1:
                return True
        return False
            
            