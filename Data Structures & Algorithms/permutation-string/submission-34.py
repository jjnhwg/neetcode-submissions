class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:



        mp = {}
        match = {}

        if len(s1) > len(s2):
            return False 

        for i in range(len(s1)):
            mp[s2[i]] = 1 + mp.get(s2[i], 0)
            match[s1[i]] = 1 + match.get(s1[i], 0)

        l, r = 0, len(s1) - 1 

        while r < len(s2):
            if mp == match:
                return True
        

            mp[s2[l]] -= 1 

            if mp[s2[l]] == 0:
                del mp[s2[l]]

            l += 1
            r += 1

            if r >= len(s2):
                return False
        
            mp[s2[r]] = 1 + mp.get(s2[r], 0)
        
        return False




        