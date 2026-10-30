class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        '''
        input given a string with the output being the amount of chars in a row you can go without having any duplicates


        '''

        mp = {}
        l, r  = 0, 0 
        res = 0

        while r < len(s):

            if s[r] in mp and mp[s[r]] >= l : #this finds if there was a duplicate 
                l = mp[s[r]] + 1 #find the duplicate and go one after 
                
            mp[s[r]] = r

            r += 1 
            
            res = max(res, r - l)
    
        return res
            


        