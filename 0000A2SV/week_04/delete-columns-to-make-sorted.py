class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row,col,removed_counter = len(strs),len(strs[0]),0
        for i in range(col):
            prev = strs[0][i]
            for j in range(row):
                if prev > strs[j][i]:
                    removed_counter +=1 
                    break
                prev = strs[j][i]
        return removed_counter
                

        