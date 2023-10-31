class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        sol = []
        for i in range(len(arr),0,-1):
            flipIndex = self.getFlipIndex(arr,i)
            if flipIndex != i:
                if flipIndex != 1:
                    sol.append(flipIndex)
                    arr = self.flipArr(arr,len(arr),flipIndex)
                sol.append(i)
                arr = self.flipArr(arr,len(arr),i)
        return sol

    def getFlipIndex(self,arr,n):
        for i in range(n):
            if arr[i] == n:
                return i+1
            
    def flipArr(self,arr,n,x):
        sol = arr.copy()
        for i in range(x):
            sol[i] = arr[x-i-1]
        return sol
        