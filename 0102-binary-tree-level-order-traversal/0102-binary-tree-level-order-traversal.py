# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        sol = []
        que = collections.deque()
        que.append(root);
        
        while que:
            each_level = []
            for i in range(len(que)):
                node = que.popleft()
                if node:
                    each_level.append(node.val);
                    que.append(node.left);
                    que.append(node.right);
            if len(each_level) != 0:
                sol.append(each_level);
        return sol;
        