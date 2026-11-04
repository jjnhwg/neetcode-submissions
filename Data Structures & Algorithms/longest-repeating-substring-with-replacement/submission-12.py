class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        so given the input of uppercase letters we are also given k which is the amount of chars we can replace 
        to get the longest substring with only one character which would be the output

        condition to use is 

        the len(substring) - the most frequent char in each substring <= k then that is the longest 


        '''

        l, r = 0, 0 

        mp = {}
        count = 0 
        res = 0

        while r < len(s):
            mp[s[r]] = 1 + mp.get(s[r], 0)
            count = max(count, mp[s[r]])


            while (r - l + 1) - count > k:
                mp[s[l]] -= 1 
                l += 1 
            
            res = max(res, r - l + 1)
            
            r += 1 
        
        return res










                




        