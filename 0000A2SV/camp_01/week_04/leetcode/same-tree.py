# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not (p or q):return True
        if not p or not q:return False
        # to be the same tree the nodes has to be the same 
        # and also their children need to be the same
        nodes_same = p.val == q.val
        children_same = self.isSameTree(q.left,p.left) and self.isSameTree(q.right,p.right)
        return nodes_same and children_same
        