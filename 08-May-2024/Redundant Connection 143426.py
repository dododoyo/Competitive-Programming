# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.size = 1

class UnionFind:
    def find(self, node):
        if node.parent != node:
            node.parent = self.find(node.parent)
        return node.parent

    def union(self, node1, node2):
        parent_1 = self.find(node1)
        parent_2 = self.find(node2)

        if parent_1 != parent_2:
            if parent_1.size > parent_2.size:
                parent_2.parent = parent_1
                parent_1.size += parent_2.size
            else:
                parent_1.parent = parent_2
                parent_2.size += parent_1.size
            return False
        else:
            return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf,node_map = UnionFind(),{}
        for i in range(1,len(edges)+1):
            node_map[i] = Node(i)

        for u,v in edges:
            if uf.union(node_map[u],node_map[v]):
                return [u,v]        