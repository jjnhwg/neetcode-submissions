class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)          # NEW: fake node in front of head
        group_prev = dummy                 # NEW: node right before the current group

        while True:                        # NEW: one pass per group
            # 1. Walk to the k-th node (KEPT, now starts from group_prev)
            curr = group_prev
            count = k
            while curr and count > 0:      # CHANGED: k steps, stop if we run out
                curr = curr.next
                count -= 1

            if not curr:                   # NEW: fewer than k left → done
                return dummy.next          #      (replaces the whole inc count)

            kth = curr

            # 2. Save the node after the group (KEPT, same idea as your `rest`)
            group_next = kth.next

            # 3. Reverse the group (KEPT, your reversal loop)
            prev = group_next              # CHANGED: was None, now the trick
            head = group_prev.next         # first node of this group
            start1 = head                  # KEPT: will become the tail
            while head != group_next:      # CHANGED: stop at the group's end
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt

            # 4. Reconnect (NEW)
            group_prev.next = kth          # previous tail → new head
            group_prev = start1            # move to this group's tail