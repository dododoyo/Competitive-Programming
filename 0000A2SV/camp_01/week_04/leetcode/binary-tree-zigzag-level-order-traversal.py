# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        solution = []
        dq = deque()
        dq.append(root)
        while dq:
            curr_len = len(dq)
            curr_row = []
            for _ in range(curr_len):
                current_node = dq.popleft()
                if current_node:
                    if current_node.left:
                        dq.append(current_node.left)
                    if current_node.right:
                        dq.append(current_node.right)
                    curr_row.append(current_node.val)
            if curr_row:
                solution.append(curr_row)
        for i in range(len(solution)):
            if i%2:
                solution[i] = solution[i][::-1]
        return solution
