class Solution:
    def repeatedCharacter(self, s: str) -> str:
        countLetter = set()
        for i in s:
            if i in countLetter:
                return i
            else:
                countLetter.add(i)
                
        