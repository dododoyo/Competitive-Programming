# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer  = []
        def dfs(root):
            if root:
                if root.val >= low and root.val <= high:
                    answer.append(root.val)
                dfs(root.left);dfs(root.right)
                return
            else:
                return
        dfs(root)
        return sum(answer)
        