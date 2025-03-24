# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], node: int) -> Optional[TreeNode]:
        if not root:
            return node

        if root.val > node.val:
            root.left = self.insertIntoBST(root.left, node)
        else:
            root.right = self.insertIntoBST(root.right ,node)

        return root
        

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            # found the node to be deleted
            # put left into right
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            root = self.insertIntoBST(root.right,root.left)

        return root

