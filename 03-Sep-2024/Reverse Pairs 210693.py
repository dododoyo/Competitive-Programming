# Problem: Reverse Pairs - https://leetcode.com/problems/reverse-pairs/description/

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.counter = 0

        def mergeSort(arr):
            n = len(arr)

            if n < 2:
                return arr

            middle = n//2

            left = mergeSort(arr[:middle])
            right = mergeSort(arr[middle:])

            return merge(left,right)

        def merge(arr1,arr2):
            n,m = len(arr1),len(arr2)

            # count solution 
            pointer1,pointer2 = 0,0
            while pointer1 < n and pointer2 < m:
                if arr1[pointer1] > 2*arr2[pointer2]:
                    self.counter += n-pointer1
                    pointer2 += 1
                else:
                    pointer1 += 1

            # merge arrays
            pointer1,pointer2 = 0,0
            solution = []
            while pointer1 < n and pointer2 < m:
                if arr1[pointer1] > arr2[pointer2]:
                    solution.append(arr2[pointer2])
                    pointer2 += 1
                else:
                    solution.append(arr1[pointer1])
                    pointer1 += 1

            solution.extend(arr1[pointer1:])
            solution.extend(arr2[pointer2:])

            """
            notice we can't merge the arrays and count solution
            at the same time because the comparison criterea is not the same
            """

            return solution

        mergeSort(nums)

        return self.counter
            