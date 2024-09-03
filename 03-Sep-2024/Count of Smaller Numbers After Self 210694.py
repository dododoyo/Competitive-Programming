# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new_nums = [(nums[i],i) for i in range(n)]
        solution = [0]*n

        def mergeSort(low,high):
            if low == high:
                return [new_nums[low]]

            middle = low + (high-low)//2

            left_arr = mergeSort(low,middle)
            right_arr = mergeSort(middle+1,high)

            return merge(left_arr,right_arr)

        def merge(left_arr,right_arr):
            rp,lp = 0,0
            r_len,l_len = len(right_arr),len(left_arr)

            merged = []

            while rp < r_len and lp < l_len:
                if left_arr[lp][0] <= right_arr[rp][0]:
                    merged.append(left_arr[lp])
                    solution[left_arr[lp][1]] += rp
                    lp += 1
                else:
                    merged.append(right_arr[rp])
                    rp += 1
                    
            merged.extend(right_arr[rp:])
   
            while lp < l_len:
                merged.append(left_arr[lp])
                solution[left_arr[lp][1]] += rp
                lp += 1
            return merged

        mergeSort(0,n-1)

        return solution