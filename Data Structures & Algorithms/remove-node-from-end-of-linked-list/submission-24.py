class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head

        # move right n + 1 steps ahead
        while n >= 0:
            if right is None:        # fell off early → removing the first node
                return head.next
            right = right.next
            n -= 1

        # move both until right falls off the end
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next   # left is the node BEFORE the target
        return head