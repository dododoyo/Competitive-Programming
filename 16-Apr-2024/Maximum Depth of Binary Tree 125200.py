# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0;

        level = 0;
        current_level = [root];
        while current_level:
            next_level = [];

            for node in current_level:
                if node.left:
                    next_level.append(node.left);
                if node.right:
                    next_level.append(node.right);

            level += 1;
            current_level = next_level;
        return level;