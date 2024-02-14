class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money_in_hand = 0
        fives,tens = 0,0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives < 1:
                    return False
                fives -= 1
                tens += 1
            else:
                if fives > 0 and tens > 0:
                    fives -= 1 
                    tens -= 1
                elif fives > 2:
                    fives -= 3
                else:
                    return False
        return True
        