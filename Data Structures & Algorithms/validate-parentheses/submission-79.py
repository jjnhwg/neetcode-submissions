class Solution:
    def isValid(self, s: str) -> bool:

        #stacks are good to keep track of unresovled features we need to implement 
        #in this case the unresolved elements are the open brackets 


        stack = []

        matches = {")":"(" ,'}':'{', ']':'['}

        for i in s:
            if i in matches:
                if not stack or (stack.pop()) != (matches[i]):
        
                    return False
            else:
                stack.append(i)


        if stack:
            return False
        else:
            return True
            
        