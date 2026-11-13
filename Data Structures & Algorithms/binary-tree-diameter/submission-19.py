# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #at each node we want to find the from the children the longest path 

        #to do that we just take the max of the children and then we want to return 1 + the max of the children 

        res = 0 

    

        def dfs(root):

            nonlocal res

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            res = max(res, left + right)


            return 1 + max(left, right)
        
        dfs(root)
        
        return res
            