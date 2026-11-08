# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:



        '''
        999
        + 1 

        '''



        dummy = head = ListNode()

        carry = 0 
        while l1 or l2 or carry:
            if l1 == None:
                val1 = 0
            else:
                val1 = l1.val 
        
            if l2 == None:
                val2 = 0
            else:
                val2 = l2.val 

            
            final = val1 + val2 + carry
            res = final % 10 
            carry = final // 10 
            head.next = ListNode(res)

            head = head.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 
        
        return dummy.next





        