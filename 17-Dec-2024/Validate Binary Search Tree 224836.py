# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeToArray(self,root):
        solution = []
        def inorder(node):
            if not node:
                return node

            inorder(node.left)
            solution.append(node.val)
            inorder(node.right)

        inorder(root)

        return solution
    # use recursion
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # what is rule of BST ?
        # curr node must be greater than all left subtree values
        # curr node must be less than all right subtree values
        def dfs(node,lower,upper):
            if not node:
                return True
            curr_valid = lower < node.val < upper
            
            if curr_valid:
                left_valid = dfs(node.left,lower,node.val)
                right_valid = dfs(node.right,node.val,upper)
                return left_valid and right_valid
            else:
                return False

        return dfs(root,-float('inf'),float('inf'))