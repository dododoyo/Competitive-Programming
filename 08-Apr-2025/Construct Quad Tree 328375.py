# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf

        self.topLeft = topLeft
        self.topRight = topRight

        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def allSame(self,r,c,n):
        val = self.grid[r][c]

        # check if all of them has the same value 
        for dr in range(r,r+n):
            for dc in range(c,c+n):
                if self.grid[dr][dc] != val:
                    return False 
        return True

    def constructTree(self,sr,sc,n):
        # if current sub grid is edge case 
        # return it's node
        currNode =  Node(0,0,None,None,None,None)
        if self.allSame(sr,sc,n):
            currNode.val = self.grid[sr][sc]
            currNode.isLeaf = True

            return currNode

        currNode.topLeft = self.constructTree(sr,sc,n//2)
        currNode.topRight = self.constructTree(sr,sc + n//2,n//2)
        currNode.bottomLeft = self.constructTree(sr + n//2,sc,n//2)
        currNode.bottomRight = self.constructTree(sr + n//2,sc + n//2,n//2)

        return currNode

    def construct(self, grid: List[List[int]]) -> 'Node':
        self.grid = grid

        # row,col,size
        return self.constructTree(0,0,len(grid))