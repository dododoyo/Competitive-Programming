# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        levels = 0
        level = [root]
        while level:
            next_level = []
            for node in level:
                for child in node.children:
                    next_level.append(child)
            level = next_level
            levels += 1
        return levels