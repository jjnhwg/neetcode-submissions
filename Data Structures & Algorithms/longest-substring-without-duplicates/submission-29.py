class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        '''
        input given a string with the output being the amount of chars in a row you can go without having any duplicates


        '''


        l, r  = 0, 0 

        seen = set()

        res = 0

        while r < len(s):

            while s[r] in seen:
                seen.remove(s[l])
                l += 1 
                
            seen.add(s[r])
            r += 1 
            
            res = max(res, r - l)
    
        return res
            


        