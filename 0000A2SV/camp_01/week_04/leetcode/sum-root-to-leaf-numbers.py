# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        leafs=[]
        def helper(root,s):
            if(root is None):
                pass
            elif(root.left is None and root.right is None):
                s += str(root.val)
                leafs.append(s)
            else:
                s += str(root.val)
                s1= s

                helper(root.left, s)
                helper(root.right, s1)
        helper(root,"")
        return sum(int(i) for i in leafs)