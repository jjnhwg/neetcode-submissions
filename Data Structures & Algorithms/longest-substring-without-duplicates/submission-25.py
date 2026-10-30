class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        input a string, the length of the longest substring w/o and dupe charactrers 
        '''



        seen = set()

        l, r = 0, 0

        lnMax = 0

        while r < len(range(len(s))):

            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])

            lnMax = max(r - l + 1, lnMax)
            r += 1
        
        return lnMax
        

            
           
