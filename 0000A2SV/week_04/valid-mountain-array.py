class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_index = 0
        for i in range(1,len(arr)):
            if arr[i] > arr[max_index]:
                max_index = i
        if max_index == 0 or max_index == len(arr)-1:
            return False
        start = 1
        while start <= max_index:
            if arr[start] <= arr[start-1]:return False
            start +=1
        while start < len(arr):
            if arr[start] >= arr[start-1]:return False
            start +=1
        return True