# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        x=head
        y=head
        while x.next is not None and y.next is not None and y.next.next is not None:
            
            x=x.next
            y=y.next.next
            if x==y:
                return True
        return False