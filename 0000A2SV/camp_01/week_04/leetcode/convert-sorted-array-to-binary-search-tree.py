# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def converter(arr):
            if not arr:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0])
            middle_index = len(arr)//2
            current_node = TreeNode(arr[middle_index])
            current_node.left = converter(arr[:middle_index])
            current_node.right = converter(arr[middle_index+1:])
            return current_node

        return converter(nums)