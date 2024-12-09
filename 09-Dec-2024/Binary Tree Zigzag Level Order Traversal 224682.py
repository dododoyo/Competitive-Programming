# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        current_level = [root]
        leftToRight = True
        solution = []

        while current_level:
            next_level = []
            if leftToRight:
                solution.append([node.val for node in current_level])
            else:
                solution.append([node.val for node in reversed(current_level)])

            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            current_level = next_level[:]
            leftToRight = not leftToRight
        
        return solution
