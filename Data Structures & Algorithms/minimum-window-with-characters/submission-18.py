class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        input - two strings with the output being the shortest string in length that has the letters of the 
        t string in the s string 
        '''


        l, r = 0, 0 

        match = {}

        for i in range(len(t)):
            match[t[i]] = 1 + match.get(t[i], 0)

        
        have = 0 
        need = len(match)

        curr = {}

        res = [-1,-1]
        resLen = float("inf")


        while r < len(s):

            curr[s[r]] = 1 + curr.get(s[r], 0)

            if s[r] in match and curr[s[r]] == match[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r + 1]
                
                curr[s[l]] -= 1
                if s[l] in match and curr[s[l]] < match[s[l]]:
                    have -= 1 
                l += 1

        
            r += 1

        

        l, r = res


        if resLen != float("inf"):
            return s[l:r]
        else:
            return ""
            





