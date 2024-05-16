# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, nums: List[int]) -> int:
        MOD = (10**9) + 7
        p_solution = {i:[0 ,0] for i in range(len(nums))}

        def merge(left , right):
            left_ = len(left)-1
            right_ = len(right)-1
            while left_ > -1 and right_ > -1:
                if nums[left[left_]] <= nums[right[right_]]:
                    p_solution[right[right_]][1] += ((len(left)-1) - left_)
                    right_ -= 1
                else:
                    left_ -= 1

            while right_ > -1:
                p_solution[right[right_]][1] += len(left) 
                right_ -= 1  

            left_ = 0
            right_ = 0
            solution = []
            while left_ < len(left) and right_ < len(right):
                if nums[left[left_]] < nums[right[right_]]:
                    solution.append(left[left_])
                    left_ += 1
                else:
                    p_solution[right[right_]][0] += left_
                    solution.append(right[right_])
                    right_ += 1

            while right_ < len(right):
                p_solution[right[right_]][0] += left_
                solution.append(right[right_])
                right_ += 1

            solution.extend(left[left_:])
            return solution
            
        def split(left , right , arr):
            if left == right:
                return [arr[right]]
            
            middle = left + (right-left)//2

            new_left = split(left , middle , arr)
            new_right = split(middle+1 , right , arr)

            return merge(new_left , new_right)
            
        indices = [i for i in range(len(nums))]
        split(0, len(nums)-1, indices)

        real_solution = 0
        for i in p_solution.keys():
            real_solution += min(p_solution[i])

        return real_solution % (MOD)
