# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

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

        reverse = True
        current_level = deque()
        current_level.append(root)
        solution = []

        while current_level:
            if reverse:
                solution.append([node.val for node in current_level])
            else:
                solution.append([node.val for node in current_level][::-1])

            reverse = not reverse

            n = len(current_level)
            for i in range(n):
                node = current_level.popleft()

                if node.left:
                    current_level.append(node.left)
                if node.right:
                    current_level.append(node.right)
            
        return solution