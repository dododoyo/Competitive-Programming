class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        dividable = self.isValid(skill)
        if dividable:return self.sumOf(skill)
        else:return -1
    def isValid(self,skills):
        left,right = 0,len(skills)-1
        summ = skills[left]+skills[right]
        while left < right:
            if skills[left]+skills[right] != summ:
                return False
            left,right = left+1,right-1
        return True
    def sumOf(self,skills):
        left,right,summ = 0,len(skills)-1,0
        while left < right:
            summ += skills[left]*skills[right]
            left,right = left+1,right-1
        return summ
        