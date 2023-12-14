class FrequencyTracker:
    def __init__(self):
        self.freq_dict = {}
        self.freq_set = {}
    def add(self, number: int) -> None:
        if number not in self.freq_dict:
            self.freq_dict[number] = 1
            if 1 in self.freq_set:
                self.freq_set[1].add(number)
            else:
                self.freq_set[1] = set([number])
        else:
            old_freq = self.freq_dict[number]
            self.freq_set[old_freq].remove(number)

            if not self.freq_set[old_freq]:
                self.freq_set.pop(old_freq)

            self.freq_dict[number] += 1

            if self.freq_dict[number] in self.freq_set:
                self.freq_set[self.freq_dict[number]].add(number)
            else:
                self.freq_set[self.freq_dict[number]] = set([number])
                
        
    def deleteOne(self, number: int) -> None:
        if number in self.freq_dict:
            self.freq_set[self.freq_dict[number]].remove(number)

            if not self.freq_set[self.freq_dict[number]]:
                self.freq_set.pop(self.freq_dict[number]) 
                
            self.freq_dict[number] -= 1
            
            if self.freq_dict[number] != 0:
                if self.freq_dict[number] in self.freq_set: 
                    self.freq_set[self.freq_dict[number]].add(number)
                else:
                    self.freq_set[self.freq_dict[number]] = set([number])
            else:
                self.freq_dict.pop(number)
                
                

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.freq_set:
            return True
        else:
            return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)