# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {root:None}
        visited,solution = set(),[]

        # do bfs to find parent
        # and change the tree into graph 
        # because we can go to the parent aswell

        current_level = [root]

        while current_level:
            next_level = []
            for node in current_level:
                if node.left:
                    parent[node.left] = node
                    next_level.append(node.left)
                if node.right:
                    parent[node.right] = node
                    next_level.append(node.right)

            current_level = next_level[:]

        # do bfs on the target node 
        # by considering it's parent as well
        
        current_level = [target]

        while current_level and k > 0:
            next_level = []

            for node in current_level:
                visited.add(node)
                if node.left and node.left not in visited:
                    next_level.append(node.left)

                if node.right and node.right not in visited:
                    next_level.append(node.right)

                if parent[node] and (parent[node] not in visited):
                    next_level.append(parent[node])

            k -= 1
            current_level = next_level[:]

        return [node.val for node in current_level]