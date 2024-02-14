# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        solution = [[-1]*n for _ in range(m)]

        left,right = 0,n-1
        up,down = 0,m-1

        while left <= right and up <= down:
            # go to the right
            for curr in range(left,right+1):
                if head:
                    solution[up][curr] = head.val
                    head = head.next
            up += 1

            # go down
            for curr in range(up,down+1):
                if head:
                    solution[curr][right] = head.val
                    head = head.next
            right -= 1

            # go to the left
            for curr in range(right,left-1,-1):
                if head:
                    solution[down][curr] = head.val
                    head = head.next
            down -= 1

            # go up
            for curr in range(down,up-1,-1):
                if head:
                    solution[curr][left] = head.val
                    head = head.next
            left += 1
        return solution