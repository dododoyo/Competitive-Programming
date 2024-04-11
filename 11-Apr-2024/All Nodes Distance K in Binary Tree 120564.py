# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        relation = {root.val:None}
        visited,solution = set(),[]

        # do bfs to find relation
        current_level = [root]
        while current_level:
            next_level = []
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                    relation[node.left.val] = node
                if node.right:
                    next_level.append(node.right)
                    relation[node.right.val] = node
            current_level = next_level

        # print(relation)
        # do bfs on target until level k
        current_level = [target]
        visited.add(target.val)
        while current_level and k:
            next_level = []
            for node in current_level:
                if node.left and node.left.val not in visited:
                    next_level.append(node.left)
                    visited.add(node.left.val)

                if node.right and node.right.val not in visited:
                    next_level.append(node.right)
                    visited.add(node.right.val)

                if relation[node.val] and relation[node.val].val not in visited:
                    next_level.append(relation[node.val])
                    visited.add(relation[node.val].val)

            # print(next_level)
            k -= 1
          
            current_level = next_level

        return [node.val for node in current_level]