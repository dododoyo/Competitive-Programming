class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:return [1]
        if rowIndex == 1:return [1,1]
        prev_row = self.getRow(rowIndex-1)
        solution = [1]*(rowIndex+1)
        for i in range(len(prev_row)-1):
            solution[i+1] = prev_row[i] + prev_row[i+1]
        return solution        