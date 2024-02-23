# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        def helper(root):
            if root:
                helper(root.right)
                nodes.append(root.val)
                helper(root.left)
        # get nodes as a list
        helper(root)

        # get occurance of each element
        freq = defaultdict(int)
        for node in nodes:
            freq[node] += 1
        # get maximum occurence in tree
        max_freq = 0
        for node in freq:
            max_freq = max(max_freq,freq[node])
        solution = []

        # append al the nodes with the maximum_occurence
        for node in freq:
            if freq[node] == max_freq:
                solution.append(node)
        return solution