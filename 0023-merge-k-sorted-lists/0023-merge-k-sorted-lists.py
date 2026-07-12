# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l=[]
        for i in lists:
            x=i
            while x:
                l.append(x.val)
                x=x.next
        l.sort()
        ll=ListNode()
        x=ll
        for i in l:
            y=ListNode(i)
            x.next=y
            x=x.next
        return ll.next
