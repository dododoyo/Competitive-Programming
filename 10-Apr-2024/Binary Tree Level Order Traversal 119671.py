# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        solution = [[root.val]]
        current_level = [root]

        while current_level:
            next_level = []

            for node in current_level:
                if node.left:next_level.append(node.left)
                if node.right:next_level.append(node.right)

            if next_level:
                solution.append([node.val for node in next_level])
                
            current_level = next_level
        return solution
