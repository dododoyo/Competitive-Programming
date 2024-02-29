class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def play_game(left,right,turn):
            if left == right:
                return nums[left]
            
            if turn:
                leftChoice = nums[left] + play_game(left+1,right,not turn)
                rightChoice = nums[right] + play_game(left,right-1,not turn)
                return max(leftChoice, rightChoice)
            else:
                leftChoice = -nums[left] + play_game(left+1,right,not turn)
                rightChoice = -nums[right] + play_game(left,right-1,not turn)
                return min(leftChoice, rightChoice)
        return play_game(0,len(nums)-1,True) >= 0