class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        '''
        given two inputs of a string s and t return the shortest substring of s in which all strings in t are present 
        in the s substring 


 
        "OUZODYXAZV"

        "XYZ"
        '''

        match = {

        }

        for i in t:
            match[i] = 1 + match.get(i, 0)

        count = {}

        have = 0 
        need = len(match)

        res = [-1, -1]
        resLen = float("inf")

        l, r = 0, 0

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)

            if s[r] in match and count[s[r]] == match[s[r]]:
                have += 1 


            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                count[s[l]] -= 1

                if s[l] in match and count[s[l]] < match[s[l]]:
                    have -= 1 
                l += 1 
        
            r += 1
        
        l, r = res
        
        if resLen != float("inf"):
            return s[l:r + 1]
        else:
            return ""
            







                









