from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        dq = deque(range(len(deck)))
        sol = [0]*len(deck)
        for card in deck:
            sol[dq.popleft()] = card
            if dq:
                popped = dq.popleft()
                dq.append(popped)
        return sol
        
        