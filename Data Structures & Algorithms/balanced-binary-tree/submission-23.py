# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        

        def dfs(root):
            if not root:
                return [True, 0]
            # this is the base where at each children node we want to find the height of that and see if it differs by more thatn 
            #one and if it does we just return false
            left = dfs(root.left)
            right = dfs(root.right)
            
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1


            return [balanced, 1 + max(left[1], right[1])]

            

        return dfs(root)[0]
        