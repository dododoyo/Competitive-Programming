# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        for i in range(len(nums1)):
            nums1[i] = nums1[i] - nums2[i]

        return self.mergeSort(nums1, 0, len(nums1)-1, diff)

    def mergeSort(self,arr, left, right, difference) -> int:
        if left >= right:
            return 0
        middle = left + (right - left) // 2
        return self.mergeSort(arr, left, middle, difference) + self.mergeSort(arr, middle+1, right, difference) + self.merge(arr, left, middle, right, difference)
        

    def merge(self, arr, start, mid, end, diff) -> int:
        j, k, index = mid+1, mid+1, 0
        sortedList = [0] * (end-start+1)
        count = 0

        for i in range(start, mid+1):
            while k <= end and arr[i] - diff > arr[k]:
                k += 1
            count += end - k + 1
            while j <= end and arr[j] < arr[i]:
                sortedList[index] = arr[j]
                index += 1
                j += 1
            sortedList[index] = arr[i]
            index += 1
        while j <= end:
            sortedList[index] = arr[j]
            index += 1
            j += 1
        for i in range(start, end+1):
            arr[i] = sortedList[i-start]

        return count