# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        '''
        given two linked list 
        l1 and l2 

        the numbers are reversed and so we need to find the sum of both linked lists 
        and return th reverse of that as well 

        3 2 1 

        4 

        '''
        '''
        321
    +   654 

        12
        +5



        '''
        head = dummy = ListNode(0)

        carry = 0 
        while l1 or l2 or carry:
            
            if l1:
                v1 = l1.val
            else:
                v1 = 0 
            if l2:
                v2 = l2.val
            else:
                v2 = 0 
                
            val = v1 + v2 + carry 

            carry = val // 10  
            val = val % 10

            head.next = ListNode(val)

            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None
            head = head.next



        return dummy.next
        









        