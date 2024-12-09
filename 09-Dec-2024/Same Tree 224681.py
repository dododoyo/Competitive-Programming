# Problem: Same Tree - https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not (p or q):
            return True

        if not p or not q:
            return False

        # to be the same tree the nodes has to be the same 
        # and also their children need to be the same
        nodes_same = p.val == q.val

        # check if left subtrees are same 
        lefts_same = self.isSameTree(q.left,p.left)

        # check if right subtrees are same
        rights_same = self.isSameTree(q.right,p.right)
    
        children_same = lefts_same and rights_same

        return nodes_same and children_same
        