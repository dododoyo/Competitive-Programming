# Problem: Recover a Tree From Preorder Traversal - https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i, n = 0, len(traversal)
        stack = []
        num = ''

        while i < n:
            level = 0

            while i < n and traversal[i] == '-': 
                i += 1
                level += 1
            
            while stack and len(stack) > level: 
                stack.pop()

            while i < n and traversal[i] != '-':
                num += traversal[i]
                i += 1

            node = TreeNode(int(num))

            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
                
            stack.append(node)
            num = ''
                
        return stack[0]
        