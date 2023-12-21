class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        total_ones = sum(nums)
        scores = [total_ones]*(len(nums)+1)
        current_sum = 0 # keeps track of the ones we got till now
        for i in range(len(nums)):
            current_sum += nums[i]
            left_zeros = i+1-current_sum
            right_ones = total_ones - current_sum
            scores[i+1] = left_zeros+right_ones
        max_score = max(scores)
        return [i for i in range(len(scores)) if scores[i] == max_score]

        