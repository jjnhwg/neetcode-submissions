# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #[1,2,3,4]

        curr = head
        count = 0
        while curr:
            count += 1 
            curr = curr.next
        
        removeNode = (count - n) 


        if removeNode == 0:
            return head.next

        new = head
        
        #finds the node before the node you want to remove 
        #if 
        while removeNode > 1:
            new = new.next
            removeNode -= 1
        
     
        new.next = new.next.next

 
        return head









        