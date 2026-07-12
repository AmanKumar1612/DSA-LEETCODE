# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=[]
        
        x=head
        while x:
            l.append(x.val)
            x=x.next
        for j in range(0,len(l)-k+1,k):
            y=[]
            for i in range(k):
                y.append(l.pop(j))
            for i in range(k):
                l.insert(j,y[i])
                



        ll=ListNode()
        x=ll
        for i in l:
            y=ListNode(i)
            x.next=y
            x=x.next
        return ll.next