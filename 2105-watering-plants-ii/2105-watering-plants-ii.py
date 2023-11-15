class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        alice_pointer = 0
        bob_pointer = len(plants)-1
        alice_can = capacityA
        bob_can = capacityB
    
        alice_refill = 0
        bob_refill  = 0
        
        while alice_pointer < bob_pointer:
            if plants[alice_pointer] > alice_can:
                alice_can = capacityA
                alice_refill += 1
            if plants[bob_pointer] > bob_can:
                bob_can = capacityB
                bob_refill += 1
            bob_can -= plants[bob_pointer]
            alice_can -= plants[alice_pointer]
            
            bob_pointer -= 1
            alice_pointer += 1
        if alice_pointer == bob_pointer and plants[alice_pointer] > alice_can and plants[bob_pointer] > bob_can:
                alice_refill += 1
            
        return bob_refill+alice_refill
                
        