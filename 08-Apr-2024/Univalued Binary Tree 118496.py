# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        value = root.val
        level = [root]
        while level:
            next_level = []
            for node in level:
                if node.val != value:
                    return False
                if node.left:next_level.append(node.left)
                if node.right:next_level.append(node.right)

            level = next_level

        return True