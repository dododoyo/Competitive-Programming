class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
                # let's first check if it is sorted 
        sorted = True
        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                sorted = False;break
        if sorted:
            return []
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
        