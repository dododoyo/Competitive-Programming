# Problem: Vertical Order Traversal of a Binary Tree - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        column_map = defaultdict(list)
        current_level = [[root,0,0]]
        column_map[0] = [[root.val,0]]

        while current_level:
            next_level = []

            for node,column,row in current_level:

                if node.left:
                    next_level.append([node.left,column-1,row+1])
                    column_map[column-1].append([node.left.val,row+1])

                if node.right:
                    next_level.append([node.right,column+1,row+1])
                    column_map[column+1].append([node.right.val,row+1])

            current_level = next_level[:]

        sorted_columns = sorted(column_map)
        solution = []
        
        for column in sorted_columns:
            vertical = [info[0] for info in sorted(column_map[column],key = lambda x: (x[1],x[0]))]
            solution.append(vertical)
        return solution
                      
        