# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        at each node we are trying to find the length of the deepest node 
        '''


        if not root:
            return 0

        right = self.maxDepth(root.right) # you need from the children left and right max depth 
        left = self.maxDepth(root.left) # you need from the children the left and right 

        length = 1 + max(right, left)

        return length


        