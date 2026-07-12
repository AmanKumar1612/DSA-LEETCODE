# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotate(self,head):
        x=head
        while x.next is not None and x.next.next is not None:
            x=x.next
        temp=x.next
        x.next=None
        temp.next=head
        return temp
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n=0
        x=head
        while x:
            n=n+1
            x=x.next
        if k>n:
            k=k%n
        y=head
        for i in range(k):
            y=self.rotate(y)
        return y