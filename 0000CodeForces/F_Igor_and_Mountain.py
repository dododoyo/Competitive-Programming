# for _ in range([int(i) for i in input().split()][0]):
#   row,col,hand = [int(i) for i in input().split()]

#   grid = []
#   for _ in range(row):
#     grid.append(input())

#   moves = []
#   for i in range(-hand,hand+1):
#     for j in range(-hand,hand+1):
#       if i == 0 and j == 0:
#         continue
      
#       if i > -1:
#         moves.append([i,j])

#   memo = [[0 for _ in range(col)] for _ in range(row)]
#   for i in range(row-1,-1,-1):
#     for j in range(col-1,-1,-1):
#       if grid[i][j] == "#":

class Solution:
    def permute(self, nums):
        solution = []

        def backtrack(curr_nums,used):
            if len(curr_nums) == len(nums):
                solution.append(curr_nums[:])
                return None
            
            for num in nums:
                if num not in used:
                    next_nums = curr_nums + [num]
                    next_used = used + [num]

                    backtrack(next_nums,next_used)

            return None

        backtrack([],[])
        return solution

test = Solution()
print(test.permute([1,2,3]))