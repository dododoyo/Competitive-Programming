class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s_list = s.split()
        prevMin = 0
        
        for i in s_list:
            if i.isnumeric():
                if int(i) > prevMin:
                    prevMin = int(i)
                else:
                    return False
        return True