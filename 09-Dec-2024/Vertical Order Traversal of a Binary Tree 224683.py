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
        current_level = [[0,0,root]]


        while current_level:
            next_level = []
            for col,row,node in current_level:
                column_map[col].append([node.val,row])

                if node.left:
                    next_level.append([col-1,row+1,node.left])
                if node.right:
                    next_level.append([col+1,row+1,node.right])

            current_level = next_level[:]

        column_index = sorted(column_map)
        solution = []

        for col in column_index:
            # sort based on row then by value
            sorted_column = sorted(column_map[col],key=lambda x: (x[1],x[0]))

            # append only their value to the column array 
            vertical = [node for  node,row in sorted_column]

            solution.append(vertical)

        return solution