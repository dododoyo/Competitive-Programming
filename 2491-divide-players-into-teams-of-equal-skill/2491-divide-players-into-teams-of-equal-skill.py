class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        l,r = 0,len(skill)-1
        each_sum = sum(skill)//(len(skill)//2)
        sol = 0
        
        while l < r:
            if skill[r]+skill[l] != each_sum:
                return -1
            else:
                sol += skill[r]*skill[l]
                r -= 1
                l += 1
        return sol
            
        