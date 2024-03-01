# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        solution = []

        dq = deque()
        dq.append(root)

        while dq:
            dq_len = len(dq)
            current_level = []

            for i in range(dq_len):
                current_node = dq.popleft()
                if current_node:
                    current_level.append(current_node.val)
                    if current_node.left:
                        dq.append(current_node.left)
                    if current_node.right:
                        dq.append(current_node.right)
            if current_level:
                solution.append(current_level)

        return solution