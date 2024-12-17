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

    def build(self,left,right,preorder,inorder_map):
        if left > right:
            return None 

        # get the node value from 'preorder'
        node_val = preorder[self.pre_index]
        self.pre_index += 1

        # create the current tree node
        node = TreeNode(node_val)
        node_index = inorder_map[node_val]

        # use recursion to append the left and right nodes
        node.left = self.build(left,node_index-1,preorder,inorder_map)
        node.right = self.build(node_index+1,right,preorder,inorder_map)

        # return node 
        
        return node


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # inorder traversal is used to check 
        # the left side and write side of current 
        # node's subtree
        inorder_map ,n = {} ,len(inorder)
        # preorder traversal is used to get the 
        # node value for each node

        for i in range(n):inorder_map[inorder[i]] = i

        return self.build(0,n-1,preorder,inorder_map)