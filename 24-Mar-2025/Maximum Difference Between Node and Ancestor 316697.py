# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

"# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        solution = [0]

        def differenceFinder(root):
            if not (root):
                return (inf,-inf)
                
            left_min,left_max = differenceFinder(root.left)
            right_min, right_max = differenceFinder(root.right)
            
            curr_min = min(left_min,right_min,root.val) 
            curr_max = max(left_max,right_max,root.val)

            solution[0] = max(solution[0],curr_max-root.val,root.val-curr_min)

            return (curr_min,curr_max)

        differenceFinder(root)

        return solution[0]
