# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not(root1 or root2):
            return None

        node_one = root1.val if root1 else 0
        node_two = root2.val if root2 else 0

        # sum the value of the current two nodes
        new_node = TreeNode(node_one+node_two)

        # left and right of the new node is the solution from the previous recursive calls 
        new_node.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        new_node.right = self.mergeTrees(root1.right if root1 else None,root2.right if root2 else None)

        return new_node
        