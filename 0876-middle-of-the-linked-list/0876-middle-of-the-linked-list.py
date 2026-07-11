# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x=head
        y=head
        while x.next is not None and y.next is not None and y.next.next is not None:
            x=x.next
            y=y.next.next
        if y.next is None:
            return x
        x=x.next
        return x
        