class ATM:
    def __init__(self):
        self.amount_map = [20,50,100,200,500]
        self.current_amount = [0,0,0,0,0]
    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.current_amount[i] += banknotesCount[i]
    def withdraw(self, amount: int) -> List[int]:
        solution = [0,0,0,0,0]
        for i in range(4,-1,-1):
            notes = amount//self.amount_map[i]
            # if the notes that are required are greater than 
            # the one that is in the ATM then we take all that
            # we have in our ATM machine
            if notes > self.current_amount[i]:
                solution[i] = self.current_amount[i]
            else:
                solution[i] = notes
            amount -= solution[i]*self.amount_map[i]
        if amount == 0:
            for i in range(5):
                self.current_amount[i] -= solution[i]        
        return [-1] if amount else solution
            