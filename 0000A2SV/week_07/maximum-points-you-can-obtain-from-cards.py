class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # since we are told to have k elements from both ends
        # we can use a sliding window inside our subarray to 
        # get the sum of elements that are not involved for each subarray

        # get min from all subarrays and subtract from the whole array sum
        curr_sum,min_sum =0,float('inf')
        for right in range(len(cardPoints)):
            if right < len(cardPoints)-k:
                curr_sum += cardPoints[right]
            else:
                curr_sum += cardPoints[right] - cardPoints[right - len(cardPoints) + k]
                
            if right > len(cardPoints) -k -2:
                min_sum = min(curr_sum,min_sum)

        return sum(cardPoints) - min_sum
        