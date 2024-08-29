# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # there can only be atmost 2 elements that satisfy this condition
        candidate1,candidate2 = 0,1
        counter1,counter2 = 0,0

        for num in nums:
            if num == candidate1:
                counter1 += 1
            elif num == candidate2:
                counter2 += 1
            elif counter1 == 0:
                candidate1 = num
                counter1 = 1
            elif counter2 == 0:
                candidate2 = num
                counter2 = 1
            else:
                # number is neither
                counter1 -= 1
                counter2 -= 1

        counter1,counter2 = 0,0
        for num in nums:
            if num == candidate1:
                counter1 += 1
            elif num == candidate2:
                counter2 += 1

        solution = []
        if counter1 > len(nums)//3:
            solution.append(candidate1)
        if counter2 > len(nums)//3:
            solution.append(candidate2)

        return solution
