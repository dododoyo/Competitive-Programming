class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        n = max(chain(*matches))+1
        players = [0] * n
        for (win, lose) in matches:     
            if players[lose]<0: players[lose]-=1      
            if players[lose]>=0: players[lose]=-1  
            if players[win]>=0: players[win]=1 
        solution = [[],[]]
        for i in range(n):
            if players[i] == 1:
                solution[0].append(i)
            elif players[i] == -1:
                solution[1].append(i)
        
        return solution