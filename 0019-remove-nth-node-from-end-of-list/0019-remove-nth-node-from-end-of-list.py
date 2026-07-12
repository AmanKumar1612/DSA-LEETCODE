# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0
        x=head
        while x is not None:
            c+=1
            x=x.next
        x=head
        c=c-n
        if c==0:
            return x.next
        for _ in range(c-1):
            x=x.next
        if x.next is not None:
            x.next=x.next.next
        else:
            return x.next
        return head