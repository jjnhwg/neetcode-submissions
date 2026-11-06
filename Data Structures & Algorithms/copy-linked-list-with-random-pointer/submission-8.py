class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # The "notebook": original node -> its copy
        # None maps to None so a missing next/random just becomes None
        old_to_new = {None: None}

        # PASS 1: make every copy (values only, no arrows yet)
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)   # A -> A'(7), B -> B'(13), C -> C'(11)
            curr = curr.next

        # PASS 2: connect the arrows using the notebook
        curr = head
        while curr:
            copy = old_to_new[curr]                  # find this node's twin
            copy.next = old_to_new[curr.next]        # A.next is B   -> A'.next = B'
            copy.random = old_to_new[curr.random]    # A.random is C -> A'.random = C'
            curr = curr.next

        return old_to_new[head]   # A', the head of the new list