# Problem: Delete Nodes And Return Forest - https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        solution = []
        to_delete_nodes = set(to_delete)
        node = root

        node = self.helper(root, to_delete_nodes, solution)
        if node is not None:
            solution.append(root)

        return solution

    def helper(self, node, to_delete_nodes, disjointTrees):
        if not node:
            return None

        left = self.helper(node.left, to_delete_nodes, disjointTrees)
        right = self.helper(node.right, to_delete_nodes, disjointTrees)

        if not left:    node.left = None
        if not right:   node.right = None

        if node.val in to_delete_nodes:
            if left:    disjointTrees.append(left)
            if right:   disjointTrees.append(right)
            node = None

        return node  