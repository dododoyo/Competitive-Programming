class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """ Given some order of cards return the order they should 
        be in so that when they are revealed using the steps they will
        be in increasing order"""

        deck.sort()
        dq = deque(range(len(deck)))
        sol = [0]*len(deck)

        for card_index in range(len(deck)):
            print(dq)
            sol[dq.popleft()] = card_index
            if dq:
                popped = dq.popleft()
                dq.append(popped)
        return [deck[card_index] for card_index in sol]
        
        