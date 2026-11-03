# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #[1,2,3,4] n =  2 

        right = head
        left = head 

        #counts the amount of nodes to put the right pointer 
        #if n = 1 and arary is just [1] this loop runs twice which causes an error 
        #this runs when n i equal to the length fo the linked list bc you are going one      node     extra

  # move right n + 1 steps ahead

        #[2, 1] tareget 1
        while n >= 0:
            if right is None:        # fell off early → removing the first node
                return head.next
            right = right.next
            n -= 1
        
        while right: 
            left = left.next 
            right = right.next

        #[1,2] n = 1 
        #edge case if when we try to set the next left value but the node 
        #we try to remove is the last node 
        

        left.next = left.next.next   # left is the node BEFORE the target
        return head

        


        

