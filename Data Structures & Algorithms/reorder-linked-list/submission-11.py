# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        '''
        find the half way point of the nodes in the array 


        '''

        curr = []
        while head:
            curr.append(head)
            head = head.next


        reverse = []

        for i in range(len(curr) - 1, -1, -1):
            reverse.append(curr[i])

        l = 0 
        r = 0 
        dummy = res = ListNode(None)
        count = 0 

        while count < len(curr):
            res.next = (curr[l])
            count += 1
            res = res.next
            l += 1 

            if count == len(curr):
                res.next = None

                return 
                
            res.next = (reverse[r])
            res = res.next 
            count += 1
            r += 1 
        
        res.next = None

        
        return 

