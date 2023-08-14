# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head;
        right = head.next;
        while left and right:
            new_node = ListNode(self.findGCD(left.val,right.val),right);
            # print(new_node.val);
            left.next = new_node;
            
            left = left.next.next;
            right = right.next;
        return head;

    def findGCD(self,a,b):
        if a==1 or b==1:
            return 1;
        else:
            the_min = min(a,b);
            while the_min:
                if (a%the_min)==0 and (b%the_min)==0:
                    return the_min;
                else:
                    the_min -=1;
    

