class Solution:
    def isValid(self, s: str) -> bool:



        #keeping track of an unresolved element and in this case the unresolved element is 
        #open brackets needing a closing bracket and so when we hit the closting bracket we check 
        #on top of ot the stack to mak esure it corresponds 


        match = {')' : '(', '}' : '{',']' :'['}

        stack = []

        for i in s:

            if i in match:
                if not stack or stack.pop() != match[i]:
                    return False 
            else:
                stack.append(i)

        if not stack:
            return True
        else:
            return False



