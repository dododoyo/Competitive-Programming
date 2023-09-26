# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:return []
        queue = deque([root])
        result = []
        while queue:
            lvl_size = len(queue)
            lvl_sum = 0
            for _ in range(lvl_size):
                node = queue.popleft()
                lvl_sum += node.val
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
            result.append(lvl_sum / lvl_size)
        return result