# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeToArray(self,root):
        solution = []
        def inorder_dfs(root):
            if not root:
                return 
            inorder_dfs(root.left)
            solution.append(root.val)
            inorder_dfs(root.right)
        inorder_dfs(root)
        return solution
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = self.treeToArray(root)
        for i in range(1,len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True
