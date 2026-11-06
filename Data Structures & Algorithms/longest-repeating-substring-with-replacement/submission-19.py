class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        input is the string and k is the amount of character's that we can swap to get the longest repeating char within a      substring 


 get it so count gets upadede to the actual count anyways and so it doesn tmatter that there is a stale count then because it wil lbe stuck



        '''


        l, r = 0, 0

        count = 0 

        mp = {}
        res = 0

        while r < len(s):
            mp[s[r]] = 1 + mp.get(s[r], 0)
            count = max(mp[s[r]], count)

            if ((r - l) + 1 - count <= k):
                res = max((r - l) + 1, res)
            
            else:
                mp[s[l]] -= 1

                l += 1
            r += 1 
            
        '''
        s="AABABBA"
k=1
        '''
            
        
        return res




 
        