# Problem: Construct Binary Tree from Preorder and Inorder Traversal - https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre_index = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(left,right):
            if left > right:
                return None

            node_val = preorder[self.pre_index]
            self.pre_index += 1
            node = TreeNode(node_val)

            inorder_index = inorder_map[node_val]
            node.left = helper(left,inorder_index-1)
            node.right = helper(inorder_index+1,right)
            
            return node
            
        inorder_map, n = {}, len(inorder)
        for i in range(n):
            inorder_map[inorder[i]] = i

        return helper(0,n-1)